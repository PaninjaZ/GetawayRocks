from cmath import nan
import pygame
import math
import random
import os
import sys
from time import sleep
pygame.init()

options = [
    ['Volume', 50, 100],
    ['Speed', 3, 5],
    ['Dies?', 1, 1],
    ['Fullscreen', 0, 1],
    ['Ball speed*', 8, 16],
    ['Fps', 30, 60],
]

class Settings(pygame.sprite.Sprite):
    def __init__(self, x, y, Path):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(p+'data/wheels.png').convert_alpha()
        self.image = pygame.image.load(Path+"data/settings_screen/menu.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_button = False
        self.is_arrow = False

class Settings_element(pygame.sprite.Sprite):
    def __init__(self, x, y, Path):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(p+'data/wheels.png').convert_alpha()
        self.image = pygame.image.load(Path+"data/settings_screen/menu_button_off.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
        self.path = Path
        self.is_button = True
        self.is_arrow = False
        self.mouse_over = False
    def click(self, mx, my, num):
        mx -= self.rect.x
        mx /= 240
        mx *= options[num][2]+1
        mx = int(mx)
        #print(str(mx) + " - " + options[num][0])
        return mx

class Settings_arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, Path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Path+"data/settings_screen/arrow.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.path = Path
        self.is_button = False
        self.is_arrow = True
        self.mouse_over = False
        

def show(Path, width, height):
    #print("Settings")
    settings = Settings(width-260,(height/2)-201, Path)
    return settings

def show_elements(Path, width, height, settingsgruppe):
    optn_number = 1
    for optns in options:
        element = Settings_element(width-260,((height/2)+optn_number*57)-201, Path)
        settingsgruppe.add(element)
        optn_number+=1

def text(settingsgruppe, scale, Path, screen):
    num = -1

    for stn in settingsgruppe:

        if stn.is_button == True:

            num += 1
    
            font = pygame.font.Font(Path+'/data/fonts/Poppins-SemiBold.ttf', scale)
            
            ################ VALUE #################
            #txt = font.render(str(options[num][1]), True, (255,255,255))
            #txtrect = txt.get_rect()
            #txtrect.center = (stn.rect.x+180, stn.rect.y+25)
            #screen.blit(txt, txtrect)

            ############### NAME ###################
            txt = font.render(str(options[num][0]), True, (255,255,255))
            txtrect = txt.get_rect()
            txtrect.center = (stn.rect.x+120, stn.rect.y+25)
            screen.blit(txt, txtrect)

            #print(num)

def refresh_elements(settingsgruppe):
    for arw in settingsgruppe:
        if arw.is_arrow == True:
            arw.kill()
    
    num = -1
    for stn in settingsgruppe:

        pos = pygame.mouse.get_pos()
        if stn.is_button == True:

            num += 1

            global arrow
            arrow = Settings_arrow(stn.rect.x+(((options[num][1])/options[num][2])*225)+4,stn.rect.y, stn.path)
            settingsgruppe.add(arrow)
            
            #for arw in settingsgruppe:
            #    if arw.is_arrow == True:
            #        arw.rect.x = stn.rect.x+(((options[num][1])/100)*240)
            #        arw.rect.y = stn.rect.y

            if stn.rect.collidepoint(pos):
                stn.mouse_over = True
                if pygame.mouse.get_pressed()[0] == 1 and stn.clicked == False:
                    stn.clicked = True
                    options[num][1] = stn.click(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1], num)
            else:
                stn.mouse_over = False

            if pygame.mouse.get_pressed()[0] == 0:
                stn.clicked = False

            if stn.mouse_over == True:
                stn.image = pygame.image.load(stn.path+"data/settings_screen/menu_button_on.png")
                arrow.image = pygame.image.load(stn.path+"data/settings_screen/arrow.png")
            else:
                stn.image = pygame.image.load(stn.path+"data/settings_screen/menu_button_off.png")
                arrow.image = pygame.image.load(stn.path+"data/settings_screen/arrow_hidden.png")
                