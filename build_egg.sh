#!/bin/bash
#  ========================================================================
#  $File: build_egg.sh $
#  $Date: 2017-01-16 01:50:03 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                    Copyright (c) 2017 by Shen, Jen-Chieh $
#  ========================================================================


# if build directory does not exits build it first.
mkdir build


# change directory to build
cd build

# force remove  the old data file
rm -rf bdist.win32
rm -rf lib

# back to root directory.
cd ..

# build the egg file
python setup.py bdist_egg
