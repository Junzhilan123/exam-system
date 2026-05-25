semesters = [
    {
        "id": 1,
        "name": "2026年春季学期",
        "code": "2026SP",
        "start_date": "2026-02-20",
        "end_date": "2026-06-30"
    },
    {
        "id": 2,
        "name": "2025年秋季学期",
        "code": "2025FA",
        "start_date": "2025-09-01",
        "end_date": "2026-01-20"
    },
    {
        "id": 3,
        "name": "2025年春季学期",
        "code": "2025SP",
        "start_date": "2025-02-23",
        "end_date": "2025-06-28"
    }
]

def get_semester_by_code(code):
    for semester in semesters:
        if semester['code'] == code:
            return semester
    return None

def get_all_semesters():
    return semesters
