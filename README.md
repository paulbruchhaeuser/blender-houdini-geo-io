satoruhiga's original
demo: https://www.youtube.com/watch?v=yz3-cj-qnd8

My personal build process:

1. adjust build.bat to you environment. For me that is:
   - create env var for cmake not beeing global
   - for Blender 4.1 change to Python 3.11
     - houdini still needs to link to 3.10 there an additional fix for that in the cmake file 
3. git clone pybind11 to /hio/libs ```git clone git@github.com:pybind/pybind11.git```
4. git clone Catch2 to /hio/Catch2 (make sure to clone the 2.x branch) ```git clone -b v2.x git@github.com:catchorg/Catch2.git```
5. ```./build.bat "C:/Program Files/Side Effects Software/Houdini 20.0.625" "h:/home/pyenv/py_win_3.11.8/Scripts/python.exe"```
