#https://github.com/PaninjaZ/GetawayRocks/releases/latest/download/GoAwayRocks.zip

import sys
import requests
import zipfile
import os
import pygame
from time import sleep
pygame.init()
clock = pygame.time.Clock()
sys.path.insert(0,'file')

def install():

    global hasdownloaded
    hasdownloaded = True

    global buttontext
    buttontext = "Wait..."

    url = 'https://github.com/PaninjaZ/GetawayRocks/releases/latest/download/GoAwayRocks.zip'
    r = requests.get(url, allow_redirects=True)

    cur_path = os.path.dirname(__file__)

    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    config_path = os.path.join(application_path)

    new_path = config_path + "/game.zip"

    with open(new_path, 'wb') as f:
        f.write(r.content)

    #try:
    #    with zipfile.ZipFile(new_path, 'r') as zip_ref:
    #        zip_ref.extractall(config_path)
    #except ValueError:
    #    try:
    #        with zipfile.ZipFile(new_path, 'r') as zip_ref:
    #            zip_ref.extractall(config_path + "/game")
    #    except ValueError:
    #        print("Something went wrong!")
    #        pass

    #with zipfile.ZipFile(new_path, 'r') as zip_ref:
    #    zip_ref.extractall(config_path)

    with zipfile.ZipFile(new_path, 'r') as zip_ref:
        zip_ref.extractall(config_path + "/game")


    if os.path.exists(config_path+"/game.zip"):
        os.remove(config_path+"/game.zip")
    else:
        buttontext = "ERROR"
        print("The file does not exist")
        return
    
    buttontext = "Done!"


################### CONTENT ################################

 #determine if application is a script file or frozen exe
#if getattr(sys, 'frozen', False):
#    application_path = os.path.dirname(sys.executable)
#    config_path = os.path.join(application_path)
#
#    Path = config_path + "/update_data/"
#elif __file__:
#    application_path = os.path.dirname(__file__)
#    config_path = os.path.join(application_path)
#
#    Path = config_path + "/update_data/"

#Path = "update_data/"

application_path = os.path.dirname(__file__)
config_path = os.path.join(application_path)

Path = config_path + "/update_data/"

print("")
print(Path)

print("")
print("  __  __  ____  _    _ _   _ _______       _____ _   _    _____          __  __ ______  _____ \n |  \/  |/ __ \| |  | | \ | |__   __|/\   |_   _| \ | |  / ____|   /\   |  \/  |  ____|/ ____|\n | \  / | |  | | |  | |  \| |  | |  /  \    | | |  \| | | |  __   /  \  | \  / | |__  | (___  \n | |\/| | |  | | |  | | . ` |  | | / /\ \   | | | . ` | | | |_ | / /\ \ | |\/| |  __|  \___ \ \n | |  | | |__| | |__| | |\  |  | |/ ____ \ _| |_| |\  | | |__| |/ ____ \| |  | | |____ ____) |\n |_|  |_|\____/ \____/|_| \_|  |_/_/    \_\_____|_| \_|  \_____/_/    \_\_|  |_|______|_____/ ")
print("")

def img(var):
    image = pygame.image.load(Path+var)
    return image

def text(value, px, py, clr, scale):
    font = pygame.font.Font(Path+'Poppins-SemiBold.ttf', scale)
    txt = font.render(value, True, clr)
    txtrect = txt.get_rect()
    txtrect.center = (px, py)
    screen.blit(txt, txtrect)

print("Loading display")

################### SCREEN ##################################
width = 440
height = 540
print("Setting up window with the size... " + str(width) + " " + str(height))
screen = pygame.display.set_mode((width, height))
#screenLogo = pygame.image.load("logo32.png")
screenLogo = img("logo32.png")
pygame.display.set_icon(screenLogo)
pygame.display.set_caption("Installer")

fscreen = False
settscreen = False
downloading = False
hasdownloaded = False
hover = False
downloadcomplete = False

buttontext = "Download"

running = True

class Logo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(p+'data/wheel.png').convert_alpha()
        self.image = img("logo225_side.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def change(self,style, x, y):
        if style == 1:
            self.image = img("logo225_side.png")
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        else:
            image = img("logo225_side2.png")
            width_img = image.get_width()
            height_img = image.get_height()
            self.image = pygame.transform.scale(image, (int(width_img*2), int(height_img*2)))
            #self.image = img("logo225_side2.png")
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(p+'data/wheel.png').convert_alpha()
        self.image = img("button.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def click(self):
        
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            global downloading
            global buttontext
            global downloadcomplete
            buttontext = "Wait..."
            if downloading == False:
                downloading = True
                buttontext = "Wait..."
            else:
                buttontext = "Done!"

    def update(self):

        global hover

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            hover = True
            self.image = img("button_down.png")
        else:
            hover = False
            self.image = img("button.png")


buttongruppe = pygame.sprite.Group()
logogruppe = pygame.sprite.Group()

button = Button(width/2-120, height/2+130)
buttongruppe.add(button)

logo = Logo(width/2-112.5,height/2-112.5)
logogruppe.add(logo)

#################### MAIN ######################
while running:

    button.update()
    
    screen.fill((233, 233, 233))

    buttongruppe.draw(screen)
    logogruppe.draw(screen)

    text("MOUNTAIN GAMES",(width/2),(height/2-200),(51, 28, 50), 40)
    text("Downloader",(width/2),(height/2-150),(51, 28, 50), 60)

    if hover:
        text(buttontext,(width/2),(height/2+160),(71, 171, 237), 40)
    else:
        text(buttontext,(width/2),(height/2+160),(51, 28, 50), 40)
    
    if downloadcomplete:
        text("Files located in game folder",(width/2),(height-50),(55,155,55),25)

    if downloading and hasdownloaded==False:
        print("Downloading")
        screen.fill((233, 233, 233))

        logo.change(2,width/2-112.5,height/2-112.5)

        logogruppe.draw(screen)

        font = pygame.font.Font(Path+'Poppins-SemiBold.ttf', 40)
        txt = font.render("Downloading", True, (155,55,55))
        txtrect = txt.get_rect()
        txtrect.center = (width/2, height/2)
        screen.blit(txt, txtrect)

        pygame.display.update()

        hasdownloaded = True

        install()

        downloadcomplete = True

        logo.change(1,width/2-112.5,height/2-112.5)

    clock.tick(30)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Click")
            button.click()
                

pygame.quit()
