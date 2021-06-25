#include <pybind11/pybind11.h>

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(delta_generator_pybind11, m) {
    m.doc() = "A module to generate android OTA"; // optional module docstring

    m.def("add", &add, "A function which adds two numbers");
}
