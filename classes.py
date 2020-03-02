#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""classes MacGyverGame"""
from contants import *
import pygame
import random


class Map:
    """Class to create the map of the game """

    def __init__(self, file):
        self.file = file
        self.structure = ""
        self.first_position = ""
        self.guard_position = ""

    def generate(self):
        """method to import the level of the game from the structure file"""
        with open(self.file, "r") as file:
            structure_map = []
            num_line = 0
            for line in file:
                line_map = []
                num_column = 0
                for sprite in line:
                    # we calculate the position in pixels
                    x = num_column * WIDTH_SPRITE
                    y = num_line * HEIGHT_SPRITE
                    # we ignore the end of the line
                    if sprite != '\n':
                        line_map.append(sprite)
                    # we save the starting position
                    if sprite == 'd':
                        self.first_position = [num_column, num_line]
                    # we save the guard position
                    if sprite == 'a':
                        self.guard_position = [num_column, num_line]
                    num_column += 1
                # we add the line to the map list
                structure_map.append(line_map)
                num_line += 1
            self.structure = structure_map

    def display(self, window):
        """method to display the map"""
        wall = pygame.image.load(IMG_WALL).convert()
        starting = pygame.image.load(IMG_STARTING).convert_alpha()
        arrival = pygame.image.load(IMG_ARRIVAL).convert_alpha()
        num_line = 0
        for line in self.structure:
            num_column = 0
            for sprite in line:
                x = num_column * WIDTH_SPRITE
                y = num_line * HEIGHT_SPRITE
                # we display the walls
                if sprite == 'm':
                    window.blit(wall, (x, y))
                num_column += 1
            num_line += 1
        # we display the starting
        starting_position = (self.first_position[0] * WIDTH_SPRITE,
                             self.first_position[1] * HEIGHT_SPRITE)
        window.blit(starting, starting_position)
        # we display arrival
        arrival_position = (self.guard_position[0] * WIDTH_SPRITE,
                            self.guard_position[1] * HEIGHT_SPRITE)
        window.blit(arrival, arrival_position)


class Items:
    """class to create and manage items"""

    def __init__(self, map):
        self.map = map
        self.position_name = ""
#        self.recovered_list = ""

    def generate(self):
        """method to generate items"""
        num_line = 0
        free_sprite = []
        for line in self.map:
            num_column = 0
            for sprite in line:
                x = num_column * WIDTH_SPRITE
                y = num_line * HEIGHT_SPRITE
                if sprite == 'O':
                    free_sprite.append((x, y))
                num_column += 1
            num_line += 1
        position_item = random.sample(free_sprite, k=3)
        self.position_name = {position_item[0]: ITEM_1,
                              position_item[1]: ITEM_2,
                              position_item[2]: ITEM_3}

    def display(self, window):
        """method to display items"""
        for cle, valeur in self.position_name.items():
            picture_item = IMG_FOLDER + valeur + IMG_EXTENSION
            window.blit(pygame.image.load(picture_item).convert_alpha(), cle)


class Character:
    """class to create and manage a character """

    def __init__(self, map, starting_position):
        self.position_x = starting_position[0]
        self.position_y = starting_position[1]
        self.x = starting_position[0] * WIDTH_SPRITE
        self.y = starting_position[1] * HEIGHT_SPRITE
        self.map = map

    def move(self, direction):
        """method to move the character"""
        # moving to the right
        if direction == 'right':
            if self.position_x < (NUMBER_SPRITE - 1):
                if self.map.structure[self.position_y][self.position_x + 1] != 'm':
                    self.position_x += 1
                    self.x = self.position_x * WIDTH_SPRITE
        # moving to the left
        if direction == 'left':
            if self.position_x > 0:
                if self.map.structure[self.position_y][self.position_x - 1] != 'm':
                    self.position_x -= 1
                    self.x = self.position_x * WIDTH_SPRITE
        # moving up
        if direction == 'up':
            if self.position_y > 0:
                if self.map.structure[self.position_y - 1][self.position_x] != 'm':
                    self.position_y -= 1
                    self.y = self.position_y * HEIGHT_SPRITE
        # moving down
        if direction == 'down':
            if self.position_y < (NUMBER_SPRITE - 1):
                if self.map.structure[self.position_y + 1][self.position_x] != 'm':
                    self.position_y += 1
                    self.y = self.position_y * HEIGHT_SPRITE