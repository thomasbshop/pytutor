class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weeee! This is fun.")
        elif self.ratio == 1:
            print("This is hard, but I am flying.")
        else:
            print("I'll just walk.")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water is lovely.")

    def quack(self):
        print("Quack, quack")

    def fly(self):
        self._wing.fly()


class Penguin:
    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it is a bit cold this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'am a penguin!")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


# this code will not run if duck is imported. Only run when executed as a file. Notice the single quotes.
if __name__ == '__main__':
    donald = Duck()
    # test_duck(donuld)
    donald.fly()

    # uncle = Penguin()
    # test_duck(uncle)

# https://en.wikipedia.org/wiki/Duck_test

# Polymorphism - different objects can inherit similar behaviour from a common base class .e.g. although ints, lists and
# floats are different types, they can all be printed Thats because they provide a __string__ or __str__ method. If a
# type doesnt provide any of these methods, it ends up being inherited from the base class.
# Inheritance isnt the only way to implement polymorphism. A class can behave the same way as another class as long as
# it has the necessary methods and data attributes.
