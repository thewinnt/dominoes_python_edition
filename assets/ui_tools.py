import pygame
import random
import time

from tkinter import TclError, Tk

def paste():
    root = Tk()
    root.withdraw()
    root.update()
    targ = root.clipboard_get()
    root.destroy()
    return targ

# def copy(text):  # DOESN'T WORK  # no, i will not be using any third-party libraries
#     root = Tk()
#     root.withdraw()
#     root.clipboard_clear()
#     root.clipboard_append(text)
#     root.update()

## Pygame UI tools, version 1.3. Based on the libraries used in thewinnt/domino_scoreboard.

list_captures_events = None # if a list is being scrolled, it will capture the events and put itself here

COLOR_MAIN = (230, 230, 230)
COLOR_HOVER = (255, 255, 255)
COLOR_CLICK = (200, 200, 200)
COLOR_TEXT = (0, 0, 0)
COLOR_OUTLINE = (0, 0, 0)

COLOR_ENABLE = (0, 240, 0)
COLOR_DISABLE = (240, 0, 0)

COLOR_ORIGIN = (240, 240, 240)
COLOR_BASE = (230, 230, 230)
COLOR_SCROLLER = (40, 40, 40)
COLOR_HOVER_ORIGIN = (255, 255, 255)
COLOR_HOVER_BASE = (240, 240, 240)
COLOR_HOVER_SCROLLER = (80, 80, 80)

COLOR_INDEX = [(0, 0, 0),
               (0, 0, 170),
               (0, 170, 0),
               (0, 170, 170),
               (170, 0, 0),
               (170, 0, 170),
               (255, 170, 0),
               (170, 170, 170),
               (85, 85, 85),
               (85, 85, 255),
               (85, 255, 85),
               (85, 255, 255),
               (255, 85, 85),
               (255, 85, 255),
               (255, 255, 85),
               (255, 255, 255)] # these are from minecraft

# button
class Button:
    def __init__(self, surface, x, y, width=100, height=50, font=None, text='', color_main=COLOR_MAIN, color_hover=COLOR_HOVER, color_click=COLOR_CLICK, color_text=COLOR_TEXT, color_outline=COLOR_OUTLINE):
        '''A simple button, version 2.1.1'''
        self.color_main = color_main
        self.color_hover = color_hover
        self.color_click = color_click
        self.color_text = color_text
        self.color_outline = color_outline
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.surface = surface

    def draw(self, mouse_pos=None, outline_width=2, click_state=None, draw_bg=True) -> bool:
        '''Draws the button on the screen and returns its click state'''
        # mouse_pos is the position relative to (0, 0) of the surface the button's on, if it isn't the display one
        # click states: None - auto-detect; 0 - not hovered; 1 - hovered, but not pressed; 2 - pressed
        ## click_state can be used for inactive buttons
        is_pressed = pygame.mouse.get_pressed()[0]
        to_return = False
        if draw_bg:
            if click_state is not None:
                if click_state == 0:
                    pygame.draw.rect(self.surface, self.color_main, (self.x, self.y, self.width, self.height))
                elif click_state == 1:
                    pygame.draw.rect(self.surface, self.color_hover, (self.x, self.y, self.width, self.height))
                elif click_state == 2:
                    pygame.draw.rect(self.surface, self.color_click, (self.x, self.y, self.width, self.height))
            else:
                if not self._is_hovered(mouse_pos):
                    pygame.draw.rect(self.surface, self.color_main, (self.x, self.y, self.width, self.height))
                elif self._is_hovered(mouse_pos) and not is_pressed:
                    pygame.draw.rect(self.surface, self.color_hover, (self.x, self.y, self.width, self.height))
                elif self._is_hovered(mouse_pos) and is_pressed:
                    pygame.draw.rect(self.surface, self.color_click, (self.x, self.y, self.width, self.height))
                    to_return = True

            if outline_width and self.color_outline:
                pygame.draw.rect(self.surface, self.color_outline, (self.x, self.y, self.width, self.height), outline_width)
        else:
            to_return = self._is_hovered(mouse_pos) and is_pressed

        if self.text and not self.font is None:
            text = self.font.render(self.text, 1, self.color_text)
            self.surface.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        
        if click_state is None and not list_captures_events:
            return to_return

    def _is_hovered(self, mouse_pos=None):
        if mouse_pos is None:
            self.pos = pygame.mouse.get_pos()
        else:
            self.pos = mouse_pos
        return self.x + self.width > self.pos[0] > self.x and self.y + self.height > self.pos[1] > self.y

