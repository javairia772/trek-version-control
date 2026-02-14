import os, json
from colorama import Fore
from trek.config import *
from trek.utils import hash_content, is_repo, is_ignored

def add(files):
    if not is_repo():
        print(f"{Fore.RED}Not a trek repository!")
        return

    index = {}
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "r") as f:
            index = json.load(f)

    for file in files:
        if is_ignored(file):
            print(f"{Fore.YELLOW}{file} ignored.")
            continue

        if not os.path.exists(file):
            print(f"{Fore.RED}{file} not found.")
            continue

        with open(file, "rb") as f:
            content = f.read()
            file_hash = hash_content(content)

        object_path = os.path.join(OBJECTS_DIR, file_hash)
        if not os.path.exists(object_path):
            with open(object_path, "wb") as obj:
                obj.write(content)

        index[file] = file_hash

    with open(INDEX_FILE, "w") as f:
        json.dump(index, f, indent=2)

    print(f"{Fore.GREEN}Files added to staging area.")
