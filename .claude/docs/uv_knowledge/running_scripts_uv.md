---
# Smart Librarian Export (v2.0)
- Page Number: 7
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/guides/scripts
- Page Title: Running scripts | uv
- Semantic Filename: running_scripts_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 19,055 characters
---

# Running scripts | uv

[ Skip to content ](https://docs.astral.sh/uv/guides/scripts/#running-scripts)
# [Running scripts](https://docs.astral.sh/uv/guides/scripts/#running-scripts)
A Python script is a file intended for standalone execution, e.g., with `python <script>.py`. Using uv to execute scripts ensures that script dependencies are managed without manually managing environments.
Note
If you are not familiar with Python environments: every Python installation has an environment that packages can be installed in. Typically, creating [declarative](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies) approach to dependencies.
## [Running a script without dependencies](https://docs.astral.sh/uv/guides/scripts/#running-a-script-without-dependencies)
If your script has no dependencies, you can execute it with `uv run`:
example.py```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-0-1)print("Hello world")

```

```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-1-1)$ uv[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-1-2)Hello world

```

Similarly, if your script depends on a module in the standard library, there's nothing more to do:
example.py```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-2-1)import os
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-2-2)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-2-3)print(os.path.expanduser("~"))

```

```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-3-1)$ uv[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-3-2)/Users/astral

```

Arguments may be provided to the script:
example.py```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-4-1)import sys
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-4-2)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-4-3)print(" ".join(sys.argv[1:]))

```

```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-5-1)$ uvtest
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-5-2)test
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-5-3)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-5-4)$ uv[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-5-5)hello world!

```

Additionally, your script can be read directly from stdin:
```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-6-1)$ echo'print("hello world!")'|
```

Or, if your shell supports 
```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-7-1)uv<<EOF
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-7-2)print("hello world!")
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-7-3)EOF

```

Note that if you use `uv run` in a _project_ , i.e., a directory with a `pyproject.toml`, it will install the current project before running the script. If your script does not depend on the project, use the `--no-project` flag to skip this:
```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-8-1)$ # Note: the `--no-project` flag must be provided _before_ the script name.
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-8-2)$ uv
```

See the [projects guide](https://docs.astral.sh/uv/guides/projects/) for more details on working in projects.
## [Running a script with dependencies](https://docs.astral.sh/uv/guides/scripts/#running-a-script-with-dependencies)
When your script requires other packages, they must be installed into the environment that the script runs in. uv prefers to create these environments on-demand instead of using a long-lived virtual environment with manually managed dependencies. This requires explicit declaration of dependencies that are required for the script. Generally, it's recommended to use a [project](https://docs.astral.sh/uv/guides/projects/) or [inline metadata](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies) to declare dependencies, but uv supports requesting dependencies per invocation as well.
For example, the following script requires `rich`.
example.py```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-9-1)import time
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-9-2)from rich.progress import track
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-9-3)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-9-4)for i in track(range(20), description="For example:"):
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-9-5)    time.sleep(0.05)

```

If executed without specifying a dependency, this script will fail:
```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-10-1)$ uv[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-10-2)Traceback (most recent call last):
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-10-3)  File "/Users/astral/example.py", line 2, in <module>
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-10-4)    from rich.progress import track
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-10-5)ModuleNotFoundError: No module named 'rich'

```

Request the dependency using the `--with` option:
```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-11-1)$ uv[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-11-2)For example: ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:01

```

Constraints can be added to the requested dependency if specific versions are needed:
```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-12-1)$ uv'rich>12,<13'
```

Multiple dependencies can be requested by repeating with `--with` option.
Note that if `uv run` is used in a _project_ , these dependencies will be included _in addition_ to the project's dependencies. To opt-out of this behavior, use the `--no-project` flag.
## [Creating a Python script](https://docs.astral.sh/uv/guides/scripts/#creating-a-python-script)
Python recently added a standard format for `uv init --script` to initialize scripts with the inline metadata:
```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-13-1)$ uv3.12

```

## [Declaring script dependencies](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies)
The inline metadata format allows the dependencies for a script to be declared in the script itself.
uv supports adding and updating inline script metadata for you. Use `uv add --script` to declare the dependencies for the script:
```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-14-1)$ uv'requests<3''rich'

```

This will add a `script` section at the top of the script declaring the dependencies using TOML:
example.py```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-15-1)# /// script
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-15-2)# dependencies = [
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-15-3)#   "requests<3",
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-15-4)#   "rich",
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-15-5)# ]
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-15-6)# ///
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-15-7)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-15-8)import requests
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-15-9)from rich.pretty import pprint
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-15-10)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-15-11)resp = requests.get("https://peps.python.org/api/peps.json")
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-15-12)data = resp.json()
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-15-13)pprint([(k, v["title"]) for k, v in data.items()][:10])

```

uv will automatically create an environment with the dependencies necessary to run the script, e.g.:
```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-16-1)$ uv[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-16-2)[
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-16-3)│   ('1', 'PEP Purpose and Guidelines'),
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-16-4)│   ('2', 'Procedure for Adding New Modules'),
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-16-5)│   ('3', 'Guidelines for Handling Bug Reports'),
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-16-6)│   ('4', 'Deprecation of Standard Modules'),
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-16-7)│   ('5', 'Guidelines for Language Evolution'),
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-16-8)│   ('6', 'Bug Fix Releases'),
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-16-9)│   ('7', 'Style Guide for C Code'),
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-16-10)│   ('8', 'Style Guide for Python Code'),
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-16-11)│   ('9', 'Sample Plaintext PEP Template'),
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-16-12)│   ('10', 'Voting Guidelines')
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-16-13)]

```

Important
When using inline script metadata, even if `uv run` is [used in a _project_](https://docs.astral.sh/uv/concepts/projects/run/), the project's dependencies will be ignored. The `--no-project` flag is not required.
uv also respects Python version requirements:
example.py```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-17-1)# /// script
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-17-2)# requires-python = ">=3.12"
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-17-3)# dependencies = []
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-17-4)# ///
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-17-5)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-17-6)# Use some syntax added in Python 3.12
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-17-7)type Point = tuple[float, float]
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-17-8)print(Point)

```

Note
The `dependencies` field must be provided even if empty.
`uv run` will search for and use the required Python version. The Python version will download if it is not installed — see the documentation on [Python versions](https://docs.astral.sh/uv/concepts/python-versions/) for more details.
## [Using a shebang to create an executable file](https://docs.astral.sh/uv/guides/scripts/#using-a-shebang-to-create-an-executable-file)
A shebang can be added to make a script executable without using `uv run` — this makes it easy to run scripts that are on your `PATH` or in the current folder.
For example, create a file called `greet` with the following contents
greet```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-18-1)#!/usr/bin/env -S uv run --script
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-18-2)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-18-3)print("Hello, world!")

```

Ensure that your script is executable, e.g., with `chmod +x greet`, then run the script:
```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-19-1)$ ./greet
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-19-2)Hello, world!

```

Declaration of dependencies is also supported in this context, for example:
example```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-20-1)#!/usr/bin/env -S uv run --script
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-20-2)#
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-20-3)# /// script
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-20-4)# requires-python = ">=3.12"
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-20-5)# dependencies = ["httpx"]
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-20-6)# ///
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-20-7)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-20-8)import httpx
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-20-9)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-20-10)print(httpx.get("https://example.com"))

```

## [Using alternative package indexes](https://docs.astral.sh/uv/guides/scripts/#using-alternative-package-indexes)
If you wish to use an alternative [package index](https://docs.astral.sh/uv/concepts/indexes/) to resolve dependencies, you can provide the index with the `--index` option:
```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-21-1)$ uv"https://example.com/simple"'requests<3''rich'

```

This will include the package data in the inline metadata:
```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-22-1)# [[tool.uv.index]]
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-22-2)# url = "https://example.com/simple"

```

If you require authentication to access the package index, then please refer to the [package index](https://docs.astral.sh/uv/concepts/indexes/) documentation.
## [Locking dependencies](https://docs.astral.sh/uv/guides/scripts/#locking-dependencies)
uv supports locking dependencies for PEP 723 scripts using the `uv.lock` file format. Unlike with projects, scripts must be explicitly locked using `uv lock`:
```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-23-1)$ uv
```

Running `uv lock --script` will create a `.lock` file adjacent to the script (e.g., `example.py.lock`).
Once locked, subsequent operations like `uv run --script`, `uv add --script`, `uv export --script`, and `uv tree --script` will reuse the locked dependencies, updating the lockfile if necessary.
If no such lockfile is present, commands like `uv export --script` will still function as expected, but will not create a lockfile.
## [Improving reproducibility](https://docs.astral.sh/uv/guides/scripts/#improving-reproducibility)
In addition to locking dependencies, uv supports an `exclude-newer` field in the `tool.uv` section of inline script metadata to limit uv to only considering distributions released before a specific date. This is useful for improving the reproducibility of your script when run at a later point in time.
The date should be specified as an `2006-12-02T02:07:43Z`).
example.py```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-24-1)# /// script
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-24-2)# dependencies = [
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-24-3)#   "requests",
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-24-4)# ]
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-24-5)# [tool.uv]
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-24-6)# exclude-newer = "2023-10-16T00:00:00Z"
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-24-7)# ///
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-24-8)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-24-9)import requests
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-24-10)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-24-11)print(requests.__version__)

```

## [Using different Python versions](https://docs.astral.sh/uv/guides/scripts/#using-different-python-versions)
uv allows arbitrary Python versions to be requested on each script invocation, for example:
example.py```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-25-1)import sys
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-25-2)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-25-3)print(".".join(map(str, sys.version_info[:3])))

```

```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-26-1)$ # Use the default Python version, may differ on your machine
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-26-2)$ uv[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-26-3)3.12.6

```

```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-27-1)$ # Use a specific Python version
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-27-2)$ uv3.10[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-27-3)3.10.15

```

See the [Python version request](https://docs.astral.sh/uv/concepts/python-versions/#requesting-a-version) documentation for more details on requesting Python versions.
## [Using GUI scripts](https://docs.astral.sh/uv/guides/scripts/#using-gui-scripts)
On Windows `uv` will run your script ending with `.pyw` extension using `pythonw`:
example.pyw```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-28-1)from tkinter import Tk, ttk
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-28-2)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-28-3)root = Tk()
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-28-4)root.title("uv")
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-28-5)frm = ttk.Frame(root, padding=10)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-28-6)frm.grid()
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-28-7)ttk.Label(frm, text="Hello World").grid(column=0, row=0)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-28-8)root.mainloop()

```

```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-29-1)PS> uv run example.pyw

```

![Run Result](https://docs.astral.sh/uv/assets/uv_gui_script_hello_world.png)
Similarly, it works with dependencies as well:
example_pyqt.pyw```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-30-1)import sys
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-30-2)from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-30-3)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-30-4)app = QApplication(sys.argv)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-30-5)widget = QWidget()
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-30-6)grid = QGridLayout()
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-30-7)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-30-8)text_label = QLabel()
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-30-9)text_label.setText("Hello World!")
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-30-10)grid.addWidget(text_label)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-30-11)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-30-12)widget.setLayout(grid)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-30-13)widget.setGeometry(100, 100, 200, 50)
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-30-14)widget.setWindowTitle("uv")
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-30-15)widget.show()
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-30-16)sys.exit(app.exec_())

```

```
[](https://docs.astral.sh/uv/guides/scripts/#__codelineno-31-1)PS> uv run --with PyQt5 example_pyqt.pyw

```

![Run Result](https://docs.astral.sh/uv/assets/uv_gui_script_hello_world_pyqt.png)
## [Next steps](https://docs.astral.sh/uv/guides/scripts/#next-steps)
To learn more about `uv run`, see the [command reference](https://docs.astral.sh/uv/reference/cli/#uv-run).
Or, read on to learn how to [run and install tools](https://docs.astral.sh/uv/guides/tools/) with uv.
December 9, 2025
