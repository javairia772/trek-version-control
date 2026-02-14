import os
from colorama import Fore
from trek.config import OBJECTS_DIR
from trek.utils import get_current_head, write_head, hash_content

def merge(target_commit):
    current_commit = get_current_head()
    if current_commit == target_commit:
        print(f"{Fore.CYAN}Already up-to-date")
        return

    print(f"{Fore.GREEN}Merging {target_commit[:7]} into {current_commit[:7]}")

    # Load trees
    def load_tree(commit_hash):
        commit_path = os.path.join(OBJECTS_DIR, commit_hash)
        if not os.path.exists(commit_path):
            return {}
        with open(commit_path,"r") as f:
            lines = f.readlines()
        tree_line = next((l for l in lines if l.startswith("tree ")), None)
        if not tree_line: return {}
        tree_hash = tree_line.strip().split(" ")[1]
        tree_path = os.path.join(OBJECTS_DIR, tree_hash)
        if not os.path.exists(tree_path): return {}
        with open(tree_path,"r") as tf:
            return dict(l.strip().split(" ",1) for l in tf.readlines())
    current_tree = load_tree(current_commit)
    target_tree = load_tree(target_commit)

    # Simple merge (fast-forward if possible)
    for file, hash_val in target_tree.items():
        if file not in current_tree:
            # New file → copy to current
            obj_path = os.path.join(OBJECTS_DIR, hash_val)
            with open(obj_path,"rb") as f:
                content = f.read()
            with open(file,"wb") as f:
                f.write(content)
            current_tree[file] = hash_val
        elif current_tree[file] != hash_val:
            # Conflict → add markers
            curr_path = os.path.join(OBJECTS_DIR, current_tree[file])
            with open(curr_path,"r") as f:
                curr_content = f.read()
            target_path = os.path.join(OBJECTS_DIR, hash_val)
            with open(target_path,"r") as f:
                target_content = f.read()
            with open(file,"w") as f:
                f.write(f"<<<<<<< HEAD\n{curr_content}\n=======\n{target_content}\n>>>>>>>")
            print(f"{Fore.RED}Conflict in {file}")

    # Create new merge commit
    from trek.commit import commit
    commit(f"Merge {target_commit[:7]} into current branch")
    print(f"{Fore.GREEN}Merge completed.")
