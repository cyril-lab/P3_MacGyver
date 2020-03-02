#!/usr/bin/python3
# -*- coding: Utf-8 -*

""" MacGyver game """

from classes import *
from pygame.locals import *

# Start program
pygame.init()
# Open pygame window
window = pygame.display.set_mode(WINDOW_SIZE)
background = pygame.image.load(IMG_BACKGROUND).convert()
# Icon
icon = pygame.image.load(IMG_ICON)
pygame.display.set_icon(icon)
# Title
pygame.display.set_caption(TITLE)

# Main loop pygame
stay = 1
game = 0
while stay:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            stay = 0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game = 0
    # if Macgyver has not picked up all the objects
    # when he appears before the guard he lose
    if game == 1:
        window.blit(pygame.image.load(IMG_LOSE).convert(), (0, 0))
        pygame.display.flip()
    if game == 2:
        window.blit(pygame.image.load(IMG_WIN).convert(), (0, 0))
        pygame.display.flip()
    if game == 0:
        # Map creation
        map = Map('structure')
        map.generate()
        map.display(window)
        # Item creation
        items = Items(map.structure)
        items.generate()
        items.display(window)
        # MacGyver character creation
        mg = Character(map, map.first_position)
        pygame.display.flip()

        # Loop game
        stay_game = 1
        while stay_game:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    stay_game = 0
                    stay = 0
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        stay_game = 0
                    elif event.key == K_RIGHT:
                        mg.move('right')
                    elif event.key == K_LEFT:
                        mg.move('left')
                    elif event.key == K_UP:
                        mg.move('up')
                    elif event.key == K_DOWN:
                        mg.move('down')

            window.blit(background, (0, 0))
            map.display(window)
            items.display(window)
            window.blit(pygame.image.load(IMG_CHARACTER).convert_alpha(),
                        (mg.x, mg.y))
            pygame.display.flip()
            # If the coordinates of Macgyver are the sames of the guard,
            # the game stop.
            if map.guard_position == [mg.position_x, mg.position_y]:
                game = 2
                stay_game = 0