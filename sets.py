nums = {1,3,5,6,}
nums.add(5)
nums.add(2)
print(nums)

graphicDesigner = {'InDesign', 'Photoshop', 'Acrobat', 'Premiere', 'Bridge'}

graphicDesigner.add('Illustrator')
print(graphicDesigner)

graphicDesigner.remove('Illustrator')
print(graphicDesigner)

#graphicDesigner.remove('4444')
#print(graphicDesigner)

graphicDesigner.discard('4444')
print(graphicDesigner)

graphicDesigner.discard('Bridge')
print(graphicDesigner)

graphicDesigner.pop()
print(graphicDesigner)

for skill in graphicDesigner:
    print(skill)


#dataScientist = (sorted(graphicDesigner))
dataScientist = list(sorted(graphicDesigner))
print(type(dataScientist))
print(dataScientist)

dataScientist = (sorted(graphicDesigner,reverse=True))
print(dataScientist)

#remove duplicates
print(list(set([1, 2, 3, 1, 7])))

a = [1,2,3,4,5]
b = [2,3,4,5,6]

overlaps = set(a) & set(b)
print(overlaps)

alllaps = list(sorted(set(a).union(set(b))))
print(alllaps)
print(graphicDesigner )

