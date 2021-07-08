class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage


string = list('The quick brown fox jusmps over the lazy dog')
result = []
for i in string:
        if i == 'o':
                i = '0'
        result.append(i)
print(''.join(result))

str1 = "i am a string with space"

mystr=str1
print(mystr[:-1].zfill(40)[::-1])

#print(str1.split())
print('#'.join(mystr))

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

import pickle

dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }

filename = 'dogs'
outfile = open(filename,'wb')
pickle.dump(dogs_dict,outfile)
outfile.close()

infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()
print(new_dict)
print(new_dict==dogs_dict)
print(type(new_dict))


a=[1.1 , 2.1 ,3.1]
a.append(3.4)
print(a)
a.extend([4.5,6.3,6.8])
print(a)
a.insert(2,3.8)
print(a)