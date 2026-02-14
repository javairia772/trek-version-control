import os, json
from datetime import datetime
from colorama import Fore
from trek.config import *
from trek.utils import hash_content, is_repo, get_current_head, write_head

def commit(message, author="User <user@example.com>"):
    if not is_repo():
        print(f"{Fore.RED}Not a trek repository!")
        return

    if not os.path.exists(INDEX_FILE):
        print(f"{Fore.RED}Nothing to commit.")
        return

    with open(INDEX_FILE, "r") as f:
        index = json.load(f)

    if not index:
        print(f"{Fore.RED}Nothing to commit.")
        return

    parent = get_current_head()
    tree_content = "\n".join([f"{h} {f}" for f, h in index.items()])
    tree_hash = hash_content(tree_content.encode())
    tree_path = os.path.join(OBJECTS_DIR, tree_hash)
    if not os.path.exists(tree_path):
        with open(tree_path, "w") as f:
            f.write(tree_content)

    commit_content = f"tree {tree_hash}\n"
    if parent:
        commit_content += f"parent {parent}\n"
    commit_content += f"author {author}\n"
    commit_content += f"date {datetime.now()}\n\n{message}"

    commit_hash = hash_content(commit_content.encode())
    commit_path = os.path.join(OBJECTS_DIR, commit_hash)
    with open(commit_path, "w") as f:
        f.write(commit_content)

    write_head(commit_hash)

    with open(INDEX_FILE, "w") as f:
        json.dump({}, f)

    print(f"{Fore.YELLOW}[{commit_hash[:7]}] {message}")
