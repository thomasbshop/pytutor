# Remember that child classes can also override attributes and behaviors from the parent class.


# The SomeBreed() class inherits the species from the parent class, while the SomeOtherBreed()
# class overrides the species, setting it to reptile.
class Dog:
    species = 'mammal'


class SomeBreed(Dog):
    pass


class SomeOtherBreed(Dog):
    species = 'reptile'


frank = SomeBreed()
print(frank.species)

beans = SomeOtherBreed()
print(beans.species)
