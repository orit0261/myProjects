def squared(num):
    return num**2


cars = ['CR-V', 'Silverado', 'F-150']
manufacturers = ['Honda', 'GM', 'Ford']
print('---------')
for i in range(len(cars)):
    print(cars[i], manufacturers[i])
print('---------')
for car,manu in zip(cars,manufacturers):
    print(car,manu)

print('---------')
for i in range(len(cars)):
    print(i, cars[i])

print('---------')
for i, car in enumerate(cars):
    print(i, car)

numbers = [1, 2, 3, 4, 5]
squares = map(squared, numbers)
print('---------')
for i in squares:
    print(i)

#squares = [x**2 for x in numbers]
squares = [squared(x) for x in numbers]
print('---------')
for i in squares:
    print(i)



