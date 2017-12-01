from settings import Setting

import sys

from image import Image

import functions

import pygame

# the function run_game will cotaine all what we need to have an empty screen
def run_game():

    #Insialising the game & Creating a screen object
    pygame.init()
    ai_settings=Setting()

    #creating screen object
    screen=pygame.display.set_mode((ai_settings.width,ai_settings.hight))

    pygame.display.set_caption("hello from Fhope")

    #making a ship
    s_hip=Image(screen)

    #the main loop for the game will detect events and react
    while True:
        functions.update_screen(screen,ai_settings.bg_color,s_hip)
        functions.events_cheker(s_hip)
        s_hip.move_right()
        s_hip.move_left()
    

run_game()
