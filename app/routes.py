from flask import render_template, request, redirect, url_for, session, jsonify
from app import app
from app.data.questions import get_exam_questions, single_choice_questions, true_false_questions, design_questions, sql_questions
from app.data.question_bank import get_questions_by_subject_semester, get_all_questions_for_subject, question_bank, reload_bank
from app.data.bank_storage import get_bank_stats, merge_questions, save_bank
from app.data.storage import save_exam_result, get_all_results, delete_result, get_statistics
from app.data.subjects import get_all_subjects, get_subject_by_code
from app.data.semesters import get_all_semesters, get_semester_by_code
from app.data.question_types import get_all_question_types, get_question_type_by_id
from app.data.members import add_member, get_member_by_student_id, update_member_score, get_all_members, get_member_level, member_levels, update_member_level, update_member_status, delete_member, get_members_by_level
from app.exam_helpers import normalize_questions, build_exam_sections, grade_exam
from app.redis_store import create_scan_code, get_scan_status, complete_scan, delete_scan_code
import copy
import json
import os
import time

TEACHER_CREDENTIALS = {
    'username': os.environ.get('TEACHER_USERNAME', 'teacher'),
    'password': os.environ.get('TEACHER_PASSWORD', '123456')
}

def _prepare_exam_context(questions, **kwargs):
    questions = normalize_questions(questions)
    exam_sections, total_questions = build_exam_sections(questions)
    return dict(
        questions=questions,
        exam_sections=exam_sections,
        total_questions=total_questions,
        **kwargs,
    )

def check_scan_status(code):
    return get_scan_status(code)

@app.route('/')
def index():
    subjects = get_all_subjects()
    semesters = get_all_semesters()
    question_types = get_all_question_types()
    return render_template('index.html', subjects=subjects, semesters=semesters, question_types=question_types)

@app.route('/generate_qrcode')
def generate_qrcode():
    code = create_scan_code()
    return jsonify({'code': code})

@app.route('/check_scan/<code>')
def check_scan(code):
    status = check_scan_status(code)
    if status:
        return jsonify(status)
    return jsonify({'status': 'expired'})

@app.route('/scan_login/<code>', methods=['POST'])
def scan_login(code):
    data = request.get_json()
    student_id = data.get('student_id')
    student_name = data.get('student_name')
    
    if complete_scan(code, student_id, student_name):
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'})

@app.route('/scan_login_page/<code>')
def scan_login_page(code):
    status = check_scan_status(code)
    if not status or status['status'] != 'waiting':
        return render_template('error.html', message='二维码已过期或无效')
    return render_template('scan_login_page.html', code=code)

@app.route('/start_exam_scan/<code>')
def start_exam_scan(code):
    status = check_scan_status(code)
    if not status or status['status'] != 'completed':
        return redirect(url_for('index'))
    
    student_info = status['student_info']
    
    wechat_id = f"wx_{code}"
    member = get_member_by_student_id(student_info['student_id'])
    
    if not member:
        add_member(student_info['student_id'], student_info['student_name'], wechat_id)
        session['member_registered'] = True
    else:
        session['member_registered'] = False
    
    questions = normalize_questions(get_exam_questions())
    
    session['student_id'] = student_info['student_id']
    session['student_name'] = student_info['student_name']
    session['questions'] = questions
    session['answers'] = {}
    session.modified = True
    
    delete_scan_code(code)
    
    return render_template('exam.html', **_prepare_exam_context(
        questions,
        student_id=student_info['student_id'],
        student_name=student_info['student_name'],
    ))

