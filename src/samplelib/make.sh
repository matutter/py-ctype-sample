#!/bin/bash

here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
name="libsample.so"
pyheader="/usr/include/python3.5m/"

g++ -I$pyheader -c -fPIC "$here/samplelib.cpp" -o "$here/sample.o"
g++ -shared -Wl,-soname,$name -o "$here/$name"  "$here/sample.o"

