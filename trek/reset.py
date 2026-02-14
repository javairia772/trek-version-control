import os, json
from colorama import Fore
from trek.config import *
from trek.utils import get_current_head, write_head
from trek.commit import commit

undo_stack = []
redo_stack = []

def reset(commit_hash, hard=False):
    from os.path import join
    from trek.utils import hash_content
    from trek.dag import walk_dag

    commit_path = join(OBJECTS_DIR, commit_hash)
    if not os.path.exists(commit_path):
        print(f"{Fore.RED}Commit {commit_hash} not found")
        return

    if hard:
        # Load tree
        with open(commit_path,"r") as f:
            lines = f.readlines()
        tree_line = next((l for l in lines if l.startswith("tree ")),None)
        if tree_line:
            tree_hash = tree_line.strip().split(" ")[1]
            tree_path = join(OBJECTS_DIR, tree_hash)
            if os.path.exists(tree_path):
                with open(tree_path,"r") as tf:
                    for l in tf.readlines():
                        file_hash, file_name = l.strip().split(" ")
                        obj_path = join(OBJECTS_DIR, file_hash)
                        with open(obj_path,"rb") as of:
                            content = of.read()
                        with open(file_name,"wb") as wf:
                            wf.write(content)
    write_head(commit_hash)
    print(f"{Fore.GREEN}Reset to {commit_hash[:7]}")
