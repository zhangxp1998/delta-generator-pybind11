from glob import glob
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext
from distutils.spawn import find_executable
import os
import subprocess
from pathlib import Path
import sys

__version__ = "0.0.1"

# Find the Protocol Compiler.
if 'PROTOC' in os.environ and os.path.exists(os.environ['PROTOC']):
    protoc = os.environ['PROTOC']
else:
    protoc = find_executable("protoc")

def generate_proto(source):
  """Invokes the Protocol Compiler to generate a pb.h from the given
  .proto file.  Does nothing if the output already exists and is newer than
  the input."""

  header = Path("src/") / source.replace(".proto", ".pb.h")
  cc_file = Path("src/") / source.replace(".proto", ".pb.cc")
  outputs = [header, cc_file]
  def should_regenerate(path):
      return not os.path.exists(path) or \
        os.path.getmtime(source) > os.path.getmtime(path)
  regenerate = all([should_regenerate(f) for f in outputs])

  if regenerate:
    print("Generating %s ..." % outputs)

    if not os.path.exists(source):
      sys.stderr.write("Can't find required file: %s\n" % source)
      sys.exit(-1)

    if protoc == None:
      sys.stderr.write(
          "protoc is not installed nor found.  Please compile it "
          "or install the binary package.\n")
      sys.exit(-1)

    protoc_command = [ protoc, "-I./src", "-I.", "--cpp_out=src", source ]
    print(protoc_command)
    if subprocess.call(protoc_command) != 0:
      sys.exit(-1)

generate_proto("src/update_metadata.proto")

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
