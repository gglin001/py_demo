# py_sample

sample project with Python & C++

## install in editable mode

```sh
# pip install -e .
pip install --no-build-isolation -e .
# pip install --no-build-isolation -e . -vvv
```

for local debuging

```sh
DEBUG=1 pip install -e .
# or
DEBUG=1 SKIP_CMAKE=1 pip install -e .
```

## Reference

- https://packaging.python.org/en/latest/
- https://setuptools.pypa.io/en/latest/
- https://github.com/pypa/sampleproject
- https://github.com/pybind/cmake_example
