import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "backend")
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

os.chdir(BACKEND_DIR)

# Vercel filesystem is ephemeral; keep runtime files under /tmp
os.environ.setdefault("DATABASE_FILE", "/tmp/rag_chatbot.db")
os.environ.setdefault("VECTOR_DB_PATH", "/tmp/chroma_db")
os.environ.setdefault("UPLOAD_FOLDER", "/tmp/documents")

from simple_app import app as app
