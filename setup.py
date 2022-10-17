import os
import pathlib
import subprocess
import sys

from setuptools import Extension, find_packages, setup
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=""):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def build_extensions(self):
        os.makedirs(self.build_temp, exist_ok=True)
        os.makedirs(self.build_lib, exist_ok=True)

        debug = int(os.environ.get("DEBUG", 0)) if self.debug is None else self.debug
        cfg = "Debug" if debug else "Release"
        cmake_args = [
            f"-DCMAKE_BUILD_TYPE={cfg}",
            f"-DPython3_EXECUTABLE={sys.executable}",
            f"-DCMAKE_INSTALL_PREFIX={here}/src/sample",
        ]
        build_args = []
        # Adding CMake arguments set as environment variable
        if "CMAKE_ARGS" in os.environ:
            cmake_args += [item for item in os.environ["CMAKE_ARGS"].split(" ") if item]

        try:
            import ninja  # noqa: F401

            ninja_executable_path = os.path.join(ninja.BIN_DIR, "ninja")
            cmake_args += [
                "-GNinja",
                f"-DCMAKE_MAKE_PROGRAM:FILEPATH={ninja_executable_path}",
            ]
        except ImportError:
            raise Exception("please install ninja first.")

        build_lib = self.build_temp
        cmd = ["cmake"] + cmake_args + [f"-S{here}", f"-B{build_lib}"]
        subprocess.check_call(cmd, cwd=here)
        cmd = (
            ["cmake", "--build"] + build_args + [f"{build_lib}", '--target', 'install']
        )
        subprocess.check_call(cmd, cwd=here)

        # copy extensions
        for ext in self.extensions:
            fullname = self.get_ext_fullname(ext.name)
            filename = self.get_ext_filename(fullname)
            src = os.path.join(self.build_temp, filename)
            dst = os.path.join(os.path.realpath(self.build_lib), filename)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            self.copy_file(src, dst)

        # TODO copy otherv files
        # src = os.path.join(here, 'src', 'sample', 'lib')
        # dst = os.path.join(os.path.realpath(self.build_lib), 'sample', 'lib')
        # self.copy_tree(src, dst)


if __name__ == "__main__":
    here = pathlib.Path(__file__).parent.resolve()
    extensions = [
        CMakeExtension("sample._C"),
    ]
    cmdclass = {"build_ext": CMakeBuild}
    setup(
        name='sample',
        version=f"0.1.0",
        description='sample mixin Python & C++ project',
        author='Allen Guo',
        author_email='guosonglin001@gmail.com',
        ext_modules=extensions,  # type: ignore
        cmdclass=cmdclass,
        install_requires=[
            'numpy',
        ],
        package_dir={'': 'src'},
        packages=find_packages(where='src'),
    )
