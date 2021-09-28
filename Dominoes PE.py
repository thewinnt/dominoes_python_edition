# init
import time

t = time.time()
init_t = t

import pygame

pygame_import = time.time() - t
t = time.time()

import random
import os
from datetime import date
import tkinter as tk
from tkinter import filedialog
import ast
import json
import math
import assets.ui_tools as ui_tools
import assets.domino as domino
import traceback
pygame.mixer.pre_init()
pygame.init()

rest_import = time.time() - t
t = time.time()

max_fps = 60
gametick = pygame.time.Clock()

# config setup
try:
    with open('domino_config.json', 'r', -1, 'utf-8') as config:
        try:
            config_data = json.load(config)
        except:
            print("File error: error while decoding config file - it may have been corrupted")
            config_data = {"windowed_score": 1, "fastmode": 0, "theme_id": 1, "custom_themes": [], "blink_time": 10, "lang": "en_us"}
except OSError:
    print("File error: config file is missing")
    config_data = {"windowed_score": 1, "fastmode": 0, "theme_id": 1, "custom_themes": [], "blink_time": 10, "lang": "en_us"}

# language setup
try:
    lang_type = config_data['lang']
except:
    print("File error: language not specified, using English")
    lang_type = 'en_us'
    config_data["windowed_score"] = 1
try:
    with open(f'assets/lang/{lang_type}.json', 'r', -1, 'utf-8') as lang_file:
        lang = json.load(lang_file)
except:
    try:
        print(f'File error: language file "assets/lang/{lang_type}.json" not found, gotta use English')
        with open('assets/lang/en_us.json', 'r', -1, 'utf-8') as lang_file:
            lang = json.load(lang_file)
        lang_type = 'en_us'
        config_data['lang'] = 'en_us'
    except:
        print('File error: ENGLISH LANGUAGE FILE (assets/lang/en_us.json) NOT FOUND')
        input('Cannot start the program, press Enter to exit...')
        exit(-1)

lang_ids = os.listdir('assets/lang')
langs = []
lang_names = []
for i in range(len(lang_ids)):
    lang_ids[i] = lang_ids[i][:-5]
    with open(f'assets/lang/{lang_ids[i]}.json', 'r', -1, 'utf-8') as file:
        langs.append(json.load(file))
        lang_names.append(langs[i]['lang_name'])

lang_values = ['lang_name', 'game_name', 'theme_light_name', 'theme_light_desc', 'theme_dark_desc', 'theme_dark_name', 
               'theme_upd_0', 'theme_upd_pre1', 'err_future_theme', 'err_no_setting', 'invalid_theme', 
               'bot', 'player', 'bazar_empty', 'btn_continue', 'btn_load_game_short', 'btn_load_game_full', 
               'btn_new_game', 'btn_exit', 'local_game', 'in_development', 'singleplayer', 'bot_battle', 'btn_back',
               'btn_next_round', 'how_to_play', 'btn_next_player', 'btn_start_game', 'lnk_theme_settings',
               'lnk_exit_settings', 'btn_go_menu', 'btn_save_quit', 'filetype_json', 'filetype_all', 'thanks',
               'select_gamemode', 'playerdata_single', 'playerdata_name', 'playerdata_score', 'playerdata_vict',
               'player_chose_nothing', 'wrong_turn', 'cant_place_domino', 'game_over', 'click_to_place',
               'wait_next_player', 'your_turn', 'press_space_ok_1', 'press_space_ok_2', 'opt_big_windows',
               'opt_fastmode', 'opt_error_sound', 'opt_place_sound', 'opt_vict_show_time', 'game_paused', 'settings',
               'theme_selection', 'choose_theme', 'selected_theme', 'more_themes', 'delete_theme', 'test_button',
               'import', 'filetype_dth', 'filetype_txt', 'err_scorelim_not_positive', 'err_min_score_too_high',
               'err_players_should_have_dmn', 'err_not_enough_dmns', 'err_too_much_players', 'err_too_little_players',
               'setup', 'scorelim', 'min_score', 'player_dominoes', 'player_count', 'start_with_double', 'tutorial',
               'config_inaccessible', 'language', 'btn_go_menu', 'board_default', 'board_spiral_cw', 'board_spiral_ccw',
               'lnk_board_type', 'translatable_splash', 'import_board_msg', 'name_board', 'theme_upd_1']  # all the translation keys
for i in range(len(langs)):
    for key in lang_values:
        try:
            langs[i][key]
        except KeyError:
            langs[i][key] = key

lang = langs[lang_ids.index(lang_type)]

conf_setup = time.time() - t
t = time.time()

window = pygame.display.set_mode((1280, 720))
icon = pygame.image.load("assets/window.png").convert_alpha()
pygame.display.set_icon(icon)

def update_win_caption():
    pygame.display.set_caption(f"{lang['game_name']}: Python Edition v. Beta 1.8 pre-release 1")
update_win_caption()
game_version = "v. Beta 1.8-pre1"

useless = tk.Tk()
useless.withdraw()

# variables
current_ui = "menu_main" # defines what kind of image to draw (game/ui/etc.)
debug = False # toggles debug features
splashes = ["Python recreation!",
            "Less lag!",
            "My brain is gonna explode...",
            "Uses Pygame!",
            "HD!",
            "What a nice window!",
            "Indie!",
            "Made in Russia!",
            "Also try Minecraft!",
            "Endless possibilities!",
            "bruh",
            "Made during coronavirus pandemic!",
            "Beta!",
            "class Domino:",
            "100% free!",
            "No one paid me for this!",
            "Over 2000 lines!",
            # "domino:splashes/namespaced_splash",
            "Quite stable!",
            "Made by a 13-year-old!", # i'm leaving this in since i wrote around half of the current code at 13
            "Thanks, Google!",
            "Thanks, StackOverflow!",
            "youtu.be/dQw4w9WgXcQ",
            "Has a lot of comments!",
            "I'm not a pro programmer btw",
            "&&&&&&!",
            "Getting advanced!",
            "We need more splashes!",
            "Can I put you in a bucket?",
            "thinn fonts",
            "As simple as possible!",
            "I'm lazy",
            "Contains some bugs!",
            "Tested!",
            "Offline!",
            "Instructions unclear, lost a friend",
            "Friends not included",
            "Doesn't require a friend!",
            "Split up!",
            "Almost abandoned!",
            "A bit messy!",
            "Still looks like spaghetti",
            "This code is awful!",
            "A giant bodge",
            "Can be played at parties!",
            "Look, it's pulsating!",
            "Supports gaming mouses!",
            "Overly complicated",
            "Optimized!",
            "Made by a 14-year-old!",
            "Look mom, no one helped me!",
            "69420",
            0,
            "Customizable!",
            "Multilingual!",
            "lang['translatable_splash']",
            "Totally yours!",
            "Whatever you prefer!",
            "Not exactly super advanced",
            "A bit less laggy"] # the list of existing splashes
