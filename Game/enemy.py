import random


class Enemy:
    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name  # we should not be changing these attributes therefore the underscore.
        self._lives = lives
        self._hit_points = hit_points
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points damage and have {} lives left.".format(damage, self._lives))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life!".format(self))
            else:
                print("{0._name} is gone!".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)


class Troll(Enemy):
    def __init__(self, name):
        # call our super class __init__ method here.
        super().__init__(name=name, hit_points=23, lives=1)  # no arg 'self'

    def grunt(self):
        return print("Me {0._name}, {0._name} stomp you!".format(self))


class Vampire(Enemy):
    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3)

    def dodge(self):
        if random.randint(1, 3) == 3:
            print("***** {0._name} dodged your blow *****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):  # method overriding. This method exists in the superclass.
        if not self.dodge():
            super().take_damage(damage=damage)


class VampireKing(Vampire):  # python uses child first approach therefore start with the child(immediate parent)
    #  first.
    def __init__(self, name):
        super().__init__(name=name)
        self._hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage=damage // 4)  # integer division rounds down.

