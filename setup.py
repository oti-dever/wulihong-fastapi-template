from distutils.core import setup

import toml
from Cython.Build import cythonize
from Cython.Compiler import Options

Options.docstrings = False

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

with open("pyproject.toml", encoding="utf-8") as f:
    pyproject = toml.load(f)
    poetry_config = pyproject["tool"]["poetry"]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name=poetry_config["name"],
    version=poetry_config["version"],
    description=poetry_config["description"],
    long_description=readme,
    author=poetry_config["authors"][0],
    ext_modules=cythonize(
        [
            "main.py",
            "app/**/*.py",
        ],
        compiler_directives={"language_level": 3},
    ),
)
