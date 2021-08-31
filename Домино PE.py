# init
import pygame
import random
from datetime import date
import tkinter as tk
from tkinter import filedialog
import ast
import json
import assets.ui_tools as ui_tools
import assets.domino as domino
pygame.mixer.pre_init()
pygame.init()

max_fps = 60
gametick = pygame.time.Clock()

icon = pygame.image.load("assets/window.png").convert_alpha()
pygame.display.set_icon(icon)
window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Домино: Python Edition v. Beta 1.7 pre-release 1")
game_version = "v. Beta 1.7-pre1"

useless = tk.Tk()
useless.withdraw()

# variables
current_ui = "menu_main" # defines what kind of image to draw (game/ui/etc.)
debug = False # toggles debug features
game_state = "menu" # defines what is happening right now (gm selection, setup, playing, etc.)
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
            "domino:splashes/namespaced_splash",
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
            "subscribe to pewdiepie",
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
            "This code is awful!"] # the list of existing splashes
random_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/*-+()[]{}абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" # the list of charasters that are used in splashes with randomized characters
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
font_setup = pygame.font.Font('assets/denhome.otf', 90)
font_header = pygame.font.Font('assets/denhome.otf',50)
font_d60 = pygame.font.Font('assets/denhome.otf',   60)
sound_place = pygame.mixer.Sound('assets/place.wav')
sound_error = pygame.mixer.Sound('assets/error.wav')
current_splash = random.choice(splashes)
today = date.today()
if today.strftime("%d%m") == "1408":
    current_splash = "Happy birthday, §§§§!"
elif today.strftime("%d%m") == "1907":
    current_splash = "Happy birthday, WinNT!"
splash = current_splash
visible_scores = [0] * 2 # actually needed here

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
ren_start_x = 0 # gonna reimplement soon
ren_start_y = 0
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
#               meta: author                     20
#               meta: name                       21
#               meta: description                22
#               meta: file format (1 for b1.7)   23
default_themes = [
                    [(0, 0, 0),
                    (0, 0, 0),
                    (255, 255, 255),
                    (255, 0, 0),
                    (255, 128, 0),
                    (242, 242, 0),
                    (0, 255, 0),
                    (0, 255, 255),
                    (0, 0, 255),
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
                    "WinNT",
                    "Стандартная светлая",
                    "Классическая светлая тема",
                    1],
                  
                    [(127, 127, 127),
                    (127, 127, 127),
                    (20, 20, 20),
                    (255, 0, 0),
                    (255, 128, 0),
                    (255, 255, 0),
                    (0, 255, 0),
                    (0, 255, 255),
                    (0, 0, 255),
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
                    "WinNT",
                    "Стандартная тёмная",
                    "Классическая тёмная тема",
                    1]
                 ] # the list of default themes

try:
    with open('domino_config.json', 'r', -1, 'utf-8') as config:
        try:
            config_data = json.load(config)
        except:
            print("File error: error while decoding config file - it may have been corrupted")
            config_data = {"windowed_score": 1, "fastmode": 1, "theme_id": 1, "custom_themes": [], "blink_time": 10}
except OSError:
    print("File error: config file is missing")
    config_data = {"windowed_score": 1, "fastmode": 0, "theme_id": 1, "custom_themes": [], "blink_time": 10}

custom_themes_pre = config_data["custom_themes"]
##for i in range(len(custom_themes)):
##    custom_themes[i] = ast.literal_eval(custom_themes[i])
def update_theme(theme):
    if theme[-1] == 0:
        theme.insert(8, theme[7])
        theme.insert(8, theme[7])
        theme.insert(8, theme[7])
        theme.insert(1, theme[0])
        theme[-1] = 1
        return theme
    elif theme[-1] > 1:
        return False
    else:
        return theme

custom_themes = []
for i in custom_themes_pre:
    theme = update_theme(i)
    if theme is False:
        print(f'Found incompatible theme: {theme}, not loading it')
    else:
        custom_themes.append(theme)
config_data["custom_themes"] = custom_themes

try:
    windowed_score = bool(int(config_data["windowed_score"]))
except:
    print("File error: windowed_score setting not found, setting it to true")
    windowed_score = True
    config_data["windowed_score"] = 1

try:
    fastmode = bool(int(config_data["fastmode"]))
except:
    print("File error: fastmode setting not found, setting it to false")
    fastmode = True
    config_data["fastmode"] = 1

try:
    theme_id = int(config_data["theme_id"])
except:
    print("File error: theme_id setting not found, setting it to 1")
    theme_id = 1
    config_data["theme_id"] = 1

try:
    blink_time = int(config_data["blink_time"])
except:
    print("File error: blink_time setting not found, setting it to 10")
    blink_time = 10
    config_data["blink_time"] = 10

try:
    play_place_sound = bool(int(config_data["place_sound"]))
    sound_place.set_volume(float(play_place_sound))
except:
    print("File error: place_sound setting not found, setting it to true")
    play_place_sound = True
    sound_place.set_volume(1.0)
    config_data["place_sound"] = True

try:
    play_error_sound = int(config_data["error_sound"])
    sound_error.set_volume(float(play_error_sound))
except:
    print("File error: error_sound setting not found, setting it to true")
    play_error_sound = True
    sound_error.set_volume(1.0)
    config_data["error_sound"] = True

theme_list = default_themes + custom_themes
try:
    current_theme = theme_list[theme_id]
except IndexError:
    print("File error: invalid theme selected")
    config_data["theme_id"] = 1
    theme_id = int(config_data["theme_id"])
    current_theme = theme_list[theme_id]

is_theme_updated = False
backup_ui = "menu_main"

framerate_output = pygame.USEREVENT+1
output_fps = pygame.event.Event(framerate_output)
pygame.time.set_timer(framerate_output, 500)
current_fps = "FPS: (wait)"
is_config_open = False # is the config file open

scroll_offset = 0
start_y = -1
start_offset = 0

min_write = 13
player_size = 7
scorelim = 125
begin_with_double = False

test_bool = True

# utility functions
def draw_rect(x1, y1, x2, y2, surface, color_id=8, outline=3, outline_color_id=0):
    if x1 > x2 or y1 > y2:
        raise ValueError("first set of coordinates must represent top left corner")
    dx = x2 - x1
    dy = y2 - y1
    pygame.draw.rect(surface, current_theme[color_id], (x1, y1, dx, dy))
    pygame.draw.rect(surface, current_theme[outline_color_id], (x1, y1, dx, dy), outline)
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
    def __init__(self, settings, ui_hooks, mid_game=None, filename='con'):
        '''A Dominoes PE game'''
        self.double_start = settings['begin_with_double'] # expects a bool
        self.score_limit = settings['score_limit'] # expects an int
        self.player_count = settings['players'] # expects an int
        self.player_init_give = settings['give_players'] # expects an int, at most (1+2+3+...+highest_number_on_domino) / player_count
        self.set_type = settings['set_type'] + 1
        self.ai_count = settings['ai_count'] # expects an int, at most player_count
        self.dominoes_set = [] # expects an int
        for i in range(self.set_type):
            for j in range(self.set_type):
                if not str(j) + str(i) in self.dominoes_set:
                    self.dominoes_set.append(str(i) + str(j))
        self.min_score = settings['min_score'] # expects an int
        self.save_file_name = filename # expects a string
        self.save_data = None

        if mid_game: # a set of values that appear after starting the game
            self.board = mid_game['board']['dominoes'] # expects a list of lists of ints
            self.board_inv = mid_game['board']['inversion'] # expects a list of lists of bools
            self.center = mid_game['board']['dmn0'] # expects an int

            self.ends = []
            self.ability = []
            for i in range(len(self.board)):
                self.ability.append([])
                if self.board_inv[i][-1]:
                    self.ends.append(self.dominoes_set[self.board[i][-1]][1])
                else:
                    self.ends.append(self.dominoes_set[self.board[i][-1]][0])

            self.bazar = mid_game['player_data']['bazar'] # expects a list of ints  ## i still don't know how it's called in English
            self.player_inv = mid_game['player_data']['inventories'] # expects a list of lists of ints
            self.player_scores = mid_game['player_data']['scores'] # expects a list of floats
            self.player_victories = mid_game['player_data']['victories'] # expects a list of ints
            self.player_names = mid_game['player_data']['names'] # expects a list of strings
            self.current_move = mid_game['current_move'] # expects an int, at most player_count

            self.game_stage = mid_game['stage'] # expects 'beginning' or 'game'
            self.game_number = mid_game['game_number'] # expects an int
            self.restarted_from = mid_game['last_restart'] # expects 'battle' or 'game'
        else:
            self.game_number = 0
            self.restarted_from = 'game'
            self.player_scores = [0] * self.player_count
            self.player_victories = [0] * self.player_count
            self.player_names = ['Player'] * self.player_count
            
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
            self.current_move = random.randint(1, self.player_count)
        elif self.restarted_from == 'game':
            self.player_scores = [0 for i in range(self.player_count)]
            if self.double_start:
                self.enforced_domino = 0
                for i in self.player_inv:
                    for j in range(self.set_type):
                        k = self.dominoes_set.index(str(j) * 2) 
                        if k in i and j == self.game_number % 7 + 1:
                            self.current_move = self.player_inv.index(i) + 1
                            self.enforced_domino = k
                            break
            if self.current_move == 0:
                self.current_move = random.randint(1, self.player_count)
                self.enforced_domino = None


    def give_player(self, player: int) -> bool:
        '''Give a domino to a player from the bazar and return the success value'''
        try:
            choice = random.choice(self.bazar)
        except:
            if player < self.player_count - self.ai_count:
                print(f"Can't give a domino to player {player} - bazar is empty!")
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
                    if str(i) in dmn:
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
        '''Updates the players' scoers and returns the actions (difference, victories)'''
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
                        self.next_player(self.current_move, self.player_count, fastmode)
                        self.incr_player()
                        return True
                    else:
                        return False
                else:
                    self.center = self.player_inv[source-1][id]
                    self.player_inv[source-1].pop(id)
                    self.ends = [targ_dmn_type[0], targ_dmn_type[1]]
                    self.game_stage = 'game'
                    self.next_player(self.current_move, self.player_count, fastmode)
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
                    if side == 'l':
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
                self.next_player(self.current_move, self.player_count, fastmode)
                self.incr_player()
                return True
        else:
            return False

class ui: # the game's GUI
    def __init__(self, surface, init=True):
        self.surface = surface

        self.btn_play = ui_tools.Button(self.surface, 480, 390, 320, 55, font_d60, "Играть", current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])
        self.btn_settings = ui_tools.Button(self.surface, 480, 455, 320, 55, font_d60, "Настройки", current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])
        self.btn_how_to_play = ui_tools.Button(self.surface, 480, 520, 155, 55, font_d60, "Как играть", current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])
        self.btn_exit = ui_tools.Button(self.surface, 645, 520, 155, 55, font_d60, 'Выйти', current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])

        self.btn_gm_local = ui_tools.Button(self.surface, 250, 400, 300, 55, font_d60, "Локальная игра", current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])
        self.btn_gm_internet = ui_tools.Button(self.surface, 250, 500, 300, 55, font_d60, "В разработке...", current_theme[14], current_theme[12], current_theme[13], current_theme[16], current_theme[0])
        self.btn_gm_pva = ui_tools.Button(self.surface, 730, 400, 300, 55, font_d60, "Одиночная игра", current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])
        self.btn_gm_ava = ui_tools.Button(self.surface, 730, 500, 300, 55, font_d60, "Битва ботов", current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])
        self.btn_gm_back = ui_tools.Button(self.surface, 490, 600, 300, 55, font_d60, "Назад", current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])

        self.btn_give_1 = ui_tools.Button(self.surface, 600, 0, 80, 20, font_fps, "Нету!", current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])
        self.btn_give_2 = ui_tools.Button(self.surface, 600, 700, 80, 20, font_fps, "Нету!", current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])

        self.btn_next_battle = ui_tools.Button(self.surface, 540, 420, 200, 40, font_d60, "Дальше", current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])

        self.btn_next_player = ui_tools.Button(self.surface, 540, 500, 200, 50, font_d60, "OK", current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])

        self.ren_domino = domino.Domino(self.surface, current_theme[0], current_theme[2], current_theme[1], current_theme[3:12])

        # sliders in settings menu
        self.test_slider = ui_tools.Switch(self.surface, 640, 360, 86, 36, 4, current_theme[14], current_theme[12], current_theme[0], current_theme[18], current_theme[19]) # for tests

        self.s_windowed_score = ui_tools.Switch(self.surface, 1145, 145, 86, 36, 4, current_theme[14], current_theme[12], current_theme[0], current_theme[18], current_theme[19])
        self.s_fastmode = ui_tools.Switch(self.surface, 1145, 215, 86, 36, 4, current_theme[14], current_theme[12], current_theme[0], current_theme[18], current_theme[19])
        self.s_place_sound = ui_tools.Switch(self.surface, 1145, 285, 86, 36, 4, current_theme[14], current_theme[12], current_theme[0], current_theme[18], current_theme[19])
        self.s_error_sound = ui_tools.Switch(self.surface, 1145, 355, 86, 36, 4, current_theme[14], current_theme[12], current_theme[0], current_theme[18], current_theme[19])

        self.setup_win = pygame.Surface((780, 620))
        self.s_begin_with_double = ui_tools.Switch(self.setup_win, 664, 337, 86, 36, 4, current_theme[14], current_theme[12], current_theme[0], current_theme[18], current_theme[19])

        if init:
            self.game = Game({'begin_with_double': False, 'score_limit': 100, 'players': 2, 'give_players': 7, 'set_type': 6, 'min_score': 0, 'ai_count': 0},
                             {'side_select': self.handle_lor_dilemma, 'score_upd': self.ren_score_update, 'next_player': self.next_player})
        self.left_side = self.game.get_board(1, False)
        self.left_is_inv = self.game.get_board(1, True)
        self.right_side = self.game.get_board(2, False)
        self.right_is_inv = self.game.get_board(2, True)

        # other smart stuff in settings
        self.go_set_theme = ui_tools.Hyperlink(self.surface, 40, 476, '§nНастройки темы...', font_d60, current_theme[15])
        self.go_menu = ui_tools.Hyperlink(self.surface, 50, 66, '§n< Назад', font_d60, current_theme[15])
        self.exit_game = ui_tools.Button(self.surface, 1040, 630, 200, 50, font_d60, 'Выйти в меню', current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])
        self.blink_time = ui_tools.TextField(self.surface, 1100, 411, font_d60, 130, 50, blink_time, '','string',
                                               current_theme[15], current_theme[16], current_theme[12])

        self.theme_surface = pygame.Surface((780, 620))
        self.inner_surface = pygame.Surface((510, 450))

        self.tutorial = pygame.Surface((500, 450))

        self.tutorial_back = ui_tools.Button(self.surface, 175, 390, 150, 50, self.tutorial, 'Назад')

        self.score_lim = ui_tools.TextField(self.setup_win, 580, 85, font_gm_sel, 170, 65, '125', '', 'int',
                                              current_theme[15], current_theme[16], current_theme[12])
        self.min_score = ui_tools.TextField(self.setup_win, 580, 165, font_gm_sel, 170, 65, '13', '', 'int',
                                              current_theme[15], current_theme[16], current_theme[12])
        self.give_players = ui_tools.TextField(self.setup_win, 580, 245, font_gm_sel, 170, 65, '7', '', 'int',
                                                 current_theme[15], current_theme[16], current_theme[12])

        self.btn_setup_play = ui_tools.Button(self.setup_win, 590, 550, 170, 50, font_d50, 'Начать игру', current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])
        self.btn_setup_back = ui_tools.Button(self.setup_win, 410, 550, 170, 50, font_d50, 'Назад', current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])
        self.tutorial_back = ui_tools.Button(self.tutorial, 165, 390, 170, 50, font_d50, 'Назад', current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])

    # render functions
    def render_main_menu(self, btn=True):
        global current_ui
        global game_version
        global is_rendered
        global test_bool
        global backup_ui
        self.surface.fill(current_theme[12])
        blit('Домино', font_title, (640, 0), self.surface, True, current_theme[15])
        blit('Python Edition', font_pe, (640, 210), self.surface, True, current_theme[15])
        ren_splash = font_splash.render(splash, 4, current_theme[17])
        ren_splash = pygame.transform.rotate(ren_splash, 30)
        self.surface.blit(ren_splash, (900 - (ren_splash.get_width() / 2), 210 - (ren_splash.get_height() / 2)))
        version = font_ver.render(game_version, 4, current_theme[15])
        self.surface.blit(version, (4, 720 - version.get_height()))
        if btn:
            if self.btn_play.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                current_ui = "menu_gamemode_select"
                pygame.event.clear()
            # settings button
            if self.btn_settings.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                backup_ui = "menu_main"
                current_ui = "settings"
            # quit button
            if self.btn_exit.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                with open("domino_config.json", 'w', -1, 'utf-8') as config:
                    config.write(json.dumps(config_data, indent=4, ensure_ascii=False))
                pygame.quit()
                print("Thanks for playing!")
                exit(0)
            # how to play button
            if self.btn_how_to_play.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                current_ui = 'how_to_play'

    def render_menu_gm_sel(self, btn=True):
        global current_ui
        global game_version
        global is_rendered
        self.render_main_menu(False)
        # inactive button
        self.btn_gm_internet.draw(click_state=2)
        # texts
        gm_sel = font_gm_sel.render("Выберите режим игры:", 4, current_theme[15])
        self.surface.blit(gm_sel, (640 - (gm_sel.get_width() / 2), 300 - (gm_sel.get_height() / 2)))
        is_rendered = True
        if self.btn_gm_local.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
            current_ui = "local_setup"
            self.gamemode = "local"
        # back button
        if self.btn_gm_back.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
            current_ui = "menu_main"
        # gamemode = pva button
        if self.btn_gm_pva.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
            current_ui = "local_setup"
            self.gamemode = "pva"
        # gamemode = bot_battle button
        if self.btn_gm_ava.draw() and pygame.event.get(pygame.MOUSEBUTTONDOWN):
            current_ui = "local_setup"
            self.gamemode = "bot_battle"

    def game_ren(self, custom_board=None):
        self.surface.fill(current_theme[12])
        if not custom_board:
            left_side = self.game.get_board(1, False)
            right_side = self.game.get_board(2, False)
            left_is_inv = self.game.get_board(1, True)
            right_is_inv = self.game.get_board(2, True)
        else:
            left_side, right_side, left_is_inv, right_is_inv = custom_board
        dmn0 = self.game.get_board(0, False)
        p1 = self.game.get_player(1)['inv']
        p2 = self.game.get_player(2)['inv']
        ds = self.game.dominoes_set
        # render the dominoes
        for i in range(len(left_side)):
            inv = (ren_dmn_left_is_inv[i] or left_is_inv[i]) and not (ren_dmn_left_is_inv[i] and left_is_inv[i])
            self.ren_domino.draw(ds[left_side[i]], (ren_dmn_left_start_x[i], ren_dmn_left_start_y[i]), ren_dmn_left_is_vert[i], inv)
        for i in range(len(right_side)):
            inv = (ren_dmn_right_is_inv[i] or right_is_inv[i]) and not (ren_dmn_right_is_inv[i] and right_is_inv[i])
            self.ren_domino.draw(ds[right_side[i]], (ren_dmn_right_start_x[i], ren_dmn_right_start_y[i]), ren_dmn_right_is_vert[i], inv)
        if dmn0:
            self.ren_domino.draw(ds[dmn0], (608, 300), True, False)
        pygame.draw.rect(self.surface, current_theme[0], (20, 580, 1239, 119))
        pygame.draw.rect(self.surface, current_theme[12], (24, 584, 1230, 111))
        pygame.draw.rect(self.surface, current_theme[0], (20, 20, 1239, 119))
        pygame.draw.rect(self.surface, current_theme[12], (24, 24, 1230, 111))
        for i in range(len(p1)):
            if self.game.current_move < 2 or not self.gamemode == "local":
                self.ren_domino.draw(ds[self.game.get_player(1)['inv'][i]], (20+(i*59), 20), True, False)
            else:
                pygame.draw.rect(self.surface, current_theme[0], (20+((i)*59), 20, 63, 119))
                pygame.draw.rect(self.surface, current_theme[2], (24+((i)*59), 24, 55, 111))
        for i in range(len(p2)):
            if (self.game.current_move == 2 and self.gamemode == "local") or self.game.current_move == 0 or self.gamemode == "bot_battle":
                self.ren_domino.draw(ds[self.game.get_player(2)['inv'][i]], (20+(i*59), 580), True, False)
            else:
                pygame.draw.rect(self.surface, current_theme[0], (20+((i)*59), 580, 63, 119))
                pygame.draw.rect(self.surface, current_theme[2], (24+((i)*59), 584, 55, 111))
        playerdata1 = font_pd.render((self.game.get_player(1)['name'] + " - " + str(self.game.get_player(1)['score']) + " очков, " + str(self.game.get_player(2)['victories']) + " побед"), 4, current_theme[15], current_theme[13])
        self.surface.blit(playerdata1, (24, 21-playerdata1.get_height()))
        pygame.draw.rect(self.surface, current_theme[0], (21, 1, playerdata1.get_width()+5, 21), 4)
        playerdata2 = font_pd.render((self.game.get_player(2)['name'] + " - " + str(self.game.get_player(2)['score']) + " очков, " + str(self.game.get_player(2)['victories']) + " побед"), 4, current_theme[15], current_theme[13])
        self.surface.blit(playerdata2, (24, 717-playerdata2.get_height()))
        pygame.draw.rect(self.surface, current_theme[0], (21, 697, playerdata2.get_width()+5, 21), 4)

    def local_game_ctrl(self):
        if self.game.is_ai(self.game.current_move):
            self.ai(self.game.current_move)
            return
        self.btn_give_1.draw()
        self.btn_give_2.draw()
        if bool(pygame.event.get(pygame.MOUSEBUTTONDOWN)):
            if self.btn_give_1._is_hovered() and self.game.current_move == 1:
                self.game.give_player(1)
            if self.btn_give_2._is_hovered() and self.game.current_move == 2:
                self.game.give_player(2)
            # detect the clicked domino
            lpos = pygame.mouse.get_pos()
            mouse_is_over = [0, 0]
            if lpos[0] > 26 and lpos[0] < 1252 and lpos[1] > 24 and lpos[1] < 134:
                mouse_is_over[0] = 1
                mouse_is_over[1] = int((lpos[0] - 26) / 59) + 1
    ##                if debug:
                # print("Player", mouse_is_over[0], "domino", mouse_is_over[1])
            elif lpos[0] > 26 and lpos[0] < 1252 and lpos[1] > 584 and lpos[1] < 704:
                mouse_is_over[0] = 2
                mouse_is_over[1] = int((lpos[0] - 26) / 59) + 1
            else:
                mouse_is_over = [0, 0]
    ##                if debug:
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
                        print("Player error: you are trying to use nothing")
                        sound_error.play()
                    error = 1
            if self.game.current_move != mouse_is_over[0] and mouse_is_over[0] != 0:
                if self.game.is_ai(mouse_is_over[0]):
                    print("Player error: it's not your turn")
                    sound_error.play()
                error = 1
            if error == 0:
                if not self.game.place(mouse_is_over[1] - 1, self.game.current_move) and not self.game.is_ai(mouse_is_over[0]):
                    print("Player error - cannot use that domino")
                    sound_error.play()
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
        self.game_ren()
        # init
        if windowed_score:
            # render base
            pygame.draw.rect(self.surface, current_theme[13], (50, 200, 540, 320))
            pygame.draw.rect(self.surface, current_theme[13], (690, 200, 540, 320))
            pygame.draw.rect(self.surface, current_theme[0], (50, 200, 540, 320), 4)
            pygame.draw.rect(self.surface, current_theme[0], (690, 200, 540, 320), 4)
            # render text
            score1 = font_score.render(str(scores_old[0]), 4, current_theme[15])
            self.surface.blit(score1, (320 - (score1.get_width()/2), 360 - (score1.get_height()/2)))
            score2 = font_score.render(str(scores_old[1]), 4, current_theme[15])
            self.surface.blit(score2, (960 - (score2.get_width()/2), 360 - (score1.get_height()/2)))
            # increase score - init
            score_diff = []
            for i in range(len(scores_old)):
                score_diff.append(scores_new[i] - scores_old[i])
            incr_count = max(score_diff)
            delay = 50
            if 0 < incr_count < 10:
                delay = 500 / incr_count
            elif incr_count == 0:
                delay = 0
            p1_score = scores_old[0]
            p2_score = scores_old[1]
            # increase score
            for i in range(incr_count):
                # ask for input to prevent "not responding" message
                if bool(pygame.event.get(pygame.K_SPACE)):
                    print(":)")
                # wait for a while
                pygame.time.delay(int(delay))
                # add 1 to each player
                if score_diff[0]:
                    p1_score += 1
                    score_diff[0] -= 1
                if score_diff[1]:
                    p2_score += 1
                    score_diff[1] -= 1
                    # render base
                pygame.draw.rect(self.surface, current_theme[13], (50, 200, 540, 320))
                pygame.draw.rect(self.surface, current_theme[13], (690, 200, 540, 320))
                pygame.draw.rect(self.surface, current_theme[0], (50, 200, 540, 320), 4)
                pygame.draw.rect(self.surface, current_theme[0], (690, 200, 540, 320), 4)
                # render text
                score1 = font_score.render(str(p1_score), 4, current_theme[15])
                self.surface.blit(score1, (320 - (score1.get_width()/2), 360 - (score1.get_height()/2)))
                score2 = font_score.render(str(p2_score), 4, current_theme[15])
                self.surface.blit(score2, (960 - (score2.get_width()/2), 360 - (score1.get_height()/2)))
                # finish frame
                pygame.display.update()
                gametick.tick(60)
            if vict:
                for i in range(blink_time):
                    # ask for input to prevent "not responding" message
                    if bool(pygame.event.get(pygame.K_SPACE)):
                        print(":)")
                    # render base
                    pygame.draw.rect(self.surface, current_theme[19 - int(0 in vict)], (50, 200, 540, 320))
                    pygame.draw.rect(self.surface, current_theme[19 - int(1 in vict)], (690, 200, 540, 320)) # what have i done
                    pygame.draw.rect(self.surface, current_theme[0], (50, 200, 540, 320), 4)
                    pygame.draw.rect(self.surface, current_theme[0], (690, 200, 540, 320), 4)
                    # render text
                    score1 = font_score.render(str(p1_score), 4, current_theme[15])
                    self.surface.blit(score1, (320 - (score1.get_width()/2), 360 - (score1.get_height()/2)))
                    score2 = font_score.render(str(p2_score), 4, current_theme[15])
                    self.surface.blit(score2, (960 - (score2.get_width()/2), 360 - (score1.get_height()/2)))
                    # finish frame
                    pygame.display.update()
                    gametick.tick(60)
                    # wait
                    pygame.time.delay(500)
                    # render base
                    pygame.draw.rect(self.surface, current_theme[13], (50, 200, 540, 320))
                    pygame.draw.rect(self.surface, current_theme[13], (690, 200, 540, 320))
                    pygame.draw.rect(self.surface, current_theme[0], (50, 200, 540, 320), 4)
                    pygame.draw.rect(self.surface, current_theme[0], (690, 200, 540, 320), 4)
                    # render text
                    score1 = font_score.render(str(p1_score), 4, current_theme[15])
                    self.surface.blit(score1, (320 - (score1.get_width()/2), 360 - (score1.get_height()/2)))
                    score2 = font_score.render(str(p2_score), 4, current_theme[15])
                    self.surface.blit(score2, (960 - (score2.get_width()/2), 360 - (score1.get_height()/2)))
                    # finish frame
                    pygame.display.update()
                    gametick.tick(60)
                    # wait
                    pygame.time.delay(500)
        
        # END DATA
        # draw a fancy window
        pygame.draw.rect(self.surface, current_theme[14], (440, 250, 400, 220))
        pygame.draw.rect(self.surface, current_theme[0], (440, 250, 400, 220), 4)
        pygame.draw.rect(self.surface, current_theme[12], (440, 250, 400, 40))
        pygame.draw.rect(self.surface, current_theme[0], (440, 250, 400, 40), 4)
        text_title = font_ver.render("Конец игры", 4, current_theme[15])
        text_p1_name = font_gm_sel.render(self.game.get_player(1)['name'], 4, current_theme[15])
        text_p2_name = font_gm_sel.render(self.game.get_player(2)['name'], 4, current_theme[15])
        text_p1_score = font_gm_sel.render(str(scores_new[0] - scores_old[0]), 4, current_theme[15])
        text_p2_score = font_gm_sel.render(str(scores_new[1] - scores_old[1]), 4, current_theme[15])
        self.surface.blit(text_p1_name, (450, 290))
        self.surface.blit(text_p2_name, (450, 340))
        self.surface.blit(text_p1_score, (830 - text_p1_score.get_width(), 290))
        self.surface.blit(text_p2_score, (830 - text_p2_score.get_width(), 340))
        self.surface.blit(text_title, (640 - (text_title.get_width() / 2), 270 - (text_title.get_height() / 2)))
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
            if random.randint(0, 1):
                return 'r'
            else:
                return 'l'
        is_solved = False
        
        while not is_solved:
            ren_left_side = board[0][0].copy()
            ren_left_is_inv = board[1][0].copy()
            ren_right_side = board[0][1].copy()
            ren_right_is_inv = board[1][1].copy()
            pos = pygame.mouse.get_pos()
            if pos[1] < 360:
                ren_left_side.append(dmn)
                if self.game.dominoes_set[dmn - 1][0] == str(self.game.ends[0]):
                    ren_left_is_inv.append(True)
                else:
                    ren_left_is_inv.append(False)
                self.game_ren([ren_left_side, ren_right_side, ren_left_is_inv, ren_right_is_inv])
                hint_use = font_gm_sel.render("Нажмите, чтобы поставить", 4, current_theme[15], current_theme[12])
                pygame.draw.rect(self.surface, current_theme[0], (636 - (hint_use.get_width() / 2), 76 - (hint_use.get_height() / 2), hint_use.get_width() + 8, hint_use.get_height() + 8))
                self.surface.blit(hint_use, (640 - (hint_use.get_width() / 2), 80 - (hint_use.get_height() / 2)))
                pygame.display.update()
                gametick.tick(60)
                if bool(pygame.event.get(pygame.MOUSEBUTTONDOWN)):
                    is_solved = True
                    return 'l'
                ren_left_side = board[0][0].copy()
            else:
                ren_right_side.append(dmn)
                if self.game.dominoes_set[int(dmn) - 1][0] == str(self.game.ends[0]):
                    ren_right_is_inv.append(False)
                else:
                    ren_right_is_inv.append(True)
                self.game_ren([ren_left_side, ren_right_side, ren_left_is_inv, ren_right_is_inv])
                hint_use = font_gm_sel.render("Нажмите, чтобы поставить", 4, current_theme[15], current_theme[12])
                pygame.draw.rect(self.surface, current_theme[0], (636 - (hint_use.get_width() / 2), 76 - (hint_use.get_height() / 2), hint_use.get_width() + 8, hint_use.get_height() + 8))
                self.surface.blit(hint_use, (640 - (hint_use.get_width() / 2), 80 - (hint_use.get_height() / 2)))
                pygame.display.update()
                gametick.tick(60)
                if bool(pygame.event.get(pygame.MOUSEBUTTONDOWN)):
                    is_solved = True
                    return 'r'
                ren_right_side = board[0][1].copy()

    def next_player(self, current_move, player_count, fastmode):
        if not fastmode:
            new_player = current_move + 1
            if new_player > player_count:
                new_player = 1
            self.game_ren()
            # draw a fancy window
            pygame.draw.rect(self.surface, current_theme[10], (350, 150, 580, 420))
            pygame.draw.rect(self.surface, current_theme[0], (350, 150, 580, 420), 4)
            pygame.draw.rect(self.surface, current_theme[8], (350, 150, 580, 40))
            pygame.draw.rect(self.surface, current_theme[0], (350, 150, 580, 40), 4)
            # draw exclamation sign
            pygame.draw.circle(self.surface, current_theme[0], (640, 270), 70, 4)
            pygame.draw.ellipse(self.surface, current_theme[0], [627, 215, 26, 20])
            pygame.draw.polygon(self.surface, current_theme[0], [[627, 225], [638, 297], [642, 297], [653, 225]])
            pygame.draw.circle(self.surface, current_theme[0], [640, 315], 9)
            # draw all the texts
            window_title = font_header.render("Ожидание след. игрока", 4, current_theme[15])
            self.surface.blit(window_title, (355, 170 - (window_title.get_height() / 2)))
            line1 = font_gm_sel.render(f"Игрок {new_player}, ваш ход!", 4, current_theme[15])
            sl1 = font_gm_sel.size(f"Игрок {new_player}, ваш ход!")
            self.surface.blit(line1, (640 - sl1[0]/2, 360 - sl1[1]/2))
            line2 = font_gm_sel.render("Нажмите клавишу Пробел или кноп-", 4, current_theme[15])
            sl2 = font_gm_sel.size("Нажмите клавишу Пробел или кноп-")
            line3 = font_gm_sel.render("ку ОК и сделайте ход.", 4, current_theme[15])
            sl3 = font_gm_sel.size("ку ОК и сделайте ход.")
            self.surface.blit(line2, (640 - sl2[0]/2, 410 - sl2[1]/2))
            self.surface.blit(line3, (640 - sl3[0]/2, 460 - sl3[1]/2))
            done = False
            while not done:
                if self.btn_next_player.draw() or pygame.key.get_pressed()[pygame.K_SPACE]:
                    return
                pygame.display.update()
                gametick.tick(60)
        else:
            return

    def settings(self):
        ## init
        global font_gm_sel
        global windowed_score
        global fastmode
        global current_theme
        global current_ui
        global is_rendered
        global is_theme_updated
        global backup_ui
        global config
        global config_data
        global is_config_open
        global blink_time
        global play_place_sound
        global play_error_sound
        pygame.draw.rect(self.surface, current_theme[14], (25, 25, 1230, 670))
        pygame.draw.rect(self.surface, current_theme[0], (25, 25, 1230, 670), 4)
        pygame.draw.rect(self.surface, current_theme[12], (25, 25, 1230, 40))
        pygame.draw.rect(self.surface, current_theme[0], (25, 25, 1230, 40), 4)
        ## draw the sliders
        # show scores in the two windows
        if self.s_windowed_score.draw(windowed_score):
            windowed_score = not windowed_score
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
        # change the theme ui_tools
        if self.go_set_theme.draw():
            current_ui = "theme_" + current_ui
        # exit ui_tools
        if self.go_menu.draw():
            current_ui = backup_ui
            is_rendered = False
        ## the option descriptions
        opt1 = font_gm_sel.render("Отображать изменение счёта в отдельных окнах", 4, current_theme[15])
        self.surface.blit(opt1, (40, 126))
        opt3 = font_gm_sel.render("Быстрый режим", 4, current_theme[15])
        self.surface.blit(opt3, (40, 196))
        opt4 = font_gm_sel.render("Звук установки доминошки", 4, current_theme[15])
        self.surface.blit(opt4, (40, 266))
        opt5 = font_gm_sel.render("Звук ошибки", 4, current_theme[15])
        self.surface.blit(opt5, (40, 336))
        blit('Время отображения побед/поражений игроков', font_gm_sel, (40, 396), self.surface, color=current_theme[15])
        if current_ui == "pause":
            titl = font_header.render("Игра на паузе", 4, current_theme[15]) # typo intentional
            # back to main menu ui_tools
            if self.exit_game.draw():
                current_ui = 'menu_main'
        else:
            titl = font_header.render("Настройки", 4, current_theme[15])
        self.surface.blit(titl, (640 - titl.get_width() / 2, 45 - titl.get_height() / 2))
        # score blinking time
        temp = self.blink_time.draw(text_color=current_theme[15])
        if temp is not False:
            blink_time = temp
            config_data["blink_time"] = blink_time

    def ai(self, whoami=2):
        pygame.time.delay(50)
        inv = self.game.get_player(whoami)['inv']
        for i in range(len(inv)):
            pygame.time.delay(50)
            self.game_ren()
            pygame.display.update()
            gametick.tick(60)
            # print(f'[DEBUG] Trying to place dmn #{i} of {whoami}')
            if self.game.current_move == whoami and self.game.place(i, whoami):
                # print(f'[DEBUG] Succesful place of dmn #{i} of {whoami}')
                return
        while True:
            pygame.time.delay(50)
            self.game_ren()
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
        global current_theme
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
        pygame.draw.rect(self.theme_surface, current_theme[14], (0, 0, 780, 620))
        pygame.draw.rect(self.theme_surface, current_theme[0], (0, 0, 780, 620), 4)
        pygame.draw.rect(self.theme_surface, current_theme[12], (0, 0, 780, 40))
        pygame.draw.rect(self.theme_surface, current_theme[0], (0, 0, 780, 40), 4)
        title123 = font_header.render("Выбор темы", 4, current_theme[15])
        self.theme_surface.blit(title123, (390 - title123.get_width() / 2, 20 - title123.get_height() / 2))
        # this is where the fun begins - we'll have to make a big nice ui which is very difficult
        # let's start with the texts:
        title123 = font_gm_sel.render("Выберите тему из списка:", 4, current_theme[15])
        self.theme_surface.blit(title123, (20, 50))
        title123 = font_ver.render("Выбранная тема:", 4, current_theme[15])
        self.theme_surface.blit(title123, (550, 160))
        title123 = font_ver.render("Больше тем:", 4, current_theme[15])
        self.theme_surface.blit(title123, (550, 370))
        title123 = font_ver.render(current_theme[21], 4, current_theme[15])
        self.theme_surface.blit(title123, (550, 200))
        blit_multiline(self.theme_surface, current_theme[20] + ' · ' + current_theme[22], (550, 240), 720, font_fps, current_theme[15])
        pos = pygame.mouse.get_pos()
        win_pos = [pos[0] - 250, pos[1] - 50]
        self.inner_surface.fill(current_theme[14])
        # now it's time to make the scrollable list...
        # let's start with the list itself
        for i in range(len(theme_list)):
            if len(theme_list) > 3:
                width = 470
            else:
                width = 500
            in_pos = [win_pos[0] - 20, win_pos[1] - 135]
            start_y = in_pos[1]
            pygame.draw.rect(self.inner_surface, theme_list[i][12], (5, 5+scroll_offset+150*i, width, 140))
            pygame.draw.rect(self.inner_surface, theme_list[i][0], (5, 5+scroll_offset+150*i, width, 140), 3)
            title123 = font_ver.render(theme_list[i][21], 4, theme_list[i][11])
            self.inner_surface.blit(title123, (10, 5+scroll_offset+150*i))
            title123 = font_fps.render(theme_list[i][20] + ' · ' + theme_list[i][22], 4, theme_list[i][15])
            self.inner_surface.blit(title123, (10, 37+scroll_offset+150*i))
            # now i have to render the demo thing...
            example_domino = domino.Domino(self.inner_surface, theme_list[i][0], theme_list[i][2], theme_list[i][1], theme_list[i][3:12])
            example_domino.draw('12', (12, 70+scroll_offset+150*i))
            example_domino.draw('34', (127, 70+scroll_offset+150*i))
            example_domino.draw('56', (242, 70+scroll_offset+150*i))
            demo_slider = ui_tools.Switch(self.inner_surface, 365, 67+scroll_offset+150*i, 86, 36, 4, theme_list[i][13], theme_list[i][14],
                                        theme_list[i][0], theme_list[i][18], theme_list[i][19])
            demo_slider.draw(test_bool, in_pos)
            if pygame.event.peek(pygame.MOUSEBUTTONDOWN) and demo_slider.is_over(in_pos):
                test_bool = not test_bool
                pygame.event.clear()
            test_button = ui_tools.Button(self.inner_surface, 370, 112+scroll_offset+150*i, 80, 25, font_ver, '=)', theme_list[i][14], theme_list[i][12], theme_list[i][13], theme_list[i][15], theme_list[i][0])
            test_button.draw(in_pos)
            btn_del = ui_tools.Button(self.inner_surface, 370, 15+scroll_offset+150*i, 80, 25, font_ver, 'Удалить', theme_list[i][14], theme_list[i][12], theme_list[i][13], theme_list[i][15], theme_list[i][0])
            if i > 1 and i != theme_id:
                if btn_del.draw(in_pos) and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    theme_list.pop(i)
                    config_data["custom_themes"].pop(i-2)
                    return
            if pos[0] > 275 and pos[0] < 275+width and pos[1] > 190+scroll_offset+150*i and pos[1] < 330+scroll_offset+150*i:
                if not test_button._is_hovered(in_pos) and not demo_slider.is_over(in_pos) and not btn_del._is_hovered(in_pos) and pygame.mouse.get_pressed()[0] and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    theme_awaits_setting = i
        # now let's make the "scroller"
        if len(theme_list) > 3:
            pygame.draw.rect(self.inner_surface, current_theme[0], (479, 5, 26, 26), 4)
            pygame.draw.polygon(self.inner_surface, current_theme[0], [[484, 26], [500, 26], [492, 10]])
            pygame.draw.rect(self.inner_surface, current_theme[0], (479, 419, 26, 26), 4)
            pygame.draw.polygon(self.inner_surface, current_theme[0], [[484, 425], [500, 425], [492, 440]])
            pygame.draw.rect(self.inner_surface, current_theme[0], (479, int(36+scroller_pos), 26, scroller_size), 4)
            if in_pos[0] > 479 and in_pos[0] < 505 and pygame.mouse.get_pressed()[0]:
                pygame.event.clear()
                if in_pos[1] > 5 and in_pos[1] < 35:
                    scroll_offset += 30
                if in_pos[1] > 415 and in_pos[1] < 445:
                    scroll_offset -= 30
    ##            print(start_y, in_pos[1], scroller_pos, scroll_per_pixel, scroll_offset)
            if in_pos[0] > 479 and in_pos[0] < 505 and pygame.mouse.get_pressed()[0]:
                if in_pos[1] > 40 and in_pos[1] < 410:
    ##                start_offset =
    ##                scroll_offset = -(start_offset*3 + (start_y + in_pos[1]) * scroll_per_pixel)
    ##                while in_pos[0] > 479 and in_pos[0] < 505 and pygame.mouse.get_pressed()[0]:
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
                    pygame.draw.rect(self.theme_surface, current_theme[0], (20, 135, 510, 450), 4)
    ##                window.blit(self.theme_surface, (250, 50))
    ##                pygame.display.update()
                    pygame.event.get()
    ##                print(start_y, in_pos[1], scroller_pos, scroll_per_pixel, scroll_offset)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        scroll_offset += 50
                    if event.button == 5:
                        scroll_offset -= 50
        else:
            scroll_offset = 0
        # go back button
        back = ui_tools.Button(self.theme_surface, 650, 570, 120, 40, font_d50, "Назад", current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])
        if back.draw(win_pos):
            current_ui = source
        # import button
        back = ui_tools.Button(self.theme_surface, 550, 415, 100, 30, font_d50, "Импорт", current_theme[14], current_theme[12], current_theme[13], current_theme[15], current_theme[0])
        if back.draw(win_pos):
            new_theme_source = filedialog.askopenfilename(title='Выберите тему', filetypes=[('Файл темы Домино PE в спец. формате', '*.dth'), ('Файл темы Домино PE в текстовом формате', '*.txt'), ('Все файлы', '*.*')])
            try:
                with open(new_theme_source, 'r', -1, 'utf-8') as new_theme_file:
                    to_add = new_theme_file.readlines()
                    for i in to_add:
                        new_theme = update_theme(ast.literal_eval(i))
                        if new_theme is False:
                            print(f'Found incompatible theme: {new_theme}, not loading it')
                        else:
                            custom_themes.append(new_theme)
                            theme_list.append(new_theme)
                            config_data["custom_themes"].append(new_theme)
            except:
                pass
        # finish rendering
        self.theme_surface.blit(self.inner_surface, (20, 135))
        pygame.draw.rect(self.theme_surface, current_theme[0], (20, 135, 510, 450), 4)
        window.blit(self.theme_surface, (250, 50))
        if theme_awaits_setting is not None:
            i = theme_awaits_setting
            current_theme = theme_list[i]
            config_data["theme_id"] = i
            theme_id = i
            self.__init__(self.surface, False)
            pygame.event.clear()

    def game_setup(self):
        # init
        global current_ui
        global scorelim
        global min_write
        global player_size
        global begin_with_double
        self.error_type = [0]
        error_messages = ["\n",
                        "Лимит очков должен быть больше нуля\n",
                        "У игроков должно быть хотя бы по одной фишке\n",
                        "Минимум для записи не должен превышать лимит очков\n",
                        "У игроков должно быть не более 14 фишек, иначе фишек не хватит на всех\n"
                        ]
        # render everything AND detect input in a loop
        error_message = ''
        for i in self.error_type:
            error_message = error_message + error_messages[i]
        pos = pygame.mouse.get_pos()
        win_pos = [pos[0] - 250, pos[1] - 50]
        # draw the window
        pygame.draw.rect(self.setup_win, current_theme[14], (0, 0, 780, 620))
        pygame.draw.rect(self.setup_win, current_theme[0], (0, 0, 780, 620), 4)
        pygame.draw.rect(self.setup_win, current_theme[12], (0, 0, 780, 40))
        pygame.draw.rect(self.setup_win, current_theme[0], (0, 0, 780, 40), 4)
        # draw the texts
        window_title = font_d50.render("Настройка", 4, current_theme[15])
        self.setup_win.blit(window_title, (390 - (window_title.get_width() / 2), 45 - window_title.get_height()))
        txt_score_limit = font_setup.render("Лимит очков", 4, current_theme[15])
        self.setup_win.blit(txt_score_limit, (35, 70))
        txt_min_write = font_setup.render("Начало записи", 4, current_theme[15])
        self.setup_win.blit(txt_min_write, (35, 150))
        txt_player_size = font_setup.render("Фишек у игроков", 4, current_theme[15])
        self.setup_win.blit(txt_player_size, (35, 230))
        txt_begin_with_double = font_setup.render("Начинать новую игру с дубля", 4, current_theme[15])
        self.setup_win.blit(txt_begin_with_double, (35, 310))
        blit_multiline(self.setup_win, error_message, [30, 390], 750, font_d50, current_theme[15])
        # draw the input boxes
        temp = self.score_lim.draw(text_color=current_theme[15], bkp_pos=win_pos)
        if temp is not False:
            scorelim = temp
        temp = self.min_score.draw(text_color=current_theme[15], bkp_pos=win_pos)
        if temp is not False:
            min_write = temp
        temp = self.give_players.draw(text_color=current_theme[15], bkp_pos=win_pos)
        if temp is not False:
            player_size = temp
        self.s_begin_with_double.draw(begin_with_double, win_pos)
        # detect input
        if self.s_begin_with_double.draw(begin_with_double, win_pos):
            begin_with_double = not begin_with_double
            pos = pygame.mouse.get_pos()
            win_pos = [pos[0] - 250, pos[1] - 50]
        if self.btn_setup_play.draw(win_pos):
            # check for errors and exit
            try:
                scorelim = int(scorelim)
                min_write = int(min_write)
                player_size = int(player_size)
            except ValueError:
                if scorelim == '':
                    scorelim = 125
                if min_write == '':
                    min_write == 13
                if player_size == '':
                    player_size = 7
            self.error_type = []
            if scorelim < 1:
                self.error_type.append(1)
            if player_size < 1:
                self.error_type.append(2)
            if min_write > scorelim:
                self.error_type.append(3)
            if player_size > 14:
                self.error_type.append(4)
            if self.error_type == []:
                pygame.event.clear()
                self.game = Game({'begin_with_double': begin_with_double, 'score_limit': scorelim, 'players': 2, 
                                    'give_players': player_size, 'set_type': 6, 'min_score': min_write, 
                                    'ai_count': ['local', 'pva', 'bot_battle'].index(self.gamemode)},
                                    {'side_select': self.handle_lor_dilemma, 'score_upd': self.ren_score_update, 
                                    'next_player': self.next_player})
                current_ui = 'local_game'
        if self.btn_setup_back.draw(win_pos) and pygame.event.get(pygame.MOUSEBUTTONDOWN):
            current_ui = 'menu_gamemode_select'
        self.surface.blit(self.setup_win, (250, 50))

    def how_to_play(self):
        global current_ui
        pygame.draw.rect(self.tutorial, current_theme[14], (0, 0, 500, 450))
        pygame.draw.rect(self.tutorial, current_theme[0], (0, 0, 500, 450), 4)
        pygame.draw.rect(self.tutorial, current_theme[12], (0, 0, 500, 40))
        pygame.draw.rect(self.tutorial, current_theme[0], (0, 0, 500, 40), 4)
        a = "    Выберите режим игры и установите желаемые настройки (необязательно). Вы можете стваить только те доминошки, которые можно приставить к одному из концов на поле такой же стороной. Сделать это можно, нажав на нужную доминошку мышкой. Когда у кого-то закончатся кости или ходить станет невозможно (рыба), то начнётся подсчёт очков. Побеждает тот, у кого меньше всего очков. Приятной игры!"
        blit_multiline(self.tutorial, a, (10, 45), 490, font_ver, current_theme[15])
        titl = font_ver.render("Как играть", 4, current_theme[15])
        self.tutorial.blit(titl, (250 - titl.get_width() / 2, 0))
        in_pos = pygame.mouse.get_pos()
        in_pos = [in_pos[0] - 390, in_pos[1] - 150]
        if self.tutorial_back.draw(in_pos) and pygame.event.get(pygame.MOUSEBUTTONDOWN):
            current_ui = 'menu_main'
        self.surface.blit(self.tutorial, (390, 150))

ui_game = ui(window)
delay = 6

backup_ui == 'none'
def esc_ctrl(current_ui) -> str:
    global backup_ui
    if current_ui == 'pause':
        return backup_ui
    elif current_ui == 'settings':
        return 'menu_main'
    elif current_ui == 'theme_settings':
        return 'settings'
    elif current_ui == 'theme_pause':
        return 'pause'
    elif current_ui == 'menu_gamemode_select':
        return 'menu_main'
    elif current_ui == 'local_setup':
        return 'menu_gamemode_select'
    elif current_ui == 'menu_main':
        return 'settings'
    elif current_ui == 'how_to_play':
        return 'menu_main'
    else:
        backup_ui = current_ui
        return 'pause'

while True: # game tick, running at 60 FPS
    if bool(pygame.event.peek(pygame.QUIT)):
        with open("domino_config.json", 'w', -1, 'utf-8') as config:
            config.write(json.dumps(config_data, indent=4, ensure_ascii=False))
        pygame.quit()
        print("Thanks for playing!")
        exit(0)
    for event in pygame.event.get(pygame.KEYDOWN):
        if event.key == pygame.K_ESCAPE:
            current_ui = esc_ctrl(current_ui)
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
        delay -= 1
    if current_ui == "menu_main":
        ui_game.render_main_menu()
    elif current_ui == "pause" or current_ui == 'settings':
        ui_game.settings()
    elif current_ui == "theme_settings":
        ui_game.theme_set_ui('settings')
    elif current_ui == "theme_pause":
        ui_game.theme_set_ui('pause')
    elif current_ui == "menu_gamemode_select":
        ui_game.render_menu_gm_sel()
    elif current_ui == "local_setup":
        ui_game.game_setup()
    elif current_ui == 'local_init':
        ui_game.game.init()
        current_ui = 'local_game'
    elif current_ui == "local_game":
        ui_game.game_ren()
        ui_game.local_game_ctrl()
    elif current_ui == "end":
        ui_game.game_ren()
        ui_game.ren_score_update()
    elif current_ui == 'how_to_play':
        ui_game.how_to_play()
    if bool(pygame.event.get(framerate_output)):
        current_fps = "FPS: " + str(round(gametick.get_fps()))
    fpsr = font_fps.render(current_fps, 4, current_theme[15])
    pygame.draw.rect(window, current_theme[12], (1215, 695, 100, 100))
    window.blit(fpsr, (1278 - fpsr.get_width(), 722 - fpsr.get_height()))
    pygame.display.update()
    gametick.tick(60)