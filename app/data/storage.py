import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
RESULTS_FILE = os.path.join(DATA_DIR, 'exam_results.json')

def save_exam_result(result):
    """保存考试成绩到文件"""
    os.makedirs(DATA_DIR, exist_ok=True)
    
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'r', encoding='utf-8') as f:
            results = json.load(f)
    else:
        results = []
    
    results.append(result)
    
    with open(RESULTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

def get_all_results():
    """获取所有考试成绩"""
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def get_result_by_student_id(student_id):
    """根据学号获取成绩"""
    results = get_all_results()
    return [r for r in results if r['student_id'] == student_id]

def delete_result(result_index):
    """删除指定成绩"""
    results = get_all_results()
    if 0 <= result_index < len(results):
        deleted = results.pop(result_index)
        with open(RESULTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        return deleted
    return None

def get_statistics():
    """获取成绩统计信息"""
    results = get_all_results()
    if not results:
        return {
            'total_students': 0,
            'average_score': 0,
            'highest_score': 0,
            'lowest_score': 0,
            'excellent_count': 0,
            'good_count': 0,
            'pass_count': 0,
            'fail_count': 0
        }
    
    scores = [r['score'] for r in results]
    return {
        'total_students': len(results),
        'average_score': round(sum(scores) / len(scores), 2),
        'highest_score': max(scores),
        'lowest_score': min(scores),
        'excellent_count': sum(1 for r in results if r['score'] >= 90),
        'good_count': sum(1 for r in results if 80 <= r['score'] < 90),
        'pass_count': sum(1 for r in results if 60 <= r['score'] < 80),
        'fail_count': sum(1 for r in results if r['score'] < 60)
    }
