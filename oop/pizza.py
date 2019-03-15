
# Instance methods need a class instance and can access the instance through self.
# Class methods don’t need a class instance. They can’t access the instance (self) but they have access
# to the class itself via cls.
# Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.
# Static and class methods communicate and (to a certain degree) enforce developer intent about class
# design. This can have maintenance benefits.


#
# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     def __repr__(self):
#         """
#         Return a string containing a printable representation of an object. For many types, this function makes an
#         attempt to return a string that would yield an object with the same value when passed to eval(), otherwise
#         the representation is a string enclosed in angle brackets that contains the name of the type of the object
#         together with additional information often including the name and address of the object. A class can control
#         what this function returns for its instances by defining a __repr__() method.
#         :return:
#         """
#         return f'Pizza({self.ingredients!r})'
#
#     @classmethod
#     def margherita(cls):
#         return cls(['mozzarella', 'tomatoes'])
#
#     @classmethod
#     def prosciutto(cls):
#         return cls(['mozzarella', 'tomatoes', 'ham'])
#
#
# Pizza.margherita()
#
# import math
#
# class AnotherPizza:
#     def __init__(self, radius, ingredients):
#         self.radius = radius
#         self.ingredients = ingredients
#
#     def __repr__(self):
#         return (f'AnotherPizza({self.radius!r}, '
#                 f'{self.ingredients!r})')
#
#     def area(self):
#         return self.circle_area(self.radius)
#
#     @staticmethod
#     def circle_area(r):
#         return r ** 2 * math.pi


class ClassName:
    pass  # "pass" often used as a place holder where code will eventually go. It allows us to run this code without
          # throwing an error.

class Dog:

    # Class Attribute - While instance attributes are specific to each object, class attributes are the same for
    # all instances.
    species = 'mammal'

    # Initializer / Instance Attributes. Is also an instance method.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
jake = Dog("Jake", 7)
doug = Dog("Doug", 6)
william = Dog("William", 8)

# Access the instance attributes
print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))

# Is Philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))


def get_biggest_number(*args):
    return max(args)


# Output
print("The oldest dog is {} years old.".format(
    get_biggest_number(jake.age, doug.age, william.age)))

# call our instance methods
print(mikey.description())
print(mikey.speak("Gruff! Gruff!"))


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child classes inherit attributes and
# behaviors from the parent class
jim = Bulldog("Jim", 12)
print(jim.description())

# Child classes have specific attributes
# and behaviors as well
print(jim.run("slowly"))

# Is jim an instance of Dog()?
print(isinstance(jim, Dog))

# Is julie an instance of Dog()?
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

# Is johnny walker an instance of Bulldog()
johnnywalker = RussellTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))

