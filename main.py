import pygame
import math
import random
import os
import sys
from time import sleep
pygame.init()
clock = pygame.time.Clock()
#width = 960
#height = 540

################### CONTENT ################################

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

config_path = os.path.join(application_path)

Path = config_path +"/"

print("")
print(Path)


print("")
print("  __  __  ____  _    _ _   _ _______       _____ _   _    _____          __  __ ______  _____ \n |  \/  |/ __ \| |  | | \ | |__   __|/\   |_   _| \ | |  / ____|   /\   |  \/  |  ____|/ ____|\n | \  / | |  | | |  | |  \| |  | |  /  \    | | |  \| | | |  __   /  \  | \  / | |__  | (___  \n | |\/| | |  | | |  | | . ` |  | | / /\ \   | | | . ` | | | |_ | / /\ \ | |\/| |  __|  \___ \ \n | |  | | |__| | |__| | |\  |  | |/ ____ \ _| |_| |\  | | |__| |/ ____ \| |  | | |____ ____) |\n |_|  |_|\____/ \____/|_| \_|  |_/_/    \_\_____|_| \_|  \_____/_/    \_\_|  |_|______|_____/ ")
print("")

sleep(1)

def img(var):
    image = pygame.image.load(Path+"data/"+var)
    return image

def splay(var, chnl = 0):
    if chnl == 0:
        global channel
        sound = pygame.mixer.Sound(Path+"data/sounds/"+str(var))
        channel.play(sound, loops=0)
    else:
        CUSTOMchannel = pygame.mixer.Channel(chnl)
        sound = pygame.mixer.Sound(Path+"data/sounds/"+str(var))
        CUSTOMchannel.play(sound, loops=0)

def text(value, px, py, clr, scale):
    font = pygame.font.Font(Path+'/data/fonts/Poppins-SemiBold.ttf', scale)
    txt = font.render(value, True, clr)
    txtrect = txt.get_rect()
    txtrect.center = (px, py)
    screen.blit(txt, txtrect)

################### SCREEN ##################################
width = round(pygame.display.get_desktop_sizes()[0][0] / 2)
height = round(pygame.display.get_desktop_sizes()[0][1] / 2)
print("Setting up window with the size... " + str(width) + " " + str(height))
screen = pygame.display.set_mode((width, height))
#screenLogo = pygame.image.load(p+"/data/logo32.png")
screenLogo = img("logo32.png")
pygame.display.set_icon(screenLogo)
pygame.display.set_caption("Get away rocks!")

fscreen = False

running = True
gameover = False
score = 0
scoretwo = 0
playerhasmoved = False
timewaituntilspawn = 40
levelnum = 0
devmode = False
hasgameover = False


#################### MAPS #####################

custommap = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

level = [[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 5, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
],
[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 5, 0, 0, 1, 0, 0, 2, 0, 1],
    [1, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 4, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
],
[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 2, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
],
[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 5, 0, 0, 5, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 1, 0, 2, 2, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1, 0, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 5, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 2, 1, 0, 2, 0, 0, 0, 2, 0, 1],
    [1, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
],
]

################ MUSIC #############
channel = pygame.mixer.Channel(0)
print("Playing music")
songchannel = pygame.mixer.Channel(1)
musicsound = pygame.mixer.Sound(Path+'/data/sounds/songLQ.wav')
songchannel.play(musicsound, loops=-1)
songchannel.set_volume(.2)

########################################################################
############################## CHARACTERS ##############################

