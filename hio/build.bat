rem build.bat "C:/Program Files/Side Effects Software/Houdini 20.0.625" "h:/home/pyenv/py_win_3.11.8/Scripts/python.exe"

cd /d %~dp0

rd /s /q _build

mkdir _build
cd _build

:: set cmake
set CMAKE=H:/tools/00_develop_tools/cmake-3.24.0-rc4-windows-x86_64/bin/cmake.exe

cmake .. -G "Visual Studio 16 2019" -DHFS=%1 -DPYTHON_EXECUTABLE=%2
cmake --build . --config release
::del CMakeCache.txt

cd ..
::rd /s /q _build
