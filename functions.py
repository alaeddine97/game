
import pygame

import sys

def events_cheker(object):
    #DETECTING  EVNTS


    for event in pygame.event.get():
        #pygame.event.get() will store tetected events
        if event.type == pygame.QUIT:
            sys.exit()#this will exit the programe
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                object.flag = True
            elif event.key == pygame.K_LEFT:
                object.flag_l  = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                object.flag  = False
            elif event.key == pygame.K_LEFT:
                object.flag_l = False
def update_screen(screen,screen_object,image_object):
    screen.fill(screen_object)#background color
    image_object.blitme()#function that drow the image in the screen
    # Make the most recently drawn screen visible.
    pygame.display.flip()
#def moving_r_l(flagl,flagr):
    #pygame.event.get() will store tetected events
