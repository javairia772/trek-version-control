import os

REPO_DIR = ".trek"
OBJECTS_DIR = os.path.join(REPO_DIR, "objects")
REFS_DIR = os.path.join(REPO_DIR, "refs", "heads")
TAGS_DIR = os.path.join(REPO_DIR, "refs", "tags")
HEAD_FILE = os.path.join(REPO_DIR, "HEAD")
INDEX_FILE = os.path.join(REPO_DIR, "index")
IGNORE_FILE = os.path.join(REPO_DIR, ".gitignore")
