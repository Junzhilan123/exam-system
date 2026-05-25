import copy
import json
import os
import time

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
MEMBERS_FILE = os.path.join(DATA_DIR, "members.json")

member_levels = [
    {
        "id": "guest",
        "name": "游客",
        "description": "未注册用户，仅能浏览",
        "icon": "👤",
        "color": "gray",
        "max_exams": 1,
        "features": ["基础考试"],
    },
    {
        "id": "free",
        "name": "免费会员",
        "description": "注册用户，享受基础服务",
        "icon": "⭐",
        "color": "green",
        "max_exams": 10,
        "features": ["基础考试", "成绩记录", "错题解析"],
    },
    {
        "id": "vip",
        "name": "VIP会员",
        "description": "付费会员，享受高级服务",
        "icon": "👑",
        "color": "gold",
        "max_exams": 50,
        "features": ["基础考试", "成绩记录", "错题解析", "模拟考试", "题库下载"],
    },
    {
        "id": "admin",
        "name": "管理员",
        "description": "系统管理员",
        "icon": "🔧",
        "color": "red",
        "max_exams": -1,
        "features": ["全部功能"],
    },
]

_DEFAULT_MEMBERS = [
    {
        "id": 1,
        "student_id": "20252310820001",
        "student_name": "张三",
        "wechat_id": "zhangsan_wx",
        "member_level": "free",
        "member_since": "2026-01-15",
        "exams_taken": 5,
        "total_score": 420,
        "status": "active",
    },
    {
        "id": 2,
        "student_id": "20252310820002",
        "student_name": "李四",
        "wechat_id": "lisi_wx",
        "member_level": "vip",
        "member_since": "2026-02-20",
        "exams_taken": 3,
        "total_score": 285,
        "status": "active",
    },
    {
        "id": 3,
        "student_id": "20252310820003",
        "student_name": "管理员",
        "wechat_id": "admin_wx",
        "member_level": "admin",
        "member_since": "2026-01-01",
        "exams_taken": 0,
        "total_score": 0,
        "status": "active",
    },
]


def _save():
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(MEMBERS_FILE, "w", encoding="utf-8") as f:
        json.dump({"members": members}, f, ensure_ascii=False, indent=2)


def _load():
    if os.path.exists(MEMBERS_FILE):
        with open(MEMBERS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("members", [])
    saved = copy.deepcopy(_DEFAULT_MEMBERS)
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(MEMBERS_FILE, "w", encoding="utf-8") as f:
        json.dump({"members": saved}, f, ensure_ascii=False, indent=2)
    return saved


members = _load()


def get_member_level(level_id):
    for level in member_levels:
        if level["id"] == level_id:
            return level
    return member_levels[0]


def add_member(student_id, student_name, wechat_id, level="free"):
    next_id = max((m["id"] for m in members), default=0) + 1
    member = {
        "id": next_id,
        "student_id": student_id,
        "student_name": student_name,
        "wechat_id": wechat_id,
        "member_level": level,
        "member_since": time.strftime("%Y-%m-%d"),
        "exams_taken": 0,
        "total_score": 0,
        "status": "active",
    }
    members.append(member)
    _save()
    return member


def get_member_by_student_id(student_id):
    for member in members:
        if member["student_id"] == student_id:
            return member
    return None


def get_member_by_wechat_id(wechat_id):
    for member in members:
        if member["wechat_id"] == wechat_id:
            return member
    return None


def update_member_score(student_id, score):
    member = get_member_by_student_id(student_id)
    if member:
        member["exams_taken"] += 1
        member["total_score"] += score
        _save()
    return member


def update_member_level(member_id, new_level):
    for member in members:
        if member["id"] == member_id:
            member["member_level"] = new_level
            _save()
            return member
    return None


def update_member_status(member_id, status):
    for member in members:
        if member["id"] == member_id:
            member["status"] = status
            _save()
            return member
    return None


def get_all_members():
    return members


def get_members_by_level(level):
    return [m for m in members if m["member_level"] == level]


def delete_member(member_id):
    global members
    members = [m for m in members if m["id"] != member_id]
    _save()
    return True
