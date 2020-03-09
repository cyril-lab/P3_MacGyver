#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""classes MacGyverGame"""
import constants
import pygame


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
        wall = pygame.image.load(constants.IMG_WALL).convert()
        starting = pygame.image.load(constants.IMG_STARTING).convert_alpha()
        arrival = pygame.image.load(constants.IMG_ARRIVAL).convert_alpha()
        num_line = 0
        for line in self.structure:
            num_column = 0
            for sprite in line:
                x = num_column * constants.WIDTH_SPRITE
                y = num_line * constants.HEIGHT_SPRITE
                # we display the walls
                if sprite == 'm':
                    window.blit(wall, (x, y))
                num_column += 1
            num_line += 1
        # we display the starting
        starting_position = (self.first_position[0] * constants.WIDTH_SPRITE,
                             self.first_position[1] * constants.HEIGHT_SPRITE)
        window.blit(starting, starting_position)
        # we display arrival
        arrival_position = (self.guard_position[0] * constants.WIDTH_SPRITE,
                            self.guard_position[1] * constants.HEIGHT_SPRITE)
        window.blit(arrival, arrival_position)
