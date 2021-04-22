from string import Template
import calendar
import json

x = 'x'
if True:
    y = "y"
    print(y)
    print(y)
    print(x)

print(y)

z = 123
print('this is : {:10}'.format(z))

str_a = "bill"
str_b = f"this is a {str_a:<30}" + "x"
print(str_b)

water = 6
cup = 30
print(f'water/cup ratio:{water / cup}')


str1 = Template("$who was the $what")
print(str1.substitute(who="JOHN", what="WINNER"))


print(calendar.calendar(2020, w=2, l=1, c=3))

#raise ZeroDivisionError("hi")
a=1
b=2
print(f"try to print variable {a}\t=\t{b}")


