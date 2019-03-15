import random


def guess_the_number1():
    lives = 4
    random_number = random.randint(0, 10)
    guessed_number = input("Input your number. Remember you only have " + lives + " tries left: ")

    if guessed_number == random_number:
        return True
    elif guessed_number != random_number:
        lives -= 1
        print("The number did not match. Try again: ")
        if lives == 0:
            print("You exceeded your tries. The number is ")
            return False


def guess_the_number():
    lives = 4
    random_number = random.randrange(0, 11)

    while lives > 0:
        guessed_number = int(input("Input a random number between 0 and 11. You have " + str(lives) + " tries left: "))
        # assert isinstance(guessed_number, int)
        if guessed_number == random_number:
            print("Great, you guessed correct.")
            return True
        elif guessed_number != random_number:
            lives -= 1
            print("The number did not match.\n The number is {} Try again: ".format(random_number))
    else:
        print("You exceeded your tries. The number is {}".format(random_number))
        return False


guess_the_number()

import unittest

class KnownValues(unittest.TestCase):
    # test random
    def test_random_number(self):
        # capture the results of the function
        result =
        # check for expected output.
        expected =
        self.assertEqual(expected, result)