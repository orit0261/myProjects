class Car_class():
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


    def __str__(self):
        return "The {} car has {:,} miles".format(self.color, self.mileage)

blue_car = Car_class('blue',20000)
red_car = Car_class('red',30000)
print(blue_car)
print(red_car)