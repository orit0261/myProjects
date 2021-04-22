class Car:
    def __init__(self, model, color, price):
        self.__model = model
        self.__color = color
        self.__price = price

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def __str__(self):
        return f'model {self.__model}, color: {self.__color},price: {self.__price}'


car1 = Car("mazda", "red", 30000)
car2 = Car("fiat", "blue", 10000)

if car1.get_price() > car2.get_price():
    print(car1)
else:
    print(car2)
