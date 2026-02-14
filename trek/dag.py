import os
from trek.config import OBJECTS_DIR, REPO_DIR, HEAD_FILE, REFS_DIR

def build_commit_graph():
    """
    Builds a DAG of commits:
    - keys: commit hashes
    - values: parent commit hashes (can be None or multiple for merges)
    """
    graph = {}
    commits_seen = set()

    # Traverse all objects to find commits
    for obj_file in os.listdir(OBJECTS_DIR):
        obj_path = os.path.join(OBJECTS_DIR, obj_file)
        if not os.path.isfile(obj_path):
            continue
        with open(obj_path, "r") as f:
            content = f.read()
        if content.startswith("tree "):
            lines = content.splitlines()
            parents = [l.split(" ")[1] for l in lines if l.startswith("parent ")]
            graph[obj_file] = parents if parents else []
            commits_seen.add(obj_file)
    return graph


def get_branches():
    """
    Returns a dict of branch_name -> commit_hash
    """
    branches = {}
    for b in os.listdir(REFS_DIR):
        path = os.path.join(REFS_DIR, b)
        if os.path.isfile(path):
            with open(path, "r") as f:
                commit = f.read().strip()
            branches[b] = commit
    return branches


def print_graph(start_commit):
    """
    Prints an ASCII DAG of commits starting from HEAD.
    Marks branch names pointing to commits.
    """
    graph = build_commit_graph()
    branches = get_branches()

    visited = set()
    stack = [(start_commit, 0)]  # (commit_hash, level)

    lines = []

    while stack:
        commit, level = stack.pop()
        if commit in visited:
            continue
        visited.add(commit)

        indent = " " * (level * 4)
        branch_labels = [b for b, c in branches.items() if c == commit]
        label = f" ({','.join(branch_labels)})" if branch_labels else ""
        lines.append(f"{indent}* {commit[:7]}{label}")

        for parent in graph.get(commit, []):
            stack.append((parent, level + 1))

    # Print in topological order
    for line in reversed(lines):
        print(line)
