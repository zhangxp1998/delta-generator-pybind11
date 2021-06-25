from glob import glob
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

__version__ = "0.0.1"

ext_modules = [
    Pybind11Extension(
        "delta_generator_pybind11",
        sorted(glob("src/*.cpp")),  # Sort source files for reproducibility
    ),
]

setup(
    name="delta_generator_pybind11",
    version = __version__,
    author="Kelvin Zhang",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
