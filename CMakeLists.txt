cmake_minimum_required(VERSION 3.28.0)

project(py_demo LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_BUILD_WITH_INSTALL_RPATH ON)
set(CMAKE_INSTALL_RPATH $ORIGIN)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/py_demo/)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/py_demo/)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/py_demo/)

# options
option(USE_SYSTEM_LIBS "use system libs or not" OFF)

include(FetchContent)
set(FETCHCONTENT_QUIET FALSE)

# TODO: use nanobind instead ?
# TODO: support using system pybind11
# pybind11
if(USE_SYSTEM_LIBS)
  find_package(pybind11 CONFIG REQUIRED)
else()
  FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11
    GIT_TAG v2.11.1
    GIT_SHALLOW TRUE)
  if(NOT pybind11_POPULATED)
    FetchContent_Populate(pybind11)
    add_subdirectory(${pybind11_SOURCE_DIR}/ ${pybind11_BINARY_DIR}
                     EXCLUDE_FROM_ALL SYSTEM)
  endif()
endif()

# packages
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
message("Python3: ${Python3_EXECUTABLE}")
message("Python3_SITEARCH: ${Python3_SITEARCH}")

include_directories(csrc)
add_subdirectory(csrc)
