"""
File: die.py

This module defines the Die class.
"""

from random import randint

class Die:
    """This class represents a six-sided die."""

    def __init__(self, value):
        """Creates a new die with a value of 1."""
        value = 1

    def roll(value):
        """Resets the die's value to a random number
        between 1 and 6."""
        value = randint(1, 6)
        return value

    def getValue(value):
        """Returns the value of the die's top face."""
        return value

    def __str__(self):
        """Returns the string rep of the die."""
        return str(self.getValue())

def main():
    d = Die
    rollNum=1
    rollNum=d.roll(rollNum)
    print('You rolled', rollNum)
    yesNo()

def yesNo():
    choice = input('Would you like to roll again? [y/n] : ')
    if choice == 'y':
        main()
    elif choice =='n':
        return
    else:
        print('Invalid input!')
        yesNo()
        
main()