class Switch:
    def __init__(self, surface, x, y, width=90, height=40, outline=4, default_color=COLOR_MAIN, hover_color=COLOR_HOVER, outline_color=COLOR_OUTLINE, enable_color=COLOR_ENABLE, disable_color=COLOR_DISABLE):
        '''A switch that acts like a button, version 2.1'''
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.outline = outline
        self.surface = surface

        self.outline_color = outline_color
        self.hover_color = hover_color
        self.default_color = default_color
        self.enable_color = enable_color
        self.disable_color = disable_color

        self.was_pressed = False

        self.sel_radius = height / 2

    def raw_draw(self, active, bkp_pos=None, is_over=False):
        '''Simply draws the switch and does nothing'''
        # I am sorry for the long lines, pygame do be like that sometimes
        if bkp_pos == None:
            self.pos = pygame.mouse.get_pos()
        else:
            self.pos = bkp_pos
        
        if is_over:
            pygame.draw.rect(self.surface, self.hover_color, (self.x, self.y, self.width, self.height), 0, int(self.height / 2))
        else:
            pygame.draw.rect(self.surface, self.default_color, (self.x, self.y, self.width, self.height), 0, int(self.height / 2))
        
        pygame.draw.rect(self.surface, self.outline_color, (self.x - self.outline//2, self.y - self.outline//2, self.width + self.outline, self.height + self.outline), self.outline, int(self.height / 2))

        if active:
            pygame.draw.circle(self.surface, self.enable_color, (self.x + self.width - self.sel_radius + self.outline // 2, self.y + self.sel_radius), self.sel_radius)
            pygame.draw.circle(self.surface, self.outline_color, (self.x + self.width - self.sel_radius + self.outline // 2, self.y + self.sel_radius), self.sel_radius, self.outline)
        
        else:
            pygame.draw.circle(self.surface, self.disable_color, (self.x + self.sel_radius - self.outline//2, self.y + self.sel_radius), self.sel_radius)
            pygame.draw.circle(self.surface, self.outline_color, (self.x + self.sel_radius - self.outline//2, self.y + self.sel_radius), self.sel_radius, self.outline)

    def is_over(self, bkp_pos=None) -> bool:
        '''Returns true if mouse is hovering over the switch'''
        if bkp_pos == None:
            self.pos = pygame.mouse.get_pos()
        else:
            self.pos = bkp_pos
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width and self.pos[1] > self.y and self.pos[1] < self.y + self.height:
            return True
        else:
            return False

    def draw(self, active, bkp_pos=None) -> bool:
        '''Draws the switch and returns if it's been clicked at recently'''
        self.raw_draw(active, bkp_pos, self.is_over(bkp_pos))
        if not self.was_pressed and pygame.mouse.get_pressed()[0]:
            self.was_pressed = True
            is_clicked = True
        elif self.was_pressed and pygame.mouse.get_pressed()[0]:
            self.was_pressed = True
            is_clicked = False
        else:
            self.was_pressed = False
            is_clicked = False
        if not list_captures_events:
            return self.is_over(bkp_pos) and is_clicked

class Hyperlink:
    def __init__(self, surface, x, y, text, font, color=COLOR_TEXT):
        '''Some text that can be clicked to bring you somewhere else, version 2.2'''
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.text = text
        self.font = font

        self.was_pressed = False

    def is_over(self, bkp_pos=None) -> bool:
        '''Returns true, if the cursor is pointing at the link'''
        if bkp_pos == None:
            self.pos = pygame.mouse.get_pos()
        else:
            self.pos = bkp_pos
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width and self.pos[1] > self.y and self.pos[1] < self.y + self.height:
            return True
        else:
            return False

    def draw(self, bkp_pos=None) -> bool:
        '''Draws the link and returns its click state'''
        txt = fancy_blit(self.surface, self.x, self.y, self.text, self.font, self.color, None)
        self.width, self.height = self.font.size(txt)
        if not self.was_pressed and pygame.mouse.get_pressed()[0]:
            self.was_pressed = True
            is_clicked = True
        elif self.was_pressed and pygame.mouse.get_pressed()[0]:
            self.was_pressed = True
            is_clicked = False
        else:
            self.was_pressed = False
            is_clicked = False
        if not list_captures_events:
            return self.is_over(bkp_pos) and is_clicked

class DropdownList:
    def __init__(self, surface, x, y, options, font, right_sided=True, chosen=0, min_width=150, require_hover=False, max_len=6, color_base=COLOR_BASE, color_origin=COLOR_ORIGIN, color_text=COLOR_TEXT, color_outline=COLOR_OUTLINE, color_scroll=COLOR_SCROLLER, color_hover_base=COLOR_HOVER_BASE, color_hover_origin=COLOR_HOVER_ORIGIN, color_hover_scroll=COLOR_HOVER_SCROLLER):
        '''A dropdown list, version 1.3'''
        self.x = x
        self.y = y
        self.orig_x = self.x
        self.orig_y = self.y
        self.max_len = max_len
        self.font = font
        self.surface = surface
        self.targ_surf = surface
        self.right_sided = right_sided # might be the wanted behavior because the width might be unpredictable

        self.color_base = color_base
        self.color_origin = color_origin
        self.color_text = color_text
        self.color_outline = color_outline
        self.color_scroller = color_scroll
        self.color_hover_base = color_hover_base
        self.color_hover_origin = color_hover_origin
        self.color_hover_scroll = color_hover_scroll

        self.options = options
        self.open = False
        self.chosen_option_index = chosen # aka origin
        self.scroll_offset = 0 # 0 <= scroll_offset <= len(options) - max_len
        self.require_hover = require_hover # whether the list will be closed when mouse cursor isn't at it

        self.min_width = min_width

        self.was_pressed = False
        self.scrolling = False
        self.start_y = None
        self.start_offset = None

        self.prepare_options()

    def add_option(self, what, where=-1):
        '''Adds an option to the list at a desired position'''
        self.options.insert(where, str(what))
        self.prepare_options()
    
    def remove_option(self, option):
        '''Removes an option with specified contents or index'''
        if type(option) == int or not option in self.options:
            self.options.pop(int(option))
        elif type(option) == str:
            self.options.remove(option)
        else:
            raise TypeError('expected an int or a string matching the contents of an option')
        if len(self.options) > self.max_len and self.max_len + self.scroll_offset > len(self.options):
            self.scroll_offset = len(self.options) - self.max_len
        self.prepare_options()

    def prepare_options(self):
        '''Prepares the sizes of the list - must be run every time the options change! 
        (unless you redefine the list or use the built-in methods)'''
        self.height = int(self.font.size('*Ёy,gj')[1] * 1.1) # this should do the trick
        option_sizes = []
        for i in self.options:
            option_sizes.append(self.font.size(i)[0] + int(self.height))
        self.width = max(max(option_sizes), self.min_width)
        if not self.right_sided:
            self.x = self.width
            self.y = 0
        self.hitbox_closed = [(self.x - self.width, self.y), (self.x, self.y + self.height)] # the corners of the list when it's closed
        self.hitbox_open = [(self.x - self.width, self.y), (self.x, self.y + self.height * (min(len(self.options), self.max_len) + 1))]
        self.hitbox_options = [] # format: self.hitbox_options[option][corner: top left or bottom right][coordinate: x or y]
        for i in range(min(len(self.options), self.max_len)):
            self.hitbox_options.append([(self.x - self.width, self.y + self.height * (i+1)), (self.x, self.y + self.height * (i+2))])
        self.ren_chosen = self.font.render(self.options[self.chosen_option_index], 1, self.color_text)
        self.ren_opt = []
        for i in self.options:
            self.ren_opt.append(self.font.render(i, 1, self.color_text))

    def draw(self) -> int:
        '''Draws the list, updates it and returns the last clicked value'''
        global list_captures_events
        hbo = self.hitbox_options # this is much shorter

        ## prepare force left side (i was too lazy to rewrite this code)
        if not self.right_sided:
            if self.open:
                self.surface = pygame.Surface((self.hitbox_open[1][0] + 1, self.hitbox_open[1][1] + 1)).convert_alpha()
            else:
                self.surface = pygame.Surface((self.hitbox_closed[1][0] + 1, self.hitbox_closed[1][1] + 1)).convert_alpha()
        
        ## gather events
        if list_captures_events == None or list_captures_events == self:
            pos = list(pygame.mouse.get_pos())
            if not self.right_sided:
                pos[0] -= self.orig_x
                pos[1] -= self.orig_y
            if pygame.mouse.get_pressed()[0] and not self.was_pressed:
                self.was_pressed = True
                if self.open:
                    if hbo[0][1][0] - self.height*0.2 < pos[0] < hbo[0][1][0] and self.y+self.height+self.scroll_pos < pos[1] < self.y+self.height+self.scroll_pos+self.scroll_len:
                        self.scrolling = True
                        self.start_y = pos[1]
                        self.start_offset = self.scroll_offset
                    elif not (hbo[0][1][0] - self.height*0.2 < pos[0] < hbo[0][1][0] and hbo[0][0][1] < pos[1] < self.hitbox_open[1][1]):
                        self.open = False
                        for i in range(len(hbo)):
                            if hbo[i][0][0] < pos[0] < hbo[i][1][0] - self.height*0.2 and hbo[i][0][1] < pos[1] < hbo[i][1][1]:
                                self.chosen_option_index = i + self.scroll_offset
                                self.ren_chosen = self.font.render(self.options[self.chosen_option_index], 1, self.color_text)
                                return self.chosen_option_index
                elif not self.open and self.x - self.width < pos[0] < self.x and self.y < pos[1] < self.y + self.height:
                    self.open = True
            elif pygame.mouse.get_pressed()[0] and self.was_pressed: 
                self.was_pressed = True
            else:
                self.was_pressed = False
            if self.open and self.require_hover and not self.scrolling:
                if not (self.hitbox_open[0][0] < pos[0] < self.hitbox_open[1][0] and self.hitbox_open[0][1] < pos[1] < self.hitbox_open[1][1]):
                    self.open = False
            if len(self.options) > self.max_len:
                event = pygame.event.get(pygame.MOUSEWHEEL)
                if event:
                    self.scroll_offset -= event[0].y
                    if self.scroll_offset < 0:
                        self.scroll_offset = 0
                    elif self.scroll_offset > len(self.options) - self.max_len:
                        self.scroll_offset = len(self.options) - self.max_len

        ## calculate scroll bar position
        if len(self.options) > self.max_len:
            self.scroll_len = max(self.height, min(self.height * len(self.options) / (len(self.options) - self.max_len), self.height * (self.max_len - 1)))
            self.scroll_step = (self.height * self.max_len - self.scroll_len) / (len(self.options) - self.max_len) 
            self.scroll_pos = self.scroll_step * self.scroll_offset

            ## proces scrolling
            if self.scrolling and list_captures_events == None or list_captures_events == self:
                list_captures_events = self
                if not pygame.mouse.get_pressed()[0]:
                    self.scrolling = False
                    list_captures_events = None
                else:
                    self.scroll_offset = self.start_offset + int((pos[1] - self.start_y) // self.scroll_step)
                    if self.scroll_offset < 0:
                        self.scroll_offset = 0
                    elif self.scroll_offset > len(self.options) - self.max_len:
                        self.scroll_offset = len(self.options) - self.max_len
            if (hbo[0][1][0] - self.height*0.2 < pos[0] < hbo[0][1][0] and self.y+self.height+self.scroll_pos < pos[1] < self.y+self.height+self.scroll_pos+self.scroll_len) or self.scrolling:
                is_scroller_hovered = True
            else:
                is_scroller_hovered = False
        
        ## draw origin
        if self.hitbox_closed[0][0] < pos[0] < self.hitbox_closed[1][0] and self.hitbox_closed[0][1] < pos[1] < self.hitbox_closed[1][1]:
            pygame.draw.rect(self.surface, self.color_hover_origin, (self.x - self.width, self.y, self.width, self.height))
        else:
            pygame.draw.rect(self.surface, self.color_origin, (self.x - self.width, self.y, self.width, self.height))

        if self.open:
            pygame.draw.polygon(self.surface, self.color_outline, ([self.x - self.height * 0.3, self.y + self.height * 0.7],
                                                                   [self.x - self.height * 0.7, self.y + self.height * 0.7],
                                                                   [self.x - self.height * 0.5, self.y + self.height * 0.3]))
        else:
            pygame.draw.polygon(self.surface, self.color_outline, ([self.x - self.height * 0.3, self.y + self.height * 0.3],
                                                                   [self.x - self.height * 0.7, self.y + self.height * 0.3],
                                                                   [self.x - self.height * 0.5, self.y + self.height * 0.7]))
        self.surface.blit(self.ren_chosen, (self.x - self.width + self.height * 0.15, self.y + 2))
        pygame.draw.rect(self.surface, self.color_outline, (self.x - self.width, self.y, self.width, self.height), 2)

        ## draw base
        if self.open:
            for i in range(min(len(self.options), self.max_len)):
                if hbo[i][0][0] < pos[0] < hbo[i][1][0] - self.height * 0.2 and hbo[i][0][1] < pos[1] < hbo[i][1][1]:
                    pygame.draw.rect(self.surface, self.color_hover_base, (hbo[i][0][0], 
                                                                           hbo[i][0][1], 
                                                                           hbo[i][1][0] - hbo[i][0][0], 
                                                                           hbo[i][1][1] - hbo[i][0][1])) # the line is too long
                else:
                    pygame.draw.rect(self.surface, self.color_base, (hbo[i][0][0], 
                                                                     hbo[i][0][1], 
                                                                     hbo[i][1][0] - hbo[i][0][0], 
                                                                     hbo[i][1][1] - hbo[i][0][1]))
                self.surface.blit(self.ren_opt[i + self.scroll_offset], (hbo[i][0][0] + self.height * 0.1, hbo[i][0][1] + 2))
            pygame.draw.rect(self.surface, self.color_outline, (self.hitbox_open[0][0],
                                                                self.hitbox_open[0][1],
                                                                self.hitbox_open[1][0] - self.hitbox_open[0][0],
                                                                self.hitbox_open[1][1] - self.hitbox_open[0][1]), 2)
            if len(self.options) > self.max_len:
                if is_scroller_hovered:
                    pygame.draw.rect(self.surface, self.color_hover_scroll, (self.x - self.height * 0.2,
                                                                             self.y + self.scroll_pos + self.height,
                                                                             self.height * 0.2,
                                                                             self.scroll_len))
                else:
                    pygame.draw.rect(self.surface, self.color_scroller, (self.x - self.height * 0.2,
                                                                         self.y + self.scroll_pos + self.height,
                                                                         self.height * 0.2,
                                                                         self.scroll_len))

        # blit to target
        if not self.right_sided:
            self.targ_surf.blit(self.surface, (self.orig_x, self.orig_y))

def fancy_blit(surface, x, y, text, font, default_color=COLOR_TEXT, background_color=COLOR_MAIN, return_surfaces=False, reset_at_color=False) -> str:
    '''Draws the text and returns it in a normal way (without technical symbols), version 2.1'''
    # this is all from minecraft
    rendered_parts = []
    color = -1
    randomize = False
    cross = False
    word = ''
    random_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    set_mode = False
    normal = ''
    was_bold = font.get_bold()
    was_italic = font.get_italic()
    was_underline = font.get_underline()
    for i in text:
        if set_mode:
            set_mode = False
            if not i in '0123456789abcdefklmnor':
                word += '§' + i
            else:
                if color == -1:
                    rendered_parts.append(font.render(word, 1, default_color, background_color))
                else:
                    rendered_parts.append(font.render(word, 1, COLOR_INDEX[color], background_color))
                size = rendered_parts[-1].get_size()
                if cross:
                    pygame.draw.line(rendered_parts[-1], COLOR_INDEX[color], (0, size[1] // 2), (size[0], size[1] // 2), 3)
                normal += word
                word = ''
                if i in '0123456789abcdef':
                    color = '0123456789abcdef'.index(i)
                    if reset_at_color: # if true, java edition logic is applied when a color code clears the formatting
                        randomize = False
                        font.set_bold(False)
                        cross = False
                        font.set_underline(False)
                        font.set_italic(False)
                elif i in 'klmnor':
                    if i == 'k': 
                        randomize = True
                    elif i == 'l': 
                        font.set_bold(True)
                    elif i == 'm': 
                        cross = True
                    elif i == 'n': 
                        font.set_underline(True)
                    elif i == 'o': 
                        font.set_italic(True)
                    else:
                        randomize = False
                        font.set_bold(False)
                        cross = False
                        font.set_underline(False)
                        font.set_italic(False)
        elif i == '§':
            set_mode = True
            continue
        else:
            if randomize:
                word += random_chars[random.randint(0, len(random_chars) - 1)]
            else:
                word += i
    if color == -1:
        rendered_parts.append(font.render(word, 1, default_color, background_color))
    else:
        rendered_parts.append(font.render(word, 1, COLOR_INDEX[color], background_color))
    size = rendered_parts[-1].get_size()
    if cross:
        pygame.draw.line(rendered_parts[-1], COLOR_INDEX[color], (0, size[1] // 2), (size[0], size[1] // 2), 3)
    if not return_surfaces:
        normal += word
        offset = 0
        for i in rendered_parts:
            surface.blit(i, (x + offset, y))
            offset += i.get_width()
        font.set_bold(was_bold)
        font.set_underline(was_underline)
        font.set_italic(was_italic)
        return normal
    else:
        size = 0
        for i in rendered_parts:
            size += i.get_width()
        targ_surf = pygame.Surface((size, i.get_height())).convert_alpha()
        offset = 0
        for i in rendered_parts:
            targ_surf.blit(i, (offset, 0))
            offset += i.get_width()
        return targ_surf

class TextField:
    def __init__(self, surface, x, y, font, width=100, height=50, default_value='', hint='', type_='string', outline_color_active=(0, 0, 0), outline_color_inactive=(50, 50, 50), field_color=(240, 240, 240), select_color=(0, 0, 255)):
        '''A rectangle which you can click to write something, version 2.0-pre1'''
        self.width = width
        self.height = height

        self.x = x
        self.y = y

        self.text = str(default_value)
        self.default = default_value
        self.hint = hint
        self.font = font

        self.outline_color_active = outline_color_active
        self.outline_color_inactive = outline_color_inactive
        self.field_color = field_color
        self.selection_color = select_color

        self.surface = surface
        self.active = False

        self.type = type_

        self.was_clicked = False
        self.enter = False # if the typing was stopped by pressing Enter

        self.cursor_visible = True
        self.cursor = len(self.text)
        self.selection = None

        self.t = time.time()
        self.cursor_timer = 0.0

        self.key_init = 0.0
        self.key_timer = 0.0

    def is_over(self, bkp_pos=None) -> bool:
        '''Returns true if mouse is hovering the text field'''
        if bkp_pos == None:
            self.pos = pygame.mouse.get_pos()
        else:
            self.pos = bkp_pos
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width and self.pos[1] > self.y and self.pos[1] < self.y + self.height:
            return True
        else:
            return False

    def update(self) -> str:
        '''Update the contents of the box and return the new value'''
        self.enter = False
        self.was_clicked = pygame.mouse.get_pressed()[0]
        for event in pygame.event.get():
            if event.type == pygame.TEXTINPUT:
                bkp_text = self.text
                if self.selection is None:
                    self.text = str(self.text[:self.cursor]) + event.text + str(self.text[self.cursor:])
                else:
                    val1 = min(self.selection)
                    val2 = max(self.selection)
                    self.text = str(self.text)[:val1] + event.text + str(self.text)[val2:]
                    self.selection = None
                error = False
                if self.type == 'int':
                    try:
                        int(self.text + '0')
                    except ValueError:
                        self.text = bkp_text
                        error = True
                if self.type == 'float':
                    try:
                        float(self.text + '0')
                    except ValueError:
                        self.text = bkp_text
                        error = True
                if not error:
                    self.cursor += 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    self.was_clicked = True
                    self.enter = True
                    break
                # elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE or event.mod == pygame.KMOD_NONE:
                #     break
                # else:
                #     if event.unicode:
                #         bkp_text = self.text
                        
                #         if self.selection is None:
                #             self.text = str(self.text[:self.cursor]) + event.unicode + str(self.text[self.cursor:])
                #         else:
                #             val1 = min(self.selection)
                #             val2 = max(self.selection)
                #             self.text = str(self.text)[:val1] + event.unicode + str(self.text)[val2:]
                #             self.selection = None
                #         error = False
                #         if self.type == 'int':
                #             try:
                #                 int(self.text + '0')
                #             except ValueError:
                #                 self.text = bkp_text
                #                 error = True
                #         if self.type == 'float':
                #             try:
                #                 float(self.text + '0')
                #             except ValueError:
                #                 self.text = bkp_text
                #                 error = True
                #         if not error:
                #             self.cursor += 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.was_clicked = True
        return self.text

    def draw(self, update=True, text_color=(0, 0, 0), bkp_pos=None, hint_color=(100, 100, 100), fancy_format=False) -> str:
        '''Usage: 'temp = field_name.draw(...); if temp is not False: target = temp' where target is the string you want to get as user input'''
        self.dt = time.time() - self.t
        self.t = time.time()
        self.cursor_timer += self.dt

        if self.cursor_timer >= 0.5:
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = 0.0

        self.was_clicked = pygame.mouse.get_pressed()[0]
        if self.active and update and not list_captures_events:
            outline_color = self.outline_color_active
            outline_width = 4
            self.update()
        else:
            outline_color = self.outline_color_inactive
            outline_width = 2

        if self.active:
            keys = pygame.key.get_pressed()

            if self.selection is not None:
                val1 = min(self.selection)
                val2 = max(self.selection)

            if keys[pygame.K_LEFT]:
                if self.key_init == 0:
                    self.cursor -= 1
                    if keys[pygame.K_LSHIFT]:
                        if self.selection is None:
                            self.selection = [self.cursor, self.cursor + 1]
                        else:
                            if self.selection[0] == self.cursor + 1:
                                self.selection[0] -= 1
                            else:
                                self.selection[1] -= 1
                    else:
                        self.selection = None
                    if self.cursor < 0:
                        self.cursor = 0
                self.key_init += self.dt
                if self.key_init >= 0.5:
                    self.key_timer += self.dt
                    if self.key_timer >= 0.05:
                        self.key_timer = 0
                        self.cursor -= 1
                        if keys[pygame.K_LSHIFT]:
                            if self.selection is None:
                                self.selection = [self.cursor, self.cursor + 1]
                            else:
                                if self.selection[0] == self.cursor + 1:
                                    self.selection[0] -= 1
                                else:
                                    self.selection[1] -= 1
                        else:
                            self.selection = None
                        if self.cursor < 0:
                            self.cursor = 0

            elif keys[pygame.K_RIGHT]:
                if self.key_init == 0:
                    self.cursor += 1
                    if keys[pygame.K_LSHIFT]:
                        if self.selection is None:
                            self.selection = [self.cursor - 1, self.cursor]
                        else:
                            if self.selection[1] == self.cursor - 1:
                                self.selection[1] += 1
                            else:
                                self.selection[0] += 1
                    else:
                        self.selection = None
                    if self.cursor > len(self.text):
                        self.cursor = len(self.text)
                self.key_init += self.dt
                if self.key_init >= 0.5:
                    self.key_timer += self.dt
                    if self.key_timer >= 0.05:
                        self.key_timer = 0
                        self.cursor += 1
                        if keys[pygame.K_LSHIFT]:
                            if self.selection is None:
                                self.selection = [self.cursor - 1, self.cursor]
                            else:
                                if self.selection[1] == self.cursor - 1:
                                    self.selection[1] += 1
                                else:
                                    self.selection[0] += 1
                        else:
                            self.selection = None
                        if self.cursor > len(self.text):
                            self.cursor = len(self.text)

            elif keys[pygame.K_BACKSPACE] and (self.cursor > 0 or self.selection is not None):
                if self.key_init == 0:
                    if self.selection is None:
                        self.text = str(self.text)[:self.cursor-1] + str(self.text)[self.cursor:]
                        self.cursor -= 1
                    else:
                        self.text = str(self.text)[:self.selection[0]] + str(self.text)[self.selection[1]:]
                        self.selection = None
                self.key_init += self.dt
                if self.key_init >= 0.5:
                    self.key_timer += self.dt
                    if self.key_timer >= 0.05:
                        if self.selection is None:
                            self.key_timer = 0
                            self.text = str(self.text)[:self.cursor-1] + str(self.text)[self.cursor:]
                        else:
                            self.text = str(self.text)[:self.selection[0]] + str(self.text)[self.selection[1]:]
                            self.selection = None
                        self.cursor -= 1

            elif keys[pygame.K_DELETE] and self.cursor < len(self.text):
                if self.key_init == 0:
                    if self.selection is None:
                        self.text = str(self.text)[:self.cursor] + str(self.text)[self.cursor+1:]
                    else:
                        self.text = str(self.text)[:self.selection[0]] + str(self.text)[self.selection[1]:]
                        self.selection = None
                self.key_init += self.dt
                if self.key_init >= 0.5:
                    self.key_timer += self.dt
                    if self.key_timer >= 0.05:
                        self.key_timer = 0
                        if self.selection is None:
                            self.text = str(self.text)[:self.cursor] + str(self.text)[self.cursor+1:]
                        else:
                            self.text = str(self.text)[:self.selection[0]] + str(self.text)[self.selection[1]:]
                            self.selection = None

            elif keys[pygame.K_HOME]:
                if keys[pygame.K_LSHIFT]:
                    if self.selection is not None:
                        if self.selection[0] == self.cursor:
                            self.selection[0] = 0
                        else:
                            self.selection[1] = 0
                    else:
                        self.selection = [0, self.cursor]
                self.cursor = 0
                
            elif keys[pygame.K_END]:
                if keys[pygame.K_LSHIFT]:
                    if self.selection is not None:
                        if self.selection[0] == self.cursor:
                            self.selection[0] = len(self.text)
                        else:
                            self.selection[1] = len(self.text)
                    else:
                        self.selection = [self.cursor, len(self.text)]
                self.cursor = len(self.text)
            elif keys[pygame.K_LCTRL]:
                if self.key_init == 0:
                    # if self.selection is not None:  # copying text to the clipboard doesn't seem to work...
                    #     if keys[pygame.K_x]:
                    #         copy(self.text[val1:val2])
                    #         self.text = str(self.text)[:self.selection[0]] + str(self.text)[self.selection[1]:]
                    #         self.selection = None
                    #     if keys[pygame.K_c]:
                    #         copy(self.text[val1:val2])
                    #         self.selection = None
                    if keys[pygame.K_v]:
                        
                        try:
                            to_add = paste()
                        except TclError:
                            return False
                        bkp_text = self.text
                        bkp_cur = self.cursor
                        if self.selection is None:
                            self.text = str(self.text[:self.cursor]) + to_add + str(self.text[self.cursor:])
                            self.cursor = min(self.cursor + len(to_add), len(self.text))
                        else:
                            self.text = str(self.text)[:val1] + to_add + str(self.text)[val2:]
                            self.cursor = val1 + len(to_add)
                            self.selection = None
                        err = False
                        if self.type == 'int':
                            try:
                                int(self.text + '0')
                            except ValueError:
                                self.text = bkp_text
                                self.cursor = bkp_cur
                                err = True
                        if self.type == 'float':
                            try:
                                float(self.text + '0')
                            except ValueError:
                                self.text = bkp_text
                                self.cursor = bkp_cur
                                err = True
                        if not err:
                            self.selection = None
                    if keys[pygame.K_a]:
                        self.selection = [0, len(self.text)]
            else:
                self.key_init = 0

            if self.selection is not None:
                val1 = min(self.selection)
                val2 = max(self.selection)
        else:
            self.selection = None

        pygame.draw.rect(self.surface, self.field_color, (self.x, self.y, self.width, self.height))

        if self.selection is None:
            text = self.font.render(str(self.text), 4, text_color, self.field_color)
            self.surface.blit(text, (self.x + 5, self.y + self.height // 2 - text.get_height() // 2))
        else:
            text = self.font.render(str(self.text[:val1]), 4, text_color, self.field_color)
            self.surface.blit(text, (self.x + 5, self.y + self.height // 2 - text.get_height() // 2))

            offset = text.get_width()

            text = self.font.render(str(self.text[val1:val2]), 4, self.field_color, self.selection_color)
            self.surface.blit(text, (self.x + 5 + offset, self.y + self.height // 2 - text.get_height() // 2))

            offset += text.get_width()

            text = self.font.render(str(self.text[val2:]), 4, text_color, self.field_color)
            self.surface.blit(text, (self.x + 5 + offset, self.y + self.height // 2 - text.get_height() // 2))

        if self.text == '':
            fancy_blit(self.surface, self.x + 5, self.y + self.height // 2 - text.get_height() // 2, self.hint, self.font, hint_color, self.field_color)

        if self.active and self.cursor_visible:
            size = self.font.size(self.text[:self.cursor])
            pygame.draw.rect(self.surface, text_color, (self.x + size[0] + 5, self.y + self.height // 2 - text.get_height() // 2, 2, size[1]))

        pygame.draw.rect(self.surface, outline_color, (self.x, self.y, self.width, self.height), outline_width)

        if update and self.was_clicked and not list_captures_events:
            if not self.enter:
                self.was_clicked = False
                temp = self.active
                self.active = self.is_over(bkp_pos)
                if self.active and not temp:
                    pygame.event.get()
                if temp == self.active or self.active:
                    return False
            else:
                self.active = False
                self.enter = False
            if not self.active:
                if self.type == 'string':
                    return self.text
                elif self.type == 'float':
                    if self.text:
                        return float(self.text)
                    else:
                        self.text = str(self.default)
                        return float(self.default)
                elif self.type == 'int':
                    if self.text:
                        return int(self.text)
                    else:
                        self.text = str(self.default)
                        return int(self.default)
                else:
                    raise SyntaxError(f"Invalid type of value to return: {self.type}, it must be either 'int', 'float' or 'string' (default)")
        else:
            return False

if __name__ == '__main__': # debug
    pygame.init()
    window = pygame.display.set_mode((360, 460))
    default_font = pygame.font.SysFont('arialms', 30)
    underlined_font = pygame.font.SysFont("arialms", 30)
    underlined_font.set_underline(True)

    test_list = DropdownList(window, 10, 10, ['Option 1', 'Two', '3', 'Четыре (пять)', 'Never', 'Gonna', 'Give', 'You', 'Up'], default_font, False, 0, 250)
    test_button = Button(window, 10, 70, 100, 50, default_font, 'button')
    test_field = TextField(window, 10, 130, default_font, 250, 150, hint='§7§oType something...')
    test_switch = Switch(window, 10, 290, 100, 50)
    test_link = Hyperlink(window, 10, 350, 'Click me!', underlined_font)

    lol = False
    add = ''

    while True:
        if pygame.event.get(pygame.QUIT):
            pygame.quit()
            exit(0)
        window.fill(COLOR_MAIN)
        if test_button.draw():
            print('You clicked the button')
            if add:
                test_list.add_option(add)
        temp = test_field.draw()
        if temp is not False:
            add = temp
            print('You typed:', temp)
        if test_switch.draw(lol):
            lol = not lol
        if test_link.draw():
            print('Not redirecting you anywhere')
            if add:
                try:
                    test_list.remove_option(add)
                except: 
                    pass
        fancy_blit(window, 10, 410, '§00§11§22§33§m§44§55§66§n§77§88§99§o§aa§bb§cc§r§l§k§dd§ee§ff', default_font)
        temp = test_list.draw()
        if temp is not None:
            print('You chose "' + test_list.options[temp] + '"')
        pygame.time.Clock().tick(0)
        pygame.display.update()