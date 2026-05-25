"""Redis 连接与扫码登录状态存储。"""

import json
import os
import time
import uuid

_redis_client = None

SCAN_PREFIX = "scan:"
SCAN_TTL = 600


def get_redis():
    global _redis_client
    if _redis_client is None:
        import redis

        url = os.environ.get("REDIS_URL", "redis://localhost:6379/0")
        _redis_client = redis.from_url(url, decode_responses=True)
    return _redis_client


def ping_redis():
    try:
        return get_redis().ping()
    except Exception:
        return False


def create_scan_code():
    code = str(uuid.uuid4())[:8]
    data = {"created_at": time.time(), "status": "waiting", "student_info": None}
    get_redis().setex(f"{SCAN_PREFIX}{code}", SCAN_TTL, json.dumps(data, ensure_ascii=False))
    return code


def get_scan_status(code):
    raw = get_redis().get(f"{SCAN_PREFIX}{code}")
    if not raw:
        return None
    return json.loads(raw)


def complete_scan(code, student_id, student_name):
    key = f"{SCAN_PREFIX}{code}"
    raw = get_redis().get(key)
    if not raw:
        return False
    data = json.loads(raw)
    data["status"] = "completed"
    data["student_info"] = {"student_id": student_id, "student_name": student_name}
    get_redis().setex(key, SCAN_TTL, json.dumps(data, ensure_ascii=False))
    return True


def delete_scan_code(code):
    get_redis().delete(f"{SCAN_PREFIX}{code}")
