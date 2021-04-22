def square_num(nums):
    for i in nums:
        yield i * i


my_nums = square_num([1, 3, 5, 8])
for j in my_nums:
    print(j)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x=car.popitem()

print(x)