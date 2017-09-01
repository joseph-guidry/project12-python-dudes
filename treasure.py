#! /usr/bin/env python3

from random import *


class Treasure:
    
    random_items = [ "Sword", "Potion", "Googles"]
    
    def __init__(self):
        self.name = Treasure.random_items[randrange(0, len(Treasure.random_items))]
        self.bonus = self.name
        self.amout = self.name

    def __str__(self):
        return "{} {} {}".format(self.name, self.bonus, self.amount)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, item):
        if item is "Sword":
            self._bonus = "Damage"
        elif item is "Googles":
            self._bonus = "Accuracy"
        elif item is "Potion":
            self._bonus = "Health"

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amout(self, item):
        if item is "Sword":
            self._amount = 2
        elif item is "Googles":
            self._amount = 1
        elif item is "Potion":
            self._amount = 5