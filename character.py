#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""classes MacGyverGame"""
import constants


class Character:
    """class to create and manage a character """

    def __init__(self, map, starting_position):
        self.position_x = starting_position[0]
        self.position_y = starting_position[1]
        self.x = starting_position[0] * constants.WIDTH_SPRITE
        self.y = starting_position[1] * constants.HEIGHT_SPRITE
        self.map = map

    def move(self, direction):
        """method to move the character"""
        # moving to the right
        if direction == 'right':
            if self.position_x < (constants.NUMBER_SPRITE - 1):
                if self.map.structure[self.position_y][self.position_x + 1] \
                        != 'm':
                    self.position_x += 1
                    self.x = self.position_x * constants.WIDTH_SPRITE
        # moving to the left
        if direction == 'left':
            if self.position_x > 0:
                if self.map.structure[self.position_y][self.position_x - 1] \
                        != 'm':
                    self.position_x -= 1
                    self.x = self.position_x * constants.WIDTH_SPRITE
        # moving up
        if direction == 'up':
            if self.position_y > 0:
                if self.map.structure[self.position_y - 1][self.position_x] \
                        != 'm':
                    self.position_y -= 1
                    self.y = self.position_y * constants.HEIGHT_SPRITE
        # moving down
        if direction == 'down':
            if self.position_y < (constants.NUMBER_SPRITE - 1):
                if self.map.structure[self.position_y + 1][self.position_x] \
                        != 'm':
                    self.position_y += 1
                    self.y = self.position_y * constants.HEIGHT_SPRITE
