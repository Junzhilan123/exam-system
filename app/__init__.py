from flask import Flask
from flask_cors import CORS
from flask_session import Session
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_dir = os.path.join(base_dir, "templates")
static_dir = os.path.join(base_dir, "static")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "exam_system_secret_key")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = True
app.config["SESSION_KEY_PREFIX"] = "exam_session:"

redis_url = os.environ.get("REDIS_URL")
if redis_url:
    import redis

    app.config["SESSION_TYPE"] = "redis"
    app.config["SESSION_REDIS"] = redis.from_url(redis_url, decode_responses=False)
else:
    session_dir = os.path.join(base_dir, "flask_session")
    os.makedirs(session_dir, exist_ok=True)
    app.config["SESSION_TYPE"] = "filesystem"
    app.config["SESSION_FILE_DIR"] = session_dir

Session(app)
CORS(app)

from app.config import SYSTEM_NAME


@app.context_processor
def inject_globals():
    return {"system_name": SYSTEM_NAME}


from app import routes