random_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/*-+()[]{}абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" # the list of charasters that are used in splashes with randomized characters

font_title = pygame.font.Font('assets/denhome.otf',300)
font_splash = pygame.font.Font('assets/comic.ttf',  40)
font_pe = pygame.font.Font('assets/bahnschrift.ttf',30)
font_gm_sel = pygame.font.Font('assets/denhome.otf',70)
font_pd = pygame.font.Font('assets/bahnschrift.ttf',20)
font_ver = pygame.font.Font('assets/denhome.otf',   40)
font_score = pygame.font.Font('assets/denhome.otf',250)
font_d50 = pygame.font.Font('assets/denhome.otf',   50)
font_fps = pygame.font.Font('assets/denhome.otf',   30)
font_setup = pygame.font.Font('assets/denhome.otf', 90)
font_header = pygame.font.Font('assets/denhome.otf',50)
font_d60 = pygame.font.Font('assets/denhome.otf',   60)
font_scroll = pygame.font.Font('assets/arial.ttf',  25)
font_error = pygame.font.Font('assets/dhmbold.ttf', 35)
font_field = pygame.font.Font('assets/dhmbold.ttf', 70)
sound_place = pygame.mixer.Sound('assets/place.wav')
sound_error = pygame.mixer.Sound('assets/error.wav')
current_splash = random.choice(splashes)
today = date.today()
if today.strftime("%d%m") == "1408":
    current_splash = "Happy birthday, &&&&!"
elif today.strftime("%d%m") == "1907":
    current_splash = "Happy birthday, WinNT!"
splash = current_splash
if current_splash == 0:
    splash = lang['translatable_splash']
visible_scores = [0] * 2 # actually needed here
def update_translatables(): # updates all the strings that are set once
    global splash
    if current_splash == 0: # you need to declare globals only when you want to write to them
        splash = lang['translatable_splash']

# generate domino positions on the board
dmn_x = [[], []]
dmn_y = [[], []]
dmn_rot = [[], []]
rot = 2
x, y = 0, 0

def get_rot(rot) -> tuple:
    '''Converts a rotation to a tuple, answering if the domino is vertical and is it inverted'''
    return (bool(rot % 2), bool(rot // 2))

def finish_domino(side):
    '''Actually adds the domino to the line'''
    dmn_x[side].append(x)
    dmn_y[side].append(y)
    dmn_rot[side].append(rot)

def straight(count, side, start=False): 
    '''Adds some dominoes in front of the line'''
    global dmn_x
    global dmn_y
    global dmn_rot
    global rot
    global x
    global y
    rot_type = get_rot(rot)
    if start:
        x, y = 0, 0
        if not rot_type[0]:
            x -= 30 * (-1 if rot == 2 else (1 if rot == 0 else 0))
    for i in range(count):
        if rot_type[0]:
            y += 119 * (-1 if rot == 3 else 1)
        else:
            x += 119 * (-1 if rot == 2 else 1)  # this eliminates the long if-elif construction, shortening the function
        finish_domino(side)

def turn(right: bool, side):
    '''Makes a turn in the domino line'''
    global dmn_x
    global dmn_y
    global dmn_rot
    global rot
    global x
    global y
    if right:
        if rot == 0: # i couldn't do this another way
            x += 89
            y += 30
        elif rot == 1:
            x -= 30
            y += 89
        elif rot == 2:
            x -= 89
            y -= 30
        elif rot == 3:
            x += 30
            y -= 89
        rot = (rot + 1) % 4
    else:
        if rot == 0:
            x += 89
            y -= 30
        elif rot == 1:
            x += 30
            y += 89
        elif rot == 2:
            x -= 89
            y += 30
        elif rot == 3:
            x -= 30
            y -= 89
        rot = (rot - 1) % 4
    finish_domino(side)

ren_x = []
ren_y = []

def convert_board():
    '''Converts the board from edit format to render format'''
    global ren_x
    global ren_y
    ren_x = dmn_x.copy()
    ren_y = dmn_y.copy()
    for side in range(len(dmn_x)):
        for i in range(len(dmn_x[side])):
            if dmn_rot[side][i] % 2:
                ren_x[side][i] -= 30
                ren_y[side][i] -= 59
            else:
                ren_x[side][i] -= 59
                ren_y[side][i] -= 30

def import_board(board: str):
    '''Imports a board'''
    global dmn_x
    global dmn_y
    global dmn_rot
    global rot
    global x
    global y
    board = board.upper()
    x, y = 0, 0
    side = -1
    init_rot = []
    valid = False
    for i in range(len(board)):
        if i == 0:
            sides = int(board[i])
            dmn_x, dmn_y, dmn_rot = [], [], []
            for j in range(int(board[i])):
                dmn_x.append([])
                dmn_y.append([])
                dmn_rot.append([])
        elif 1 <= i <= sides:
            init_rot.append(int(board[i]))
        else:
            if board[i] == '|':
                side += 1
                rot = init_rot[side]
                x, y = 0, 0
                if board[i+1] != 'S':
                    straight(1, side, True)
                    valid = True
            elif board[i] == 'F':
                straight(1, side)
            elif board[i] == 'L':
                turn(False, side)
            elif board[i] == 'R':
                turn(True, side)
            else:
                if not board[i] == ' ':
                    if not valid:
                        print(f'Invalid character at column {i} in board: {board[i]}')
                    valid = False

ren_start_x = 640
ren_start_y = 360
board_scale = 0.75
# documentation:
# first digit = number of sides
# then, the initial rotations of the dominoes (0→  1↓  2←  3↑)
# then, the sides divided by '|': F - go straight, R - turn right, L - turn left
# there's always a forward domino in the line unless you put 'S' in the beginning
# i recommend having at least 100 dominoes in a line, 189 is the effective maximum that is ideal
default_boards2 = [[lang['board_default'], '220|FFFRRFFFFFFFFLLFFFFFFFFRRFFFFFFFFLLFFFFFFFFRRFFFFFFFFLLFFFFFFFFRRFFFFFFFFLLFFFFFFFFRRFFFFFFFFLLFFFFFFFFRRFFFFFFFFLLFFFFFFFFRRFFFFFFFFLLFFFFFFFFRRFFFFFFFFLLFFFFFFFFRRFFFFFFFFLLFFFFFFFF|FFFRRFFFFFFFFLLFFFFFFFFRRFFFFFFFFLLFFFFFFFFRRFFFFFFFFLLFFFFFFFFRRFFFFFFFFLLFFFFFFFFRRFFFFFFFFLLFFFFFFFFRRFFFFFFFFLLFFFFFFFFRRFFFFFFFFLLFFFFFFFFRRFFFFFFFFLLFFFFFFFFRRFFFFFFFFLLFFFFFFFF'],
                   [lang['board_spiral_cw'], '220|LLFFFLFFLFFFFFLFFFFLFFFFFFFLFFFFFFLFFFFFFFFFLFFFFFFFFLFFFFFFFFFFFLFFFFFFFFFFLFFFFFFFFFFFFFLFFFFFFFFFFFFLFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFF|LLFFFLFFLFFFFFLFFFFLFFFFFFFLFFFFFFLFFFFFFFFFLFFFFFFFFLFFFFFFFFFFFLFFFFFFFFFFLFFFFFFFFFFFFFLFFFFFFFFFFFFLFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFF'],
                   [lang['board_spiral_ccw'], '220|RRFFFRFFRFFFFFRFFFFRFFFFFFFRFFFFFFRFFFFFFFFFRFFFFFFFFRFFFFFFFFFFFRFFFFFFFFFFRFFFFFFFFFFFFFRFFFFFFFFFFFFRFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFF|RRFFFRFFRFFFFFRFFFFRFFFFFFFRFFFFFFRFFFFFFFFFRFFFFFFFFRFFFFFFFFFFFRFFFFFFFFFFRFFFFFFFFFFFFFRFFFFFFFFFFFFRFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFF']]
default_boards4 = [[lang['board_default'], '42301|FFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFF|FFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFF|FFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFF|FFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFFRRFFFFFFFLLFFFFFFF'],
                   [lang['board_spiral_cw'], '42301|LFFLFFFFFLFFFFFFFFLFFFFFFFFFFFLFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFFFFFFFFFFFFF|LFFLFFFFFLFFFFFFFFLFFFFFFFFFFFLFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFFFFFFFFFFFFF|LFFLFFFFFLFFFFFFFFLFFFFFFFFFFFLFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFFFFFFFFFFFFF|LFFLFFFFFLFFFFFFFFLFFFFFFFFFFFLFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFFFFFFFFFFLFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'],
                   [lang['board_spiral_ccw'], '42301|RFFRFFFFFRFFFFFFFFRFFFFFFFFFFFRFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFFFFFFFFFFFFF|RFFRFFFFFRFFFFFFFFRFFFFFFFFFFFRFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFFFFFFFFFFFFF|RFFRFFFFFRFFFFFFFFRFFFFFFFFFFFRFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFFFFFFFFFFFFF|RFFRFFFFFRFFFFFFFFRFFFFFFFFFFFRFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFFFFFFFFFFRFFFFFFFFFFFFFFFFFFFFFFFFFFFFF']]
# theme_desc = [domino outline,                  0
#               domino divider,                  1
#               domino color,                    2
#               1,                               3
#               2,                               4
#               3,                               5
#               4,                               6
#               5,                               7
#               6,                               8
#               7,                               9
#               8,                               10
#               9,                               11
#               main ui color,                   12
#               inactive/pressed button color    13
#               default button color,            14
#               active text color,               15
#               inactive text color,             16
#               splash color,                    17
#               victory (green) color,           18
#               failure (red) color              19
#               inventory scroll button hover    20
#               selected text background         21
#               10,                              22
#               11,                              23
#               12,                              24
#               13,                              25
#               14,                              26
#               15,                              27
#               16,                              28
#               17,                              29
#               18,                              30
#               meta: author                     31
#               meta: name                       32
#               meta: description                33
#               meta: file format (2 for b1.8)   34
default_themes = [
                    [(0, 0, 0),
                    (0, 0, 0),
                    (242, 242, 242),
                    (224, 0, 0),
                    (255, 96, 0),
                    (255, 192, 0),
                    (0, 224, 0),
                    (0, 192, 255),
                    (0, 0, 224),
                    (128, 0, 255),
                    (255, 0, 255),
                    (0, 0, 0),
                    (3, 209, 255),
                    (0, 156, 191),
                    (1, 175, 216),
                    (0, 0, 0),
                    (45, 45, 45),
                    (240, 255, 0),
                    (0, 200, 0),
                    (200, 0, 0),
                    (50, 224, 255),
                    (0, 0, 255, 192),
                    (112, 0, 0),
                    (128, 48, 0),
                    (128, 96, 0),
                    (0, 112, 0),
                    (0, 96, 128),
                    (0, 0, 112),
                    (64, 0, 128),
                    (128, 0, 128),
                    (0, 0, 0),
                    "WinNT",
                    lang['theme_light_name'],
                    lang['theme_light_desc'],
                    2],
                  
                    [(127, 127, 127),
                    (127, 127, 127),
                    (20, 20, 20),
                    (255, 0, 0),
                    (255, 128, 0),
                    (255, 255, 0),
                    (0, 255, 0),
                    (0, 255, 255),
                    (0, 64, 255),
                    (128, 0, 255),
                    (255, 0, 255),
                    (255, 255, 255),
                    (20, 20, 20),
                    (0, 0, 0),
                    (10, 10, 10),
                    (200, 200, 200),
                    (100, 100, 100),
                    (160, 170, 0),
                    (0, 127, 0),
                    (127, 0, 0),
                    (40, 40, 40),
                    (0, 0, 255, 192),
                    (255, 0, 0),
                    (255, 128, 0),
                    (255, 255, 0),
                    (0, 255, 0),
                    (0, 255, 255),
                    (0, 64, 255),
                    (128, 0, 255),
                    (255, 0, 255),
                    (255, 255, 255),
                    "WinNT",
                    lang['theme_dark_name'],
                    lang['theme_dark_desc'],
                    2]
                 ] # the list of default themes

# color_none = pygame.Color(0, 0, 0, 0)
# load settings
total_themes = config_data["custom_themes"].copy()
##for i in range(len(custom_themes)):
##    custom_themes[i] = ast.literal_eval(custom_themes[i])
def update_theme(theme: list):
    '''Updates the theme from any version to version 2'''
    if theme[-1] == 0:
        print(lang['theme_upd_0'].format(theme=theme))
        theme.insert(8, theme[7])
        theme.insert(8, theme[7])
        theme.insert(8, theme[7])
        theme.insert(1, theme[0])
        theme.insert(20, (min(255, theme[12][0] + 15), min(255, theme[12][1] + 15), min(255, theme[12][2] + 15)))
        theme[-1] = 1
        return update_theme(theme) # this is not infinite recursion, since input data is different
    if len(theme) == 24: # update from pre1
        print(lang['theme_upd_pre1'].format(theme=theme))
        theme.insert(20, (min(255, theme[12][0] + 15), min(255, theme[12][1] + 15), min(255, theme[12][2] + 15)))
        return update_theme(theme)
    if theme[-1] == 1:
        print(lang['theme_upd_1'].format(theme=theme))
        theme.insert(21, (0, 0, 255, 192))
        theme = theme[:22] + theme[3:12] + theme[22:]
        theme[-1] = 2
        return theme
    if len(theme) == 26:
        print(lang['theme_upd_2pre1'].format(theme=theme))
        theme = theme[:22] + theme[3:12] + theme[22:]
        return theme
    elif theme[-1] > 2:
        return False
    else:
        return theme

var_init = time.time() - t
t = time.time()

custom_themes = []
for i in total_themes:
    theme = update_theme(i)
    if theme is False:
        print(lang['err_future_theme'].format(theme=i))
    else:
        custom_themes.append(theme)
config_data["custom_themes"] = custom_themes

try:
    windowed_score = bool(int(config_data["windowed_score"]))
except:
    print(lang['err_no_setting'].format(param='windowed_score'))
    windowed_score = True
    config_data["windowed_score"] = True

try:
    fastmode = bool(int(config_data["fastmode"]))
except:
    print(lang['err_no_setting'].format(param='fastmode'))
    fastmode = True
    config_data["fastmode"] = True

try:
    theme_id = int(config_data["theme_id"])
except:
    print(lang['err_no_setting'].format(param='theme_id'))
    theme_id = 1
    config_data["theme_id"] = 1

try:
    blink_time = int(config_data["blink_time"])
except:
    print(lang['err_no_setting'].format(param='blink_time'))
    blink_time = 10
    config_data["blink_time"] = 10

try:
    play_place_sound = bool(int(config_data["place_sound"]))
    sound_place.set_volume(float(play_place_sound))
except:
    print(lang['err_no_setting'].format(param='place_sound'))
    play_place_sound = True
    sound_place.set_volume(1.0)
    config_data["place_sound"] = True

try:
    play_error_sound = int(config_data["error_sound"])
    sound_error.set_volume(float(play_error_sound))
except:
    print(lang['err_no_setting'].format(param='error_sound'))
    play_error_sound = True
    sound_error.set_volume(1.0)
    config_data["error_sound"] = True

try:
    selected_board2 = bool(int(config_data["selected_board2"]))
except:
    print(lang['err_no_setting'].format(param='selected_board2'))
    selected_board2 = 0
    config_data["selected_board2"] = 0

try:
    selected_board4 = bool(int(config_data["selected_board4"]))
except:
    print(lang['err_no_setting'].format(param='selected_board4'))
    selected_board4 = 0
    config_data["selected_board4"] = 0

try:
    custom_boards2 = config_data['custom_boards2'].copy()
    total_boards2 = config_data['custom_boards2'].copy()
except:
    print(lang['err_no_setting'].format(param='custom_boards2'))
    custom_boards2 = []
    total_boards2 = []
    config_data["custom_boards2"] = []

try:
    custom_boards4 = config_data['custom_boards4'].copy()
    total_boards4 = config_data['custom_boards4'].copy()
except:
    print(lang['err_no_setting'].format(param='custom_boards4'))
    total_boards4 = []
    custom_boards4 = []
    config_data["custom_boards4"] = []


boards2 = default_boards2 + custom_boards2
boards4 = default_boards4 + custom_boards4

import_board(boards2[selected_board2][1])
convert_board()

theme_list = default_themes + custom_themes
try:
    theme = theme_list[theme_id]
except IndexError:
    print(lang['invalid_theme'])
    config_data["theme_id"] = 1
    theme_id = int(config_data["theme_id"])
    theme = theme_list[theme_id]

is_theme_updated = False
backup_ui = "menu_main"

framerate_output = pygame.USEREVENT+1
output_fps = pygame.event.Event(framerate_output)
pygame.time.set_timer(framerate_output, 500)
current_fps = "FPS: (wait)"

scroll_offset = 0
start_y = -1
start_offset = 0

min_write = 0
player_size = 7
scorelim = 100
player_count = 2
begin_with_double = False

test_bool = True

is_game_running = False

darken = pygame.Surface((1280, 720)).convert_alpha()
darken.fill((0, 0, 0))
darken.set_alpha(128)

conf_load = time.time() - t
t = time.time()

# utility functions
def draw_rect(x1, y1, x2, y2, surface, color_id=8, outline=3, outline_color_id=0):
    '''Draws a rect with one line and without you needing to specify the width and length'''
    if x1 > x2 or y1 > y2:
        raise ValueError("first set of coordinates must represent top left corner")
    dx = x2 - x1
    dy = y2 - y1
    if type(color_id) == int:
        pygame.draw.rect(surface, theme[color_id], (x1, y1, dx, dy))
    else:
        pygame.draw.rect(surface, color_id, (x1, y1, dx, dy))
    if type(outline_color_id) == int:
        pygame.draw.rect(surface, theme[outline_color_id], (x1, y1, dx, dy), outline)
    else:
        pygame.draw.rect(surface, outline_color_id, (x1, y1, dx, dy), outline)
def blit(text, font, pos, surface, center=False, color=(0, 0, 0)):
    '''Blits some text to a chosen surface with only one line instead of two'''
    j = font.render(text, 1, color)
    if center is True:
        pos = (pos[0]-j.get_width() / 2, pos[1])
    elif center == 'back': # interprets the given x coord as the right end and not 
        pos = (pos[0]-j.get_width(), pos[1])
    surface.blit(j, pos)
# this function was copied from StackOverflow (with some edits) and is made by Ted Klein Bergman (thank you!)
def blit_multiline(surface, text, pos, limit_x, font, color):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 4, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= limit_x:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
def draw_window(x1, y1, x2, y2, title, surface, header_color_id=8, fill_color_id=10, outline_color_id=0):
    draw_rect(x1, y1, x2, y2, fill_color_id, 3, outline_color_id)
    draw_rect(x1, y1, x2, y1+40, header_color_id, 3, outline_color_id)
    header = font_header.render(title, 4, outline_color_id)
    surface.blit(header, (x2-x1) / 2 - header.get_width() / 2 + x1, y1 - 20 - header.get_height() / 2)

# game operations
class Game: # probably the most complicated class i've ever made
    def __init__(self, settings, ui_hooks, mid_game={'initialized': False}, filename=None):
        '''A Dominoes PE game'''
        # if settings['gamemode'] == 'custom':
        self.double_start = settings['begin_with_double'] # expects a bool
        self.score_limit = settings['score_limit'] # expects an int
        self.player_count = settings['players'] # expects an int
        self.player_init_give = settings['give_players'] # expects an int, at most (1+2+3+...+highest_number_on_domino) / player_count
        self.set_type = settings['set_type'] + 1 # expects an int, 3-18
        self.ai_count = settings['ai_count'] # expects an int, at most player_count
        self.dominoes_set = [] 
        for i in range(self.set_type):
            for j in range(self.set_type):
                if not [j, i] in self.dominoes_set:
                    self.dominoes_set.append([i, j])
        self.min_score = settings['min_score'] # expects an int

        self.save_file_name = filename # expects a string
        self.save_data = None

        if mid_game['initialized']: # a set of values that appear after starting the game
            # 'initialized' tag allows to load config-only games, for example, to change the inaccessible settings; it's a bool
            self.board = mid_game['board']['dominoes'] # expects a list of lists of ints
            self.board_inv = mid_game['board']['inversion'] # expects a list of lists of bools
            self.center = mid_game['board']['dmn0'] # expects an int

            self.ends = mid_game['board']['ends']

            self.bazar = mid_game['player_data']['bazar'] # expects a list of ints  ## i still don't know how it's called in English
            self.player_inv = mid_game['player_data']['inventories'] # expects a list of lists of ints
            self.player_scores = mid_game['player_data']['scores'] # expects a list of floats
            self.player_victories = mid_game['player_data']['victories'] # expects a list of ints
            self.player_names = mid_game['player_data']['names'] # expects a list of strings
            self.current_move = mid_game['current_move'] # expects an int, at most player_count

            self.game_stage = mid_game['stage'] # expects 'beginning' or 'game'
            self.game_number = mid_game['game_number'] # expects an int
            self.restarted_from = mid_game['last_restart'] # expects 'battle' or 'game'
            
            self.update_ability()
        else:
            self.game_number = 0
            self.restarted_from = 'game'
            self.player_scores = [0] * self.player_count
            self.player_victories = [0] * self.player_count
            self.player_names = []
            p, b = 1, 1
            for i in range(self.player_count):
                if self.is_ai(i+1):
                    self.player_names.append(lang['bot'].format(n=b))
                    b += 1
                else:
                    self.player_names.append(lang['player'].format(n=p))
                    p += 1
            
            self.init()

        # ui hooks: a set of functions that allow integration with pretty much any graphical shell, specified by user

        # side_select is called whenever a player can place a domino on multiple sides, it returns the ID of the chosen side (int)
        # score_upd is called to show the new scores after a round ends, it doesn't return anything
        # next_player shows a prompt for the next player to come and make their move if needed

        self.side_select = ui_hooks['side_select'] # expects a function with args: board ([sides, inv]), target (int), is_ai (bool)
        self.score_upd = ui_hooks['score_upd'] # expects a function with args: score_orig (list of ints), score_new (list of ints), vict (int)
        self.next_player = ui_hooks['next_player'] # expects a function with args: current_move (int), player_count (int), fastmode (bool)

    def init(self):
        '''Initializes the game/battle'''
        self.board = []
        self.board_inv = []
        for i in range(2):
            self.board.append([])
            self.board_inv.append([])
        self.center = None

        self.ends = [0] * 2
        self.ability = [[0]] * 2
        
        self.player_inv = []
        for i in range(self.player_count):
            self.player_inv.append([]) # for whatever reason, just multiplying the list makes it act weird
        self.game_stage = 'beginning'

        inv = list(range(len(self.dominoes_set)))
        for i in range(self.player_count):
            for j in range(self.player_init_give):
                give = -1
                while not give in inv:
                    give = random.randint(0, len(self.dominoes_set) - 1)
                self.player_inv[i].append(give)
                inv.remove(give)
        self.bazar = inv.copy()

        self.current_move = 0
        self.enforced_domino = None
        if self.restarted_from == 'battle':
            if [] in self.player_inv:
                self.current_move = self.player_inv.index([])
            else:
                self.current_move = random.randint(1, self.player_count)
        elif self.restarted_from == 'game':
            self.player_scores = [0 for i in range(self.player_count)]
            if self.double_start:
                self.enforced_domino = 0
                for i in self.player_inv:
                    for j in range(self.set_type):
                        k = self.dominoes_set.index([j, j]) 
                        if k in i and j == self.game_number % self.set_type + 1:
                            self.current_move = self.player_inv.index(i) + 1
                            self.enforced_domino = k
                            break
            if self.current_move == 0:
                self.current_move = random.randint(1, self.player_count)
                self.enforced_domino = None

    def generate_save(self) -> dict:
        '''Generates the save data'''
        self.save_data = {"settings": {"begin_with_double": self.double_start,
                                       "score_limit": self.score_limit,
                                       "players": self.player_count,
                                       "give_players": self.player_init_give,
                                       "set_type": self.set_type - 1,
                                       "ai_count": self.ai_count,
                                       "min_score": self.min_score},
                          "mid_game": {"initialized": True,
                                       "board": {"dominoes": self.board,
                                                 "inversion": self.board_inv,
                                                 "ends": self.ends,
                                                 "dmn0": self.center},
                                       "player_data": {"bazar": self.bazar,
                                                       "inventories": self.player_inv,
                                                       "scores": self.player_scores,
                                                       "victories": self.player_victories,
                                                       "names": self.player_names},
                                       "current_move": self.current_move,
                                       "stage": self.game_stage,
                                       "game_number": self.game_number,
                                       "last_restart": self.restarted_from}}
        return self.save_data

    def give_player(self, player: int) -> bool:
        '''Give a domino to a player from the bazar and return the success value'''
        try:
            choice = random.choice(self.bazar)
        except:
            if player < self.player_count - self.ai_count:
                print(lang['bazar_empty'])
            return False
        else:
            self.bazar.remove(choice)
            self.player_inv[player-1].append(choice)

    def get_player(self, player: int) -> dict:
        '''Returns all the info about a player (as a dict), or all of them (as a list)'''
        if 0 < player < self.player_count+1:
            return {'inv': self.player_inv[player - 1],
                    'victories': self.player_victories[player - 1],
                    'score': self.player_scores[player - 1],
                    'name': self.player_names[player - 1]}
        else:
            temp = []
            for i in range(self.player_count):
                temp.append({'inv': self.player_inv[i],
                             'victories': self.player_victories[i],
                             'score': self.player_scores[i],
                             'name': self.player_names[i]})
            return temp
    
    def get_board(self, side: int, inv: bool) -> list:
        '''Returns the chosen side of the board, or the middle domino'''
        if side == 0:
            return self.center
        elif side < 0:
            if inv:
                return self.board_inv
            else:
                return self.board
        else:
            if inv:
                return self.board_inv[side-1]
            else:
                return self.board[side-1]

    def update_ability(self) -> list:
        '''Updates the lists of dominoes that you can place at each end and returns it (for debugging)'''
        if self.game_stage == 'beginning':
            return None
        else:
            j = 0 # i think this looks better
            self.ability = []
            for i in self.ends:
                self.ability.append([])
                for dmn in self.dominoes_set:
                    if i in dmn:
                        self.ability[j].append(self.dominoes_set.index(dmn))
                j += 1
            self.ability2 = False
            for dmn in sum(self.player_inv, start=[]) + self.bazar:
                if dmn in sum(self.ability, start=[]):
                    self.ability2 = True
                    break
            if not self.ability2:
                return False
            return self.ability
        
    def update_score(self) -> list:
        '''Updates the players' scores and returns the actions (difference, victories)'''
        to_add = [0] * self.player_count
        vict = False
        for i in range(self.player_count):
            for j in self.player_inv[i]:
                to_add[i] += int(self.dominoes_set[j][0]) + int(self.dominoes_set[j][1])
            if self.player_scores[i] + to_add[i] < self.min_score:
                to_add[i] = 0
            self.player_scores[i] += to_add[i]
            if self.player_scores[i] >= self.score_limit:
                vict = True
        if vict:
            vict_val = min(self.player_scores)
            vict_targ = []
            for i in range(self.player_count):
                if self.player_scores[i] == vict_val:
                    vict_targ.append(i)
                    self.player_victories[i] += 1
            self.restarted_from = 'game'
        else:
            vict_targ = None
            self.restarted_from = 'battle'
        return [to_add, vict_targ]

    def is_ai(self, player):
        return player > self.player_count - self.ai_count

    def incr_player(self):
        self.current_move += 1
        if self.current_move > self.player_count:
            self.current_move = 1

    def fastmode_needed(self, initial_player):
        if fastmode:
            return True
        else:
            initial_player += 1
            if initial_player > self.player_count:
                initial_player = 1
            return self.is_ai(initial_player)

    def place(self, id, source) -> bool:
        '''Place a domino #<id> at player <source> and return the success value'''
        if self.current_move == source:
            targ_dmn_type = self.dominoes_set[self.player_inv[source-1][id]]
            targ_dmn_num = self.player_inv[source-1][id]
            if self.game_stage == 'beginning':
                if self.restarted_from == 'game' and self.double_start:
                    if self.enforced_domino is None or targ_dmn_num == self.enforced_domino:
                        self.center = self.player_inv[source-1][id]
                        self.player_inv[source-1].pop(id)
                        self.ends = [targ_dmn_type[0], targ_dmn_type[1]]
                        self.game_stage = 'game'
                        self.next_player(self.current_move, self.player_count, self.fastmode_needed(self.current_move))
                        self.incr_player()
                        return True
                    else:
                        return False
                else:
                    self.center = self.player_inv[source-1][id]
                    self.player_inv[source-1].pop(id)
                    self.ends = [targ_dmn_type[0], targ_dmn_type[1]]
                    self.game_stage = 'game'
                    self.next_player(self.current_move, self.player_count, self.fastmode_needed(self.current_move))
                    self.incr_player()
                    return True
            else:
                if self.update_ability() is False:
                    old_score = self.player_scores.copy()
                    vict = self.update_score()[1]
                    new_score = self.player_scores.copy()
                    self.score_upd(old_score, new_score, vict)
                    self.init()
                    return True
                if targ_dmn_num in self.ability[0] and not targ_dmn_num in self.ability[1]:
                    self.board[0].append(targ_dmn_num) # place left
                    self.player_inv[source-1].pop(id)
                    if targ_dmn_type[0] == self.ends[0]:
                        self.board_inv[0].append(True)
                        self.ends[0] = targ_dmn_type[1]
                    else:
                        self.board_inv[0].append(False)
                        self.ends[0] = targ_dmn_type[0]
                elif targ_dmn_num in self.ability[1] and not targ_dmn_num in self.ability[0]:
                    self.board[1].append(targ_dmn_num) # place right
                    self.player_inv[source-1].pop(id)
                    if targ_dmn_type[0] == self.ends[1]:
                        self.board_inv[1].append(False)
                        self.ends[1] = targ_dmn_type[1]
                    else:
                        self.board_inv[1].append(True)
                        self.ends[1] = targ_dmn_type[0]
                elif targ_dmn_num in self.ability[0] and targ_dmn_num in self.ability[1]:
                    side = self.side_select([self.board, self.board_inv], targ_dmn_num, self.is_ai(source))
                    if side == 0:
                        self.board[0].append(targ_dmn_num) # place left
                        self.player_inv[source-1].pop(id)
                        if targ_dmn_type[0] == self.ends[0]:
                            self.board_inv[0].append(True)
                            self.ends[0] = targ_dmn_type[1]
                        else:
                            self.board_inv[0].append(False)
                            self.ends[0] = targ_dmn_type[0]
                    else:
                        self.board[1].append(targ_dmn_num) # place right
                        self.player_inv[source-1].pop(id)
                        if targ_dmn_type[0] == self.ends[1]:
                            self.board_inv[1].append(False)
                            self.ends[1] = targ_dmn_type[1]
                        else:
                            self.board_inv[1].append(True)
                            self.ends[1] = targ_dmn_type[0]
                else:
                    return False
                if [] in self.player_inv:
                    old_score = self.player_scores.copy()
                    vict = self.update_score()[1]
                    new_score = self.player_scores.copy()
                    self.score_upd(old_score, new_score, vict)
                    self.init()
                    return True
                self.next_player(self.current_move, self.player_count, self.fastmode_needed(self.current_move))
                self.incr_player()
                return True
        else:
            return False

class ui: # the game's GUI
    def __init__(self, surface, init=True):
        self.surface = surface

        self.btn_continue = ui_tools.Button(self.surface, 480, 420, 155, 55, font_d60, lang['btn_continue'], theme[14], theme[12], theme[13], theme[15], theme[0])
        self.btn_load_game = ui_tools.Button(self.surface, 645, 420, 155, 55, font_d60, lang['btn_load_game_full'], theme[14], theme[12], theme[13], theme[15], theme[0])
        self.btn_new_game = ui_tools.Button(self.surface, 480, 355, 320, 55, font_d60, lang['btn_new_game'], theme[14], theme[12], theme[13], theme[15], theme[0])
        self.btn_settings = ui_tools.Button(self.surface, 480, 485, 320, 55, font_d60, lang['settings'], theme[14], theme[12], theme[13], theme[15], theme[0])
        self.btn_how_to_play = ui_tools.Button(self.surface, 480, 550, 155, 55, font_d60, lang['how_to_play'], theme[14], theme[12], theme[13], theme[15], theme[0])
        self.btn_exit = ui_tools.Button(self.surface, 645, 550, 155, 55, font_d60, lang['btn_exit'], theme[14], theme[12], theme[13], theme[15], theme[0])

        self.btn_gm_local = ui_tools.Button(self.surface, 250, 400, 300, 55, font_d60, lang['local_game'], theme[14], theme[12], theme[13], theme[15], theme[0])
        self.btn_gm_internet = ui_tools.Button(self.surface, 250, 500, 300, 55, font_d60, lang['in_development'], theme[14], theme[12], theme[13], theme[16], theme[16])
        self.btn_gm_pva = ui_tools.Button(self.surface, 730, 400, 300, 55, font_d60, lang['singleplayer'], theme[14], theme[12], theme[13], theme[15], theme[0])
        self.btn_gm_ava = ui_tools.Button(self.surface, 730, 500, 300, 55, font_d60, lang['bot_battle'], theme[14], theme[12], theme[13], theme[15], theme[0])
        self.btn_gm_back = ui_tools.Button(self.surface, 490, 600, 300, 55, font_d60, lang['btn_back'], theme[14], theme[12], theme[13], theme[15], theme[0])

        self.btn_next_battle = ui_tools.Button(self.surface, 540, 420, 200, 40, font_d60, lang['btn_next_round'], theme[14], theme[12], theme[13], theme[15], theme[0])

        self.btn_next_player = ui_tools.Button(self.surface, 540, 500, 200, 50, font_d60, lang['btn_next_player'], theme[14], theme[12], theme[13], theme[15], theme[0])

        self.ren_domino = domino.Domino(self.surface, theme[0], theme[2], theme[1], theme[3:12] + theme[22:31])

        # sliders in settings menu
        self.test_slider = ui_tools.Switch(self.surface, 640, 360, 86, 36, 4, theme[14], theme[12], theme[0], theme[18], theme[19]) # for tests

        self.s_windowed_score = ui_tools.Switch(self.surface, 1145, 145, 86, 36, 4, theme[14], theme[12], theme[0], theme[18], theme[19])
        self.s_fastmode = ui_tools.Switch(self.surface, 1145, 215, 86, 36, 4, theme[14], theme[12], theme[0], theme[18], theme[19])
        self.s_place_sound = ui_tools.Switch(self.surface, 1145, 285, 86, 36, 4, theme[14], theme[12], theme[0], theme[18], theme[19])
        self.s_error_sound = ui_tools.Switch(self.surface, 1145, 355, 86, 36, 4, theme[14], theme[12], theme[0], theme[18], theme[19])
        
        self.lang_list = ui_tools.DropdownList(self.surface, 1230, 466, lang_names, font_d50, True, lang_ids.index(lang_type), 200, False, 6, theme[13], theme[14], theme[15], theme[0], pygame.Color(list(theme[0]) + [64]), theme[14], theme[12], theme[0])

        if init:
            
            self.game = Game({'begin_with_double': False, 'score_limit': 100, 'players': 2, 'give_players': 7, 'set_type': 6, 'min_score': 0, 'ai_count': 0},
                             {'side_select': self.handle_lor_dilemma, 'score_upd': self.ren_score_update, 'next_player': self.next_player})
        self.left_side = self.game.get_board(1, False)
        self.left_is_inv = self.game.get_board(1, True)
        self.right_side = self.game.get_board(2, False)
        self.right_is_inv = self.game.get_board(2, True)

        # other smart stuff in settings
        self.go_set_theme = ui_tools.Hyperlink(self.surface, 40, 476, lang['lnk_theme_settings'], font_d60, theme[15])
        self.go_menu = ui_tools.Hyperlink(self.surface, 50, 66, lang['lnk_exit_settings'], font_d60, theme[15])
        self.exit_game = ui_tools.Button(self.surface, 990, 630, 250, 50, font_d60, lang['btn_go_menu'], theme[14], theme[12], theme[13], theme[15], theme[0])
        self.save_game = ui_tools.Button(self.surface, 730, 630, 250, 50, font_d60, lang['btn_save_quit'], theme[14], theme[12], theme[13], theme[15], theme[0])
        self.blink_time = ui_tools.TextField(self.surface, 1100, 406, font_d60, 130, 50, blink_time, '5','string',
                                               theme[15], theme[16], theme[12], theme[21])
        self.go_set_board = ui_tools.Hyperlink(self.surface, 40, 536, lang['lnk_board_type'], font_d60, theme[15])

        self.theme_surface = pygame.Surface((780, 620))
        self.inner_surface = pygame.Surface((510, 450))

        self.tutorial = pygame.Surface((500, 450))

        self.tutorial_back = ui_tools.Button(self.surface, 175, 390, 150, 50, self.tutorial, lang['btn_back'])

        self.setup_win = pygame.Surface((780, 620))

        self.score_lim = ui_tools.TextField(self.setup_win, 580, 85, font_field, 170, 65, '100', '100', 'int',
                                              theme[15], theme[16], theme[12], theme[21])
        self.min_score = ui_tools.TextField(self.setup_win, 580, 165, font_field, 170, 65, '0', '0', 'int',
                                              theme[15], theme[16], theme[12], theme[21])
        self.give_players = ui_tools.TextField(self.setup_win, 580, 245, font_field, 170, 65, '7', '7', 'int',
                                                 theme[15], theme[16], theme[12], theme[21])
        self.player_count = ui_tools.TextField(self.setup_win, 580, 325, font_field, 170, 65, '2', '2', 'int',
                                                 theme[15], theme[16], theme[12], theme[21])

        self.s_begin_with_double = ui_tools.Switch(self.setup_win, 664, 427, 86, 36, 4, theme[14], theme[12], theme[0], theme[18], theme[19])

        self.btn_setup_play = ui_tools.Button(self.setup_win, 590, 550, 170, 50, font_d50, lang['btn_start_game'], theme[14], theme[12], theme[13], theme[15], theme[0])
        self.btn_setup_back = ui_tools.Button(self.setup_win, 410, 550, 170, 50, font_d50, lang['btn_back'], theme[14], theme[12], theme[13], theme[15], theme[0])
        self.tutorial_back = ui_tools.Button(self.tutorial, 165, 390, 170, 50, font_d50, lang['btn_back'], theme[14], theme[12], theme[13], theme[15], theme[0])

        self.scroll_board2_l = ui_tools.Button(self.surface, 50, 20, 30, 30, font_scroll, '◄', None, None, None, theme[15], None)
        self.scroll_board2_r = ui_tools.Button(self.surface, 80, 20, 30, 30, font_scroll, '►', None, None, None, theme[15], None)
        self.scroll_board4_l = ui_tools.Button(self.surface, 50, 60, 30, 30, font_scroll, '◄', None, None, None, theme[15], None)
        self.scroll_board4_r = ui_tools.Button(self.surface, 80, 60, 30, 30, font_scroll, '►', None, None, None, theme[15], None)
        self.return_from_board = ui_tools.Button(self.surface, 1160, 645, 100, 55, font_d50, lang['btn_back'], theme[14], theme[12], theme[13], theme[15], theme[0])
        self.import_board = ui_tools.Button(self.surface, 1050, 645, 100, 55, font_d50, lang['import'], theme[14], theme[12], theme[13], theme[15], theme[0])
        self.selector_board2 = ui_tools.Button(self.surface, 15, 25, 20, 20, font_scroll, '●', None, None, None, theme[15], None)
        self.selector_board4 = ui_tools.Button(self.surface, 15, 65, 20, 20, font_scroll, '○', None, None, None, theme[15], None)

        self.board_import_field = ui_tools.TextField(self.surface, 10, 650, font_field, 1260, 60, '', lang['import_board_msg'], 'string', theme[15], theme[16], theme[12], theme[21])
        self.board_name = ui_tools.TextField(self.surface, 10, 650, font_field, 1260, 60, '', lang['name_board'], 'string', theme[15], theme[16], theme[12], theme[21])

        self.delete_board = ui_tools.Button(self.surface, 15, 105, 100, 55, font_error, lang['delete_theme'], theme[14], theme[12], theme[13], theme[15], theme[0])

        self.splash_size = 0.0
        self.board_demo = 2

        self.ai_timer = 0

    # render functions
    def render_main_menu(self, btn=True):
        global current_ui
        global game_version
        global is_rendered
        global test_bool
        global backup_ui
        global is_game_running
        self.splash_size += dt / 5
        self.surface.fill(theme[12])
        blit(lang['game_name'], font_title, (640, 0), self.surface, True, theme[15])
        blit('Python Edition', font_pe, (640, 210), self.surface, True, theme[15])
        ren_splash = font_splash.render(splash, 4, theme[17])
        ren_splash = pygame.transform.rotozoom(ren_splash, 30, 1 + math.sin(self.splash_size) / 30)
        version = font_ver.render(game_version, 4, theme[15])
        self.surface.blit(version, (8, 720 - version.get_height()))
        if btn:
            # continue button
            if is_game_running:
                self.btn_load_game.x = 645
                self.btn_load_game.width = 155
                self.btn_load_game.text = lang['btn_load_game_short']
                if self.btn_continue.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    current_ui = "local_game"
            else:
                self.btn_load_game.x = 480
                self.btn_load_game.width = 320
                self.btn_load_game.text = lang['btn_load_game_full']
            # new game button
            if self.btn_new_game.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                current_ui = "menu_gamemode_select"
                pygame.event.clear()
            
            # load game button
            if self.btn_load_game.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                file = filedialog.askopenfilename(title=lang['btn_load_game_full'], filetypes=[(lang['filetype_json'], '*.json'), (lang['filetype_all'], '*.*')])
                if file:
                    with open(file, 'r', -1, 'utf-8') as game:
                        try:
                            data = json.load(game)
                        except Exception:
                            traceback.format_exc()
                    self.game = Game(data['settings'], {'side_select': self.handle_lor_dilemma, 'score_upd': self.ren_score_update, 'next_player': self.next_player}, data['mid_game'])
                    self.gamemode = data['gamemode']
                    self.offsets = [0, 0]
                    self.init_player_controls(data['settings']['players'])
                    self.bazar_empty = player_size == len(self.game.dominoes_set)
                    is_game_running = True
                    current_ui = "local_game"
            # settings button
            if self.btn_settings.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                backup_ui = "menu_main"
                current_ui = "settings"
            # quit button
            if self.btn_exit.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                save_config()
                pygame.quit()
                print(lang['thanks'])
                exit(0)
            # how to play button
            if self.btn_how_to_play.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                current_ui = 'how_to_play'
        self.surface.blit(ren_splash, (900 - (ren_splash.get_width() / 2), 210 - (ren_splash.get_height() / 2)))

    def render_menu_gm_sel(self, btn=True):
        global current_ui
        global game_version
        global is_rendered
        global is_game_running
        self.render_main_menu(False)
        # inactive button
        self.btn_gm_internet.draw(click_state=2)
        # texts
        gm_sel = font_gm_sel.render(lang['select_gamemode'], 4, theme[15])
        self.surface.blit(gm_sel, (640 - (gm_sel.get_width() / 2), 315 - (gm_sel.get_height() / 2)))
        is_rendered = True
        if self.btn_gm_local.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN) and btn:
            current_ui = "local_setup"
            self.gamemode = "local"
        # back button
        if self.btn_gm_back.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN) and btn:
            current_ui = "menu_main"
        # gamemode = pva button
        if self.btn_gm_pva.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN) and btn:
            current_ui = "local_setup"
            self.gamemode = "pva"
        # gamemode = bot_battle button
        if self.btn_gm_ava.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN) and btn:
            current_ui = "local_setup"
            self.gamemode = "bot_battle"

    def game_ren(self, custom_board=None, scale=0.75, debug=False):
        global ren_start_x
        global ren_start_y
        global board_scale
        self.surface.fill(theme[12])
        if debug:
            self.ren_domino.draw_scaled([0, 0], (ren_start_x - 30*board_scale, ren_start_y - 59*board_scale), board_scale, True, False)
            for side in range(len(ren_x)):
                for i in range(len(ren_x[side])): # DEBUG FEATURE
                    self.ren_domino.draw_scaled([0, side+1], (ren_x[side][i]*board_scale + ren_start_x, ren_y[side][i]*board_scale + ren_start_y), board_scale, dmn_rot[side][i] % 2, dmn_rot[side][i] // 2)
            # for i in range(len(ren_x[0])): # DEBUG FEATURE
            #     self.ren_domino.draw_scaled('19', (ren_x[0][i]*scale + ren_start_x, ren_y[0][i]*scale + ren_start_y), scale, dmn_rot[0][i] % 2, dmn_rot[0][i] // 2)
            #     self.ren_domino.draw_scaled('19', (ren_x[1][i]*scale + ren_start_x, ren_y[1][i]*scale + ren_start_y), scale, dmn_rot[1][i] % 2, dmn_rot[1][i] // 2)
            #     self.ren_domino.draw_scaled('11', (ren_start_x - 30*scale, ren_start_y - 59*scale), scale, True, False)
            return
        if not custom_board:
            sides = self.game.get_board(-1, False)
            sides_inv = self.game.get_board(-1, True)
        else:
            sides, sides_inv = custom_board
        dmn0 = self.game.get_board(0, False)
        p = self.game.get_player(0)
        ds = self.game.dominoes_set
        ## render the dominoes
        for side in range(len(ren_x)):
            for i in range(len(sides[side])): # DEBUG FEATURE
                inv = (not dmn_rot[0][i] // 2) + sides_inv[side][i] == 1
                self.ren_domino.draw_scaled(ds[sides[side][i]], (ren_x[side][i]*board_scale + ren_start_x, ren_y[side][i]*board_scale + ren_start_y), board_scale, dmn_rot[side][i] % 2, inv)

        if dmn0 is not None:
            self.ren_domino.draw_scaled(ds[dmn0], (ren_start_x - 30*board_scale, ren_start_y - 59*board_scale), board_scale, True, False)

        # player dominoes
        if len(p) == 4:
            for i in range(len(p)):
                #    ----
                if i == 0:
                    draw_rect(150, 30, 1140, 120, self.surface, 12, 4)
                    for j in range(min(len(p[i]['inv']), 23)):
                        if self.game.current_move == 1 or self.game.is_ai(1):
                            self.ren_domino.draw_scaled(ds[p[i]['inv'][j + self.offsets[i]]], (152+43*j, 32), 0.75, True)
                        else:
                            draw_rect(150+43*j, 31, 194+43*j, 120, self.surface, 2, 3, 0)
                    if len(p[i]['inv']) > 23:
                        self.scroll_len = max(43.5, min(43.5 * len(p[i]['inv']) / (len(p[i]['inv']) - 23), 957))
                        self.scroll_step = (990 - self.scroll_len) / (len(p[i]['inv']) - 23) 
                        self.scroll_pos = self.scroll_step * self.offsets[i]
                        pygame.draw.rect(self.surface, theme[0], (150+self.scroll_pos, 115, self.scroll_len, 5))
                    playerdata = font_pd.render(lang['playerdata_single'].format(player=p[i]['name'], score=p[i]['score'], vict=p[i]['victories']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
                    pygame.draw.rect(self.surface, theme[0], (150, 0, playerdata.get_width()+4, 30), 3)
                    self.surface.blit(playerdata, (152, 4))
                # |
                elif i == 1:
                    draw_rect(30, 140, 120, 570, self.surface, 12, 4)
                    for j in range(min(len(p[i]['inv']), 10)):
                        if (self.game.current_move == 2) and not self.game.is_ai(2) or self.gamemode == 'bot_battle':
                            self.ren_domino.draw_scaled(ds[p[i]['inv'][j + self.offsets[i]]], (33, 142+43*j), 0.75)
                        else:
                            draw_rect(31, 140+43*j, 121, 184+43*j, self.surface, 2, 3, 0)
                    if len(p[i]['inv']) > 10:
                        self.scroll_len = max(43.5, min(43.5 * len(p[i]['inv']) / (len(p[i]['inv']) - 10), 391.5))
                        self.scroll_step = (435 - self.scroll_len) / (len(p[i]['inv']) - 10) 
                        self.scroll_pos = self.scroll_step * self.offsets[i]
                        pygame.draw.rect(self.surface, theme[0], (115, 140+self.scroll_pos, 5, self.scroll_len))
                    playerdata = font_pd.render(lang['playerdata_name'].format(player=p[i]['name']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
                    score = font_pd.render(lang['playerdata_score'].format(score=p[i]['score']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
                    vict = font_pd.render(lang['playerdata_vict'].format(vict=p[i]['victories']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
                    draw_rect(30, 60, 120, 140, self.surface, 13 - int(self.game.current_move == i + 1), 3)
                    self.surface.blit(playerdata, (75 - playerdata.get_width()/2, 63))
                    self.surface.blit(score, (75 - score.get_width()/2, 90))
                    self.surface.blit(vict, (75 - vict.get_width()/2, 112))
                    
                #    ____
                elif i == 2:
                    draw_rect(150, 600, 1140, 690, self.surface, 12, 4)
                    for j in range(min(len(p[i]['inv']), 23)):
                        if (self.game.current_move == 3) and not self.game.is_ai(3) or self.gamemode == 'bot_battle':
                            self.ren_domino.draw_scaled(ds[p[i]['inv'][j + self.offsets[i]]], (152+43*j, 602), 0.75, True)
                        else:
                            draw_rect(150+43*j, 601, 194+43*j, 690, self.surface, 2, 3, 0)
                    if len(p[i]['inv']) > 23:
                        self.scroll_len = max(43.5, min(43.5 * len(p[i]['inv']) / (len(p[i]['inv']) - 23), 957))
                        self.scroll_step = (990 - self.scroll_len) / (len(p[i]['inv']) - 23) 
                        self.scroll_pos = self.scroll_step * self.offsets[i]
                        pygame.draw.rect(self.surface, theme[0], (150+self.scroll_pos, 685, self.scroll_len, 5))
                    playerdata = font_pd.render(lang['playerdata_single'].format(player=p[i]['name'], score=p[i]['score'], vict=p[i]['victories']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
                    pygame.draw.rect(self.surface, theme[0], (150, 570, playerdata.get_width()+4, 30), 3)
                    self.surface.blit(playerdata, (152, 574))
                #            |
                elif i == 3:
                    draw_rect(1160, 140, 1250, 570, self.surface, 12, 4)
                    for j in range(min(len(p[i]['inv']), 10)):
                        if (self.game.current_move == 4) and not self.game.is_ai(4) or self.gamemode == 'bot_battle':
                            self.ren_domino.draw_scaled(ds[p[i]['inv'][j + self.offsets[i]]], (1163, 142+43*j), 0.75)
                        else:
                            draw_rect(1161, 140+43*j, 1251, 184+43*j, self.surface, 2, 3, 0)
                    if len(p[i]['inv']) > 10:
                        self.scroll_len = max(43.5, min(43.5 * len(p[i]['inv']) / (len(p[i]['inv']) - 10), 391.5))
                        self.scroll_step = (435 - self.scroll_len) / (len(p[i]['inv']) - 10) 
                        self.scroll_pos = self.scroll_step * self.offsets[i]
                        pygame.draw.rect(self.surface, theme[0], (1245, 140+self.scroll_pos, 5, self.scroll_len))
                    playerdata = font_pd.render(lang['playerdata_name'].format(player=p[i]['name']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
                    score = font_pd.render(lang['playerdata_score'].format(score=p[i]['score']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
                    vict = font_pd.render(lang['playerdata_vict'].format(vict=p[i]['victories']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
                    draw_rect(1160, 60, 1250, 140, self.surface, 13 - int(self.game.current_move == i + 1), 3)
                    self.surface.blit(playerdata, (1205 - playerdata.get_width()/2, 63))
                    self.surface.blit(score, (1205 - score.get_width()/2, 90))
                    self.surface.blit(vict, (1205 - vict.get_width()/2, 112))
        elif len(p) == 3:
            for i in range(len(p)):
                #    ----
                if i == 0:
                    draw_rect(150, 30, 1140, 120, self.surface, 12, 4)
                    for j in range(min(len(p[i]['inv']), 23)):
                        if self.game.current_move == 1 or self.game.is_ai(1):
                            self.ren_domino.draw_scaled(ds[p[i]['inv'][j + self.offsets[i]]], (152+43*j, 32), 0.75, True)
                        else:
                            draw_rect(150+43*j, 31, 194+43*j, 120, self.surface, 2, 3, 0)
                    if len(p[i]['inv']) > 23:
                        self.scroll_len = max(43.5, min(43.5 * len(p[i]['inv']) / (len(p[i]['inv']) - 23), 957))
                        self.scroll_step = (990 - self.scroll_len) / (len(p[i]['inv']) - 23) 
                        self.scroll_pos = self.scroll_step * self.offsets[i]
                        pygame.draw.rect(self.surface, theme[0], (150+self.scroll_pos, 115, self.scroll_len, 5))
                    playerdata = font_pd.render(lang['playerdata_single'].format(player=p[i]['name'], score=p[i]['score'], vict=p[i]['victories']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
                    pygame.draw.rect(self.surface, theme[0], (150, 0, playerdata.get_width()+4, 30), 3)
                    self.surface.blit(playerdata, (152, 4))
                # |
                elif i == 1:
                    draw_rect(30, 140, 120, 570, self.surface, 12, 4)
                    for j in range(min(len(p[i]['inv']), 10)):
                        if (self.game.current_move == 2 or self.gamemode == 'bot_battle') and not self.game.is_ai(2):
                            self.ren_domino.draw_scaled(ds[p[i]['inv'][j + self.offsets[i]]], (33, 142+43*j), 0.75)
                        else:
                            draw_rect(31, 140+43*j, 121, 184+43*j, self.surface, 2, 3, 0)
                    if len(p[i]['inv']) > 10:
                        self.scroll_len = max(43.5, min(43.5 * len(p[i]['inv']) / (len(p[i]['inv']) - 10), 391.5))
                        self.scroll_step = (435 - self.scroll_len) / (len(p[i]['inv']) - 10) 
                        self.scroll_pos = self.scroll_step * self.offsets[i]
                        pygame.draw.rect(self.surface, theme[0], (115, 140+self.scroll_pos, 5, self.scroll_len))
                    playerdata = font_pd.render(lang['playerdata_name'].format(player=p[i]['name']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
                    score = font_pd.render(lang['playerdata_score'].format(score=p[i]['score']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
                    vict = font_pd.render(lang['playerdata_vict'].format(vict=p[i]['victories']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
                    draw_rect(30, 60, 120, 140, self.surface, 13 - int(self.game.current_move == i + 1), 3)
                    self.surface.blit(playerdata, (75 - playerdata.get_width()/2, 63))
                    self.surface.blit(score, (75 - score.get_width()/2, 90))
                    self.surface.blit(vict, (75 - vict.get_width()/2, 112))
                    
                #            |
                elif i == 2:
                    draw_rect(1160, 140, 1250, 570, self.surface, 12, 4)
                    for j in range(min(len(p[i]['inv']), 10)):
                        if (self.game.current_move == 3 or self.gamemode == 'bot_battle') and not self.game.is_ai(3):
                            self.ren_domino.draw_scaled(ds[p[i]['inv'][j + self.offsets[i]]], (1163, 142+43*j), 0.75)
                        else:
                            draw_rect(1161, 140+43*j, 1251, 184+43*j, self.surface, 2, 3, 0)
                    if len(p[i]['inv']) > 10:
                        self.scroll_len = max(43.5, min(43.5 * len(p[i]['inv']) / (len(p[i]['inv']) - 10), 391.5))
                        self.scroll_step = (435 - self.scroll_len) / (len(p[i]['inv']) - 10) 
                        self.scroll_pos = self.scroll_step * self.offsets[i]
                        pygame.draw.rect(self.surface, theme[0], (1245, 140+self.scroll_pos, 5, self.scroll_len))
                    playerdata = font_pd.render(lang['playerdata_name'].format(player=p[i]['name']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
                    score = font_pd.render(lang['playerdata_score'].format(score=p[i]['score']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
                    vict = font_pd.render(lang['playerdata_vict'].format(vict=p[i]['victories']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
                    draw_rect(1160, 60, 1250, 140, self.surface, 13 - int(self.game.current_move == i + 1), 3)
                    self.surface.blit(playerdata, (1205 - playerdata.get_width()/2, 63))
                    self.surface.blit(score, (1205 - score.get_width()/2, 90))
                    self.surface.blit(vict, (1205 - vict.get_width()/2, 112))
        else:
            draw_rect(20, 30, 1259, 138, self.surface, 12, 4, 0)
            draw_rect(20, 581, 1259, 689, self.surface, 12, 4, 0)
            for i in range(min(len(p[0]['inv']), 23)):
                if self.game.current_move == 1 or self.game.is_ai(1):
                    self.ren_domino.draw_scaled(ds[p[0]['inv'][i + self.offsets[0]]], (22+54*i, 32), 0.91, True)
                else:
                    draw_rect(18+i*54, 30, 81+i*54, 138, self.surface, 2, 4, 0)
            if len(p[0]['inv']) > 23:
                self.scroll_len = max(54, min(54 * len(p[0]['inv']) / (len(p[0]['inv']) - 23), 1188))
                self.scroll_step = (1232 - self.scroll_len) / (len(p[0]['inv']) - 23) 
                self.scroll_pos = self.scroll_step * self.offsets[0]
                pygame.draw.rect(self.surface, theme[0], (20+self.scroll_pos, 133, self.scroll_len, 5))
            playerdata = font_pd.render(lang['playerdata_single'].format(player=p[0]['name'], score=p[0]['score'], vict=p[0]['victories']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
            self.give[0].x = 21 + playerdata.get_width()
            pygame.draw.rect(self.surface, theme[0], (18, 0, playerdata.get_width()+5, 30), 3)
            self.surface.blit(playerdata, (20, 2))

            for i in range(min(len(p[1]['inv']), 23)):
                if self.game.current_move == 2 or self.gamemode == 'bot_battle':
                    self.ren_domino.draw_scaled(ds[p[1]['inv'][i + self.offsets[1]]], (22+54*i, 583), 0.91, True)
                else:
                    draw_rect(18+i*54, 581, 81+i*54, 689, self.surface, 2, 4, 0)
            if len(p[1]['inv']) > 23:
                self.scroll_len = max(54, min(54 * len(p[1]['inv']) / (len(p[1]['inv']) - 23), 1188))
                self.scroll_step = (1232 - self.scroll_len) / (len(p[1]['inv']) - 23) 
                self.scroll_pos = self.scroll_step * self.offsets[1]
                pygame.draw.rect(self.surface, theme[0], (20+self.scroll_pos, 684, self.scroll_len, 5))
            playerdata = font_pd.render(lang['playerdata_single'].format(player=p[1]['name'], score=p[1]['score'], vict=p[1]['victories']), 4, theme[15], theme[13 - int(self.game.current_move == i + 1)])
            self.give[1].x = 21 + playerdata.get_width()
            pygame.draw.rect(self.surface, theme[0], (18, 689, playerdata.get_width()+5, 30), 3)
            self.surface.blit(playerdata, (20, 691))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ren_start_x -= 5 * dt
        if keys[pygame.K_RIGHT]:
            ren_start_x += 5 * dt
        if keys[pygame.K_UP]:
            ren_start_y -= 5 * dt
        if keys[pygame.K_DOWN]:
            ren_start_y += 5 * dt
        if keys[pygame.K_KP_PLUS] or keys[pygame.K_PLUS]:
            board_scale *= 1.05
        if keys[pygame.K_KP_MINUS] or keys[pygame.K_MINUS]:
            board_scale /= 1.05
        if keys[pygame.K_ASTERISK] or keys[pygame.K_KP_MULTIPLY]:
            ren_start_x = 640
            ren_start_y = 360
            board_scale = 0.75

    def is_hor(self, player):
        if self.game.player_count == 2:
            return 1
        else:
            return (player+1) % 2

    def local_game_ctrl(self):
        if self.game.is_ai(self.game.current_move):
            self.ai(self.game.current_move)
            return
        for i in range(self.game.player_count):
            if not self.game.is_ai(i+1):
                self.give[i].draw()
                self.scroll[i*2].draw()
                self.scroll[i*2+1].draw()
        lpos = pygame.mouse.get_pos()
        p = self.game.get_player(0)
        
        if self.game.player_count > 2:
            if pygame.event.peek(pygame.MOUSEWHEEL):
                event = pygame.event.get(pygame.MOUSEWHEEL)[0]
                if 30 < lpos[0] < 120 and 140 < lpos[1] < 570:
                    self.offsets[i] = max(0, min(self.offsets[i] - event.y, len(p[1]['inv']) - 10))
                elif 1160 < lpos[0] < 1250 and 140 < lpos[1] < 570:
                    self.offsets[i] = max(0, min(self.offsets[i] - event.y, len(p[self.game.player_count - 1]['inv']) - 10))
        if pygame.mouse.get_pressed()[0] and pygame.event.get(pygame.MOUSEBUTTONDOWN):
            for i in range(self.game.player_count):
                if len(p[i]['inv']) > 10 + 13*self.is_hor(i) and not self.game.is_ai(i+1):
                    if self.offsets[i] < len(p[i]['inv']) - (10 + 13*self.is_hor(i)) and self.scroll[i*2].draw():
                        self.offsets[i] += 1
                        return
                    elif self.offsets[i] > 0 and self.scroll[i*2+1].draw():
                        self.offsets[i] -= 1
                        return
                if self.give[i]._is_hovered() and self.game.current_move == i + 1:
                    if self.bazar_empty:
                        self.game.incr_player()
                    elif self.game.give_player(i + 1) is False:
                        self.bazar_empty = True
                        sound_error.play()
                    else:
                        if len(p[i]['inv']) > 10 + 13*self.is_hor(i):
                            self.offsets[i] = len(p[i]['inv']) - (10 + 13*self.is_hor(i))
                    return
            # detect the clicked domino
            
            mouse_is_over = [0, 0]
            if self.game.player_count == 2:
                if lpos[0] > 26 and lpos[0] < 1252 and lpos[1] > 30 and lpos[1] < 150:
                    mouse_is_over[0] = 1
                    mouse_is_over[1] = int((lpos[0] - 26) / 54) + 1
                elif lpos[0] > 26 and lpos[0] < 1252 and lpos[1] > 570 and lpos[1] < 690:
                    mouse_is_over[0] = 2
                    mouse_is_over[1] = int((lpos[0] - 26) / 54) + 1
                else:
                    mouse_is_over = [0, 0]
            elif self.game.player_count == 3:
                if 150 < lpos[0] < 1130 and 30 < lpos[1] < 120:
                    mouse_is_over[0] = 1
                    mouse_is_over[1] = int((lpos[0] - 150) // 43) + 1
                elif 30 < lpos[0] < 120 and 140 < lpos[1] < 570:
                    mouse_is_over[0] = 2
                    mouse_is_over[1] = int((lpos[1] - 140) // 43) + 1
                elif 1160 < lpos[0] < 1250 and 140 < lpos[1] < 570:
                    mouse_is_over[0] = 3
                    mouse_is_over[1] = int((lpos[1] - 140) // 43) + 1
                else:
                    mouse_is_over = [0, 0]
            elif self.game.player_count == 4:
                if 150 < lpos[0] < 1130 and 30 < lpos[1] < 120:
                    mouse_is_over[0] = 1
                    mouse_is_over[1] = int((lpos[0] - 150) // 43) + 1
                elif 30 < lpos[0] < 120 and 140 < lpos[1] < 570:
                    mouse_is_over[0] = 2
                    mouse_is_over[1] = int((lpos[1] - 140) // 43) + 1
                elif 150 < lpos[0] < 1130 and 600 < lpos[1] < 690:
                    mouse_is_over[0] = 3
                    mouse_is_over[1] = int((lpos[0] - 150) // 43) + 1
                elif 1160 < lpos[0] < 1250 and 140 < lpos[1] < 570:
                    mouse_is_over[0] = 4
                    mouse_is_over[1] = int((lpos[1] - 140) // 43) + 1
                else:
                    mouse_is_over = [0, 0]
            mouse_is_over[1] += self.offsets[mouse_is_over[0] - 1]

            # print("Player", mouse_is_over[0], "domino", mouse_is_over[1])
            # check if there is anything at click position
            error = 0
            if mouse_is_over[0] == 0:
                error = 1
            else:
                try:
                    self.game.get_player(mouse_is_over[0])['inv'][mouse_is_over[1] - 1]
                except IndexError:
                    if not self.game.is_ai(mouse_is_over[0]):
                        print(lang['player_chose_nothing'])
                        sound_error.play()
                    error = 1
            if self.game.current_move != mouse_is_over[0] and mouse_is_over[0] != 0:
                if not self.game.is_ai(mouse_is_over[0]):
                    print(lang['wrong_turn'])
                    sound_error.play()
                error = 1
            if error == 0:
                bkp_offset = self.offsets.copy()
                if self.offsets[mouse_is_over[0] - 1] == len(p[mouse_is_over[0] - 1]['inv']) - (10 + 13*self.is_hor(mouse_is_over[0])):
                    self.offsets[mouse_is_over[0] - 1] = len(p[mouse_is_over[0] - 1]['inv']) - (11 + 13*self.is_hor(mouse_is_over[0]))
                if not self.game.place(mouse_is_over[1] - 1, self.game.current_move) and not self.game.is_ai(mouse_is_over[0]):
                    print(lang['cant_place_domino'])
                    sound_error.play()
                    self.offsets = bkp_offset
                
            # print("P1:", self.game.get_player(1))
            # print("P2:", self.game.get_player(2))
            # print("Bazar:", self.game.bazar)
            # print("Left side:", self.game.get_board(1, False), "with length of", len(self.game.get_board(1, False)), "ending with", self.game.ends[0])
            # print("Right side:", self.game.get_board(2, False), "with length of", len(self.game.get_board(2, False)), "ending with", self.game.ends[1])
            # print("Center domino:", self.game.get_board(0, False))
            # print("\n")

    def ren_score_update(self, scores_old, scores_new, vict):
        global current_ui
        current_ui = 'out_of_cycle'
        self.game_ren(scale=board_scale)
        players = len(scores_old)
        t = time.time()
        dt = 0.0
        sum_dt = 0.0
        # init
        if windowed_score:
            # increase score - init
            score_diff = []
            for i in range(players):
                score_diff.append(scores_new[i] - scores_old[i])
            
            # increase score
            while sum_dt < 1:
                dt = (time.time() - t) / 2
                sum_dt += dt
                t = time.time()
                # ask for input to prevent "not responding" message
                # actually, there's an intended way to do this in pygame, but this will be an easter egg
                if bool(pygame.event.get(pygame.KEYDOWN)):
                    print(":)")
                # render base
                if players == 2:
                    pygame.draw.rect(self.surface, theme[13], (50, 200, 540, 320))
                    pygame.draw.rect(self.surface, theme[13], (690, 200, 540, 320))
                    pygame.draw.rect(self.surface, theme[0], (50, 200, 540, 320), 4)
                    pygame.draw.rect(self.surface, theme[0], (690, 200, 540, 320), 4)
                    # render text
                    score1 = font_score.render(str(int(scores_old[0] + score_diff[0]*sum_dt)), 4, theme[15])
                    self.surface.blit(score1, (320 - (score1.get_width()/2), 360 - (score1.get_height()/2)))
                    score2 = font_score.render(str(int(scores_old[1] + score_diff[1]*sum_dt)), 4, theme[15])
                    self.surface.blit(score2, (960 - (score2.get_width()/2), 360 - (score1.get_height()/2)))
                else:
                    pygame.draw.rect(self.surface, theme[13], (50, 20, 540, 320))
                    pygame.draw.rect(self.surface, theme[13], (690, 20, 540, 320))
                    pygame.draw.rect(self.surface, theme[0], (50, 20, 540, 320), 4)
                    pygame.draw.rect(self.surface, theme[0], (690, 20, 540, 320), 4)
                    # render text
                    score1 = font_score.render(str(int(scores_old[0] + score_diff[0]*sum_dt)), 4, theme[15])
                    self.surface.blit(score1, (320 - (score1.get_width()/2), 180 - (score1.get_height()/2)))
                    score2 = font_score.render(str(int(scores_old[1] + score_diff[1]*sum_dt)), 4, theme[15])
                    self.surface.blit(score2, (960 - (score2.get_width()/2), 180 - (score1.get_height()/2)))
                    if players == 3:
                        pygame.draw.rect(self.surface, theme[13], (370, 380, 540, 320))
                        pygame.draw.rect(self.surface, theme[0], (370, 380, 540, 320), 4)
                        score3 = font_score.render(str(int(scores_old[2] + score_diff[2]*sum_dt)), 4, theme[15])
                        self.surface.blit(score3, (640 - (score3.get_width()/2), 540 - (score3.get_height()/2)))
                    if players == 4:
                        pygame.draw.rect(self.surface, theme[13], (50, 380, 540, 320))
                        pygame.draw.rect(self.surface, theme[13], (690, 380, 540, 320))
                        pygame.draw.rect(self.surface, theme[0], (50, 380, 540, 320), 4)
                        pygame.draw.rect(self.surface, theme[0], (690, 380, 540, 320), 4)
                        # render text
                        score3 = font_score.render(str(int(scores_old[2] + score_diff[2]*sum_dt)), 4, theme[15])
                        self.surface.blit(score3, (320 - (score3.get_width()/2), 540 - (score3.get_height()/2)))
                        score4 = font_score.render(str(int(scores_old[3] + score_diff[3]*sum_dt)), 4, theme[15])
                        self.surface.blit(score4, (960 - (score4.get_width()/2), 540 - (score4.get_height()/2)))
                # finish frame
                pygame.display.update()
                gametick.tick(60)
            if vict:
                for i in range(blink_time):
                    # ask for input to prevent "not responding" message
                    if bool(pygame.event.get(pygame.K_SPACE)):
                        print(":)")
                    # render base
                    if players == 2:
                        pygame.draw.rect(self.surface, theme[19 - int(0 in vict)], (50, 200, 540, 320))
                        pygame.draw.rect(self.surface, theme[19 - int(1 in vict)], (690, 200, 540, 320))
                        pygame.draw.rect(self.surface, theme[0], (50, 200, 540, 320), 4)
                        pygame.draw.rect(self.surface, theme[0], (690, 200, 540, 320), 4)
                        # render text
                        score1 = font_score.render(str(int(scores_old[0] + score_diff[0]*sum_dt)), 4, theme[15])
                        self.surface.blit(score1, (320 - (score1.get_width()/2), 360 - (score1.get_height()/2)))
                        score2 = font_score.render(str(int(scores_old[1] + score_diff[1]*sum_dt)), 4, theme[15])
                        self.surface.blit(score2, (960 - (score2.get_width()/2), 360 - (score1.get_height()/2)))
                    else:
                        pygame.draw.rect(self.surface, theme[19 - int(0 in vict)], (50, 20, 540, 320))
                        pygame.draw.rect(self.surface, theme[19 - int(1 in vict)], (690, 20, 540, 320))
                        pygame.draw.rect(self.surface, theme[0], (50, 20, 540, 320), 4)
                        pygame.draw.rect(self.surface, theme[0], (690, 20, 540, 320), 4)
                        # render text
                        score1 = font_score.render(str(int(scores_old[0] + score_diff[0]*sum_dt)), 4, theme[15])
                        self.surface.blit(score1, (320 - (score1.get_width()/2), 180 - (score1.get_height()/2)))
                        score2 = font_score.render(str(int(scores_old[1] + score_diff[1]*sum_dt)), 4, theme[15])
                        self.surface.blit(score2, (960 - (score2.get_width()/2), 180 - (score1.get_height()/2)))
                        if players == 3:
                            pygame.draw.rect(self.surface, theme[19 - int(2 in vict)], (370, 380, 540, 320))
                            pygame.draw.rect(self.surface, theme[0], (370, 380, 540, 320), 4)
                            score3 = font_score.render(str(int(scores_old[2] + score_diff[2]*sum_dt)), 4, theme[15])
                            self.surface.blit(score3, (640 - (score3.get_width()/2), 540 - (score3.get_height()/2)))
                        if players == 4:
                            pygame.draw.rect(self.surface, theme[19 - int(2 in vict)], (50, 380, 540, 320))
                            pygame.draw.rect(self.surface, theme[19 - int(3 in vict)], (690, 380, 540, 320))
                            pygame.draw.rect(self.surface, theme[0], (50, 380, 540, 320), 4)
                            pygame.draw.rect(self.surface, theme[0], (690, 380, 540, 320), 4)
                            # render text
                            score3 = font_score.render(str(int(scores_old[2] + score_diff[2]*sum_dt)), 4, theme[15])
                            self.surface.blit(score3, (320 - (score3.get_width()/2), 540 - (score3.get_height()/2)))
                            score4 = font_score.render(str(int(scores_old[3] + score_diff[3]*sum_dt)), 4, theme[15])
                            self.surface.blit(score4, (960 - (score4.get_width()/2), 540 - (score4.get_height()/2)))
                    # finish frame
                    pygame.display.update()
                    gametick.tick(60)
                    # wait
                    pygame.time.delay(500)
                    # render base
                    if players == 2:
                        pygame.draw.rect(self.surface, theme[13], (50, 200, 540, 320))
                        pygame.draw.rect(self.surface, theme[13], (690, 200, 540, 320))
                        pygame.draw.rect(self.surface, theme[0], (50, 200, 540, 320), 4)
                        pygame.draw.rect(self.surface, theme[0], (690, 200, 540, 320), 4)
                        # render text
                        score1 = font_score.render(str(int(scores_old[0] + score_diff[0]*sum_dt)), 4, theme[15])
                        self.surface.blit(score1, (320 - (score1.get_width()/2), 360 - (score1.get_height()/2)))
                        score2 = font_score.render(str(int(scores_old[1] + score_diff[1]*sum_dt)), 4, theme[15])
                        self.surface.blit(score2, (960 - (score2.get_width()/2), 360 - (score1.get_height()/2)))
                    else:
                        pygame.draw.rect(self.surface, theme[13], (50, 20, 540, 320))
                        pygame.draw.rect(self.surface, theme[13], (690, 20, 540, 320))
                        pygame.draw.rect(self.surface, theme[0], (50, 20, 540, 320), 4)
                        pygame.draw.rect(self.surface, theme[0], (690, 20, 540, 320), 4)
                        # render text
                        score1 = font_score.render(str(int(scores_old[0] + score_diff[0]*sum_dt)), 4, theme[15])
                        self.surface.blit(score1, (320 - (score1.get_width()/2), 180 - (score1.get_height()/2)))
                        score2 = font_score.render(str(int(scores_old[1] + score_diff[1]*sum_dt)), 4, theme[15])
                        self.surface.blit(score2, (960 - (score2.get_width()/2), 180 - (score1.get_height()/2)))
                        if players == 3:
                            pygame.draw.rect(self.surface, theme[13], (370, 380, 540, 320))
                            pygame.draw.rect(self.surface, theme[0], (370, 380, 540, 320), 4)
                            score3 = font_score.render(str(int(scores_old[2] + score_diff[2]*sum_dt)), 4, theme[15])
                            self.surface.blit(score3, (640 - (score3.get_width()/2), 540 - (score3.get_height()/2)))
                        if players == 4:
                            pygame.draw.rect(self.surface, theme[13], (50, 380, 540, 320))
                            pygame.draw.rect(self.surface, theme[13], (690, 380, 540, 320))
                            pygame.draw.rect(self.surface, theme[0], (50, 380, 540, 320), 4)
                            pygame.draw.rect(self.surface, theme[0], (690, 380, 540, 320), 4)
                            # render text
                            score3 = font_score.render(str(int(scores_old[2] + score_diff[2]*sum_dt)), 4, theme[15])
                            self.surface.blit(score3, (320 - (score3.get_width()/2), 540 - (score3.get_height()/2)))
                            score4 = font_score.render(str(int(scores_old[3] + score_diff[3]*sum_dt)), 4, theme[15])
                            self.surface.blit(score4, (960 - (score4.get_width()/2), 540 - (score4.get_height()/2)))
                    # finish frame
                    pygame.display.update()
                    gametick.tick(60)
                    # wait
                    pygame.time.delay(500)
        
        # END DATA
        # draw a fancy window
        pygame.draw.rect(self.surface, theme[14], (440, 360-(120+50*players)//2, 400, 120+50*players))
        pygame.draw.rect(self.surface, theme[0], (440, 360-(120+50*players)//2, 400, 120+50*players), 4)
        pygame.draw.rect(self.surface, theme[12], (440, 360-(120+50*players)//2, 400, 40))
        pygame.draw.rect(self.surface, theme[0], (440, 360-(120+50*players)//2, 400, 40), 4)
        text_title = font_ver.render(lang['game_over'], 4, theme[15])
        for i in range(players):
            blit(self.game.get_player(i+1)['name'], font_gm_sel, (450, 360-(120+50*players)//2+40 + i*50), self.surface, color=theme[15])
            blit(str(scores_new[i] - scores_old[i]), font_gm_sel, (830, 360-(120+50*players)//2+40 + i*50), self.surface, 'back', theme[15])
        self.btn_next_battle.y = 360+((120+50*players)//2) - 50
        self.surface.blit(text_title, (640 - (text_title.get_width() / 2), 360-(120+50*players)//2))
        # ui_tools
        while current_ui == "out_of_cycle":
            if self.btn_next_battle.draw():
                current_ui = 'local_init'
            else:
                pygame.event.get()
            pygame.display.update()
            gametick.tick(60)

    def handle_lor_dilemma(self, board, dmn, is_ai=False): # is called whenever the player is able to place a domino on both left and right sides and shows a nice gui
        if is_ai:
            return random.randint(0, 1)
        is_solved = False
        
        while not is_solved:
            ren_left_side = board[0][0].copy()
            ren_left_is_inv = board[1][0].copy()
            ren_right_side = board[0][1].copy()
            ren_right_is_inv = board[1][1].copy()
            pos = pygame.mouse.get_pos()
            if pos[1] < 360:
                ren_left_side.append(dmn)
                ren_left_is_inv.append(int(self.game.dominoes_set[dmn - 1][0]) == int(self.game.ends[0]))
                self.game_ren([[ren_left_side, ren_right_side], [ren_left_is_inv, ren_right_is_inv]], scale=board_scale)
                hint_use = font_gm_sel.render(lang['click_to_place'], 4, theme[15], theme[12])
                pygame.draw.rect(self.surface, theme[0], (636 - (hint_use.get_width() / 2), 76 - (hint_use.get_height() / 2), hint_use.get_width() + 8, hint_use.get_height() + 8))
                self.surface.blit(hint_use, (640 - (hint_use.get_width() / 2), 80 - (hint_use.get_height() / 2)))
                pygame.display.update()
                gametick.tick(60)
                if bool(pygame.event.get(pygame.MOUSEBUTTONDOWN)):
                    is_solved = True
                    return 0
                ren_left_side = board[0][0].copy()
            else:
                ren_right_side.append(dmn)
                ren_right_is_inv.append(not int(self.game.dominoes_set[dmn - 1][0]) == int(self.game.ends[1]))
                self.game_ren([[ren_left_side, ren_right_side], [ren_left_is_inv, ren_right_is_inv]], scale=board_scale)
                hint_use = font_gm_sel.render(lang['click_to_place'], 4, theme[15], theme[12])
                pygame.draw.rect(self.surface, theme[0], (636 - (hint_use.get_width() / 2), 76 - (hint_use.get_height() / 2), hint_use.get_width() + 8, hint_use.get_height() + 8))
                self.surface.blit(hint_use, (640 - (hint_use.get_width() / 2), 80 - (hint_use.get_height() / 2)))
                pygame.display.update()
                gametick.tick(60)
                if bool(pygame.event.get(pygame.MOUSEBUTTONDOWN)):
                    is_solved = True
                    return 1
                ren_right_side = board[0][1].copy()

    def next_player(self, current_move, player_count, fastmode):
        if not fastmode:
            new_player = current_move + 1
            if new_player > player_count:
                new_player = 1
            self.game_ren(scale=board_scale)
            # draw a fancy window
            pygame.draw.rect(self.surface, theme[14], (350, 150, 580, 420))
            pygame.draw.rect(self.surface, theme[0], (350, 150, 580, 420), 4)
            pygame.draw.rect(self.surface, theme[12], (350, 150, 580, 40))
            pygame.draw.rect(self.surface, theme[0], (350, 150, 580, 40), 4)
            # draw exclamation sign
            pygame.draw.circle(self.surface, theme[0], (640, 270), 70, 4)
            pygame.draw.ellipse(self.surface, theme[0], [627, 215, 26, 20])
            pygame.draw.polygon(self.surface, theme[0], [[627, 225], [638, 297], [642, 297], [653, 225]])
            pygame.draw.circle(self.surface, theme[0], [640, 315], 9)
            # draw all the texts
            window_title = font_header.render(lang['wait_next_player'], 4, theme[15])
            self.surface.blit(window_title, (355, 170 - (window_title.get_height() / 2)))
            line1 = font_gm_sel.render(lang['your_turn'].format(player=new_player), 4, theme[15])
            sl1 = font_gm_sel.size(lang['your_turn'].format(player=new_player))
            self.surface.blit(line1, (640 - sl1[0]/2, 360 - sl1[1]/2))
            line2 = font_gm_sel.render(lang['press_space_ok_1'], 4, theme[15])
            sl2 = font_gm_sel.size(lang['press_space_ok_1'])
            line3 = font_gm_sel.render(lang['press_space_ok_2'], 4, theme[15])
            sl3 = font_gm_sel.size(lang['press_space_ok_2'])
            self.surface.blit(line2, (640 - sl2[0]/2, 410 - sl2[1]/2))
            self.surface.blit(line3, (640 - sl3[0]/2, 460 - sl3[1]/2))
            done = False
            while not done:
                if self.btn_next_player.draw() or pygame.key.get_pressed()[pygame.K_SPACE]:
                    return
                pygame.event.pump()
                pygame.display.update()
                gametick.tick(60)
        else:
            return

    def settings(self):
        ## init
        global font_gm_sel
        global windowed_score
        global fastmode
        global theme
        global current_ui
        global is_rendered
        global is_theme_updated
        global backup_ui
        global config
        global config_data
        global blink_time
        global play_place_sound
        global play_error_sound
        global lang
        global lang_type
        global theme_list
        pygame.draw.rect(self.surface, theme[14], (25, 25, 1230, 670))
        pygame.draw.rect(self.surface, theme[0], (25, 25, 1230, 670), 4)
        pygame.draw.rect(self.surface, theme[12], (25, 25, 1230, 40))
        pygame.draw.rect(self.surface, theme[0], (25, 25, 1230, 40), 4)
        temp = self.lang_list.draw()
        if temp is not None:
            lang = langs[temp]
            lang_type = lang_ids[temp]
            self.__init__(self.surface, False)
            config_data['lang'] = lang_ids[temp]
            update_win_caption()
            update_translatables()
            theme_list[0][-3] = lang['theme_light_name']
            theme_list[0][-2] = lang['theme_light_desc']
            theme_list[1][-3] = lang['theme_dark_name']
            theme_list[1][-2] = lang['theme_dark_desc']
            default_boards2[0][0] = lang['board_default']
            default_boards2[1][0] = lang['board_spiral_cw']
            default_boards2[2][0] = lang['board_spiral_ccw']
            default_boards4[0][0] = lang['board_default']
            default_boards4[1][0] = lang['board_spiral_cw']
            default_boards4[2][0] = lang['board_spiral_ccw']
        ## draw the sliders
        # show scores in the two windows
        if self.s_windowed_score.draw(windowed_score):
            windowed_score = not windowed_score
            self.lang_list.prepare_options()
            if windowed_score:
                config_data["windowed_score"] = True
            else:
                config_data["windowed_score"] = False
        # do not confirm move changes (for testing purposes)
        if self.s_fastmode.draw(fastmode):
            fastmode = not fastmode
            if fastmode:
                config_data["fastmode"] = True
            else:
                config_data["fastmode"] = False
        # play domino place sound
        if self.s_place_sound.draw(play_place_sound):
            play_place_sound = not play_place_sound
            sound_place.set_volume(float(play_place_sound))
            if play_place_sound:
                config_data["place_sound"] = True
            else:
                config_data["place_sound"] = False
        # play error sound
        if self.s_error_sound.draw(play_error_sound):
            play_error_sound = not play_error_sound
            sound_error.set_volume(float(play_error_sound))
            if play_error_sound:
                config_data["error_sound"] = True
            else:
                config_data["error_sound"] = False
        # change the theme button
        if self.go_set_theme.draw():
            current_ui = "theme_" + current_ui
        if self.go_set_board.draw():
            current_ui = "board_" + current_ui
        # exit button
        if self.go_menu.draw():
            save_config()
            current_ui = backup_ui
            is_rendered = False
        ## the option descriptions
        opt1 = font_gm_sel.render(lang['opt_big_windows'], 4, theme[15])
        self.surface.blit(opt1, (40, 126))
        opt3 = font_gm_sel.render(lang['opt_fastmode'], 4, theme[15])
        self.surface.blit(opt3, (40, 196))
        opt4 = font_gm_sel.render(lang['opt_place_sound'], 4, theme[15])
        self.surface.blit(opt4, (40, 266))
        opt5 = font_gm_sel.render(lang['opt_error_sound'], 4, theme[15])
        self.surface.blit(opt5, (40, 336))
        opt6 = font_gm_sel.render(lang['language'], 4, theme[15])
        if windowed_score:
            blit(lang['opt_vict_show_time'], font_gm_sel, (40, 396), self.surface, color=theme[15])
            self.surface.blit(opt6, (40, 456))
            self.go_set_theme.y = 526
            self.lang_list.y = 466
            self.lang_list.orig_y = 466
            self.go_set_board.y = 586
        else:
            self.surface.blit(opt6, (40, 396))
            self.go_set_theme.y = 466
            self.lang_list.y = 406
            self.lang_list.orig_y = 406
            self.go_set_board.y = 526
        if current_ui == "pause":
            titl = font_header.render(lang['game_paused'], 4, theme[15]) # typo intentional
            # back to main menu button
            if self.exit_game.draw():
                save_config()
                current_ui = 'menu_main'
            if self.save_game.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                save_config()
                to_save = self.game.generate_save()
                filename = filedialog.asksaveasfilename(defaultextension = '.json', filetypes = [('Файлы JSON', '*.json'), (lang['filetype_all'], '*.*')], title = 'Сохранить игру')
                if filename:
                    to_save["gamemode"] = self.gamemode
                    current_ui = 'menu_main'
                    with open(filename, 'w', -1, 'utf-8') as save_file:
                        save_file.write(json.dumps(to_save, indent=2, ensure_ascii=False))
        else:
            titl = font_header.render(lang['settings'], 4, theme[15])
        self.surface.blit(titl, (640 - titl.get_width() / 2, 45 - titl.get_height() / 2))
        # score blinking time
        if windowed_score:
            temp = self.blink_time.draw(text_color=theme[15], hint_color=theme[16])
            if temp is not False:
                blink_time = temp
                config_data["blink_time"] = blink_time

    def ai(self, whoami=2):
        inv = self.game.get_player(whoami)['inv']
        self.offsets = [0] * self.game.player_count
        self.ai_timer += dt
        if self.ai_timer < 3:
            return
        else:
            self.ai_timer = 0
        for i in range(len(inv)):
            upd_dt()
            self.game_ren(scale=board_scale)
            pygame.display.update()
            gametick.tick(60)
            # print(f'[DEBUG] Trying to place dmn #{i} of {whoami}')
            # if self.game.player_count > 2 and i > 10:
            #     self.offsets[whoami - 1] = i - 10 # just a visual effect :)  # that doesn't work
            if self.game.current_move == whoami and self.game.place(i, whoami):
                # print(f'[DEBUG] Succesful place of dmn #{i} of {whoami}')
                return
        while True:
            upd_dt()
            self.game_ren(scale=board_scale)
            pygame.display.update()
            gametick.tick(60)
            if self.game.give_player(whoami) is False:
                # print('[DEBUG] Bazar is empty - skipping move')
                self.game.incr_player()
                return
            # print(f'[DEBUG] Trying to place dmn #{len(self.game.get_player(1)["inv"]) - 1} of {whoami} after getting a domino')
            if self.game.current_move == whoami and self.game.place(-1, whoami):
                return

    
    def theme_set_ui(self, source="settings"): # a sub-ui inside the settings menu - here you can set your theme and import new ones
        # init
        global theme
        global theme_list
        global scroll_offset
        global test_bool
        global start_y
        global start_offset
        global scroll_percent
        global scroller_size
        global max_physical_offset
        global scroller_pos
        global current_ui
        global config_data
        global is_theme_updated
        global theme_id
        theme_awaits_setting = None
        if len(theme_list) > 3:
            if scroll_offset > 0:
                scroll_offset = 0
            elif scroll_offset < (150*(len(theme_list)-3))*-1:
                scroll_offset = (150*(len(theme_list)-3))*-1
            max_offset = (150*(len(theme_list)-3))
            scroll_percent = round(scroll_offset/-max_offset, 2)
            scroller_size = int(40000/max_offset)
            max_physical_offset = 378 - scroller_size
            if scroller_size < 40:
                scroller_size = 40
            scroller_pos = (378 - scroller_size) * scroll_percent
            scroll_per_pixel = max_offset / max_physical_offset
        # draw the window
        pygame.draw.rect(self.theme_surface, theme[14], (0, 0, 780, 620))
        pygame.draw.rect(self.theme_surface, theme[0], (0, 0, 780, 620), 4)
        pygame.draw.rect(self.theme_surface, theme[12], (0, 0, 780, 40))
        pygame.draw.rect(self.theme_surface, theme[0], (0, 0, 780, 40), 4)
        title123 = font_header.render(lang['theme_selection'], 4, theme[15])
        self.theme_surface.blit(title123, (390 - title123.get_width() / 2, 20 - title123.get_height() / 2))
        title123 = font_gm_sel.render(lang['choose_theme'], 4, theme[15])
        self.theme_surface.blit(title123, (20, 50))
        title123 = font_ver.render(lang['selected_theme'], 4, theme[15])
        self.theme_surface.blit(title123, (550, 160))
        title123 = font_ver.render(lang['more_themes'], 4, theme[15])
        self.theme_surface.blit(title123, (550, 370))
        title123 = font_ver.render(theme[-3], 4, theme[15])
        self.theme_surface.blit(title123, (550, 200))
        blit_multiline(self.theme_surface, theme[-4] + ' · ' + theme[-2], (550, 240), 720, font_fps, theme[15])
        pos = pygame.mouse.get_pos()
        win_pos = [pos[0] - 250, pos[1] - 50]
        self.inner_surface.fill(theme[14])
        # theme demo
        for i in range(len(theme_list)):
            if len(theme_list) > 3:
                width = 470
            else:
                width = 500
            in_pos = [win_pos[0] - 20, win_pos[1] - 135]
            start_y = in_pos[1]
            pygame.draw.rect(self.inner_surface, theme_list[i][12], (5, 5+scroll_offset+150*i, width, 140))
            pygame.draw.rect(self.inner_surface, theme_list[i][0], (5, 5+scroll_offset+150*i, width, 140), 3)
            title123 = font_ver.render(theme_list[i][-3], 4, theme_list[i][11])
            self.inner_surface.blit(title123, (10, 5+scroll_offset+150*i))
            title123 = font_fps.render(theme_list[i][-4] + ' · ' + theme_list[i][-2], 4, theme_list[i][15])
            self.inner_surface.blit(title123, (10, 37+scroll_offset+150*i))
            example_domino = domino.Domino(self.inner_surface, theme_list[i][0], theme_list[i][2], theme_list[i][1], theme_list[i][3:12])
            example_domino.draw([1, 2], (12, 70+scroll_offset+150*i))
            example_domino.draw([3, 4], (127, 70+scroll_offset+150*i))
            example_domino.draw([5, 6], (242, 70+scroll_offset+150*i))
            demo_slider = ui_tools.Switch(self.inner_surface, 365, 67+scroll_offset+150*i, 86, 36, 4, theme_list[i][13], theme_list[i][14],
                                        theme_list[i][0], theme_list[i][18], theme_list[i][19])
            if demo_slider.draw(test_bool, in_pos) and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                test_bool = not test_bool
                pygame.event.clear()
            test_button = ui_tools.Button(self.inner_surface, 370, 112+scroll_offset+150*i, 80, 25, font_ver, lang['test_button'], theme_list[i][14], theme_list[i][12], theme_list[i][13], theme_list[i][15], theme_list[i][0])
            test_button.draw(in_pos)
            btn_del = ui_tools.Button(self.inner_surface, 370, 15+scroll_offset+150*i, 80, 25, font_ver, lang['delete_theme'], theme_list[i][14], theme_list[i][12], theme_list[i][13], theme_list[i][15], theme_list[i][0])
            if i > 1 and i != theme_id:
                if btn_del.draw(in_pos) and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    total_themes.remove(theme_list[i])
                    theme_list.pop(i)
                    config_data["custom_themes"].pop(i-2)
                    return
            if pos[0] > 275 and pos[0] < 275+width and pos[1] > 190+scroll_offset+150*i and pos[1] < 330+scroll_offset+150*i:
                if not test_button._is_hovered(in_pos) and not demo_slider.is_over(in_pos) and not btn_del._is_hovered(in_pos) and pygame.mouse.get_pressed()[0] and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    theme_awaits_setting = i
        # scroll bar
        if len(theme_list) > 3:
            pygame.draw.rect(self.inner_surface, theme[0], (479, 5, 26, 26), 4)
            pygame.draw.polygon(self.inner_surface, theme[0], [[484, 26], [500, 26], [492, 10]])
            pygame.draw.rect(self.inner_surface, theme[0], (479, 419, 26, 26), 4)
            pygame.draw.polygon(self.inner_surface, theme[0], [[484, 425], [500, 425], [492, 440]])
            pygame.draw.rect(self.inner_surface, theme[0], (479, int(36+scroller_pos), 26, scroller_size), 4)
            if in_pos[0] > 479 and in_pos[0] < 505 and pygame.mouse.get_pressed()[0]:
                pygame.event.clear()
                if in_pos[1] > 5 and in_pos[1] < 35:
                    scroll_offset += 30
                if in_pos[1] > 415 and in_pos[1] < 445:
                    scroll_offset -= 30
            if in_pos[0] > 479 and in_pos[0] < 505 and pygame.mouse.get_pressed()[0]:
                if in_pos[1] > 40 and in_pos[1] < 410:
                    pos = pygame.mouse.get_pos()
                    win_pos = [pos[0] - 250, pos[1] - 50]
                    in_pos = [win_pos[0] - 20, win_pos[1] - 135]
                    scroller_pos = in_pos[1] - (20 + scroller_size/2)
                    scroll_offset = -(scroller_pos * scroll_per_pixel)
                    if scroll_offset > 0:
                        scroll_offset = 0
                    elif scroll_offset < (150*(len(theme_list)-3))*-1:
                        scroll_offset = (150*(len(theme_list)-3))*-1
                    self.theme_surface.blit(self.inner_surface, (20, 135))
                    pygame.draw.rect(self.theme_surface, theme[0], (20, 135, 510, 450), 4)
            for event in pygame.event.get(pygame.MOUSEWHEEL):
                scroll_offset += event.y * 50
        else:
            scroll_offset = 0
        # go back button
        back = ui_tools.Button(self.theme_surface, 650, 570, 120, 40, font_d50, lang['btn_back'], theme[14], theme[12], theme[13], theme[15], theme[0])
        if back.draw(win_pos):
            current_ui = source
        # import button
        back = ui_tools.Button(self.theme_surface, 550, 415, 100, 30, font_d50, lang['import'], theme[14], theme[12], theme[13], theme[15], theme[0])
        if back.draw(win_pos):
            new_theme_source = filedialog.askopenfilename(title=lang['choose_theme'], filetypes=[(lang['filetype_dth'], '*.dth'), (lang['filetype_txt'], '*.txt'), (lang['filetype_all'], '*.*')])
            try:
                with open(new_theme_source, 'r', -1, 'utf-8') as new_theme_file:
                    to_add = new_theme_file.readlines()
                    for i in to_add:
                        new_theme = update_theme(ast.literal_eval(i))
                        if new_theme is False:
                            print(lang['err_future_theme'].format(theme=i))
                        else:
                            custom_themes.append(new_theme)
                            theme_list.append(new_theme)
                            config_data["custom_themes"].append(new_theme)
                        total_themes.append(i)
            except:
                pass
        # finish rendering
        self.theme_surface.blit(self.inner_surface, (20, 135))
        pygame.draw.rect(self.theme_surface, theme[0], (20, 135, 510, 450), 4)
        window.blit(self.theme_surface, (250, 50))
        if theme_awaits_setting is not None:
            i = theme_awaits_setting
            theme = theme_list[i]
            config_data["theme_id"] = i
            theme_id = i
            self.__init__(self.surface, False)
            self.init_player_controls(self.game.player_count)
            pygame.event.clear()

    def init_player_controls(self, player_count):
        self.give = []
        self.scroll = []
        if player_count == 2:
            self.give.append(ui_tools.Button(self.surface, 1229, 0, 30, 30, font_scroll, '+', theme[14], theme[12], theme[13], theme[15], theme[0]))
            self.scroll.append(ui_tools.Button(self.surface, 1260, 75, 30, 30, font_scroll, '►', theme[12], theme[20], theme[14], theme[0], None))
            self.scroll.append(ui_tools.Button(self.surface, 0, 75, 30, 30, font_scroll, '◄', theme[12], theme[20], theme[14], theme[0], None))
            self.give.append(ui_tools.Button(self.surface, 1229, 689, 30, 30, font_scroll, '+', theme[14], theme[12], theme[13], theme[15], theme[0]))
            self.scroll.append(ui_tools.Button(self.surface, 1260, 615, 30, 30, font_scroll, '►', theme[12], theme[20], theme[14], theme[0], None))
            self.scroll.append(ui_tools.Button(self.surface, 0, 615, 30, 30, font_scroll, '◄', theme[12], theme[20], theme[14], theme[0], None))
        elif player_count == 3:
            self.give.append(ui_tools.Button(self.surface, 1110, 0, 30, 30, font_scroll, '+', theme[14], theme[12], theme[13], theme[15], theme[0]))
            self.scroll.append(ui_tools.Button(self.surface, 1150, 28, 30, 30, font_scroll, '►', theme[12], theme[20], theme[14], theme[0], None))
            self.scroll.append(ui_tools.Button(self.surface, 100, 28, 30, 30, font_scroll, '◄', theme[12], theme[20], theme[14], theme[0], None))
            self.give.append(ui_tools.Button(self.surface, 60, 590, 30, 30, font_scroll, '+', theme[12], theme[20], theme[14], theme[15], None))
            self.scroll.append(ui_tools.Button(self.surface, 90, 590, 30, 30, font_scroll, '▼', theme[12], theme[20], theme[14], theme[0], None))
            self.scroll.append(ui_tools.Button(self.surface, 30, 590, 30, 30, font_scroll, '▲', theme[12], theme[20], theme[14], theme[0], None))
            self.give.append(ui_tools.Button(self.surface, 1190, 590, 30, 30, font_scroll, '+', theme[12], theme[20], theme[13], theme[15], None))
            self.scroll.append(ui_tools.Button(self.surface, 1220, 590, 30, 30, font_scroll, '▼', theme[12], theme[20], theme[14], theme[0], None))
            self.scroll.append(ui_tools.Button(self.surface, 1160, 590, 30, 30, font_scroll, '▲', theme[12], theme[20], theme[14], theme[0], None))
        else:
            self.give.append(ui_tools.Button(self.surface, 1110, 0, 30, 30, font_scroll, '+', theme[14], theme[12], theme[13], theme[15], theme[0]))
            self.scroll.append(ui_tools.Button(self.surface, 1150, 28, 30, 30, font_scroll, '►', theme[12], theme[20], theme[14], theme[0], None))
            self.scroll.append(ui_tools.Button(self.surface, 100, 28, 30, 30, font_scroll, '◄', theme[12], theme[20], theme[14], theme[0], None))
            self.give.append(ui_tools.Button(self.surface, 60, 590, 30, 30, font_scroll, '+', theme[12], theme[20], theme[14], theme[15], None))
            self.scroll.append(ui_tools.Button(self.surface, 90, 590, 30, 30, font_scroll, '▼', theme[12], theme[20], theme[14], theme[0], None))
            self.scroll.append(ui_tools.Button(self.surface, 30, 590, 30, 30, font_scroll, '▲', theme[12], theme[20], theme[14], theme[0], None))
            self.give.append(ui_tools.Button(self.surface, 1110, 570, 30, 30, font_scroll, '+', theme[14], theme[12], theme[13], theme[15], theme[0]))
            self.scroll.append(ui_tools.Button(self.surface, 1150, 630, 30, 30, font_scroll, '►', theme[12], theme[20], theme[14], theme[0], None))
            self.scroll.append(ui_tools.Button(self.surface, 100, 630, 30, 30, font_scroll, '◄', theme[12], theme[20], theme[14], theme[0], None))
            self.give.append(ui_tools.Button(self.surface, 1190, 590, 30, 30, font_scroll, '+', theme[12], theme[20], theme[14], theme[15], None))
            self.scroll.append(ui_tools.Button(self.surface, 1220, 590, 30, 30, font_scroll, '▼', theme[12], theme[20], theme[14], theme[0], None))
            self.scroll.append(ui_tools.Button(self.surface, 1160, 590, 30, 30, font_scroll, '▲', theme[12], theme[20], theme[14], theme[0], None))

    def game_setup(self):
        # init
        global current_ui
        global scorelim
        global min_write
        global player_size
        global player_count
        global begin_with_double
        global is_game_running
        self.render_menu_gm_sel(False)
        self.error_type = []
        if scorelim < 1:
            self.error_type.append(1)
        if min_write > scorelim:
            self.error_type.append(2)
        if player_size < 1:
            self.error_type.append(3)
        if player_size > 28//player_count:
            self.error_type.append(4)
        if player_count > 4:
            self.error_type.append(5)
        elif player_count < 2:
            self.error_type.append(6)
        error_messages = ['',
                        lang['err_scorelim_not_positive'],
                        lang['err_min_score_too_high'],
                        lang['err_players_should_have_dmn'],
                        lang['err_not_enough_dmns'].format(amount=28//player_count),
                        lang['err_too_much_players'],
                        lang['err_too_little_players']
                        ]
        # render everything AND detect input in a loop
        error_message = ''
        for i in self.error_type:
            error_message = error_message + error_messages[i]
        pos = pygame.mouse.get_pos()
        win_pos = [pos[0] - 250, pos[1] - 50]
        # draw the window
        pygame.draw.rect(self.setup_win, theme[14], (0, 0, 780, 620))
        pygame.draw.rect(self.setup_win, theme[0], (0, 0, 780, 620), 4)
        pygame.draw.rect(self.setup_win, theme[12], (0, 0, 780, 40))
        pygame.draw.rect(self.setup_win, theme[0], (0, 0, 780, 40), 4)
        # draw the texts
        window_title = font_d50.render(lang['setup'], 4, theme[15])
        self.setup_win.blit(window_title, (390 - (window_title.get_width() / 2), 45 - window_title.get_height()))
        txt_score_limit = font_setup.render(lang['scorelim'], 4, theme[15])
        self.setup_win.blit(txt_score_limit, (35, 70))
        txt_min_write = font_setup.render(lang['min_score'], 4, theme[15])
        self.setup_win.blit(txt_min_write, (35, 150))
        txt_player_size = font_setup.render(lang['player_dominoes'], 4, theme[15])
        self.setup_win.blit(txt_player_size, (35, 230))
        txt_begin_with_double = font_setup.render(lang['player_count'], 4, theme[15])
        self.setup_win.blit(txt_begin_with_double, (35, 310))
        txt_begin_with_double = font_setup.render(lang['start_with_double'], 4, theme[15])
        self.setup_win.blit(txt_begin_with_double, (35, 390))
        j = 0
        for i in self.error_type:
            blit(error_messages[i], font_error, (30, 462+j*26), self.setup_win, color=theme[19])
            j += 1
        if self.s_begin_with_double.draw(begin_with_double, win_pos):
            begin_with_double = not begin_with_double
            pos = pygame.mouse.get_pos()
            win_pos = [pos[0] - 250, pos[1] - 50]
        # draw the input boxes
        temp = self.score_lim.draw(text_color=theme[15], bkp_pos=win_pos, hint_color=theme[16])
        if temp is not False:
            scorelim = temp
        temp = self.min_score.draw(text_color=theme[15], bkp_pos=win_pos, hint_color=theme[16])
        if temp is not False:
            min_write = temp
        temp = self.give_players.draw(text_color=theme[15], bkp_pos=win_pos, hint_color=theme[16])
        if temp is not False:
            player_size = temp
        temp = self.player_count.draw(text_color=theme[15], bkp_pos=win_pos, hint_color=theme[16])
        if temp is not False:
            player_count = temp
        # detect input
        if self.btn_setup_back.draw(win_pos):
            current_ui = 'menu_gamemode_select'
        if self.btn_setup_play.draw(win_pos) and pygame.event.get(pygame.MOUSEBUTTONDOWN):
            if self.error_type == []:
                pygame.event.clear()
                if self.gamemode == 'local':
                    ai_count = 0
                elif self.gamemode == 'pva':
                    ai_count = player_count - 1
                elif self.gamemode == 'bot_battle':
                    ai_count = player_count
                self.game = Game({'begin_with_double': begin_with_double, 'score_limit': scorelim, 'players': player_count, 
                                    'give_players': player_size, 'set_type': 6, 'min_score': min_write, 'ai_count': ai_count},
                                    {'side_select': self.handle_lor_dilemma, 'score_upd': self.ren_score_update, 
                                    'next_player': self.next_player})
                self.offsets = [0] * player_count
                self.init_player_controls(player_count)
                self.bazar_empty = player_size == len(self.game.dominoes_set)
                is_game_running = True
                current_ui = 'local_game'
                import_board(boards2[selected_board2][1])
                convert_board()
        
        self.surface.blit(self.setup_win, (250, 50))

    def how_to_play(self):
        global current_ui
        pygame.draw.rect(self.tutorial, theme[14], (0, 0, 500, 450))
        pygame.draw.rect(self.tutorial, theme[0], (0, 0, 500, 450), 4)
        pygame.draw.rect(self.tutorial, theme[12], (0, 0, 500, 40))
        pygame.draw.rect(self.tutorial, theme[0], (0, 0, 500, 40), 4)
        a = lang['tutorial']
        blit_multiline(self.tutorial, a, (10, 45), 490, font_ver, theme[15])
        titl = font_ver.render(lang['how_to_play'], 4, theme[15])
        self.tutorial.blit(titl, (250 - titl.get_width() / 2, 0))
        in_pos = pygame.mouse.get_pos()
        in_pos = [in_pos[0] - 390, in_pos[1] - 150]
        if self.tutorial_back.draw(in_pos) and pygame.event.get(pygame.MOUSEBUTTONDOWN):
            current_ui = 'menu_main'
        self.surface.blit(self.tutorial, (390, 150))

    def select_board_layout(self):
        global boards2
        global boards4
        global selected_board2
        global selected_board4
        global current_ui
        global ren_start_x
        global ren_start_y
        global board_scale
        self.game_ren(None, board_scale, True)

        board = False
        name = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ren_start_x -= 5 * dt
        if keys[pygame.K_RIGHT]:
            ren_start_x += 5 * dt
        if keys[pygame.K_UP]:
            ren_start_y -= 5 * dt
        if keys[pygame.K_DOWN]:
            ren_start_y += 5 * dt
        if keys[pygame.K_KP_PLUS] or keys[pygame.K_PLUS]:
            board_scale *= 1.05
        if keys[pygame.K_KP_MINUS] or keys[pygame.K_MINUS]:
            board_scale /= 1.05
        if keys[pygame.K_ASTERISK] or keys[pygame.K_KP_MULTIPLY]:
            ren_start_x = 640
            ren_start_y = 360
            board_scale = 0.75

        blit(boards2[selected_board2][0], font_error, (110, 20), self.surface, False, theme[15])
        blit(boards4[selected_board4][0], font_error, (110, 60), self.surface, False, theme[15])

        if self.selector_board2.draw(draw_bg=False) and pygame.event.get(pygame.MOUSEBUTTONDOWN):
            self.board_demo = 2
            self.selector_board2.text = '●'
            self.selector_board4.text = '○'
            import_board(boards2[selected_board2][1])
            convert_board()
        elif self.selector_board4.draw(draw_bg=False) and pygame.event.get(pygame.MOUSEBUTTONDOWN):
            self.board_demo = 4
            self.selector_board2.text = '○'
            self.selector_board4.text = '●'
            import_board(boards4[selected_board4][1])
            convert_board()

        if self.board_demo == 2:
            if self.scroll_board2_l.draw(draw_bg=False) and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                selected_board2 -= 1
                if selected_board2 < 0:
                    selected_board2 = len(boards2) - 1
                import_board(boards2[selected_board2][1])
                convert_board()
            elif self.scroll_board2_r.draw(draw_bg=False) and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                selected_board2 += 1
                if selected_board2 > len(boards2) - 1:
                    selected_board2 = 0
                import_board(boards2[selected_board2][1])
                convert_board()
            if selected_board2 > 2:
                if self.delete_board.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    total_boards2.remove(boards2[selected_board2])
                    boards2.pop(selected_board2)
                    config_data['custom_boards2'].pop(selected_board2-3)
                    if selected_board2 > len(boards2) - 1:
                        selected_board2 = len(boards2) - 1
                    import_board(boards2[selected_board2][1])
                    convert_board()
        else:
            if self.scroll_board4_l.draw(draw_bg=False) and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                selected_board4 -= 1
                if selected_board4 < 0:
                    selected_board4 = len(boards4) - 1
                import_board(boards4[selected_board4][1])
                convert_board()
            elif self.scroll_board4_r.draw(draw_bg=False) and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                selected_board4 += 1
                if selected_board4 > len(boards4) - 1:
                    selected_board4 = 0
                import_board(boards4[selected_board4][1])
                convert_board()
            if selected_board4 > 2:
                if self.delete_board.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    total_boards4.remove(boards4[selected_board4])
                    boards4.pop(selected_board4)
                    config_data['custom_boards4'].pop(selected_board4-3)
                    if selected_board4 > len(boards4) - 1:
                        selected_board4 = len(boards4) - 1
                    import_board(boards4[selected_board4][1])
                    convert_board()

        if self.return_from_board.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
            self.surface.fill(theme[12])
            current_ui = current_ui[6:]
            config_data['selected_board2'] = selected_board2
            config_data['selected_board4'] = selected_board4

        if self.import_board.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
            self.surface.blit(darken, (0, 0))
            while board is False:
                board = self.board_import_field.draw(text_color=theme[15], hint_color=theme[16])
                pygame.display.update()
                gametick.tick(60)
                pygame.event.pump()
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    return
            import_board(board)
            convert_board()
            while name is False:
                name = self.board_name.draw(text_color=theme[15], hint_color=theme[16])
                pygame.display.update()
                gametick.tick(60)
                pygame.event.pump()
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    return
            if board[0] == '2':
                boards2.append([name, board])
                config_data['custom_boards2'].append([name, board])
                total_boards2.append([name, board])
                selected_board2 = len(boards2) - 1
                self.board_demo = 2
                self.selector_board2.text = '●'
                self.selector_board4.text = '○'
            elif board[0] == '4':
                boards4.append([name, board])
                config_data['custom_boards4'].append([name, board])
                total_boards4.append([name, board])
                selected_board4 = len(boards4) - 1
                self.board_demo = 4
                self.selector_board2.text = '○'
                self.selector_board4.text = '●'

ui_game = ui(window)
delay = 6

backup_ui == 'none'
def esc_ctrl(current_ui, mouse=False) -> str:
    global backup_ui
    if current_ui == 'pause':
        try:
            save_config()
        except PermissionError:
            print(lang['config_inaccessible'])
        return backup_ui
    elif current_ui == 'settings':
        save_config()
        return 'menu_main'
    elif current_ui == 'theme_settings' or current_ui == 'board_settings':
        return 'settings'
    elif current_ui == 'theme_pause' or current_ui == 'board_pause':
        return 'pause'
    elif current_ui == 'menu_gamemode_select':
        return 'menu_main'
    elif current_ui == 'local_setup':
        return 'menu_gamemode_select'
    elif current_ui == 'menu_main':
        if not mouse:
            return 'settings'
        else:
            return current_ui
    elif current_ui == 'how_to_play':
        return 'menu_main'
    else:
        if not mouse:
            backup_ui = current_ui
            return 'pause'
        else:
            return current_ui

def_ui = time.time() - t
t = time.time()
total_load = time.time() - init_t
## this prints the time it took to start the game. on my computer, it's usually around 0.7 seconds total
##print(f'pygame importing took {pygame_import} seconds')
##print(f'importing the rest of the stuff took {rest_import} seconds')
##print(f'preparing config and display took {conf_setup} seconds')
##print(f'variable setup took {var_init} seconds')
##print(f'config loading took {conf_load} seconds')
##print(f'class definition and initializing took {def_ui} seconds')
##print(f'Total loading time - {total_load} seconds')

t = time.time()
dt = 0.0

def upd_dt():
    global t
    global dt
    dt = time.time() - t
    dt *= 60
    t = time.time()

def save_config(): # implements the fix for future settings not being saved
    try:
        with open('domino_config.json', 'r', -1, 'utf-8') as config:
            try:
                init_data = json.load(config) # load the old data to merge the new one into it
            except:
                init_data = {} # if couldn't load, then it was empty at start
    except OSError:
        init_data = {}
    init_data.update(config_data) # overwrites the old data with the new data while keeping the old one
    init_data['custom_themes'] = total_themes # it contains all the themes ever loaded in the game session, except the deleted ones
    init_data['custom_boards2'] = total_boards2 # same as total_themes
    init_data['custom_boards4'] = total_boards4
    with open('domino_config.json', 'w', -1, 'utf-8') as config:
        config.write(json.dumps(init_data, indent=4, ensure_ascii=False))

while True: # game tick, running at 60 FPS
    upd_dt()

    if bool(pygame.event.peek(pygame.QUIT)):
        save_config()
        pygame.quit()
        print(lang['thanks'])
        exit(0)
    
    if current_splash != 0:
        if delay == 0:
            delay = 3
            for i in range(len(current_splash)):
                if current_splash[i] == '&':
                    splash = list(splash)
                    splash[i] = random_characters[random.randint(0, len(random_characters) - 1)]
                    temp = ''
                    for j in splash:
                        temp += j
                    splash = temp
        else:
            delay -= 1
    if current_ui == "menu_main":
        ui_game.render_main_menu()
    elif current_ui == "pause" or current_ui == 'settings':
        ui_game.settings()
    elif current_ui == "theme_settings":
        ui_game.theme_set_ui('settings')
    elif current_ui == "theme_pause":
        ui_game.theme_set_ui('pause')
    elif current_ui == 'board_settings' or current_ui == 'board_pause':
        ui_game.select_board_layout()
    elif current_ui == "menu_gamemode_select":
        ui_game.render_menu_gm_sel()
    elif current_ui == "local_setup":
        ui_game.game_setup()
    elif current_ui == 'local_init':
        ui_game.game.init()
        current_ui = 'local_game'
    elif current_ui == "local_game":
        ui_game.game_ren(scale=board_scale)
        ui_game.local_game_ctrl()
    elif current_ui == "end":
        ui_game.game_ren(scale=board_scale)
        ui_game.ren_score_update()
    elif current_ui == 'how_to_play':
        ui_game.how_to_play()
    if pygame.event.get(framerate_output):
        current_fps = "FPS: " + str(round(gametick.get_fps()))

    for event in pygame.event.get(pygame.KEYDOWN):
        if event.key == pygame.K_ESCAPE:
            current_ui = esc_ctrl(current_ui)
    if pygame.mouse.get_pressed(num_buttons=5)[3] and pygame.event.get(pygame.MOUSEBUTTONDOWN):
        current_ui = esc_ctrl(current_ui, True)
    
    fpsr = font_fps.render(current_fps, 4, theme[15])
    pygame.draw.rect(window, theme[12], (1210, 695, 70, 25))
    window.blit(fpsr, (1278 - fpsr.get_width(), 722 - fpsr.get_height()))
    pygame.display.update()
    gametick.tick(60)
