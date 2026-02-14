import os
import hashlib
from trek.config import REPO_DIR, HEAD_FILE, IGNORE_FILE

def hash_content(content: bytes):
    return hashlib.sha1(content).hexdigest()

def is_repo():
    return os.path.exists(REPO_DIR)

def is_ignored(file_path):
    if not os.path.exists(IGNORE_FILE):
        return False
    with open(IGNORE_FILE, "r") as f:
        patterns = [p.strip() for p in f.readlines()]
    return any(pattern and file_path.endswith(pattern) for pattern in patterns)

def get_current_head():
    if not os.path.exists(HEAD_FILE):
        return None
    with open(HEAD_FILE, "r") as f:
        head = f.read().strip()
    if head.startswith("ref: "):
        branch_path = os.path.join(REPO_DIR, head[5:])
        if os.path.exists(branch_path):
            with open(branch_path, "r") as bf:
                return bf.read().strip()
    return head

def write_head(commit_hash):
    with open(HEAD_FILE, "r") as f:
        head = f.read().strip()
    if head.startswith("ref: "):
        branch_path = os.path.join(REPO_DIR, head[5:])
        with open(branch_path, "w") as bf:
            bf.write(commit_hash)
    else:
        with open(HEAD_FILE, "w") as f:
            f.write(commit_hash)
