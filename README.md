# Trek – Mini Git Clone 🌌
*Simplified Git-inspired version control system implemented in Python.*


[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)

Trek 1.0 lets you learn Git internals by doing: commits, branching, merging, DAG visualization, undo/redo, and more—all in a simple Python CLI.



---

## Features

- **Repository Initialization:** `trek> init`
- **Staging & Commit:** `trek> add file.py` → `trek> commit "message"`
- **Branching:** `trek> branch feature` → `trek> checkout master`
- **Merging:** `trek> merge feature` (detects conflicts)
- **Undo / Redo / Reset:** `trek> undo`, `trek> redo`, `trek> reset <commit_hash>`
- **DAG Visualization:** `trek> graph`
- **Status Check:** `trek> status`

---
## Installation
### Users

```bash
git clone https://github.com/javairia772/trek-version-control.git
cd trek-version-control
pip install colorama
python main.py
```

### Developers

1. Clone the repository
    ```bash
    git clone https://github.com/javairia772/trek-version-control.git
    cd trek-version-control
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```


4. Edit files in trek/ modules or main.py.

5. Test your changes with:
    ```bash
    python main.py
    ```
    
---


## 📂 Project Structure

```text
Trek1.0/
 ├─ main.py             # CLI entry point
 ├─ requirements.txt
 ├─ README.md
 ├─ trek/
 │   ├─ __init__.py
 │   ├─ config.py       # Constants like .trek paths
 │   ├─ utils.py        # Helper functions
 │   ├─ repository.py   # init repo
 │   ├─ staging.py      # add/stage files
 │   ├─ commit.py       # commit logic
 │   ├─ branch.py       # branch & checkout
 │   ├─ merge.py        # merge logic
 │   ├─ reset.py        # undo/redo/reset
 │   └─ dag.py          # commit DAG visualization
 └─ .gitignore
 ```
 ---
 
## Usage

-  #### Initialize repository
    ```bash
    trek> init
    ```

-  #### Stage and commit files
    ```bash
    trek> add file1.py
    trek> commit "Add file1"
    ```

- #### Branching and switching
    ```bash
    trek> branch feature
    trek> add file2.py
    trek> commit "Add file2"
    trek> checkout master
    ```
- #### Merge branches
    ```bash
    trek> merge feature
    ```

- #### Visualize history
    ```bash
    trek> graph
    ```

- #### Undo / Redo / Reset
    ```bash
    trek> undo
    trek> redo
    trek> reset <commit_hash>
    ```
---
## 🧠 Learning Outcomes
* Understand version control internals
* Learn commit objects, trees, and branches
* Explore DAG structure and merges
* Practice Python file I/O, hashing, and CLI design

---

#### ⚠ Known Issues

* Merge conflict resolution is manual only
* Only supports text files currently
* Large repositories may slow down DAG visualization

---

## 🤝 Contributing

- Follow PEP8 coding standards
- Write descriptive commit messages
- Document new features in README.md
---
