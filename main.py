import sys
from colorama import init
init(autoreset=True)

from trek.repository import init as init_repo
from trek.staging import add
from trek.commit import commit
from trek.branch import branch, checkout_branch
from trek.merge import merge
from trek.reset import reset, undo_stack, redo_stack
from trek.dag import print_graph
from trek.utils import get_current_head, is_repo

def run():
    print("🌌 Welcome to Trek – mini Git clone")
    while True:
        try:
            cmd = input("trek> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting Trek.")
            break

        if cmd == "":
            continue

        if cmd == "exit":
            print("Bye! 👋")
            break

        if cmd == "init":
            init_repo()
        elif cmd.startswith("add "):
            add(cmd.split()[1:])
        elif cmd.startswith("commit "):
            commit(cmd[7:])
        elif cmd.startswith("branch"):
            parts = cmd.split()
            branch(parts[1] if len(parts) > 1 else None)
        elif cmd.startswith("checkout "):
            parts = cmd.split()
            checkout_branch(parts[1])
        elif cmd.startswith("merge "):
            parts = cmd.split()
            merge(parts[1])
        elif cmd.startswith("reset "):
            parts = cmd.split()
            reset(parts[1], hard=True)
        elif cmd == "undo":
            if not undo_stack:
                print("Nothing to undo.")
                continue
            last = undo_stack.pop()
            redo_stack.append(get_current_head())
            reset(last, hard=True)
        elif cmd == "redo":
            if not redo_stack:
                print("Nothing to redo.")
                continue
            last = redo_stack.pop()
            undo_stack.append(get_current_head())
            reset(last, hard=True)
        elif cmd == "graph":
            head = get_current_head()
            print_graph(head)
        elif cmd == "status":
            # Simple status: show HEAD + branch
            if not is_repo():
                print("Not a trek repository!")
                continue
            head = get_current_head()
            print(f"Current HEAD: {head[:7]}")
        else:
            print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    run()
