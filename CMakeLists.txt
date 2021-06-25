cmake_minimum_required(VERSION 3.14)
project(delta_generator_pybind11 LANGUAGES CXX)

include(FetchContent)

set(EXTERNAL_INSTALL_LOCATION ${CMAKE_BINARY_DIR}/external)

FetchContent_Declare(pybind11
	GIT_REPOSITORY https://github.com/pybind/pybind11.git
)

if(NOT pybind_POPULATED)
	FetchContent_Populate(pybind11)
	add_subdirectory(${pybind11_SOURCE_DIR} ${pybind11_BINARY_DIR})
endif()



pybind11_add_module(delta_generator_pybind11 src/delta_generator_pybind11.cpp)
