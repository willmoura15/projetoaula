#!/usr/bin/python
#-*- coding: utf-8 -*-


import pygame
from pygame import Surface, rect
from pygame.examples.cursors import surf

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # opção do menu
        self.entity_list: list[Entity] = []
        # Usa a instância de EntityFactory para obter a entidade
        self.entity_list.extend(EntityFactory.get_entity('level1bg'))


    def run(self):
        while True:
            for ent in self.entity_list:

                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            # Atualiza a tela
            pygame.display.flip()
        pass


