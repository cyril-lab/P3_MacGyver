#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""classes MacGyverGame"""
import constants
import pygame
import random


class Items:
    """class to create and manage items"""

    def __init__(self, map):
        self.map = map
        self.position_name = ""
        self.recovered_list = []

    def generate(self):
        """method to generate items"""
        num_line = 0
        free_sprite = []
        for line in self.map:
            num_column = 0
            for sprite in line:
                x = num_column * constants.WIDTH_SPRITE
                y = num_line * constants.HEIGHT_SPRITE
                if sprite == 'O':
                    free_sprite.append((x, y))
                num_column += 1
            num_line += 1
        position_item = random.sample(free_sprite, k=3)
        self.position_name = {position_item[0]: constants.ITEM_1,
                              position_item[1]: constants.ITEM_2,
                              position_item[2]: constants.ITEM_3}

    def display(self, window):
        """method to display items"""
        for cle, valeur in self.position_name.items():
            picture_item = constants.IMG_FOLDER + valeur \
                           + constants.IMG_EXTENSION
            window.blit(pygame.image.load(picture_item).convert_alpha(), cle)

    def recover(self, position_mg):
        if position_mg in self.position_name:
            self.recovered_list.append(self.position_name[position_mg])
            del self.position_name[position_mg]

    def lister(self, windows):
        i = 120
        for valeur in self.recovered_list:
            windows.blit(pygame.image.load(constants.IMG_FOLDER
                                           + valeur + constants.IMG_EXTENSION)
                         .convert_alpha(), (460, i))
            i += 60
