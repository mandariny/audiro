@echo off
echo Setting up environment for Qt usage...
set PATH=qt\5.15.0\msvc2019_64\bin;%PATH%
cd /D qt\5.15.0\msvc2019_64
echo Remember to call vcvarsall.bat to complete environment setup!
