#!/usr/bin/python
#-*- coding: utf-8 -*-

from mammal import mammal

class dog(mammal):
    def __init__(self, age, height, weight, length, position):
        super().__init__(age, height, weight, length, position)
        self.breed = None
        self.Attribute1 = None

