import csv
class dog:
    def __init__(self,name,color,age):
        self.name = name
        self.color = color
        self.age = age

    def __iter__(self):
        return iter([self.name,self.color,self.age])


d1 = dog("woof1","pink",5)
d2 = dog("woof2","brown",1)
d3 = dog("woof3","black",6)

with open('dogs.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows([d1,d2,d3])