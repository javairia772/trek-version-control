import os
from colorama import Fore
from trek.config import *

def push(source, target):
    source_path = os.path.join(REFS_DIR, source)
    target_path = os.path.join(REFS_DIR, target)

    if not os.path.exists(source_path):
        print(f"{Fore.RED}Source branch not found.")
        return

    with open(source_path, "r") as s:
        commit = s.read().strip()

    with open(target_path, "w") as t:
        t.write(commit)

    print(f"{Fore.GREEN}Pushed {source} → {target}")
