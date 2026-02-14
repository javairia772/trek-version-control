Trek – Mini Git Clone 🌌

Trek 1.0 is a simplified Git-inspired version control system implemented in Python. It supports commits, branching, merging, DAG visualization, and undo/redo operations—perfect for learning the inner workings of Git!

Features

Repository Initialization
Initialize a .trek repository in any directory:

trek> init


Staging & Commit
Stage files and save commits:

trek> add file1.py file2.py
trek> commit "Initial commit"


Branching
Create, list, and switch branches:

trek> branch               # List all branches
trek> branch feature       # Create & switch to new branch
trek> checkout master      # Switch back to master


Merge
Merge another branch into the current branch (detects conflicts):

trek> merge feature


Undo / Redo / Reset
Navigate history or reset repository to a previous commit:

trek> undo
trek> redo
trek> reset <commit_hash>


DAG Visualization
Show an ASCII commit graph with branches:

trek> graph


Example:

* a1b2c3d (master)
    * 5f6e7d8 (feature)
        * 1a2b3c4


Status
Check current HEAD and branch:

trek> status


Exit CLI

trek> exit

Installation

Clone this repository:

git clone https://github.com/yourusername/trek.git
cd trek


Install dependencies (optional for colored output):

pip install colorama


Run the CLI:

python main.py

Project Structure
trek/
 ├─ __init__.py
 ├─ config.py       # Constants like .trek paths
 ├─ utils.py        # Helper functions
 ├─ repository.py   # init repo
 ├─ staging.py      # add/stage files
 ├─ commit.py       # commit logic
 ├─ branch.py       # branch & checkout
 ├─ merge.py        # merge logic
 ├─ reset.py        # undo/redo/reset
 ├─ dag.py          # commit DAG visualization
main.py             # CLI entry point

How to Use

Initialize a new repo:

trek> init


Stage and commit files:

trek> add file1.py
trek> commit "Add file1"


Create a branch and switch to it:

trek> branch feature
trek> add file2.py
trek> commit "Add file2"


Merge branches:

trek> checkout master
trek> merge feature


Visualize history:

trek> graph

Learning Outcomes

Understand version control internals

Learn commit objects, trees, and branches

Explore DAG structure and merges

Practice Python file I/O, hashing, and CLI design

License

MIT License – free to use and modify