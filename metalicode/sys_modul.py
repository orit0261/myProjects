import sys

print(sys.platform)
print(sys.implementation)
print(sys.version_info)
print(sys.getwindowsversion())
print(sys.executable)
sys.stderr.write("ERROR!")
print(sys.builtin_module_names)
print('MODUELS:',sys.modules.keys())