@app.route('/start_exam', methods=['POST'])
def start_exam():
    student_id = request.form.get('student_id')
    student_name = request.form.get('student_name')
    subject_code = request.form.get('subject_code', 'CS201')
    semester_code = request.form.get('semester_code', '2026SP')
    
    if not student_id or not student_name:
        subjects = get_all_subjects()
        semesters = get_all_semesters()
        return render_template('index.html', subjects=subjects, semesters=semesters, error='请输入学号和姓名')
    
    bank_questions = get_questions_by_subject_semester(subject_code, semester_code)
    
    if not bank_questions or not any(bank_questions.values()):
        bank_questions = get_all_questions_for_subject(subject_code)
    
    if not bank_questions or not any(bank_questions.values()):
        bank_questions = get_exam_questions(subject_code)
    
    questions = {}
    for q_type, q_list in bank_questions.items():
        if q_list:
            questions[q_type] = q_list[:5]
    
    if not questions:
        questions = get_exam_questions(subject_code)

    questions = normalize_questions(questions)
    
    subject = get_subject_by_code(subject_code)
    semester = get_semester_by_code(semester_code)
    
    session['student_id'] = student_id
    session['student_name'] = student_name
    session['subject_code'] = subject_code
    session['subject_name'] = subject['name'] if subject else '未知科目'
    session['semester_code'] = semester_code
    session['semester_name'] = semester['name'] if semester else '未知学期'
    session['questions'] = questions
    session['answers'] = {}
    session.modified = True
    session['start_time'] = request.form.get('start_time', '')
    
    return render_template('exam.html', **_prepare_exam_context(
        questions,
        student_id=student_id,
        student_name=student_name,
        subject_name=session['subject_name'],
        semester_name=session['semester_name'],
    ))

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    data = request.get_json()
    question_id = data.get('question_id')
    answer = data.get('answer')
    question_type = data.get('question_type')
    
    # 获取当前答案字典
    answers = session.get('answers', {})
    
    # 确保嵌套字典存在
    if question_type not in answers:
        answers[question_type] = {}
    
    # 保存答案
    answers[question_type][question_id] = answer
    
    # 更新session并标记为已修改
    session['answers'] = answers
    session.modified = True
    
    return jsonify({'status': 'success', 'message': '答案已保存'})

@app.route('/submit_exam', methods=['POST'])
def submit_exam():
    if 'student_id' not in session or 'questions' not in session:
        return redirect(url_for('index'))
    
    answers = session.get('answers', {})
    questions = session['questions']

    graded = grade_exam(questions, answers)
    exam_sections, _ = build_exam_sections(graded['questions'])

    result = {
        'student_id': session['student_id'],
        'student_name': session['student_name'],
        'subject_name': session.get('subject_name', ''),
        'semester_name': session.get('semester_name', ''),
        'score': graded['score'],
        'total_score': graded['total_score'],
        'type_scores': graded['type_scores'],
        'single_score': graded['type_scores'].get('single_choice', 0),
        'tf_score': graded['type_scores'].get('true_false', 0),
        'design_score': graded['type_scores'].get('design', 0),
        'sql_score': graded['type_scores'].get('sql', 0),
        'answers': answers,
        'questions': graded['questions'],
        'exam_sections': exam_sections,
    }
    
    save_exam_result(result)
    update_member_score(session['student_id'], graded['score'])
    
    session['result'] = result
    session.modified = True
    
    return redirect(url_for('result'))

@app.route('/result')
def result():
    if 'result' not in session:
        return redirect(url_for('index'))
    
    result = session['result']
    if 'exam_sections' not in result:
        result['exam_sections'], _ = build_exam_sections(result.get('questions', {}))
    if 'type_scores' not in result:
        result['type_scores'] = {
            'single_choice': result.get('single_score', 0),
            'true_false': result.get('tf_score', 0),
            'design': result.get('design_score', 0),
            'sql': result.get('sql_score', 0),
        }
    return render_template('result.html', result=result)

@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect(url_for('index'))

@app.route('/api/questions')
def api_questions():
    questions = get_exam_questions()
    return jsonify(questions)

# 教师管理后台路由
@app.route('/teacher')
def teacher_login_page():
    if 'teacher_logged_in' in session and session['teacher_logged_in']:
        return redirect(url_for('teacher_dashboard'))
    return render_template('teacher_login.html')

