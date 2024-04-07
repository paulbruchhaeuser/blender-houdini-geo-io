import os
import sys
import importlib

from . import find_houdini

HFS = find_houdini.find_houdini()

key = ''
path = ''

for key_value in HFS:
	if (key_value == '20.0.625'):
		key = key_value
		path = HFS[key]

debug = True

if debug:
	print('[HIO INIT]\n[+] houdini path: {}'.format(path))

# from old code snippet - don't do it if you want to use it inside blender
# ERROR: ImportError: DLL load failed while importing core_19_0_622: The operating system cannot run %1.

# if you do hio_test.py - uncomment this
# 22/08/26 - seems both should be on !?
bin_dir = os.path.join(path, 'bin')
os.add_dll_directory(bin_dir)

# instead to this
os.add_dll_directory('C:/Windows/System32')

base_path = os.path.dirname(os.path.abspath(__file__))
module_name = f"core_{key.replace('.', '_')}"

if debug:
	print('[+] path: {}\n[+] module_name: {}'.format(base_path, module_name))
	print('[+] Extension: {}'.format(importlib.machinery.EXTENSION_SUFFIXES))

try:
	sys.path.append(base_path)
	core = importlib.import_module(module_name)
except ImportError as err:
    print('[+] Import Error:', err)
finally:
	sys.path.remove(base_path)
	pass

assert(core)

del find_houdini
del HFS

AttribType = core.AttribType
AttribData = core.AttribData
TypeInfo = core.TypeInfo
PrimitiveTypes = core.PrimitiveTypes

Vector2 = core.Vector2
Vector3 = core.Vector3
Vector4 = core.Vector4

Attrib = core.Attrib
Point = core.Point
Vertex = core.Vertex
Polygon = core.Polygon
BezierCurve = core.BezierCurve
NURBSCurve = core.NURBSCurve
Geometry = core.Geometry

__all__ = []