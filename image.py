import pygame

class Image():
    def __init__(self,screen):
        """this will represent the ship"""
        self.screen = screen
        #inicialising the ship
        self.ship=pygame.image.load('untitled.png')#loading the ship
        self.ship_rect=self.ship.get_rect()#the ship as rect
        self.screen_rect=screen.get_rect()#the screen as rect
        self.flag= False
        self.flag_l= False
        """inicialising position"""
        self.ship_rect.centerx=self.screen_rect.centerx
        self.ship_rect.bottom=self.screen_rect.bottom

        #this will drow the shape in screen
    def blitme(self):
        self.screen.blit(self.ship,self.ship_rect)

    def move_right(self):
        if self.flag:
            self.ship_rect.centerx += 1

    def move_left(self):
        if self.flag_l:
            self.ship_rect.centerx -= 1
