import os

PROJECT_NAME = input("Enter the package/project name :")


def create_readme():
    try:
        if "README.md" not in os.listdir():
            with open("README.md", 'w') as file:
                file.write(f"""
## **{PROJECT_NAME} Project**  

## Step 1- Create a conda environment after opening the repository

```bash
conda create -n sensor python=3.7.6 -y
```

```bash
conda activate sensor
```

```CMD
conda create -p venv python==3.7 -y
```

## Step 2 Install requirements.txt
```
pip install -r .\\requirements.txt
```
                """)
                file.close()
        else:
            print("README.md file already exists! Try with different filename")
    except Exception as e:
        print("README.md file already exists! Try with different filename")


def create_licence():
    try:
        if "LICENCE" not in os.listdir():
            with open("LICENCE", 'w') as file:
                file.write("""
MIT License

Copyright (c) 2023 Aman Gupta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

                """)
                file.close()
        else:
            print("LICENCE file already exists! Try with different filename")
    except Exception as e:
        print("LICENCE file already exists! Try with different filename")


def create_setup():
    try:
        if "setup.py" not in os.listdir():
            with open("setup.py", 'w') as file:
                file.write("""
import setuptools
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."


def get_requirements() -> List[str]:

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\\n", "") for requirement_name in requirement_list]

    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = f""
USER_NAME = ""
PROJECT_NAME = ""

setuptools.setup(
    name=f"{PROJECT_NAME}",
    version="0.0.1",
    author=USER_NAME,
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
               
                """)
                file.close()
        else:
            print("setup.py file already exists! Try with different filename")
    except Exception as e:
        print("setup.py file already exists! Try with different filename")


def create_requirements():
    try:
        if "requirements.txt" not in os.listdir():
            with open("requirements.txt", 'w') as file:
                file.write("""
numpy
joblib
pandas
typing
-e .
                """)
                file.close()
        else:
            print("requirements.txt file already exists! Try with different filename")
    except Exception as e:
        print("requirements.txt file already exists! Try with different filename")


def create_gitignore():
    try:
        if ".gitignore" not in os.listdir():
            with open(".gitignore", 'w') as file:
                file.write("""
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class
artifact
# C extensions
*.so
prediction
saved_models
demotest.py
logs
artifacts
raw_data
# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/
                """)
                file.close()
        else:
            print(".gitignore file already exists! Try with different filename")
    except Exception as e:
        print(".gitignore file already exists! Try with different filename")


def create_file(filename="default"):
    try:
        if f"{filename}.py" not in os.listdir():
            with open(f"{filename}.py", 'a') as file:
                file.close()
        else:
            print(f"{filename} file already exists! Try with different filename")
    except Exception as e:
        print(f"{filename} file already exists! Try with different file name")


def create_dir(dirname="src"):
    try:
        if f"{dirname}" not in os.listdir():
            os.mkdir(dirname)
        else:
            print(f"{dirname} folder already exists! Try with different filename")
    except Exception as e:
        print(f"{dirname} folder already exists! Try with different file name")


def make_project_structure(PROJECT_NAME):
    try:
        create_file("main")
        create_gitignore()
        create_licence()

        create_requirements()
        create_readme()
        create_setup()

        create_dir(PROJECT_NAME)
        os.chdir(PROJECT_NAME)
        path = os.getcwd()

        create_dir(dirname="components")
        create_dir(dirname="entity")
        create_dir(dirname="pipeline")

        create_file("__init__")
        create_file("config")
        create_file("exception")
        create_file("logger")
        create_file("predictor")
        create_file("utils")

        os.chdir(path+"\components")
        create_file("__init__")
        create_file("data_ingestion")
        create_file("data_transformation")
        create_file("data_validation")
        create_file("model_evaluation")
        create_file("model_pusher")
        create_file("model_trainer")

        os.chdir(path+"\pipeline")
        create_file("__init__")
        create_file("artifact_entity")
        create_file("config_entity")

        os.chdir(path+"\entity")
        create_file("__init__")
        create_file("batch_prediction")
        create_file("training_pipeline")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    make_project_structure(PROJECT_NAME)
