import os
from colorama import Fore
from trek.config import *
from trek.utils import is_repo

def init():
    if is_repo():
        print(f"{Fore.RED}Repository already exists!")
        return

    os.makedirs(OBJECTS_DIR, exist_ok=True)
    os.makedirs(REFS_DIR, exist_ok=True)
    os.makedirs(TAGS_DIR, exist_ok=True)

    with open(os.path.join(REFS_DIR, "master"), "w") as f:
        f.write("")

    with open(HEAD_FILE, "w") as f:
        f.write("ref: refs/heads/master\n")

    with open(IGNORE_FILE, "w") as f:
        f.write("")

    print(f"{Fore.GREEN}Initialized empty Trek repository.")
