import os.path

print(os.environ)
def get_file(file_name):
    with open(file_name,'r') as reader:
        return reader.readlines()

if os.path.exists('file_demo.txt'):
  lst=get_file('file_demo.txt')
  for i in lst:
      try:
        if (int(i) % 5==0)or(int(i) % 3==0):
           print(i)
      except ValueError:
          print('Invalid input')
          break

