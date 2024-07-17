from distutils.core import setup

from Cython.Build import cythonize
from Cython.Compiler import Options

Options.docstrings = False

setup(
    name="fastapi_server",
    ext_modules=cythonize(
        [
            "main.py",
            "src/**/*.py",
        ],
        compiler_directives={"language_level": 3},
    ),
)