@app.route('/teacher_login', methods=['POST'])
def teacher_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == TEACHER_CREDENTIALS['username'] and password == TEACHER_CREDENTIALS['password']:
        session['teacher_logged_in'] = True
        session.modified = True
        return redirect(url_for('teacher_dashboard'))
    else:
        return render_template('teacher_login.html', error='用户名或密码错误')

@app.route('/teacher_dashboard')
def teacher_dashboard():
    if 'teacher_logged_in' not in session or not session['teacher_logged_in']:
        return redirect(url_for('teacher_login_page'))
    
    results = get_all_results()
    stats = get_statistics()
    
    return render_template('teacher_dashboard.html', results=results, stats=stats)

@app.route('/teacher_logout')
def teacher_logout():
    session.pop('teacher_logged_in', None)
    session.modified = True
    return redirect(url_for('teacher_login_page'))

@app.route('/delete_result/<int:index>')
def delete_result_route(index):
    if 'teacher_logged_in' not in session or not session['teacher_logged_in']:
        return redirect(url_for('teacher_login_page'))
    
    delete_result(index)
    return redirect(url_for('teacher_dashboard'))

@app.route('/teacher/members')
def member_management():
    if 'teacher_logged_in' not in session or not session['teacher_logged_in']:
        return redirect(url_for('teacher_login_page'))
    
    members = get_all_members()
    levels = member_levels
    
    for member in members:
        member['level_info'] = get_member_level(member['member_level'])
        if member['exams_taken'] > 0:
            member['avg_score'] = round(member['total_score'] / member['exams_taken'], 1)
        else:
            member['avg_score'] = 0
    
    return render_template('member_management.html', members=members, levels=levels)

@app.route('/teacher/member/update_level/<int:member_id>', methods=['POST'])
def update_member_level_route(member_id):
    if 'teacher_logged_in' not in session or not session['teacher_logged_in']:
        return redirect(url_for('teacher_login_page'))
    
    new_level = request.form.get('level')
    update_member_level(member_id, new_level)
    
    return redirect(url_for('member_management'))

@app.route('/teacher/member/update_status/<int:member_id>', methods=['POST'])
def update_member_status_route(member_id):
    if 'teacher_logged_in' not in session or not session['teacher_logged_in']:
        return redirect(url_for('teacher_login_page'))
    
    new_status = request.form.get('status')
    update_member_status(member_id, new_status)
    
    return redirect(url_for('member_management'))

@app.route('/teacher/member/delete/<int:member_id>')
def delete_member_route(member_id):
    if 'teacher_logged_in' not in session or not session['teacher_logged_in']:
        return redirect(url_for('teacher_login_page'))
    
    delete_member(member_id)
    return redirect(url_for('member_management'))


def _teacher_required():
    return 'teacher_logged_in' in session and session['teacher_logged_in']


@app.route('/teacher/import', methods=['GET', 'POST'])
def question_import():
    if not _teacher_required():
        return redirect(url_for('teacher_login_page'))

    result = None
    error = None

    if request.method == 'POST':
        upload = request.files.get('bank_file')
        subject_code = request.form.get('subject_code', 'CS201')
        semester_code = request.form.get('semester_code', '2026SP')
        allow_duplicates = request.form.get('allow_duplicates') == '1'

        if not upload or not upload.filename:
            error = '请选择 JSON 文件'
        else:
            try:
                payload = json.load(upload.stream)
                bank = copy.deepcopy(question_bank)
                result = merge_questions(
                    bank,
                    subject_code,
                    semester_code,
                    payload.get(subject_code, {}).get(semester_code, payload)
                    if subject_code in payload and isinstance(payload[subject_code], dict)
                    else payload,
                    skip_duplicates=not allow_duplicates,
                )
                save_bank(bank)
                reload_bank()
            except json.JSONDecodeError:
                error = 'JSON 格式无效，请检查文件内容'
            except Exception as exc:
                error = f'导入失败: {exc}'

    return render_template(
        'question_import.html',
        subjects=get_all_subjects(),
        semesters=get_all_semesters(),
        bank_stats=get_bank_stats(question_bank),
        result=result,
        error=error,
    )
