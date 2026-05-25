"""考试组卷与评分辅助函数。"""

import re

from app.data.question_types import get_question_type_by_id

SECTION_ORDER = [
    "single_choice",
    "multiple_choice",
    "true_false",
    "fill_blank",
    "design",
    "sql",
    "code",
    "short_answer",
    "essay",
]

SECTION_META = {
    "single_choice": {"title": "单选题", "icon": "📝", "mode": "single"},
    "multiple_choice": {"title": "多选题", "icon": "☑️", "mode": "multiple"},
    "true_false": {"title": "判断题", "icon": "✅", "mode": "true_false"},
    "fill_blank": {"title": "填空题", "icon": "✏️", "mode": "text"},
    "design": {"title": "设计题", "icon": "🎨", "mode": "essay"},
    "sql": {"title": "SQL题", "icon": "💻", "mode": "essay"},
    "code": {"title": "编程题", "icon": "⌨️", "mode": "essay"},
    "short_answer": {"title": "简答题", "icon": "📋", "mode": "essay"},
    "essay": {"title": "论述题", "icon": "📖", "mode": "essay"},
}

OBJECTIVE_TYPES = {"single_choice", "multiple_choice", "true_false", "fill_blank"}
SUBJECTIVE_TYPES = {"design", "sql", "code", "short_answer", "essay"}


def _split_combined_options(options):
    """将 'A）xx B）yy' 合并格式拆分为独立选项。"""
    if not options:
        return []
    if len(options) == 1 and re.search(r"[A-E][）\)\.]", str(options[0])):
        parts = re.split(r"(?=[A-E][）\)\.])", str(options[0]))
        return [p.strip() for p in parts if p.strip()]
    return options


def _option_letter(opt, fallback):
    text = str(opt).strip()
    match = re.match(r"^([A-E])", text)
    return match.group(1) if match else fallback


def normalize_questions(questions):
    """确保每道题都有 id，返回新字典。"""
    normalized = {}
    for q_type, q_list in questions.items():
        if not q_list:
            continue
        normalized[q_type] = []
        for idx, q in enumerate(q_list, start=1):
            item = dict(q)
            if "id" not in item or item["id"] is None:
                item["id"] = idx
            if "options" in item:
                item["options"] = _split_combined_options(item["options"])
            normalized[q_type].append(item)
    return normalized


def build_exam_sections(questions):
    sections = []
    offset = 0
    for q_type in SECTION_ORDER:
        q_list = questions.get(q_type) or []
        if not q_list:
            continue
        meta = SECTION_META.get(q_type, {"title": q_type, "icon": "📌", "mode": "essay"})
        type_info = get_question_type_by_id(q_type) or {}
        sections.append(
            {
                "type": q_type,
                "title": meta["title"],
                "icon": meta["icon"],
                "mode": meta["mode"],
                "questions": q_list,
                "start_index": offset,
                "count": len(q_list),
                "score_per_item": type_info.get("score_per_item", 2),
            }
        )
        offset += len(q_list)
    return sections, offset


def _normalize_answer(answer):
    return "".join(sorted(str(answer).upper().replace(",", "").replace(" ", "")))


def _is_correct(q_type, user_answer, correct_answer):
    if not user_answer:
        return False
    if q_type == "multiple_choice":
        return _normalize_answer(user_answer) == _normalize_answer(correct_answer)
    if q_type == "fill_blank":
        return str(user_answer).strip().lower() == str(correct_answer).strip().lower()
    return str(user_answer).strip().upper() == str(correct_answer).strip().upper()


def grade_exam(questions, answers):
    """按题型评分，客观题精确匹配，主观题有作答给半分。"""
    questions = normalize_questions(questions)
    total_questions = sum(len(qs) for qs in questions.values())
    per_question = 100 / total_questions if total_questions else 0

    type_scores = {}
    graded_questions = {}

    for q_type, q_list in questions.items():
        graded_list = []
        type_score = 0
        for q in q_list:
            q_id = str(q["id"])
            user_answer = answers.get(q_type, {}).get(q_id, "")
            graded = dict(q)
            graded["user_answer"] = user_answer

            if q_type in OBJECTIVE_TYPES:
                graded["is_correct"] = _is_correct(q_type, user_answer, q.get("answer", ""))
                graded["score"] = round(per_question) if graded["is_correct"] else 0
            else:
                graded["is_correct"] = bool(str(user_answer).strip())
                graded["score"] = round(per_question * 0.5) if graded["is_correct"] else 0

            type_score += graded["score"]
            graded_list.append(graded)

        graded_questions[q_type] = graded_list
        type_scores[q_type] = type_score

    score = sum(type_scores.values())
    score = min(score, 100)

    return {
        "score": score,
        "total_score": 100,
        "type_scores": type_scores,
        "questions": graded_questions,
    }
