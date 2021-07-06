str1='abcdefgabva'

print(str1[::2])

print(str1.count('a'))

print(str1.find('a'))
print(str1.rfind('a'))

print(str1[::-1].zfill(40)[::-1])


split_str= str.split("my name is python")
print(split_str)

split_str= str.split("my@name@is@python",sep='@')
print(split_str)

join_str = "$".join(split_str)
print(join_str)