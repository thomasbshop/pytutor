class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3  # hide the lives attribute by prefixing it with an underscore - python convention
        self._level = 1
        self._score = 0

    def _get_lives(self):  # hide the the method using a preceding underscore.
        return self._lives

    def _set_lives(self, lives):  # underscore suggests to users that they should NOT be using it.
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative.")
            self._lives = 0

    lives = property(_get_lives, _set_lives)  # this is a property -- notice the methods without the parenthesis.
    #  the property must'nt have the same name as the property. If you don't specify a method to use for the setter
    # then the property is going to be read only which can be useful.
    # if u only add a setter then you can only change but not read the property. Probably useful for hidden items.

    def _set_level(self, level):
        if self._level > 0:
            delta = level - self._level
            self._score += delta * 1000
            if (delta % 2) == 0 & delta > 1:
                bonus = delta * 1000
                self._score += bonus
            self._level = level
        else:
            print("Level cannot less than one.")

    def _get_level(self):
        return self._level

    level = property(_get_level, _set_level)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):  # special printing method - string representation of the object.
        """Prints attributes so that we don't have to write print statements every time."""
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score {0.score}".format(self)


print(Player)
