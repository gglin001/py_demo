cmake_minimum_required(VERSION 3.10.0)

project(sample LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_BUILD_WITH_INSTALL_RPATH ON)
set(CMAKE_INSTALL_RPATH $ORIGIN)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/sample/)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/sample/)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/sample/)

# options
option(USE_SYSTEM_LIBS "use system libs or not" ON)

# packages
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
message("Python3: ${Python3_EXECUTABLE}")
message("Python3_SITEARCH: ${Python3_SITEARCH}")
# pybind11
add_subdirectory(third_party/pybind11)
# TODO add a lib using `FetchContent`

include_directories(csrc)
add_subdirectory(csrc)
