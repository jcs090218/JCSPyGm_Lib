@echo off
REM ========================================================================
REM $File: build_egg.bat $
REM $Date: 2017-01-16 01:43:15 $
REM $Revision: $
REM $Creator: Jen-Chieh Shen $
REM $Notice: See LICENSE.txt for modification and distribution information
REM                    Copyright (c) 2017 by Shen, Jen-Chieh $
REM ========================================================================


REM if build directory does not exits build it first.
mkdir build

REM change directory to build
cd build

REM clear the old data file
rmdir bdist.win32 /s /q
rmdir lib /s /q


REM back to root directory.
cd ..

REM build the egg file
python setup.py bdist_egg
