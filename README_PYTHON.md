# Python & Jupyter Setup for This Project

This project uses Python 3.11 and Jupyter notebooks (.ipynb).
All notebooks should run in an isolated environment to ensure reproducibility.

1. Create a Python Environment

```bash
bash

# From project root
python3.11 -m venv venv
```

2. Activate the Environment

```bash
bash

# macOS/Linux with zsh or bash
source venv/bin/activate

# To deactivate
deactivate
```

3. Install Required Packages

```bash
bash

# The project dependencies are listed in requirements.txt
pip install -r requirements.txt
```

4. Generate requirements.txt

```bash
bash

# If you install new packages, keep the list updated:
pip freeze > requirements.txt
```

5. Register the Environment as a Notebook Kernel

```bash
bash

python -m ipykernel install --user --name=proj_env --display-name "Python 3.11 (proj_env)"
```

6. Use in VS Code Notebooks

- Open a .ipynb file.

- Click the kernel selector (top-right).

- Choose Python 3.11 (proj_env).

Verify:

```python
python

import sys
print(sys.executable)
print(sys.version)
```

- sys.executable should point to .../venv/bin/python.
- All installed packages are available in the notebook.