class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass


def main():
    buddy = Dog("Buddy", 9)

    miles = Dog("Miles", 4)
    miles.species = "Felis silvestris"
    print(miles.speak("Woof Woof"))
    print(miles.speak("Bow Wow"))
    print(miles)

    miles = JackRussellTerrier("Miles", 4)
    print(miles.speak())
    buddy = Dachshund("Buddy", 9)
    jack = Bulldog("Jack", 3)
    jim = Bulldog("Jim", 5)

    print(miles.species)
    print(buddy.name)
    print(jack)
    print(jim.speak("Woof"))
    print("type(miles)=",type(miles))
    print("isinstance(miles, Dog)",isinstance(miles, Dog))


if __name__ == '__main__':
     main()
