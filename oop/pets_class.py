# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


class Pets:
    """class attributes"""
    species = "mammal"
    numOfPets = 0

    """counts the number of pets"""
    @classmethod
    def count_pets(cls):
        cls.numOfPets += 1

    @classmethod
    def get_num_pets(cls):
        print("I have {} dogs".format(cls.numOfPets))

    """instance attributes"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.count_pets()

    def description(self):
        return print("{} is {}. ".format(self.name, self.age))


Tom = Pets("Tom", 6)
Fletcher = Pets("Fletcher", 7)
Larry = Pets("Larry", 9)

# Access the instance attributes
Pets.get_num_pets()
Tom.description()
Fletcher.description()
Larry.description()
print("And they are all {}s of course.\n".format(Pets.species))
