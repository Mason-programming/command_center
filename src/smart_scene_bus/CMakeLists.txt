cmake_minimum_required(VERSION 3.4)
project(processbridge)

set(CMAKE_CXX_STANDARD 17)

find_package(pybind11 REQUIRED)

pybind11_add_module(processbridge processBridge.cpp processCommand.cpp)
