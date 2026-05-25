question_types = [
    {"id": "single_choice", "name": "单选题", "score_per_item": 2},
    {"id": "multiple_choice", "name": "多选题", "score_per_item": 3},
    {"id": "true_false", "name": "判断题", "score_per_item": 1},
    {"id": "fill_blank", "name": "填空题", "score_per_item": 2},
    {"id": "design", "name": "设计题", "score_per_item": 7.5},
    {"id": "sql", "name": "SQL题", "score_per_item": 16.67},
    {"id": "code", "name": "编程题", "score_per_item": 10},
    {"id": "short_answer", "name": "简答题", "score_per_item": 5},
    {"id": "essay", "name": "论述题", "score_per_item": 10},
]


def get_question_type_by_id(type_id):
    for q_type in question_types:
        if q_type["id"] == type_id:
            return q_type
    return None


def get_all_question_types():
    return question_types
