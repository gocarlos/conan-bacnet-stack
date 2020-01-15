#!/bin/bash

# normal compilation
export CC=/usr/bin/clang-9
export CXX=/usr/bin/clang++-9
conan create . gocarlos/testing --build missing
