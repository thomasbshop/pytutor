class Dragon:
    def __init__(self, name="Dragon", lives=2):
        self._name = name  # we should not be changing these attributes therefore the underscore.
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_lives = self._lives - damage
        if remaining_lives >= 0:
            self._lives = remaining_lives
            print("I took {} points damage and have {} lives left.".format(damage, self._lives))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life!".format(self))
            else:
                print("{0._name} is gone!".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}".format(self)


class Hero:

    def __init__(self, name="Hero"):
        self.name = name
        self._bullets = 10  # hide the lives attribute by prefixing it with an underscore - python convention

    def _get_bullets(self):  # hide the the method using a preceding underscore.
        return self._bullets

    def _set_bullets(self, bullets):
        if bullets >= 0:
            self._bullets = bullets
        else:
            print("Bullets cannot be negative.")
            self._bullets = 0

    bullets = property(_get_bullets, _set_bullets)

    def __str__(self):  # special printing method - string representation of the object.
        """Prints attributes."""
        return "Name: {0.name}, Bullets: {0.bullets}".format(self)


thomas = Hero("Thomas")
print(thomas)