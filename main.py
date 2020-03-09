#!/usr/bin/python3
# -*- coding: Utf-8 -*

""" MacGyver game """
import pygame.locals
import pygame
import constants
from map import Map
from items import Items
from character import Character


class Main:
    """ main class of the game"""

    def __init__(self):
        self.pygame_init()

    def main(self):
        # Main loop pygame
        self.stay = 1
        self.game = 0

        while self.stay:
            pygame.time.Clock().tick(60)
            # self.pygame_event()
            # if Macgyver has not picked up all the objects
            # when he appears before the guard he los

            # Menu loop
            self.stay_menu = 1
            self.stay_game = 1
            self.test_menu_leave = 1
            while self.stay_menu:
                self.pygame_test_menu()
                self.pygame_event()
            # we prevent the loading of the game if we leave the menu
            if self.test_menu_leave != 0:
                self.background = pygame.image.load(constants.IMG_BACKGROUND)\
                    .convert()
                self.map_creation()
                self.items_creation()
                self.character_creation()
            pygame.display.flip()

            # Loop game
            while self.stay_game:
                pygame.time.Clock().tick(60)
                self.pygame_game_event()
                self.window.blit(self.background, (0, 0))
                self.map.display(self.window)
                self.items.display(self.window)
                self.window.blit(pygame.image.load(constants.IMG_CHARACTER)
                                 .convert_alpha(), (self.mg.x, self.mg.y))
                self.items.recover((self.mg.x, self.mg.y))
                self.items.lister(self.window)
                pygame.display.flip()
                self.victory_test()

    def pygame_init(self):
        # Start program
        pygame.init()
        # Open pygame window
        self.window = pygame.display.set_mode(constants.WINDOW_SIZE)

        # Icon
        self.icon = pygame.image.load(constants.IMG_ICON)
        pygame.display.set_icon(self.icon)
        # Title
        pygame.display.set_caption(constants.TITLE)

    def map_creation(self):
        # Map creation
        self.map = Map('structure')
        self.map.generate()
        self.map.display(self.window)

    def items_creation(self):
        # Item creation
        self.items = Items(self.map.structure)
        self.items.generate()
        self.items.display(self.window)

    def character_creation(self):
        # MacGyver character creation
        self.mg = Character(self.map, self.map.first_position)

    def pygame_test_menu(self):
        if self.game == 1:
            self.window.blit(pygame.image.load(constants.IMG_LOSE)
                             .convert(), (0, 0))
            pygame.display.flip()
        if self.game == 2:
            self.window.blit(pygame.image.load(constants.IMG_WIN)
                             .convert(), (0, 0))
            pygame.display.flip()
        if self.game == 0:
            self.window.blit(pygame.image.load(constants.IMG_MENU)
                             .convert(), (0, 0))
            pygame.display.flip()

    def pygame_event(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                self.stay = 0
                self.stay_menu = 0
                self.stay_game = 0
                self.test_menu_leave = 0
            elif event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_ESCAPE:
                    self.stay_menu = 0
                    self.stay_game = 0
                    self.stay = 0
                    self.test_menu_leave = 0
                if event.key == pygame.locals.K_KP_ENTER \
                        or pygame.locals.K_RETURN:
                    self.stay_menu = 0

    def pygame_game_event(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                self.stay_game = 0
                self.stay_menu = 0
                self.stay = 0
            elif event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_ESCAPE:
                    self.stay_game = 0
                    self.game = 0
                elif event.key == pygame.locals.K_RIGHT:
                    self.mg.move('right')
                elif event.key == pygame.locals.K_LEFT:
                    self.mg.move('left')
                elif event.key == pygame.locals.K_UP:
                    self.mg.move('up')
                elif event.key == pygame.locals.K_DOWN:
                    self.mg.move('down')

    def victory_test(self):
        # If the coordinates of Macgyver are the sames of the guard,
        # the game stop.
        if self.map.guard_position == [self.mg.position_x, self.mg.position_y]:
            if not self.items.recovered_list or \
                    len(self.items.recovered_list) != 3:
                self.game = 1
            else:
                self.game = 2
            self.stay_game = 0


if __name__ == '__main__':
    m = Main()
    m.main()
