import copy
import json
import os

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
BANK_FILE = os.path.join(DATA_DIR, "question_bank.json")


def _ensure_nested(bank, subject_code, semester_code, question_type):
    bank.setdefault(subject_code, {})
    bank[subject_code].setdefault(semester_code, {})
    bank[subject_code][semester_code].setdefault(question_type, [])


def _question_key(question):
    text = str(question.get("question", "")).strip()
    answer = str(question.get("answer", "")).strip()
    return text, answer


def _next_id(questions):
    ids = [q.get("id", 0) for q in questions if isinstance(q.get("id"), int)]
    return max(ids, default=0) + 1


def load_bank(default_bank=None):
    if os.path.exists(BANK_FILE):
        with open(BANK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    if default_bank is not None:
        save_bank(default_bank)
        return copy.deepcopy(default_bank)
    return {}


def save_bank(bank):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(BANK_FILE, "w", encoding="utf-8") as f:
        json.dump(bank, f, ensure_ascii=False, indent=2)


def merge_questions(bank, subject_code, semester_code, incoming, skip_duplicates=True):
    """增量合并题库，返回统计信息。"""
    stats = {"added": 0, "skipped": 0, "errors": []}

    if not isinstance(incoming, dict):
        stats["errors"].append("导入数据必须是 JSON 对象")
        return stats

    for question_type, questions in incoming.items():
        if not isinstance(questions, list):
            stats["errors"].append(f"题型 {question_type} 必须是数组")
            continue

        _ensure_nested(bank, subject_code, semester_code, question_type)
        existing = bank[subject_code][semester_code][question_type]
        existing_keys = {_question_key(q) for q in existing}

        for raw in questions:
            if not isinstance(raw, dict) or not raw.get("question"):
                stats["errors"].append(f"跳过无效题目: {raw}")
                continue

            question = copy.deepcopy(raw)
            key = _question_key(question)

            if skip_duplicates and key in existing_keys:
                stats["skipped"] += 1
                continue

            if "id" not in question or not isinstance(question.get("id"), int):
                question["id"] = _next_id(existing)

            existing.append(question)
            existing_keys.add(key)
            stats["added"] += 1

    return stats


def import_from_file(file_path, subject_code, semester_code, skip_duplicates=True):
    with open(file_path, "r", encoding="utf-8") as f:
        payload = json.load(f)

    if subject_code in payload and isinstance(payload[subject_code], dict):
        semester_data = payload[subject_code].get(semester_code, payload[subject_code])
        if semester_code in payload[subject_code]:
            incoming = payload[subject_code][semester_code]
        else:
            incoming = semester_data
    elif all(isinstance(v, list) for v in payload.values()):
        incoming = payload
    else:
        raise ValueError("无法识别 JSON 格式，请使用按题型分组的格式或完整题库格式")

    from app.data.question_bank import question_bank, reload_bank

    bank = copy.deepcopy(question_bank)
    stats = merge_questions(bank, subject_code, semester_code, incoming, skip_duplicates)
    save_bank(bank)
    reload_bank()
    return stats


def get_bank_stats(bank):
    stats = {}
    for subject, semesters in bank.items():
        stats[subject] = {}
        for semester, types in semesters.items():
            stats[subject][semester] = {
                q_type: len(q_list) for q_type, q_list in types.items()
            }
    return stats
