# init
import pygame
from pygame.locals import *
import random
from datetime import date
import tkinter as tk
from tkinter import filedialog
import ast

pygame.init()

max_fps = 60
gametick = pygame.time.Clock()

icon = pygame.image.load("assets/window.png")
pygame.display.set_icon(icon)
window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Домино: Python Edition v. Beta 1.4 development version")
game_version = "v. Beta 1.4 (work in progress)"

# variables
current_ui = "menu_main" # defines what kind of image to draw (game/ui/etc.)
debug = False # toggles debug features
game_state = "menu" # defines what is happening right now (gm selection, setup, playing, etc.)
splashes = ["Python recreation!",
            "No longer looks like spaghetti!",
            "Less lag!",
            "My brain is gonna explode...",
            "Uses Pygame!",
            "HD!",
            "What a nice window!",
            "Indie!",
            "Made in Russia!",
            "Also try Minecraft!",
            #"There are private pre-releases!",
            "Endless possibilities!",
            "Hard-coded!",
            "bruh",
            "Made during coronavirus pandemic!",
            "Beta!",
            "class domino():",
            "100% free!",
            "No one paid me for this!",
            "Over 1000 lines!",
            "domino:splashes/namespaced_splash",
            #"Lacks a cool GUI!",
            "Quite stable!",
            "Made by a 13-year-old!",
            "Thanks, Google!",
            "Thanks, StackOverflow!",
            "youtu.be/dQw4w9WgXcQ",
            "Has a lot of comments!",
            "I'm not a pro programmer btw",
            "§§§§§§!",
            "Getting advanced!",
            "We need more splashes!",
            "Can I put you in a bucket?",
            "subscribe to pewdiepie"] # the list of existing splashes