ballgruppe = pygame.sprite.Group()
spillergruppe = pygame.sprite.Group()
defencegruppe = pygame.sprite.Group()
wallgruppe = pygame.sprite.Group()
loadgruppe = pygame.sprite.Group()
wheelsgruppe = pygame.sprite.Group()
exitgruppe = pygame.sprite.Group()
fixgruppe = pygame.sprite.Group()
spawngruppe = pygame.sprite.Group()
twallgruppe = pygame.sprite.Group()

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(p+'data/stone.png').convert_alpha()
        self.image = img("bigboss.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.fartx = 5
        self.farty = 5

    def flytt(self):
        self.rect.x = self.rect.x + self.fartx
        self.rect.y = self.rect.y + self.farty

    def treffVegg(self):
        if self.rect.x > width-160:
            self.fartx = self.fartx * -1
            self.rect.x = width-165

        if self.rect.x < 0:
            self.fartx = self.fartx * -1
            self.rect.x = 5

        if self.rect.y > height-160:
            self.farty = self.farty * -1
            self.rect.y = height-165

        if self.rect.y < 0:
            self.farty = self.farty * -1
            self.rect.y = 5

        veggtreffliste = pygame.sprite.spritecollide(self, wallgruppe, False)

        if veggtreffliste:
            if self.fartx > 0:
                self.rect.right = veggtreffliste[0].rect.left
            else:
                self.rect.left = veggtreffliste[0].rect.right

            self.fartx *= -1

        veggtreffliste = pygame.sprite.spritecollide(self, wallgruppe, False)

        if veggtreffliste:
            if self.farty > 0:
                self.rect.bottom = veggtreffliste[0].rect.top
            else:
                self.rect.top = veggtreffliste[0].rect.bottom

            self.farty *= -1

        # if self.rect.x > width-50 or self.rect.x < 0:
            ##self.fartx = self.fartx * -1

        # if self.rect.y > height-50 or self.rect.y < 0:
            ##self.farty = self.farty * -1


class TempWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(p+'data/out.png').convert_alpha()
        self.image = img("tempwall.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Spawn(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(p+'data/out.png').convert_alpha()
        self.image = img("spawn.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class DoorOut(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(p+'data/out.png').convert_alpha()
        self.image = img("out.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Fixstation(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(p+'data/wheels.png').convert_alpha()
        self.image = img("fix.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Wheels(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(p+'data/wheels.png').convert_alpha()
        self.image = img("wheels.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class ldnbar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(p+'data/bar.png').convert_alpha()
        self.image = img("bar.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Vegg(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(p+'data/wall.png').convert_alpha()
        self.image = img("wall.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Defence(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(p+'data/wheel.png').convert_alpha()
        self.image = img("wheel.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Spiller(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(p+'data/car.png').convert_alpha()
        self.image = img("car.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.fartud = 0
        self.fartlr = 0
        self.howmany_wheels = 0
        self.life = 100
        self.fixing = 0
        self.speedup = 3
        self.complete = False

    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.fartud = 0
        self.fartlr = 0
        self.life += 55
        self.fixing = 0
        self.speedup = 3
        if self.life > 100:
            self.life = 100
        self.howmany_wheels = int(self.howmany_wheels/2)
        self.complete = False

    def flyttUp(self):
        # if self.fartud < 0:
        #self.fartud = 0
        self.fartud -= self.speedup
        #self.fartud = self.fartud * 1.3

    def flyttDown(self):
        # if self.fartud > 0:
        #self.fartud = 0
        self.fartud += self.speedup
        #self.fartud = self.fartud * 1.3

    def flyttR(self):
        # if self.fartlr > 0:
        #self.fartlr = 0
        self.fartlr += self.speedup
        #self.fartud = self.fartlr * 1.3

    def flyttL(self):
        # if self.fartlr < 0:
        #self.fartlr = 0
        self.fartlr -= self.speedup
        #self.fartud = self.fartlr * 1.3

    def damage(self):
        if self.life > 80:
            #self.image = pygame.image.load(p+'data/car.png').convert_alpha()
            self.image = img("car.png")
        elif self.life > 50:
            #self.image = pygame.image.load(p+'data/broken/80.png').convert_alpha()
            self.image = img("broken/80.png")
        elif self.life > 30:
            #self.image = pygame.image.load(p+'data/broken/50.png').convert_alpha()
            self.image = img("broken/50.png")
        elif self.life > 0:
            #self.image = pygame.image.load(p+'data/broken/30.png').convert_alpha()
            self.image = img("broken/30.png")
        else:
            #self.image = pygame.image.load(p+'data/broken/0.png').convert_alpha()
            self.image = img("broken/0.png")

        if self.life < 0:
            self.life = 0
            global gameover
            gameover = True

    def move(self):

        if not self.fixing == 0:
            self.fixing -= 1
            self.speedup = 1
            self.life += .3
            if self.life > 100:
                self.life = 100
        else:
            self.speedup = 3

        veggtreffliste = pygame.sprite.spritecollide(self, wallgruppe, False)

        self.rect.y += self.fartud
        veggtreffliste = pygame.sprite.spritecollide(self, wallgruppe, False)
        if veggtreffliste:
            if self.fartud > 0.5:
                self.rect.bottom = veggtreffliste[0].rect.top
            elif self.fartud < -0.5:
                self.rect.top = veggtreffliste[0].rect.bottom
        self.rect.x += self.fartlr
        veggtreffliste = pygame.sprite.spritecollide(self, wallgruppe, False)
        if veggtreffliste:
            if self.fartlr > 0.5:
                self.rect.right = veggtreffliste[0].rect.left
            elif self.fartlr < -0.5:
                self.rect.left = veggtreffliste[0].rect.right

        self.fartud *= .8
        self.fartlr *= .8
        if self.fartud < 1 and self.fartud > -1:
            self.fartud = 0
        if self.fartlr < 1 and self.fartlr > -1:
            self.fartlr = 0

        wheelstreffliste = pygame.sprite.spritecollide(self, wheelsgruppe, False)
        if wheelstreffliste and gameover == False:
            splay("wheelLQ.wav")
            self.howmany_wheels += random.randint(1, 5)
            wheelstreffliste[0].kill()
        
        fixstreffliste = pygame.sprite.spritecollide(self, fixgruppe, False)
        if fixstreffliste and gameover == False and self.fixing == 0:
            splay("fixLQS.wav")
            fixstreffliste[0].kill()
            self.fixing = 120

        exittreffliste = pygame.sprite.spritecollide(self, exitgruppe, False)
        if exittreffliste and gameover == False:
            splay("doorLQ.wav",2)
            global levelnum
            global ourlevelnum
            print("Next level")
            self.complete = True
            levelnum += 1
            restart()

    def treffVegg(self):
        if self.rect.x > width-40:
            self.fartlr *= -2
            self.rect.x += self.fartlr
            #self.fartlr = 0
            self.fartud = 0
            #self.rect.x = 0

        if self.rect.x < 0:
            self.fartlr *= -2
            self.rect.x += self.fartlr
            #self.fartlr = 0
            self.fartud = 0
            #self.rect.x = width - 50

        if self.rect.y > height-40:
            self.fartud *= -2
            self.rect.y += self.fartlr
            #self.fartud = 0
            self.fartlr = 0
            #self.rect.y = 0

        if self.rect.y < 0:
            self.fartud *= -2
            self.rect.y += self.fartlr
            #self.fartud = 0
            self.fartlr = 0
            #self.rect.y = height - 50


##############################################
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, fx, fy):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(p+'data/stone.png').convert_alpha()
        self.image = img("stone.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.fartx = fx
        self.farty = fy

    def flytt(self):
        self.rect.x = self.rect.x + self.fartx
        veggtreffliste = pygame.sprite.spritecollide(self, wallgruppe, False)

        if veggtreffliste:
            if self.fartx > 0:
                self.rect.right = veggtreffliste[0].rect.left
            else:
                self.rect.left = veggtreffliste[0].rect.right

            self.fartx *= -1
            if random.randint(0,3) == 0:
                self.farty *= -1
        self.rect.y = self.rect.y + self.farty
        veggtreffliste = pygame.sprite.spritecollide(self, wallgruppe, False)

        if veggtreffliste:
            if self.farty > 0:
                self.rect.bottom = veggtreffliste[0].rect.top
            else:
                self.rect.top = veggtreffliste[0].rect.bottom

            self.farty *= -1
            if random.randint(0,3) == 0:
                self.fartx *= -1

    def treffVegg(self):
        if self.rect.x > width-50:
            self.fartx = self.fartx * -1
            self.rect.x = width-55

        if self.rect.x < 0:
            self.fartx = self.fartx * -1
            self.rect.x = 5

        if self.rect.y > height-50:
            self.farty = self.farty * -1
            self.rect.y = height-55

        if self.rect.y < 0:
            self.farty = self.farty * -1
            self.rect.y = 5

        # if self.rect.x > width-50 or self.rect.x < 0:
            ##self.fartx = self.fartx * -1

        # if self.rect.y > height-50 or self.rect.y < 0:
            ##self.farty = self.farty * -1


####################################################################
####################################################################

def loadingBar(load, quality):
    for i in range(int(load)):
        lbar = ldnbar((width/2)-((int(load)*quality)/2) +
                      i*quality, (height/2)+100)
        loadgruppe.add(lbar)


def spawnBalls():
    print("Loaded balls")
    global fscreen
    global width
    global height
    if fscreen:
        width2 = round(pygame.display.get_desktop_sizes()[0][0] / 2)
        height2 = round(pygame.display.get_desktop_sizes()[0][1] / 2)
        for i in range(10):
            ball = Ball(random.randint(0, width2), random.randint(0, height2), random.randint(1, 8), random.randint(1, 8))
            #print("Spawned ball at" + str(ball.rect.x) + ":" + str(ball.rect.y))
            ballgruppe.add(ball)
            pygame.sprite.groupcollide(spillergruppe, ballgruppe, False, True, pygame.sprite.collide_mask)
            pygame.sprite.groupcollide(wallgruppe, ballgruppe, False, True, pygame.sprite.collide_mask)
    else:
        for i in range(10):
            ball = Ball(random.randint(0, width), random.randint(0, height), random.randint(1, 8), random.randint(1, 8))
            ballgruppe.add(ball)
            pygame.sprite.groupcollide(spillergruppe, ballgruppe, False, True, pygame.sprite.collide_mask)
            pygame.sprite.groupcollide(wallgruppe, ballgruppe, False, True, pygame.sprite.collide_mask)


#########################################################

def fullscreen():

    print("Turning on fullscreen")

    width2 = round(pygame.display.get_desktop_sizes()[0][0] / 2)
    height2 = round(pygame.display.get_desktop_sizes()[0][1] / 2)
    
    spiller.rect.x += (width2/2)
    spiller.rect.y += (height2/2)
    for door in exitgruppe:
        door.rect.x += (width2/2)
        door.rect.y += (height2/2)
    wallgruppe.update()
    for spawn in spawngruppe:
        spawn.rect.x += (width2/2)
        spawn.rect.y += (height2/2)
    spawngruppe.update()
    for wall in wallgruppe:
        wall.rect.x += (width2/2)
        wall.rect.y += (height2/2)
    wallgruppe.update()
    for ball in ballgruppe:
        ball.rect.x += (width2/2)
        ball.rect.y += (height2/2)
    ballgruppe.update()
    for wheel in defencegruppe:
        wheel.rect.x += (width2/2)
        wheel.rect.y += (height2/2)
    defencegruppe.update()
    for wheels in wheelsgruppe:
        wheels.rect.x += (width2/2)
        wheels.rect.y += (height2/2)
    wheelsgruppe.update()
    for fix in fixgruppe:
        fix.rect.x += (width2/2)
        fix.rect.y += (height2/2)
    fixgruppe.update()

def noNfullscreen():

    print ("Turning off fullscreen")

    spiller.rect.x -= (width/2)
    spiller.rect.y -= (height/2)
    for door in exitgruppe:
        door.rect.x -= (width/2)
        door.rect.y -= (height/2)
    wallgruppe.update()
    for wall in wallgruppe:
        wall.rect.x -= (width/2)
        wall.rect.y -= (height/2)
    wallgruppe.update()
    for ball in ballgruppe:
        ball.rect.x -= (width/2)
        ball.rect.y -= (height/2)
    ballgruppe.update()
    for wheel in defencegruppe:
        wheel.rect.x -= (width/2)
        wheel.rect.y -= (height/2)
    defencegruppe.update()
    for wheels in wheelsgruppe:
        wheels.rect.x -= (width/2)
        wheels.rect.y -= (height/2)
    wheelsgruppe.update()
    for fix in fixgruppe:
        fix.rect.x -= (width/2)
        fix.rect.y -= (height/2)
    fixgruppe.update()

def restart(way=None):
    if not way is None:
        global songchannel
        global musicsound
        songchannel.stop()
        songchannel.play(musicsound, loops=-1)
        songchannel.set_volume(.2)
    print("Restarting")
    global score
    global scoretwo
    global playerhasmoved
    global gameover
    global hasgameover
    score = 0
    scoretwo = 0
    playerhasmoved = False
    gameover = False
    hasgameover = False

    for ball in ballgruppe:
        ball.kill()
    for wheels in wheelsgruppe:
        wheels.kill()
    for fix in fixgruppe:
        fix.kill()
    for wall in wallgruppe:
        wall.kill()
    for wheel in defencegruppe:
        wheel.kill()
    for door in exitgruppe:
        door.kill()
    for spawn in spawngruppe:
        spawn.kill()

    spawnBalls()

    ################### LEVEL CREATOR #######################
    for y, rad in enumerate(level[levelnum]):
        for x, verdi in enumerate(rad):

            if verdi == 1:
                vegg = Vegg(x*32, y*32)
                wallgruppe.add(vegg)
            elif verdi == 2:
                wheels = Wheels(x*32, y*32)
                wheelsgruppe.add(wheels)
            elif verdi == 3:
                spiller.reset(x*32, y*32)
            elif verdi == 4:
                door = DoorOut(x*32, y*32)
                exitgruppe.add(door)
            elif verdi == 5:
                fix = Fixstation(x*32,y*32)
                fixgruppe.add(fix)
            elif verdi == 6:
                boss = Boss(x*32,y*32)
                ballgruppe.add(boss)

    if fscreen:
        fullscreen()
        print("Fullscreen is on!")
    else:
        print("Fullscreen is off!")
    channel.fadeout(1000)

##############################################################

for y, rad in enumerate(level[levelnum]):
        for x, verdi in enumerate(rad):
            if verdi == 3:
                spiller = Spiller(x*32, y*32)
                spillergruppe.add(spiller)
                


def ballmove():
    for ball in ballgruppe:
        ball.treffVegg()
        ball.flytt()
    ballgruppe.update()

def balldrawscreen():
    ballgruppe.draw(screen)


timeuntilspawnball = 0

def showspeed():
    valy = spiller.fartud
    valx = spiller.fartlr
    if spiller.fartud < 0:
        valy *= -1
    if spiller.fartlr < 0:
        valx *= -1
    text((str(int(valx+valy))),(100), (height-50), (200, 100, 100), 60)


restart()

#################### MAIN ######################
while running:

    if timeuntilspawnball > timewaituntilspawn:

        if gameover==False:
            trykketliste = pygame.key.get_pressed()
            if trykketliste[pygame.K_UP] or trykketliste[pygame.K_w]:
                spiller.flyttUp()
                playerhasmoved = True
            if trykketliste[pygame.K_DOWN] or trykketliste[pygame.K_s]:
                spiller.flyttDown()
                playerhasmoved = True
            if trykketliste[pygame.K_RIGHT] or trykketliste[pygame.K_d]:
                spiller.flyttR()
                playerhasmoved = True
            if trykketliste[pygame.K_LEFT] or trykketliste[pygame.K_a]:
                spiller.flyttL()
                playerhasmoved = True

        spiller.treffVegg()
        spiller.move()
        spiller.damage()

        if playerhasmoved:
            ballmove()

    if timeuntilspawnball > timewaituntilspawn:

        treffliste = pygame.sprite.groupcollide(
            spillergruppe, ballgruppe, False, True, pygame.sprite.collide_mask)

        if treffliste and gameover == False:
            splay("breakLQ.wav",4)
            spiller.life -= 45
            if spiller.life < 0:
                gameover = True

        balltruffet = pygame.sprite.groupcollide(
            ballgruppe, defencegruppe, True, True, pygame.sprite.collide_mask)

    # ballgruppe.update()
    spillergruppe.update()
    defencegruppe.update()
    wallgruppe.update()
    loadgruppe.update()
    wheelsgruppe.update()
    exitgruppe.update()
    fixgruppe.update()
    spawngruppe.update()

    screen.fill((5, 5, 5))

    spawngruppe.draw(screen)
    exitgruppe.draw(screen)
    wheelsgruppe.draw(screen)
    fixgruppe.draw(screen)
    defencegruppe.draw(screen)
    balldrawscreen()
    ballgruppe.draw(screen)
    spillergruppe.draw(screen)
    wallgruppe.draw(screen)

    if devmode:
        mposx = pygame.mouse.get_pos()[0]
        mposy = pygame.mouse.get_pos()[1]

        mposx = int(mposx/32)
        mposy = int(mposy/32)
        for twall in twallgruppe:
            twall.kill()
        twall = TempWall(mposx*32,mposy*32)
        twallgruppe.add(twall)
        twallgruppe.draw(screen)
    else:
        for twall in twallgruppe:
            twall.kill()

    if playerhasmoved == False:
        text('Press keys to start', (width/2),
             (height-100), (255, 255, 255), 52)

    if timeuntilspawnball < timewaituntilspawn:
        screen.fill((33, 33, 33))
        text('LOADING', (width/2), (height/2), (55, 255, 55), 72)
        loadingBar((scoretwo), (5/(timewaituntilspawn/60)))
        loadgruppe.draw(screen)
        

    timeuntilspawnball += 1

    if timeuntilspawnball == 1:
        spawnBalls()

    if gameover:
        text('GAME OVER', (width/2), (height/2), (255, 55, 55), 72)
        text('Press enter', (width/2), (height/2+100), (200, 200, 200), 52)
        if hasgameover == False:
            #pygame.mixer.fadeout(1000)
            channel.fadeout(1000)
            songchannel.fadeout(3000)
            splay("gameoverLQ.wav",6)
            hasgameover = True
        

    if spiller.complete:
        text('LEVEL COMPLETE', (width/2), (height/2), (55, 255, 55), 72)

    text(('Score: ' + str(int(score/30))), (100), (50), (200, 200, 200), 30)

    text(('Wheels: ' + str(int(spiller.howmany_wheels))),(width-100), (height-50), (200, 200, 200), 30)

    text(('Health: ' + str(int(spiller.life))),(width-100), (height-100), (200, 200, 200), 30)

    if devmode:
        text('DEV', (width/2), (50), (255, 0, 0), 30)

    showspeed()

    if gameover == False and timeuntilspawnball > 220 and playerhasmoved:
        score = score + 1

    if gameover == False:
        scoretwo = scoretwo + 1
        
    if width < 960:
        width = 960
        screen = pygame.display.set_mode((width, height))
        print("You have a screen size lower than the minimum amount. If you are using repl.it resize the window or go in fullscreen.")
    if height < 540:
        height = 540
        screen = pygame.display.set_mode((width, height))
        print("You have a screen size lower than the minimum amount. If you are using repl.it resize the window or go in fullscreen.")

    clock.tick(30)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:

            print("The mouse button doesn't do anything yet")

        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_F1:
                if devmode:
                    devmode = False
                else:
                    devmode = True
            
            if event.key == pygame.K_SPACE:
                if spiller.howmany_wheels > 0 and gameover == False:
                    splay("boingLQ.wav")
                    
                    posx = int((spiller.rect.x+20)/32)
                    posy = int((spiller.rect.y+20)/32)

                    defence = Defence(posx*32, posy*32)
                    defencegruppe.add(defence)
                    spiller.howmany_wheels -= 1
            
            
            if event.key == pygame.K_F11:
                # pygame.display.quit
                if fscreen == False:
                    width = round(pygame.display.get_desktop_sizes()[0][0] / 1)
                    height = round(pygame.display.get_desktop_sizes()[0][1] / 1)
                    print("Setting up window with the size... " + str(width) + " " + str(height))
                    screen = pygame.display.set_mode((width, height), flags=(pygame.HWSURFACE))
                    pygame.display.toggle_fullscreen()

                    fscreen = True

                    fullscreen()

                    #for ball in ballgruppe:
                        #ball.rect.x += (width/2)-480
                        #ball.rect.y += (height/2)-288
                    #ballgruppe.update()

                    # for splr in spillergruppe:
                    #splr.rect.x *= 2
                    #splr.rect.y *= 2
                    # spillergruppe.update()
                else:
                    width = round(pygame.display.get_desktop_sizes()[0][0] / 2)
                    height = round(pygame.display.get_desktop_sizes()[0][1] / 2)
                    pygame.display.toggle_fullscreen()
                    print("Setting up window with the size... " + str(width) + " " + str(height))
                    screen = pygame.display.set_mode((width, height))

                    fscreen = False

                    noNfullscreen()

                    # for splr in spillergruppe:
                    #splr.rect.x /= 2
                    #splr.rect.y /= 2
                    # spillergruppe.update()

            if event.key == pygame.K_F9:
                width = 960
                height = 540
                
                if fscreen:
                    pygame.display.toggle_fullscreen()
                    noNfullscreen()
                print("Setting up window with the size... " + str(width) + " " + str(height))
                screen = pygame.display.set_mode((width, height))

                fscreen = False
            
            if event.key == pygame.K_RETURN and gameover:
                restart(1)

            if event.key == pygame.K_F2 and devmode:
                restart(1)
            
            
            if event.key == pygame.K_F3 and devmode:
                levelnum = 0
                restart(1)
            
            
            if event.key == pygame.K_F10:
                fullscreen()
            
            
            if event.key == pygame.K_F12:
                noNfullscreen()
            
            
            if event.key == pygame.K_LALT and devmode:
                mposx = pygame.mouse.get_pos()[0]
                mposy = pygame.mouse.get_pos()[1]

                mposx = int(mposx/32)
                mposy = int(mposy/32)

                print("button pressed at " + str(mposx) + ":" + str(mposy))

                custommap[mposy][mposx] += 1
                if custommap[mposy][mposx] > 6:
                    custommap[mposy][mposx] = 0
                #vegg = Vegg(mposx*32, mposy*32)
                #wallgruppe.add(vegg)

                for ball in ballgruppe:
                    ball.kill()
                for wheels in wheelsgruppe:
                    wheels.kill()
                for fix in fixgruppe:
                    fix.kill()
                for wall in wallgruppe:
                    wall.kill()
                for wheel in defencegruppe:
                    wheel.kill()
                for door in exitgruppe:
                    door.kill()
                for spawn in spawngruppe:
                    spawn.kill()
            
                ################### LEVEL CREATOR #######################
                for y, rad in enumerate(custommap):
                    for x, verdi in enumerate(rad):
                    
                        if verdi == 1:
                            vegg = Vegg(x*32, y*32)
                            wallgruppe.add(vegg)
                        elif verdi == 2:
                            wheels = Wheels(x*32, y*32)
                            wheelsgruppe.add(wheels)
                        elif verdi == 3:
                            spawn = Spawn(x*32, y*32)
                            spawngruppe.add(spawn)
                        elif verdi == 4:
                            door = DoorOut(x*32, y*32)
                            exitgruppe.add(door)
                        elif verdi == 5:
                            fix = Fixstation(x*32,y*32)
                            fixgruppe.add(fix)
                        elif verdi == 6:
                            boss = Boss(x*32,y*32)
                            ballgruppe.add(boss)
            
            
            if event.key == pygame.K_F8 and devmode:
                for y, rad in enumerate(custommap):
                    print(custommap[y])
            
            
            if event.key == pygame.K_F7 and devmode:
                for wall in wallgruppe:
                    wall.kill()
                for ball in ballgruppe:
                    ball.kill()

            if event.key == pygame.K_TAB and timeuntilspawnball < timewaituntilspawn:
                timewaituntilspawn = timeuntilspawnball
                print("Skipped")
                

pygame.quit()
