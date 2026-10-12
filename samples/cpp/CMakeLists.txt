cmake_minimum_required(VERSION 3.20)
project(cpp_sample LANGUAGES CXX)

add_executable(cpp_sample main.cpp)
target_compile_features(cpp_sample PRIVATE cxx_std_17)