random_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/*-+()[]{}абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
##color_menu_light = (3, 209, 255)
##color_button_light = (1, 175, 216)
##color_button_press_light = (0, 156, 191) # we have themes now, so we don't need this anymore
font_title = pygame.font.Font('assets/denhome.otf',300)
font_splash = pygame.font.Font('assets/comic.ttf',  40)
font_pe = pygame.font.Font('assets/bahnschrift.ttf',30)
font_gm_sel = pygame.font.Font('assets/denhome.otf',70)
font_pd = pygame.font.Font('assets/bahnschrift.ttf',15)
font_ver = pygame.font.Font('assets/denhome.otf',   40)
font_score = pygame.font.Font('assets/denhome.otf',250)
font_d50 = pygame.font.Font('assets/denhome.otf',   50)
font_fps = pygame.font.Font('assets/denhome.otf',   30)
current_splash = random.choice(splashes)
today = date.today()
if today.strftime("%d%m") == "1408":
    current_splash = "Happy birthday, §§§§!"
elif today.strftime("%d%m") == "1907":
    current_splash = "Happy birthday, WinNT!"
splash = current_splash
pressed = 0
score_val = [0, 1, 2, 3, 4, 5, 6,
             2, 3, 4, 5, 6, 7,
             4, 5, 6, 7, 8,
             6, 7, 8, 9,
             8, 9, 10,
             10, 11,
             12] # score values for dominoes, used in score counting at the end
p1 = [] # player 1's inventory
p2 = [] # player 2's inventory
dominoes = ["00", "01", "02", "03", "04", "05", "06",
            "11", "12", "13", "14", "15", "16",
            "22", "23", "24", "25", "26",
            "33", "34", "35", "36",
            "44", "45", "46",
            "55", "56",
            "66"] # the list of dominoes, used when placing them
left_able = []
right_able = []
bazar = [] # dominoes that don't belong to anyone nor are placed
right_end = 0
left_end = 0
left_side = []
right_side = []
ren_left_side = []
ren_right_side = []
ren_left_is_inv = []
ren_right_is_inv = [] # the copies of the four originals used by renderer
dmn0 = 0 # the middle domino
left_is_inv = []
right_is_inv = []
current_move = 1
backup_move = 1
p1_score = 0
p2_score = 0
p1_wins = 0
p2_wins = 0
last_domino = 0 # the last placed domino
##p1_able = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
##p2_able = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
##bazar_able = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
is_p1_able = True
is_p2_able = True
is_bazar_able = True
p1_to_add = 0
p2_to_add = 0
ren_dnm0_x = 608
ren_dmn0_y = 300
ren_dmn_left_start_x = [493, 378, 263, 148, 89, 89, 204, 319, 434, 549, 664, 779, 894, 1009, 1124, 1068, 953, 838, 723, 608, 493, 378, 263, 148]
ren_dmn_left_start_y = [328, 328, 328, 328, 272, 213, 213, 213, 213, 213, 213, 213, 213, 213, 157, 98, 98, 98, 98, 98, 98, 98, 98, 98]
ren_dmn_left_is_vert = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False]
ren_dmn_left_is_inv = [False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False]
##ren_dmn_spiral_left_start_x = []
##ren_dmn_spiral_left_start_y = []
##ren_dmn_spiral_left_is_vert = []
ren_dmn_right_start_x = [667, 782, 897, 1012, 1127, 1071, 956, 841, 726, 611, 496, 381, 266, 151, 92, 92, 207, 322, 437, 552, 667, 782, 897, 1012]
ren_dmn_right_start_y = [328, 328, 328, 328, 328, 443, 443, 443, 443, 443, 443, 443, 443, 443, 443, 558, 558, 558, 558, 558, 558, 558, 558, 558]
ren_dmn_right_is_vert = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False]
ren_dmn_right_is_inv = [False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False]
##ren_dmn_spiral_right_start_x = []
##ren_dmn_spiral_right_start_y = []
##ren_dmn_spiral_right_is_vert = []
ren_start_x = 0
ren_start_y = 0
# theme_desc = [domino outline and divider,      0
#               domino color,                    1
#               1,                               2
#               2,                               3
#               3,                               4
#               4,                               5
#               5,                               6
#               6,                               7
#               main ui color,                   8
#               inactive/pressed button color    9
#               default button color,            10
#               active text color,               11
#               inactive text color,             12
#               splash color,                    13
#               victory (green) color,           14
#               failure (red) color              15
#               meta: author                     16
#               meta: name                       17
#               meta: description                18
#               meta: file format (0 for b1.4)   19
default_themes = [
                    [(0, 0, 0),
                    (255, 255, 255),
                    (255, 0, 0),
                    (255, 128, 0),
                    (255, 255, 0),
                    (0, 255, 0),
                    (0, 255, 255),
                    (0, 0, 255),
                    (3, 209, 255),
                    (0, 156, 191),
                    (1, 175, 216),
                    (0, 0, 0),
                    (45, 45, 45),
                    (240, 255, 0),
                     (0, 200, 0),
                    (200, 0, 0),
                    "WinNT",
                    "Стандартная светлая",
                    "Классическая светлая тема",
                    0],
                  
                    [(127, 127, 127),
                    (20, 20, 20),
                    (255, 0, 0),
                    (255, 128, 0),
                    (255, 255, 0),
                    (0, 255, 0),
                    (0, 255, 255),
                    (0, 0, 255),
                    (20, 20, 20),
                    (0, 0, 0),
                    (10, 10, 10),
                    (200, 200, 200),
                    (100, 100, 100),
                    (160, 170, 0),
                    (0, 127, 0),
                    (127, 0, 0),
                    "WinNT",
                    "Стандартная тёмная",
                    "Классическая тёмная тема",
                    0]
                 ]
random_list1 = []
for i in range(1, 25):
    random_list1.append(random.randint(1, 28))
random_list2 = []
for i in range(1, 25):
    random_list2.append(random.randint(0, 1))
mouse_is_over = [0, 0]
scorelim = 125
min_write = 13
player_size = 7
##is_rendered = False
restart_type = "game" # whether we are starting a new game (must start with a double) or just a new battle (the player who last won may use anything)
beginning_double = 1 # the double that you must use on a new game
test_bool = False # a debug variable
try:
    config = open("domino_config.dc2", 'r') # check is the file is missing and if it is then make a new one with default settings
except OSError:
    print("File error: no config file present, creating a new one")
    config = open("domino_config.dc2", 'w')
    config.seek(0, 0)
    config.write('1\n0\n1')
config = open("domino_config.dc2", 'r')
config.seek(0, 0)
config_data = config.readlines()
try:
    windowed_score = bool(int(config_data[0]))
    fastmode = bool(int(config_data[1]))
    theme_id = int(config_data[2]) # try to read the config file and if we fail, recreate it
except IndexError:
    print("File error: config file is empty or corrupted")
    config = open("domino_config.dc2", 'w')
    config.seek(0, 0)
    config.write('1\n0\n1')
    windowed_score = bool(int(config_data[0]))
    fastmode = bool(int(config_data[1]))
    theme_id = int(config_data[2])

config = open("domino_config.dc2", 'r') # read the themes
config.seek(0, 0)
config_data = config.readlines()

custom_themes = []
for i in range(len(config_data) - 3):
    temp_theme = config_data[i+3]
    try:
        custom_themes.append(ast.literal_eval(temp_theme))
    except ValueError:
        print("File error: config file is corrupted - invaild theme:", temp_theme)
        custom_themes.append(default_themes[1])
if theme_id < 2:
    current_theme = default_themes[theme_id]
else:
    current_theme = custom_themes[theme_id - 2]

is_theme_updated = False
backup_ui = "menu_main"

framerate_output = pygame.USEREVENT+1
output_fps = pygame.event.Event(framerate_output)
pygame.time.set_timer(framerate_output, 500)
current_fps = "FPS: (wait)"

this_player = "player" # if a player or an AI is playing
gamemode = "not_selected" # current gamemode (local, pva, bot_battle)
is_config_open = False # is the config file open

# classes
class button():
    def __init__(self, color,x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None,font_color=current_theme[11],font_size=60):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.Font('assets/denhome.otf', font_size)
            text = font.render(self.text, 1, font_color)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width and self.pos[1] > self.y and self.pos[1] < self.y + self.height:
            return True
        else:
            return False

class slider(): # a slider that acts like a button, based on the button class
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 86
        self.height = 36

    def draw(self, active):
        #Call this method to draw the button on the screen
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width and self.pos[1] > self.y and self.pos[1] < self.y + self.height:
            pygame.draw.rect(window, current_theme[8], (self.x, self.y, self.width, self.height), 0, int(self.height / 2))
        else:
            pygame.draw.rect(window, current_theme[10], (self.x, self.y, self.width, self.height), 0, int(self.height / 2))   
        pygame.draw.rect(window, current_theme[0], (self.x-2, self.y-2, self.width+4, self.height+4), 4, int(self.height / 2))
        if active:
            pygame.draw.circle(window, current_theme[14], (self.x + 70, self.y + 18), 18)
            pygame.draw.circle(window, current_theme[0], (self.x + 70, self.y + 18), 18, 4)
        else:
            pygame.draw.circle(window, current_theme[15], (self.x + 16, self.y + 18), 18)
            pygame.draw.circle(window, current_theme[0], (self.x + 16, self.y + 18), 18, 4)

    def is_over(self):
        # returns true if mouse is over
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width and self.pos[1] > self.y and self.pos[1] < self.y + self.height:
            return True
        else:
            return False

class domino():
    def __init__(self, win, theme=current_theme):
        self.win = win
        self.theme = theme
    def draw_field(self, side, number, value, rotation=False, inverted=False):
        ren_temp_start_x = ren_dmn_left_start_x[number-1]+ren_start_x
        ren_temp_start_y = ren_dmn_left_start_y[number-1]+ren_start_y
        # left
        if side == "left" and number > 0:
            # horisontal not inverted
            if rotation == False and inverted == False:
                pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x, ren_temp_start_y, 119, 63))
                pygame.draw.rect(self.win, current_theme[1], (ren_temp_start_x+4, ren_temp_start_y+4, 111, 55))
                pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x+58, ren_temp_start_y+8, 3, 47))
                if dominoes[value-1][0] == '1':
                    pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][0] == '2':
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '3':
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '4':
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '5':
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][0] == '6':
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+31, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+31, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                ren_temp_start_x += 60
                if dominoes[value-1][1] == '1':
                    pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][1] == '2':
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '3':
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '4':
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '5':
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][1] == '6':
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+31, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+31, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
            # vertical not inverted
            if rotation == True and inverted == False:
                pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x, ren_temp_start_y, 63, 119))
                pygame.draw.rect(self.win, current_theme[1], (ren_temp_start_x+4, ren_temp_start_y+4, 55, 111))
                pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x+8, ren_temp_start_y+58, 47, 3))
                if dominoes[value-1][0] == '1':
                    pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][0] == '2':
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '3':
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '4':
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '5':
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][0] == '6':
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                ren_temp_start_y += 60
                if dominoes[value-1][1] == '1':
                    pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][1] == '2':
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '3':
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '4':
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '5':
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][1] == '6':
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
            # left inverted
            if rotation == False and inverted == True:
                pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x, ren_temp_start_y, 119, 63))
                pygame.draw.rect(self.win, current_theme[1], (ren_temp_start_x+4, ren_temp_start_y+4, 111, 55))
                pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x+58, ren_temp_start_y+8, 3, 47))
                if dominoes[value-1][1] == '1':
                    pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][1] == '2':
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '3':
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '4':
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '5':
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][1] == '6':
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+31, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+31, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                ren_temp_start_x += 60
                if dominoes[value-1][0] == '1':
                    pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][0] == '2':
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '3':
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '4':
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '5':
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][0] == '6':
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+31, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+31, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
            # vertical inverted
            if rotation == True and inverted == True:
                pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x, ren_temp_start_y, 63, 119))
                pygame.draw.rect(self.win, current_theme[1], (ren_temp_start_x+4, ren_temp_start_y+4, 55, 111))
                pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x+8, ren_temp_start_y+58, 47, 3))
                if dominoes[value-1][1] == '1':
                    pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][1] == '2':
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '3':
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '4':
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '5':
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][1] == '6':
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                ren_temp_start_y += 60
                if dominoes[value-1][0] == '1':
                    pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][0] == '2':
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '3':
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '4':
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '5':
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][0] == '6':
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
        # right
        if side == "right" and number > 0:
            ren_temp_start_x = ren_dmn_right_start_x[number-1]+ren_start_x
            ren_temp_start_y = ren_dmn_right_start_y[number-1]+ren_start_y
            if rotation == False and inverted == False:
                pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x, ren_temp_start_y, 119, 63))
                pygame.draw.rect(self.win, current_theme[1], (ren_temp_start_x+4, ren_temp_start_y+4, 111, 55))
                pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x+58, ren_temp_start_y+8, 3, 47))
                if dominoes[value-1][0] == '1':
                    pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][0] == '2':
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '3':
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '4':
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '5':
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][0] == '6':
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+31, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+31, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                ren_temp_start_x += 60
                if dominoes[value-1][1] == '1':
                    pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][1] == '2':
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '3':
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '4':
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '5':
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][1] == '6':
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+31, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+31, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
            if rotation == True and inverted == False:
                pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x, ren_temp_start_y, 63, 119))
                pygame.draw.rect(self.win, current_theme[1], (ren_temp_start_x+4, ren_temp_start_y+4, 55, 111))
                pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x+8, ren_temp_start_y+58, 47, 3))
                if dominoes[value-1][0] == '1':
                    pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][0] == '2':
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '3':
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '4':
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '5':
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][0] == '6':
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                ren_temp_start_y += 60
                if dominoes[value-1][1] == '1':
                    pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][1] == '2':
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '3':
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '4':
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '5':
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][1] == '6':
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
            if rotation == False and inverted == True:
                pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x, ren_temp_start_y, 119, 63))
                pygame.draw.rect(self.win, current_theme[1], (ren_temp_start_x+4, ren_temp_start_y+4, 111, 55))
                pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x+58, ren_temp_start_y+8, 3, 47))
                if dominoes[value-1][1] == '1':
                    pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][1] == '2':
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '3':
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '4':
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '5':
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][1] == '6':
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+31, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+31, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                ren_temp_start_x += 60
                if dominoes[value-1][0] == '1':
                    pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][0] == '2':
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '3':
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '4':
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '5':
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][0] == '6':
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+31, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+31, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
            if rotation == True and inverted == True:
                pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x, ren_temp_start_y, 63, 119))
                pygame.draw.rect(self.win, current_theme[1], (ren_temp_start_x+4, ren_temp_start_y+4, 55, 111))
                pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x+8, ren_temp_start_y+58, 47, 3))
                if dominoes[value-1][1] == '1':
                    pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][1] == '2':
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '3':
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '4':
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][1] == '5':
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][1] == '6':
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                ren_temp_start_y += 60
                if dominoes[value-1][0] == '1':
                    pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][0] == '2':
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '3':
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '4':
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                if dominoes[value-1][0] == '5':
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                if dominoes[value-1][0] == '6':
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+31), 3, 3)
                    pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
        if number == 0:
            ren_temp_start_x = 608 + ren_start_x
            ren_temp_start_y = 300 + ren_start_y
            pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x, ren_temp_start_y, 63, 119))
            pygame.draw.rect(self.win, current_theme[1], (ren_temp_start_x+4, ren_temp_start_y+4, 55, 111))
            pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x+8, ren_temp_start_y+58, 47, 3))
            if dominoes[value-1][0] == '1':
                pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
            if dominoes[value-1][0] == '2':
                pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
            if dominoes[value-1][0] == '3':
                pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
            if dominoes[value-1][0] == '4':
                pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
            if dominoes[value-1][0] == '5':
                pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
            if dominoes[value-1][0] == '6':
                pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+31), 3, 3)
                pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+31), 3, 3)
                pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
            ren_temp_start_y += 60
            if dominoes[value-1][1] == '1':
                pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
            if dominoes[value-1][1] == '2':
                pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
            if dominoes[value-1][1] == '3':
                pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
                pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
            if dominoes[value-1][1] == '4':
                pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
            if dominoes[value-1][1] == '5':
                pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
                pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
            if dominoes[value-1][1] == '6':
                pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
                pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+31), 3, 3)
                pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
                pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
                pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+31), 3, 3)
                pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
    def draw_player(self, coords, value):
        ren_temp_start_x = coords[0]
        ren_temp_start_y = coords[1]
        pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x, ren_temp_start_y, 63, 119))
        pygame.draw.rect(self.win, current_theme[1], (ren_temp_start_x+4, ren_temp_start_y+4, 55, 111))
        pygame.draw.rect(self.win, current_theme[0], (ren_temp_start_x+8, ren_temp_start_y+58, 47, 3))
        if dominoes[value-1][0] == '1':
            pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
        if dominoes[value-1][0] == '2':
            pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
            pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
        if dominoes[value-1][0] == '3':
            pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
            pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
            pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
        if dominoes[value-1][0] == '4':
            pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
            pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
            pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
            pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
        if dominoes[value-1][0] == '5':
            pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
            pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
            pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
            pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
            pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
        if dominoes[value-1][0] == '6':
            pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
            pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+31), 3, 3)
            pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
            pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
            pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+31), 3, 3)
            pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
        ren_temp_start_y += 60
        if dominoes[value-1][1] == '1':
            pygame.draw.circle(self.win, current_theme[2], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
        if dominoes[value-1][1] == '2':
            pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
            pygame.draw.circle(self.win, current_theme[3], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
        if dominoes[value-1][1] == '3':
            pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
            pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
            pygame.draw.circle(self.win, current_theme[4], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
        if dominoes[value-1][1] == '4':
            pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
            pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
            pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
            pygame.draw.circle(self.win, current_theme[5], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
        if dominoes[value-1][1] == '5':
            pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
            pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
            pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
            pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
            pygame.draw.circle(self.win, current_theme[6], (ren_temp_start_x+31, ren_temp_start_y+31), 3, 3)
        if dominoes[value-1][1] == '6':
            pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+17), 3, 3)
            pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+31), 3, 3)
            pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+17, ren_temp_start_y+45), 3, 3)
            pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+17), 3, 3)
            pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+31), 3, 3)
            pygame.draw.circle(self.win, current_theme[7], (ren_temp_start_x+45, ren_temp_start_y+45), 3, 3)
        
# button definitions
# NO LONGER USED HERE BECAUSE OF BUGS
# USED HERE AGAIN TO FIX MORE BUGS
btn_play = button(current_theme[10], 500, 400, 280, 50, "Играть")
btn_settings = button(current_theme[10], 500, 500, 280, 50, "Настройки")
btn_how_to_play = button(current_theme[9], 500, 600, 280, 50, "Как играть")

btn_gm_local = button(current_theme[10], 250, 400, 300, 50, "Локальная игра")
btn_gm_internet = button(current_theme[9], 250, 500, 300, 50, "В разработке...")
btn_gm_pva = button(current_theme[10], 730, 400, 300, 50, "Одиночная игра")
btn_gm_ava = button(current_theme[10], 730, 500, 300, 50, "Битва ботов")
btn_gm_back = button(current_theme[10], 490, 600, 300, 50, "Назад")

btn_give_1 = button(current_theme[10], 600, 2, 80, 18, "Нету!")
btn_give_2 = button(current_theme[10], 600, 699, 80, 19, "Нету!")

btn_next_battle = button(current_theme[10], 540, 420, 200, 40, "Дальше")

btn_next_player = button(current_theme[10], 540, 500, 200, 50, "OK")

ren_domino = domino(window, current_theme)

# sliders in settings menu
test_slider = slider(640, 360) # for tests

s_windowed_score = slider(1170, 85)
##s_dark_theme = slider(1170, 155) # until we make a theme api # we're making it
s_fastmode = slider(1170, 155)

# render functions
def render_main_menu():
    global current_ui
    global game_version
    global is_rendered
    global test_bool
    window.fill(current_theme[8])
    # inactive buttons
##    btn_settings.draw(window, current_theme[12], current_theme[12]) # now active!!!
    btn_how_to_play.draw(window, current_theme[12], current_theme[12])
    # texts
    title = font_title.render("Домино", 4, current_theme[11])
    window.blit(title, (410, 0))
    edition = font_pe.render("Python Edition", 4, current_theme[11])
    window.blit(edition, (550, 210))
    ren_splash = font_splash.render(splash, 4, current_theme[13])
    ren_splash = pygame.transform.rotate(ren_splash, 30)
    window.blit(ren_splash, (900 - (ren_splash.get_width() / 2), 210 - (ren_splash.get_height() / 2)))
    version = font_ver.render(game_version, 4, current_theme[11])
    window.blit(version, (4, 720 - version.get_height()))
    is_rendered = True

def render_menu_gm_sel():
    global current_ui
    global game_version
    global is_rendered
    window.fill(current_theme[8])
    # inactive buttons
    btn_gm_internet.draw(window, current_theme[12], current_theme[12])
    btn_gm_pva.draw(window, current_theme[12], current_theme[12])
    btn_gm_ava.draw(window, current_theme[12], current_theme[12])
    # texts
    title = font_title.render("Домино", 4, current_theme[11])
    window.blit(title, (410, 0))
    edition = font_pe.render("Python Edition", 4, current_theme[11])
    window.blit(edition, (550, 210))
    gm_sel = font_gm_sel.render("Выберите режим игры:", 4, current_theme[11])
    window.blit(gm_sel, (640 - (gm_sel.get_width() / 2), 300 - (gm_sel.get_height() / 2)))
    ren_splash = font_splash.render(splash, 4, current_theme[13])
    ren_splash = pygame.transform.rotate(ren_splash, 30)
    window.blit(ren_splash, (900 - (ren_splash.get_width() / 2), 210 - (ren_splash.get_height() / 2)))
    version = font_ver.render(game_version, 4, current_theme[11])
    window.blit(version, (4, 720 - version.get_height()))
    is_rendered = True

def game_ren():
    global left_side
    global right_side
    global ren_dmn_left_is_inv
    global ren_dmn_right_is_inv
    global ren_dmn_left_is_vert
    global ren_dmn_right_is_vert
    global left_is_inv
    global right_is_inv
    global dnm0
    global font_pd
    global is_rendered
    global gamemode
    window.fill(current_theme[8])
##    if debug == True: # render a full field of random dominoes to find errors
##        for i in range(1, 25):
##            ren_domino.draw_field("left", i, random_list1[i-1], ren_dmn_left_is_vert[i-1], random_list2[i-1])
##            ren_domino.draw_field("right", i, random_list1[i-1], ren_dmn_right_is_vert[i-1], random_list2[i-1])
##        ren_domino.draw_field("none", 0, random_list1[14], True, False)
##        pygame.draw.rect(window, (0, 0, 0), (20, 580, 1239, 119))
##        pygame.draw.rect(window, (color_button_press_light), (24, 584, 1230, 111))
##        pygame.draw.rect(window, (0, 0, 0), (20, 20, 1239, 119))
##        pygame.draw.rect(window, (color_button_press_light), (24, 24, 1230, 111))
##        for i in range(21):
##            if current_move == 1:
##                ren_domino.draw_player((20+((i)*59), 20), random_list1[i])
##            else:
##                pygame.draw.rect(window, theme_default[0], (20+((i)*59), 20, 63, 119))
##                pygame.draw.rect(window, theme_default[1], (24+((i)*59), 24, 55, 111))
##        for i in range(21):
##            if current_move == 2:
##                ren_domino.draw_player((20+((i)*59), 580), random_list1[i])
##            else:
##                pygame.draw.rect(window, theme_default[0], (20+((i)*59), 580, 63, 119))
##                pygame.draw.rect(window, theme_default[1], (24+((i)*59), 584, 55, 111))
    # render the dominoes
    for i in range(len(ren_left_side)):
        inv = (ren_dmn_left_is_inv[i] or ren_left_is_inv[i]) and not (ren_dmn_left_is_inv[i] and ren_left_is_inv[i])
        ren_domino.draw_field("left", i+1, ren_left_side[i], ren_dmn_left_is_vert[i], inv)
    for i in range(len(ren_right_side)):
        inv = (ren_dmn_right_is_inv[i] or ren_right_is_inv[i]) and not (ren_dmn_right_is_inv[i] and ren_right_is_inv[i])
        ren_domino.draw_field("right", i+1, ren_right_side[i], ren_dmn_right_is_vert[i], inv)
    if dmn0 > 0:
        ren_domino.draw_field("you can type anything here if a 0 comes after it", 0, dmn0, True, False)
    pygame.draw.rect(window, current_theme[0], (20, 580, 1239, 119))
    pygame.draw.rect(window, (current_theme[9]), (24, 584, 1230, 111))
    pygame.draw.rect(window, current_theme[0], (20, 20, 1239, 119))
    pygame.draw.rect(window, (current_theme[9]), (24, 24, 1230, 111))
    for i in range(len(p1)):
        if current_move < 2 or not gamemode == "local":
            ren_domino.draw_player((20+((i)*59), 20), p1[i])
        else:
            pygame.draw.rect(window, current_theme[0], (20+((i)*59), 20, 63, 119))
            pygame.draw.rect(window, current_theme[1], (24+((i)*59), 24, 55, 111))
    for i in range(len(p2)):
        if (current_move == 2 and gamemode == "local") or current_move == 0 or gamemode == "bot_battle":
            ren_domino.draw_player((20+((i)*59), 580), p2[i])
        else:
            pygame.draw.rect(window, current_theme[0], (20+((i)*59), 580, 63, 119))
            pygame.draw.rect(window, current_theme[1], (24+((i)*59), 584, 55, 111))
    playerdata1 = font_pd.render(("Игрок 1 - " + str(p1_score) + " очков, " + str(p1_wins) + " побед"), 4, current_theme[11], current_theme[9])
    window.blit(playerdata1, (24, 21-playerdata1.get_height()))
    pygame.draw.rect(window, current_theme[0], (21, 1, playerdata1.get_width()+5, 21), 4)
    playerdata2 = font_pd.render(("Игрок 2 - " + str(p2_score) + " очков, " + str(p2_wins) + " побед"), 4, current_theme[11], current_theme[9])
    window.blit(playerdata2, (24, 717-playerdata2.get_height()))
    pygame.draw.rect(window, current_theme[0], (21, 697, playerdata2.get_width()+5, 21), 4)
    btn_give_1.draw(window, current_theme[0], current_theme[11], 30)
    btn_give_2.draw(window, current_theme[0], current_theme[11], 30)
    is_rendered = True

def local_game_ctrl(inside_ai = False): # the inside_ai tag is for running inside an ai process so no infinite recursion is done
    # init variables
    global p1
    global p2
    global bazar
    global current_move
    global left_side
    global right_side
    global left_end
    global right_end
    global dmn0
    global left_is_inv
    global right_is_inv
    global last_domino
    global ren_start_x
    global ren_start_y
    global mouse_is_over
    global game_state
    global left_able
    global right_able
    global is_rendered
    global is_p1_able
    global is_p2_able
    global is_bazar_able
    global current_ui
    global ren_left_side
    global ren_right_side
    global ren_left_is_inv
    global ren_right_is_inv
    global gamemode
    # detect if someone has finished
    if len(p1) == 0 or len(p2) == 0:
        game_state = "end"
        current_ui = "end"
##        print("someone has ended!")
    # detect the dominoes that can be used
    if left_end == 0:
        left_able = [1, 2, 3, 4, 5, 6, 7]
    elif left_end == 1:
        left_able = [2, 8, 9, 10, 11, 12, 13]
    elif left_end == 2:
        left_able = [3, 9, 14, 15, 16, 17, 18]
    elif left_end == 3:
        left_able = [4, 10, 15, 19, 20, 21, 22]
    elif left_end == 4:
        left_able = [5, 11, 16, 20, 23, 24, 25]
    elif left_end == 5:
        left_able = [6, 12, 17, 21, 24, 26, 27]
    elif left_end == 6:
        left_able = [7, 13, 18, 22, 25, 27, 28]
    if right_end == 0:
        right_able = [1, 2, 3, 4, 5, 6, 7]
    elif right_end == 1:
        right_able = [2, 8, 9, 10, 11, 12, 13]
    elif right_end == 2:
        right_able = [3, 9, 14, 15, 16, 17, 18]
    elif right_end == 3:
        right_able = [4, 10, 15, 19, 20, 21, 22]
    elif right_end == 4:
        right_able = [5, 11, 16, 20, 23, 24, 25]
    elif right_end == 5:
        right_able = [6, 12, 17, 21, 24, 26, 27]
    elif right_end == 6:
        right_able = [7, 13, 18, 22, 25, 27, 28]
    # detect if anyone is able to go
    if not game_state == "beginning":
        is_p1_able = False
        is_p2_able = False
        is_bazar_able = False
        for i in p1:
            if i in left_able or i in right_able:
                is_p1_able = True
        for i in p2:
            if i in left_able or i in right_able:
                is_p2_able = True
        for i in bazar:
            if i in left_able or i in right_able:
                is_bazar_able = True
        if not is_p1_able and not is_p2_able and not is_bazar_able:
            game_state = "fish"
            current_ui = "end"
##            print("fish!")
    else:
        is_p1_able = True
        is_p2_able = True
        is_bazar_able = True
    if this_player == "ai" and not inside_ai:
        ai(current_move)
    else:
        # detect player actions
        if bool(pygame.event.get(pygame.MOUSEBUTTONDOWN)):
            is_rendered = False
            if btn_give_2.isOver():
                btn_give_2.color = current_theme[9]
                if current_move == 2:
                    try:
                        to_remove = random.choice(bazar)
                    except IndexError:
                        if not this_player == 'ai':
                            print("Value error: nothing to give to the player; skipping it's turn")
                        next_player()
                    else:
                        bazar.remove(to_remove)
                        p2.append(to_remove)
            if btn_give_1.isOver():
                btn_give_1.color = current_theme[9]
                if current_move == 1:
                    try:
                        to_remove = random.choice(bazar)
                    except IndexError:
                        if not this_player == 'ai':
                            print("Value error: nothing to give to the player; skipping it's turn")
                        next_player()
                    else:
                        bazar.remove(to_remove)
                        p1.append(to_remove)
            # detect the clicked domino
            lpos = pygame.mouse.get_pos()
            if lpos[0] > 26 and lpos[0] < 1252 and lpos[1] > 24 and lpos[1] < 134:
                mouse_is_over[0] = 1
                mouse_is_over[1] = int((lpos[0] - 26) / 59) + 1
    ##                if debug:
    ##                    print("Player", mouse_is_over[0], "domino", mouse_is_over[1])
            if lpos[0] > 26 and lpos[0] < 1252 and lpos[1] > 584 and lpos[1] < 704:
                mouse_is_over[0] = 2
                mouse_is_over[1] = int((lpos[0] - 26) / 59) + 1
    ##                if debug:
    ##                    print("Player", mouse_is_over[0], "domino", mouse_is_over[1])
            # check if there is anything at click position
            error = 0
            if mouse_is_over[0] == 1:
                try:
                    check_oob = p1[mouse_is_over[1] - 1]
                except IndexError:
                    if not this_player == 'ai':
                        print("Player error: you are trying to use nothing")
                    error = 1
            elif mouse_is_over[0] == 2:
                try:
                    check_oob = p2[mouse_is_over[1] - 1]
                except IndexError:
                    if not this_player == 'ai':
                        print("Player error: you are trying to use nothing")
                    error = 1
            if current_move != mouse_is_over[0]:
                if not this_player == 'ai':
                    print("Player error: it's not your turn")
                error = 1
            if error == 0 and mouse_is_over[0] == 1:
                to_use = p1[mouse_is_over[1] - 1]
                if game_state == "beginning":
                    dmn0 = to_use
                    p1.pop(mouse_is_over[1] - 1)
                    left_end = dominoes[dmn0 - 1][0]
                    right_end = dominoes[dmn0 - 1][1]
                    game_state = "game"
                    next_player()
                else:
                    if game_state == "game": # --- P1 ---
                        if not to_use in left_able and not to_use in right_able:
                            if not this_player == 'ai':
                                print("Player error: cannot place that domino")
                        else:
                            # if able to place on both sides
                            if to_use in left_able and to_use in right_able:
                                lor = handle_lor_dilemma(to_use) # I couldn't think of a better name than this
                                if lor == 'l':
                                    if dominoes[to_use - 1][0] == str(left_end):
                                        left_is_inv.append(True)
                                        left_side.append(to_use)
                                        left_end = dominoes[to_use - 1][1]
                                        p1.pop(mouse_is_over[1] - 1)
                                    else:
                                        left_is_inv.append(False)
                                        left_side.append(to_use)
                                        left_end = dominoes[to_use - 1][0]
                                        p1.pop(mouse_is_over[1] - 1)
                                if lor == 'r':
                                    if dominoes[to_use - 1][0] == str(right_end):
                                        right_is_inv.append(False)
                                        right_side.append(to_use)
                                        right_end = dominoes[to_use - 1][1]
                                        p1.pop(mouse_is_over[1] - 1)
                                    else:
                                        right_is_inv.append(True)
                                        right_side.append(to_use)
                                        right_end = dominoes[to_use - 1][0]
                                        p1.pop(mouse_is_over[1] - 1)
                            # if only able to place on the left but not on the right
                            if to_use in left_able and not to_use in right_able:
                                if dominoes[to_use - 1][0] == str(left_end):
                                    left_is_inv.append(True)
                                    left_side.append(to_use)
                                    left_end = dominoes[to_use - 1][1]
                                    p1.pop(mouse_is_over[1] - 1)
                                else:
                                    left_is_inv.append(False)
                                    left_side.append(to_use)
                                    left_end = dominoes[to_use - 1][0]
                                    p1.pop(mouse_is_over[1] - 1)
                            # if only able to place on the right but not on the left
                            if not to_use in left_able and to_use in right_able:
                                if dominoes[to_use - 1][0] == str(right_end):
                                    right_is_inv.append(False)
                                    right_side.append(to_use)
                                    right_end = dominoes[to_use - 1][1]
                                    p1.pop(mouse_is_over[1] - 1)
                                else:
                                    right_is_inv.append(True)
                                    right_side.append(to_use)
                                    right_end = dominoes[to_use - 1][0]
                                    p1.pop(mouse_is_over[1] - 1)
                            next_player()
            if error == 0 and mouse_is_over[0] == 2:
                to_use = p2[mouse_is_over[1] - 1]
                if game_state == "beginning":
                    dmn0 = to_use
                    p2.pop(mouse_is_over[1] - 1)
                    left_end = dominoes[dmn0 - 1][0]
                    right_end = dominoes[dmn0 - 1][1]
                    game_state = "game"
                    next_player()
                else:
                    if game_state == "game": # --- P2 ---
                        if not str(left_end) in dominoes[to_use - 1] and not str(right_end) in dominoes[to_use - 1]:
                            if not this_player == 'ai':
                                print("Player error: cannot place that domino")
                        else:
                            # if able to place on both sides
                            if str(left_end) in dominoes[to_use - 1] and str(right_end) in dominoes[to_use - 1]:
                                lor = handle_lor_dilemma(to_use)
                                if lor == 'l':
                                    if dominoes[to_use - 1][0] == str(left_end):
                                        left_is_inv.append(True)
                                        left_side.append(to_use)
                                        left_end = dominoes[to_use - 1][1]
                                        p2.pop(mouse_is_over[1] - 1)
                                    else:
                                        left_is_inv.append(False)
                                        left_side.append(to_use)
                                        left_end = dominoes[to_use - 1][0]
                                        p2.pop(mouse_is_over[1] - 1)
                                if lor == 'r':
                                    if dominoes[to_use - 1][0] == str(right_end):
                                        right_is_inv.append(False)
                                        right_side.append(to_use)
                                        right_end = dominoes[to_use - 1][1]
                                        p2.pop(mouse_is_over[1] - 1)
                                    else:
                                        right_is_inv.append(True)
                                        right_side.append(to_use)
                                        right_end = dominoes[to_use - 1][0]
                                        p2.pop(mouse_is_over[1] - 1)
                                if lor != 'l' and lor != 'r':
                                    if not this_player == 'ai':
                                        print("Player error: wrong input, must be 'l' or 'r' (case-sensitive, no quote signs)")
                            # if only able to place on the left but not on the right
                            if str(left_end) in dominoes[to_use - 1] and not str(right_end) in dominoes[to_use - 1]:
                                if dominoes[to_use - 1][0] == str(left_end):
                                    left_is_inv.append(True)
                                    left_side.append(to_use)
                                    left_end = dominoes[to_use - 1][1]
                                    p2.pop(mouse_is_over[1] - 1)
                                else:
                                    left_is_inv.append(False)
                                    left_side.append(to_use)
                                    left_end = dominoes[to_use - 1][0]
                                    p2.pop(mouse_is_over[1] - 1)
                            # if only able to place on the right but not on the left
                            if not str(left_end) in dominoes[to_use - 1] and str(right_end) in dominoes[to_use - 1]:
                                if dominoes[to_use - 1][0] == str(right_end):
                                    right_is_inv.append(False)
                                    right_side.append(to_use)
                                    right_end = dominoes[to_use - 1][1]
                                    p2.pop(mouse_is_over[1] - 1)
                                else:
                                    right_is_inv.append(True)
                                    right_side.append(to_use)
                                    right_end = dominoes[to_use - 1][0]
                                    p2.pop(mouse_is_over[1] - 1)
                            next_player()
##            if debug:
##                print("P1:", p1)
##                print("P2:", p2)
##                print("Bazar:", bazar)
##                print("Left side:", left_side, "with length of", len(left_side), "ending with", left_end)
##                print("Right side:", right_side, "with length of", len(right_side), "ending with", right_end)
##                print("Center domino:", dmn0)
##                print("\n")
    left_end = int(left_end)
    right_end = int(right_end)
    # detect board movement
    pressed = pygame.key.get_pressed() 
    if pressed[K_LEFT]:
        ren_start_x -= 5
        is_rendered = False
    if pressed[K_RIGHT]:
        ren_start_x += 5
        is_rendered = False
    if pressed[K_UP]:
        ren_start_y -= 5
        is_rendered = False
    if pressed[K_DOWN]:
        ren_start_y += 5
        is_rendered = False
    # give to P1 button
    if btn_give_1.isOver():
        btn_give_1.color = current_theme[8]
    if not btn_give_1.isOver() and not bool(pygame.event.get(pygame.MOUSEBUTTONDOWN)):
        btn_give_1.color = current_theme[10]
    btn_give_1.draw(window, current_theme[11], current_theme[11], 35)
    # give to P2 button
    if btn_give_2.isOver():
        btn_give_2.color = current_theme[8]
    if not btn_give_2.isOver() and not bool(pygame.event.get(pygame.MOUSEBUTTONDOWN)):
        btn_give_2.color = current_theme[10]
    btn_give_2.draw(window, current_theme[11], current_theme[11], 35)
    ren_left_side = left_side
    ren_right_side = right_side
    ren_left_is_inv = left_is_inv
    ren_right_is_inv = right_is_inv

def game_init():
    global p1
    global p2
    global bazar
    global current_move
    global left_side
    global right_side
    global left_end
    global right_end
    global dmn0
    global left_is_inv
    global right_is_inv
    global player_size
    p1 = []
    p2 = []
    bazar = []
    while len(p1) < player_size:
        temp_to_add = random.randint(1, 28)
        if not temp_to_add in p1:
            p1.append(temp_to_add)
    while len(p2) < player_size:
        temp_to_add = random.randint(1, 28)
        if not temp_to_add in p1 and not temp_to_add in p2:
            p2.append(temp_to_add)
    for i in range(28):
        if not i+1 in p1 and not i+1 in p2 and not i+1 in bazar:
            bazar.append(i+1)
    current_move = random.randint(1, 2)
    left_side = []
    right_side = []
    left_end = -1
    right_end = -1
    dmn0 = -1
    left_is_inv = []
    right_is_inv = []

def btn_ctrl_main():
    global current_ui
    global backup_ui
    global is_rendered
    # play button
    if btn_play.isOver():
        btn_play.color = current_theme[8]
        if bool(pygame.event.peek(pygame.MOUSEBUTTONDOWN)):
            btn_play.color = current_theme[9]
            current_ui = "menu_gamemode_select"
            is_rendered = False
            pygame.event.clear()
    if not btn_play.isOver() and not bool(pygame.event.peek(pygame.MOUSEBUTTONDOWN)):
        btn_play.color = current_theme[10]
    btn_play.draw(window, current_theme[11], current_theme[11])
    # settings button
    if btn_settings.isOver():
        btn_settings.color = current_theme[8]
        if bool(pygame.event.peek(pygame.MOUSEBUTTONDOWN)):
            btn_settings.color = current_theme[9]
            backup_ui = "menu_main"
            current_ui = "settings"
            is_rendered = False
            pygame.event.clear()
    if not btn_settings.isOver() and not bool(pygame.event.peek(pygame.MOUSEBUTTONDOWN)):
        btn_settings.color = current_theme[10]
    btn_settings.draw(window, current_theme[11], current_theme[11])

def btn_ctrl_gm_sel():
    global current_ui
    global is_rendered
    global gamemode
    global btn_gm_local
    global btn_gm_back
    global btn_gm_pva
    global btn_gm_ava
    # gamemode = local button
    if btn_gm_local.isOver():
        btn_gm_local.color = current_theme[8]
        if bool(pygame.event.peek(pygame.MOUSEBUTTONDOWN)):
            btn_gm_local.color = current_theme[9]
            current_ui = "local_setup"
            gamemode = "local"
            is_rendered = False
            pygame.event.clear()
    if not btn_gm_local.isOver() and not bool(pygame.event.peek(pygame.MOUSEBUTTONDOWN)):
        btn_gm_local.color = current_theme[10]
    btn_gm_local.draw(window, current_theme[11], current_theme[11])
    # back button
    if btn_gm_back.isOver():
        btn_gm_back.color = current_theme[8]
        if bool(pygame.event.peek(pygame.MOUSEBUTTONDOWN)):
            btn_gm_back.color = current_theme[9]
            current_ui = "menu_main"
            is_rendered = False
            pygame.event.clear()
    if not btn_gm_back.isOver() and not bool(pygame.event.peek(pygame.MOUSEBUTTONDOWN)):
        btn_gm_back.color = current_theme[10]
    btn_gm_back.draw(window, current_theme[11], current_theme[11])
    # gamemode = pva button
    if btn_gm_pva.isOver():
        btn_gm_pva.color = current_theme[8]
        if bool(pygame.event.peek(pygame.MOUSEBUTTONDOWN)):
            btn_gm_pva.color = current_theme[9]
            current_ui = "local_setup"
            gamemode = "pva"
            is_rendered = False
            pygame.event.clear()
    if not btn_gm_pva.isOver() and not bool(pygame.event.peek(pygame.MOUSEBUTTONDOWN)):
        btn_gm_pva.color = current_theme[10]
    btn_gm_pva.draw(window, current_theme[11], current_theme[11])
    # gamemode = bot_battle button
    if btn_gm_ava.isOver():
        btn_gm_ava.color = current_theme[8]
        if bool(pygame.event.peek(pygame.MOUSEBUTTONDOWN)):
            btn_gm_ava.color = current_theme[9]
            current_ui = "local_setup"
            gamemode = "bot_battle"
            is_rendered = False
            pygame.event.clear()
    if not btn_gm_ava.isOver() and not bool(pygame.event.peek(pygame.MOUSEBUTTONDOWN)):
        btn_gm_ava.color = current_theme[10]
    btn_gm_ava.draw(window, current_theme[11], current_theme[11])

def count_score():
    global p1
    global p2
    global score_val
    global p1_to_add
    global p2_to_add
    global p1_score
    global p2_score
    global min_write
    p1_to_add = 0
    p2_to_add = 0
    for i in p1:
        p1_to_add += score_val[i - 1]
    for i in p2:
        p2_to_add += score_val[i - 1]
    if p1_score + p1_to_add < min_write:
        p1_to_add = 0
    if p2_score + p2_to_add < min_write:
        p2_to_add = 0

def ren_score_update():
    # init
    global p1_wins
    global p2_wins
    global p1_score
    global p2_score
    global p1_to_add
    global p2_to_add
    global font_score
    global current_ui
    global restart_type
    global windowed_score
    global beginning_double
    if windowed_score:
        # render base
        pygame.draw.rect(window, current_theme[9], (50, 200, 540, 320))
        pygame.draw.rect(window, current_theme[9], (690, 200, 540, 320))
        pygame.draw.rect(window, current_theme[0], (50, 200, 540, 320), 4)
        pygame.draw.rect(window, current_theme[0], (690, 200, 540, 320), 4)
        # render text
        score1 = font_score.render(str(p1_score), 4, current_theme[11])
        window.blit(score1, (320 - (score1.get_width()/2), 360 - (score1.get_height()/2)))
        score2 = font_score.render(str(p2_score), 4, current_theme[11])
        window.blit(score2, (960 - (score2.get_width()/2), 360 - (score1.get_height()/2)))
    # increase score - init
    if p1_to_add > p2_to_add:
        incr_count = p1_to_add
    else:
        incr_count = p2_to_add
    delay = 50
    if incr_count < 10 and incr_count > 0:
        delay = 500 / incr_count
    elif incr_count == 0:
        delay = 0            
    # increase score
    for i in range(incr_count):
        # ask for input to prevent "not responding" message
        if bool(pygame.event.get(pygame.K_SPACE)):
            print(":)")
        # wait for a while
        pygame.time.delay(int(delay))
        # add 1 to each player
        if p1_to_add > 0:
            p1_to_add -= 1
            p1_score += 1
        if p2_to_add > 0:
            p2_to_add -= 1
            p2_score += 1
        if windowed_score:
            # render base
            pygame.draw.rect(window, current_theme[9], (50, 200, 540, 320))
            pygame.draw.rect(window, current_theme[9], (690, 200, 540, 320))
            pygame.draw.rect(window, current_theme[0], (50, 200, 540, 320), 4)
            pygame.draw.rect(window, current_theme[0], (690, 200, 540, 320), 4)
            # render text
            score1 = font_score.render(str(p1_score), 4, current_theme[11])
            window.blit(score1, (320 - (score1.get_width()/2), 360 - (score1.get_height()/2)))
            score2 = font_score.render(str(p2_score), 4, current_theme[11])
            window.blit(score2, (960 - (score2.get_width()/2), 360 - (score1.get_height()/2)))
        else:
            game_ren()
        # finish frame
        pygame.display.update()
    if (p1_score > scorelim - 1 or p2_score > scorelim - 1) and windowed_score:
        if p1_score > p2_score:
            p2_wins += 1
            for i in range(10):
                # ask for input to prevent "not responding" message
                if bool(pygame.event.get(pygame.K_SPACE)):
                    print(":)")
                # render base
                pygame.draw.rect(window, current_theme[15], (50, 200, 540, 320))
                pygame.draw.rect(window, current_theme[14], (690, 200, 540, 320))
                pygame.draw.rect(window, current_theme[0], (50, 200, 540, 320), 4)
                pygame.draw.rect(window, current_theme[0], (690, 200, 540, 320), 4)
                # render text
                score1 = font_score.render(str(p1_score), 4, current_theme[11])
                window.blit(score1, (320 - (score1.get_width()/2), 360 - (score1.get_height()/2)))
                score2 = font_score.render(str(p2_score), 4, current_theme[11])
                window.blit(score2, (960 - (score2.get_width()/2), 360 - (score1.get_height()/2)))
                # finish frame
                pygame.display.update()
                # wait
                pygame.time.delay(500)
                # render base
                pygame.draw.rect(window, current_theme[9], (50, 200, 540, 320))
                pygame.draw.rect(window, current_theme[9], (690, 200, 540, 320))
                pygame.draw.rect(window, current_theme[0], (50, 200, 540, 320), 4)
                pygame.draw.rect(window, current_theme[0], (690, 200, 540, 320), 4)
                # render text
                score1 = font_score.render(str(p1_score), 4, current_theme[11])
                window.blit(score1, (320 - (score1.get_width()/2), 360 - (score1.get_height()/2)))
                score2 = font_score.render(str(p2_score), 4, current_theme[11])
                window.blit(score2, (960 - (score2.get_width()/2), 360 - (score1.get_height()/2)))
                # finish frame
                pygame.display.update()
                # wait
                pygame.time.delay(500)
        else:
            p1_wins += 1
            for i in range(10):
                # ask for input to prevent "not responding" message
                if bool(pygame.event.get(pygame.K_SPACE)):
                    print(":)")
                # render base
                pygame.draw.rect(window, current_theme[14], (50, 200, 540, 320))
                pygame.draw.rect(window, current_theme[15], (690, 200, 540, 320))
                pygame.draw.rect(window, current_theme[0], (50, 200, 540, 320), 4)
                pygame.draw.rect(window, current_theme[0], (690, 200, 540, 320), 4)
                # render text
                score1 = font_score.render(str(p1_score), 4, current_theme[11])
                window.blit(score1, (320 - (score1.get_width()/2), 360 - (score1.get_height()/2)))
                score2 = font_score.render(str(p2_score), 4, current_theme[11])
                window.blit(score2, (960 - (score2.get_width()/2), 360 - (score1.get_height()/2)))
                # finish frame
                pygame.display.update()
                # wait
                pygame.time.delay(500)
                # render base
                pygame.draw.rect(window, current_theme[9], (50, 200, 540, 320))
                pygame.draw.rect(window, current_theme[9], (690, 200, 540, 320))
                pygame.draw.rect(window, current_theme[0], (50, 200, 540, 320), 4)
                pygame.draw.rect(window, current_theme[0], (690, 200, 540, 320), 4)
                # render text
                score1 = font_score.render(str(p1_score), 4, current_theme[11])
                window.blit(score1, (320 - (score1.get_width()/2), 360 - (score1.get_height()/2)))
                score2 = font_score.render(str(p2_score), 4, current_theme[11])
                window.blit(score2, (960 - (score2.get_width()/2), 360 - (score1.get_height()/2)))
                # finish frame
                pygame.display.update()
                # wait
                pygame.time.delay(500)
        p1_score = 0
        p2_score = 0
    elif p1_score > scorelim - 1 or p2_score > scorelim - 1:
        if p1_score > p2_score:
            p2_wins += 1
        else:
            p1_wins += 1
        p1_score = 0
        p2_score = 0
    current_ui = "out_of_cycle"

def ren_end_data():
    global font_ver
    global p1_to_add
    global p2_to_add
    global current_ui
    global font_gm_sel
    global current_move
    global btn_next_battle
    current_move = 0
    count_score()
    # draw a fancy window
    pygame.draw.rect(window, current_theme[10], (440, 250, 400, 220))
    pygame.draw.rect(window, current_theme[0], (440, 250, 400, 220), 4)
    pygame.draw.rect(window, current_theme[8], (440, 250, 400, 40))
    pygame.draw.rect(window, current_theme[0], (440, 250, 400, 40), 4)
    text_title = font_ver.render("Конец игры", 4, current_theme[11])
    text_p1_name = font_gm_sel.render("Игрок 1", 4, current_theme[11])
    text_p2_name = font_gm_sel.render("Игрок 2", 4, current_theme[11])
    text_p1_score = font_gm_sel.render(str(p1_to_add), 4, current_theme[11])
    text_p2_score = font_gm_sel.render(str(p2_to_add), 4, current_theme[11])
    window.blit(text_p1_name, (450, 290))
    window.blit(text_p2_name, (450, 340))
    window.blit(text_p1_score, (830 - text_p1_score.get_width(), 290))
    window.blit(text_p2_score, (830 - text_p2_score.get_width(), 340))
    window.blit(text_title, (640 - (text_title.get_width() / 2), 270 - (text_title.get_height() / 2)))
    # button
    while current_ui == "out_of_cycle":
        if btn_next_battle.isOver():
            btn_next_battle.color = current_theme[8]
            if bool(pygame.event.get(pygame.MOUSEBUTTONDOWN)):
                btn_next_battle.color = current_theme[9]
                current_ui = "local_setup"
                is_rendered = False
        if not btn_next_battle.isOver() and not bool(pygame.event.get(pygame.MOUSEBUTTONDOWN)):
            btn_next_battle.color = current_theme[10]
        btn_next_battle.draw(window, current_theme[11], current_theme[11])
        pygame.display.update()

def handle_lor_dilemma(cause): # is called whenever the player is able to place a domino on both left and right sides and shows a nice gui
    global left_end
    global right_end
    global left_side
    global right_side
    global font_gm_sel
    global left_is_inv
    global this_player
    global right_is_inv
    global ren_left_side
    global ren_right_side
    global ren_left_is_inv
    global ren_right_is_inv
    if this_player == 'ai':
        if random.randint(0, 1):
            return 'r'
        else:
            return 'l'
    is_solved = False
    while not is_solved:
        pos = pygame.mouse.get_pos()
        if pos[1] < 360:
            ren_left_side = left_side.copy()
            ren_left_side.append(cause)
            ren_left_is_inv = left_is_inv.copy()
            if dominoes[int(cause) - 1][0] == str(left_end):
                ren_left_is_inv.append(True)
            else:
                ren_left_is_inv.append(False)
            game_ren()
            hint_use = font_gm_sel.render("Нажмите, чтобы поставить", 4, current_theme[11], current_theme[8])
            pygame.draw.rect(window, current_theme[0], (636 - (hint_use.get_width() / 2), 76 - (hint_use.get_height() / 2), hint_use.get_width() + 8, hint_use.get_height() + 8))
            window.blit(hint_use, (640 - (hint_use.get_width() / 2), 80 - (hint_use.get_height() / 2)))
            pygame.display.update()
            if bool(pygame.event.get(pygame.MOUSEBUTTONDOWN)):
                is_solved = True
                return 'l'
            ren_left_side = left_side.copy()
        else:
            ren_right_side = right_side.copy()
            ren_right_side.append(cause)
            ren_right_is_inv = right_is_inv.copy()
            if dominoes[int(cause) - 1][0] == str(left_end):
                ren_right_is_inv.append(False)
            else:
                ren_right_is_inv.append(True)
            game_ren()
            hint_use = font_gm_sel.render("Нажмите, чтобы поставить", 4, current_theme[11], current_theme[8])
            pygame.draw.rect(window, current_theme[0], (636 - (hint_use.get_width() / 2), 76 - (hint_use.get_height() / 2), hint_use.get_width() + 8, hint_use.get_height() + 8))
            window.blit(hint_use, (640 - (hint_use.get_width() / 2), 80 - (hint_use.get_height() / 2)))
            pygame.display.update()
            if bool(pygame.event.get(pygame.MOUSEBUTTONDOWN)):
                is_solved = True
                return 'r'
            ren_right_side = right_side.copy()

def next_player():
    global current_move
    global backup_move
    global font_d50
    global btn_next_player
    global font_gm_sel
    global fastmode
    global gamemode
    backup_move = current_move
    if not fastmode and gamemode == "local":
        current_move = 3
        game_ren()
        # draw a fancy window
        pygame.draw.rect(window, current_theme[10], (350, 150, 580, 420))
        pygame.draw.rect(window, current_theme[0], (350, 150, 580, 420), 4)
        pygame.draw.rect(window, current_theme[8], (350, 150, 580, 40))
        pygame.draw.rect(window, current_theme[0], (350, 150, 580, 40), 4)
        # draw exclamation sign
        pygame.draw.circle(window, current_theme[0], (640, 270), 70, 4)
        pygame.draw.ellipse(window, current_theme[0], [627, 215, 26, 20])
        pygame.draw.polygon(window, current_theme[0], [[627, 225], [638, 297], [642, 297], [653, 225]])
        pygame.draw.circle(window, current_theme[0], [640, 315], 9)
        # draw all the texts
        window_title = font_d50.render("Ожидание след. игрока", 4, current_theme[11])
        window.blit(window_title, (355, 170 - (window_title.get_height() / 2)))
        if backup_move == 1:
            line1 = font_gm_sel.render("Игрок 2, ваш ход!", 4, current_theme[11])
            sl1 = font_gm_sel.size("Игрок 2, ваш ход!")
        else:
            line1 = font_gm_sel.render("Игрок 1, ваш ход!", 4, current_theme[11])
            sl1 = font_gm_sel.size("Игрок 1, ваш ход!")
        window.blit(line1, (640 - sl1[0]/2, 360 - sl1[1]/2))
        line2 = font_gm_sel.render("Нажмите клавишу Пробел или кноп-", 4, current_theme[11])
        sl2 = font_gm_sel.size("Нажмите клавишу Пробел или кноп-")
        line3 = font_gm_sel.render("ку ОК и сделайте ход.", 4, current_theme[11])
        sl3 = font_gm_sel.size("ку ОК и сделайте ход.")
        window.blit(line2, (640 - sl2[0]/2, 410 - sl2[1]/2))
        window.blit(line3, (640 - sl3[0]/2, 460 - sl3[1]/2))
        done = False
        while not done:
            pos = pygame.mouse.get_pos()
            if btn_next_player.isOver():
                btn_next_player.color = current_theme[8]
                if bool(pygame.event.get(pygame.MOUSEBUTTONDOWN)):
                    btn_next_player.color = current_theme[9]
                    if backup_move == 1:
                        current_move = 2
                    else:
                        current_move = 1
                    is_rendered = False
                    done = True
            if not btn_next_player.isOver() and not bool(pygame.event.get(pygame.MOUSEBUTTONDOWN)):
                btn_next_player.color = current_theme[10]
            kpress = pygame.key.get_pressed()
            if kpress[K_SPACE]:
                if backup_move == 1:
                    current_move = 2
                else:
                    current_move = 1
                is_rendered = False
                done = True
            btn_next_player.draw(window, current_theme[11], current_theme[11])
            pygame.display.update()
    else:
        if backup_move == 1:
            current_move = 2
        else:
            current_move = 1

def settings(source):
    ## init
    global font_gm_sel
    global windowed_score
    global dark_theme
    global fastmode
    global s_windowed_score
    global s_dark_theme
    global s_fastmode
    global current_theme
    global theme_dark
    global theme_default
    global current_ui
    global is_rendered
    global is_theme_updated
    global backup_ui
    global config
    global config_data
    global is_config_open
    is_clicc = bool(pygame.event.get(pygame.MOUSEBUTTONDOWN, False))
    window.fill(current_theme[8])
    ## draw the sliders
    # show scores in the two windows
    s_windowed_score.draw(windowed_score)
    if s_windowed_score.is_over() and is_clicc:
        windowed_score = not windowed_score
        if windowed_score:
            config_data[0] = '1\n'
        else:
            config_data[0] = '0\n'
    # do not confirm move changes (for testing purposes)
    s_fastmode.draw(fastmode)
    if s_fastmode.is_over() and is_clicc:
        fastmode = not fastmode
        if fastmode:
            config_data[1] = '1\n'
        else:
            config_data[1] = '0\n'
    # exit button
    font_gm_sel.set_underline(True)
    go_back = font_gm_sel.render("< Назад", 4, current_theme[11])
    window.blit(go_back, (25, 11))
    font_gm_sel.set_underline(False)
    mp = pygame.mouse.get_pos()
    if mp[0] > 25 and mp[0] < 25 + go_back.get_width() and mp[1] > 15 and mp[1] < 7 + go_back.get_height() and is_clicc:
        current_ui = backup_ui
        is_rendered = False
    ## the option descriptions
    opt1 = font_gm_sel.render("Отображать изменение счёта в отдельных окнах", 4, current_theme[11])
    window.blit(opt1, (40, 76))
    opt3 = font_gm_sel.render("Быстрый режим", 4, current_theme[11])
    window.blit(opt3, (40, 146))
    if source == "pause":
        titl = font_gm_sel.render("Игра на паузе", 4, current_theme[11]) # typo intentional
        window.blit(titl, (640 - titl.get_width() / 2, 5))

def ai(whoami = 2):
    global current_move
    global is_p1_able
    global is_p2_able
    global p1
    global p2
    pygame.time.delay(50)
    if whoami == 1:
        if not is_p1_able:
            pygame.mouse.set_pos([640, 6])
            pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
            local_game_ctrl(True)
        else:
            for i in range(len(p1)):
                pygame.time.delay(50)
                if current_move == whoami:
                    pygame.mouse.set_pos([59*(i+1), 60])
                    pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
                    local_game_ctrl(True)
                else:
                    return
    else:
        if not is_p2_able:
            pygame.mouse.set_pos([640, 705])
            pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
            local_game_ctrl(True)
        else:
            for i in range(len(p2)):
                pygame.time.delay(50)
                if current_move == whoami:
                    pygame.mouse.set_pos([59*(i+1), 600])
                    pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
                    local_game_ctrl(True)
                else:
                    return

def game_setup():
    # init
    global scorelim
    global min_write
    global player_size
    # draw the window
    window.fill(current_theme[8])

delay = 6
while True: # game tick, running at 60 TPS
    gametick.tick(max_fps)
    if bool(pygame.event.peek(pygame.QUIT)):
        with open("domino_config.dc2", 'w') as config:
            config.writelines(config_data)
        pygame.quit()
        break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE] and not current_ui == "pause" and not current_ui == "settings":
        backup_ui = current_ui
        current_ui = "pause"
        pygame.event.clear()
    if ((current_move == 2 and not gamemode == "local") or gamemode == "bot_battle"):
        this_player = "ai"
    else:
        this_player = "human"
    #window.fill(color_menu_light)
    if delay == 0:
        delay = 3
        for i in range(len(current_splash)):
            if current_splash[i] == '§':
                splash = list(splash)
                splash[i] = random_characters[random.randint(0, len(random_characters) - 1)]
                temp = ''
                for j in splash:
                    temp += j
                splash = temp
    else:
        delay = delay - 1
    if is_theme_updated:
        btn_play = button(current_theme[10], 500, 400, 280, 50, "Играть")
        btn_settings = button(current_theme[10], 500, 500, 280, 50, "Настройки")
        btn_how_to_play = button(current_theme[9], 500, 600, 280, 50, "Как играть")
        btn_gm_local = button(current_theme[10], 250, 400, 300, 50, "Локальная игра")
        btn_gm_internet = button(current_theme[9], 250, 500, 300, 50, "В разработке...")
        btn_gm_pva = button(current_theme[9], 730, 400, 300, 50, "Одиночная игра")
        btn_gm_ava = button(current_theme[9], 730, 500, 300, 50, "Битва ботов")
        btn_gm_back = button(current_theme[10], 490, 600, 300, 50, "Назад")
        btn_give_1 = button(current_theme[10], 600, 2, 80, 18, "Нету!")
        btn_give_2 = button(current_theme[10], 600, 699, 80, 19, "Нету!")
        btn_next_battle = button(current_theme[10], 540, 420, 200, 40, "Дальше")
        btn_next_player = button(current_theme[10], 540, 500, 200, 50, "OK")
        ren_domino = domino(window, current_theme)
    if current_ui == "menu_main":
        render_main_menu()
        btn_ctrl_main()
    elif current_ui == "settings":
        settings("menu")
    elif current_ui == "pause":
        settings("pause")
    elif current_ui == "menu_gamemode_select":
        render_menu_gm_sel()
        btn_ctrl_gm_sel()
    elif current_ui == "local_setup":
        game_setup()
        game_init()
        current_ui = "local_game"
        game_state = "beginning"
    elif current_ui == "local_game":
        game_ren()
        local_game_ctrl()
    elif current_ui == "end":
        count_score()
        game_ren()
        ren_score_update()
        ren_end_data()
    if bool(pygame.event.get(framerate_output)):
        current_fps = "FPS: " + str(round(gametick.get_fps()))
    fpsr = font_fps.render(current_fps, 4, current_theme[11])
    window.blit(fpsr, (1278 - fpsr.get_width(), 722 - fpsr.get_height()))
    pygame.display.update()
print("Thanks for playing!")
