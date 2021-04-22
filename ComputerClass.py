class Computer:
    # we cant change _pprice field because it's private in the class
#In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.
    def __init__(self):
        self.__maxprice = 900
        self._pprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
        print("Selling p Price: {}".format(self._pprice))

    def setMaxPrice(self, price):
        self.__maxprice = price
        self._pprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()