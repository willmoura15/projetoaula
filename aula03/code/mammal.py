#!/usr/bin/python
#-*- coding: utf-8 -*-

from animal import animal

class mammal(animal):
    def __init__(self, age, height, weight, length, position):
        super().__init__(age, height, weight, length, position)
        self.fur_type= None
        self.fur_color=None
        self.eye_color=None

    def fur_type(self, ):
        pass

