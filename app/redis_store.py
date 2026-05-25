"""Redis 连接与扫码登录状态存储（Redis 不可用时回退到内存）。"""

import json
import os
import time
import uuid

_redis_client = None
_use_memory = False
_memory_store = {}

SCAN_PREFIX = "scan:"
SCAN_TTL = 600


def get_redis():
    global _redis_client, _use_memory
    if _use_memory:
        return None
    if _redis_client is None:
        try:
            import redis

            url = os.environ.get("REDIS_URL", "redis://localhost:6379/0")
            client = redis.from_url(url, decode_responses=True)
            client.ping()
            _redis_client = client
        except Exception:
            _use_memory = True
            return None
    return _redis_client


def ping_redis():
    return get_redis() is not None


def _memory_set(code, data):
    _memory_store[code] = {"expires": time.time() + SCAN_TTL, "data": data}


def _memory_get(code):
    entry = _memory_store.get(code)
    if not entry:
        return None
    if time.time() > entry["expires"]:
        _memory_store.pop(code, None)
        return None
    return entry["data"]


def _memory_delete(code):
    _memory_store.pop(code, None)


def create_scan_code():
    code = str(uuid.uuid4())[:8]
    data = {"created_at": time.time(), "status": "waiting", "student_info": None}
    client = get_redis()
    if client:
        client.setex(f"{SCAN_PREFIX}{code}", SCAN_TTL, json.dumps(data, ensure_ascii=False))
    else:
        _memory_set(code, data)
    return code


def get_scan_status(code):
    client = get_redis()
    if client:
        raw = client.get(f"{SCAN_PREFIX}{code}")
        if not raw:
            return None
        return json.loads(raw)
    return _memory_get(code)


def complete_scan(code, student_id, student_name):
    client = get_redis()
    key = f"{SCAN_PREFIX}{code}"
    if client:
        raw = client.get(key)
        if not raw:
            return False
        data = json.loads(raw)
        data["status"] = "completed"
        data["student_info"] = {"student_id": student_id, "student_name": student_name}
        client.setex(key, SCAN_TTL, json.dumps(data, ensure_ascii=False))
        return True

    data = _memory_get(code)
    if not data:
        return False
    data["status"] = "completed"
    data["student_info"] = {"student_id": student_id, "student_name": student_name}
    _memory_set(code, data)
    return True


def delete_scan_code(code):
    client = get_redis()
    if client:
        client.delete(f"{SCAN_PREFIX}{code}")
    else:
        _memory_delete(code)
