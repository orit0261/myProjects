class Person(object):

    def __init__(self, name):
        self.name = name

    def reveval_identity(self):
        print("My Name is {}".format(self.name))


class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveval_identity(self):
        super(SuperHero, self).reveval_identity()
        print("...And I am {}".format(self.hero_name))


jack = Person('jack')
jack.reveval_identity()

spider = SuperHero('joe', 'spiderman')
spider.reveval_identity()
