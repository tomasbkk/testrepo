project(TestApp)
cmake_minimum_required(VERSION 3.1.0)

file(READ "version.txt" ver)

string(REGEX MATCH "VERSION_MAJOR ([0-9]*)" _ ${ver})
set(ver_major ${CMAKE_MATCH_1})

string(REGEX MATCH "VERSION_MINOR ([0-9]*)" _ ${ver})
set(ver_minor ${CMAKE_MATCH_1})

string(REGEX MATCH "VERSION_PATCH ([0-9]*)" _ ${ver})
set(ver_patch ${CMAKE_MATCH_1})

string(REGEX MATCH "VERSION_REV ([0-9]*)" _ ${ver})
set(ver_rev ${CMAKE_MATCH_1})

message("version: ${ver_major}.${ver_minor}.${ver_patch}.${ver_rev}")

add_executable(TestApp TestApp.cpp)