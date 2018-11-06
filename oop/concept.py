# Encapsulating all the functions that can be performed on the object. e.g. car The classes encapsulates both data
# and the methods that work on the data.
# Everything in python is an object.
# When a variable is bound to an instance of a class then it is referred to as a data attribute


class Kettle(object):

    power_source = "Electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 23.45)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 980
print(kenwood.price)

hamilton = Kettle("Hamilton", 3438)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))


""""
class: template for creating objects. All objects created using the same class will have the same characteristics.
object: an instance of a class.
instantiate: create an instance of a class.
method: a function defined in a class. function bound to an instance of a class. 'self parameter'
Attribute: a variable bound to an instance of a class. methods can also be attributes.
self: a reference to the instance of the class.
constructor: a method that is executed when an instance of a class is created. __init__
A signature is the defination of the name together with the parameters of the function as well as any return value.
"""

# we have to walk first before we can run.

print(hamilton.on)
print(hamilton.switch_on())
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

print("*"*80)
kenwood.power = 23
print(kenwood.power)
print("*"*80)

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print("*"*80)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

Kettle.power_source = "Wind"
# accessing a static field via an instance variable.
kenwood.power_source = "Solar"  # kenwood's power-source changes to solar
