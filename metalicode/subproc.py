import subprocess

print(subprocess.run("dir",shell=True,stdout=subprocess.PIPE).stdout.decode())
print(subprocess.run("date",shell=True,stdout=subprocess.PIPE).stdout.decode())