import os
from colorama import Fore
from trek.config import REPO_DIR, REFS_DIR, HEAD_FILE, OBJECTS_DIR
from trek.utils import get_current_head, write_head

def branch(name=None):
    """
    - If name is None → list all branches
    - If name is provided → create branch and switch to it
    """
    if not os.path.exists(REPO_DIR):
        print(f"{Fore.RED}Not a trek repository!")
        return

    if name is None:
        # List branches
        branches = os.listdir(REFS_DIR)
        if not branches:
            print(f"{Fore.RED}No branches found.")
            return
        print(f"{Fore.CYAN}Branches:")
        for b in branches:
            # mark current branch
            head_ref = None
            with open(HEAD_FILE,"r") as f:
                ref = f.read().strip()
            if ref.startswith("ref: "):
                head_ref = ref[5:].split("/")[-1]
            prefix = "*" if b == head_ref else " "
            print(f" {prefix} {Fore.YELLOW}{b}")
        return

    # Create branch
    current_commit = get_current_head()
    new_branch_path = os.path.join(REFS_DIR, name)

    if os.path.exists(new_branch_path):
        # Branch exists → switch to it
        with open(HEAD_FILE, "w") as f:
            f.write(f"ref: refs/heads/{name}")
        print(f"{Fore.GREEN}Switched to branch '{Fore.YELLOW}{name}{Fore.GREEN}'")
        checkout_branch_files(current_commit)
        return

    # Create branch pointing to current commit
    with open(new_branch_path, "w") as f:
        f.write(current_commit)

    # Switch HEAD to new branch
    with open(HEAD_FILE, "w") as f:
        f.write(f"ref: refs/heads/{name}")

    print(f"{Fore.GREEN}Created and switched to new branch '{Fore.YELLOW}{name}{Fore.GREEN}'")
    checkout_branch_files(current_commit)


def checkout_branch(branch_name):
    """
    Switches HEAD to the specified branch and updates working directory.
    """
    branch_path = os.path.join(REFS_DIR, branch_name)
    if not os.path.exists(branch_path):
        print(f"{Fore.RED}Branch '{Fore.YELLOW}{branch_name}{Fore.RED}' does not exist")
        return

    with open(branch_path, "r") as f:
        commit_hash = f.read().strip()

    # Update HEAD
    with open(HEAD_FILE, "w") as f:
        f.write(f"ref: refs/heads/{branch_name}")

    checkout_branch_files(commit_hash)
    print(f"{Fore.GREEN}Checked out branch '{Fore.YELLOW}{branch_name}{Fore.GREEN}'")


def checkout_branch_files(commit_hash):
    """
    Updates the working directory files to match the branch commit.
    """
    from trek.utils import is_repo

    if not is_repo() or not commit_hash:
        return

    commit_path = os.path.join(OBJECTS_DIR, commit_hash)
    if not os.path.exists(commit_path):
        print(f"{Fore.RED}Commit '{commit_hash[:7]}' does not exist.")
        return

    # Read commit tree
    with open(commit_path, "r") as f:
        lines = f.readlines()
    tree_line = next((l for l in lines if l.startswith("tree ")), None)
    if not tree_line:
        return
    tree_hash = tree_line.strip().split(" ")[1]
    tree_path = os.path.join(OBJECTS_DIR, tree_hash)
    if not os.path.exists(tree_path):
        return

    # Update files
    with open(tree_path, "r") as f:
        for line in f.readlines():
            file_hash, file_name = line.strip().split(" ")
            obj_path = os.path.join(OBJECTS_DIR, file_hash)
            if os.path.exists(obj_path):
                with open(obj_path, "rb") as obj:
                    content = obj.read()
                with open(file_name, "wb") as wf:
                    wf.write(content)
