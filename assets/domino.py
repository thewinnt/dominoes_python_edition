import pygame

class Domino:
    def __init__(self, surface, color_outline=(0, 0, 0), color_fill=(240, 240, 240), color_div=(0, 0, 0), color_numbers=[(0, 0, 0)] * 18):
        self.surface = surface
        self.color_outline = color_outline
        self.color_div = color_div
        self.color_fill = color_fill
        self.color_numbers = color_numbers
    def _draw_number(self, pos, number, color, rot=False):
        number = str(number)
        if number == '0':
            return
        targ_surface = pygame.Surface((62, 62)).convert_alpha()
        targ_surface.fill(pygame.Color(0, 0, 0, 0))
        if number == '1':
            pygame.draw.circle(targ_surface, color, (31, 31), 3, 3)
        elif number == '2':
            pygame.draw.circle(targ_surface, color, (17, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
        elif number == '3':
            pygame.draw.circle(targ_surface, color, (17, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (31, 31), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
        elif number == '4':
            pygame.draw.circle(targ_surface, color, (17, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
        elif number == '5':
            pygame.draw.circle(targ_surface, color, (17, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (31, 31), 3, 3)
        elif number == '6':
            pygame.draw.circle(targ_surface, color, (17, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (31, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (31, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
        elif number == '7':
            pygame.draw.circle(targ_surface, color, (17, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (31, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (31, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (31, 31), 3, 3)
        elif number == '8':
            pygame.draw.circle(targ_surface, color, (17, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (31, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (31, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 31), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 31), 3, 3)
        elif number == '9':
            pygame.draw.circle(targ_surface, color, (17, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (31, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (31, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 31), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 31), 3, 3)
            pygame.draw.circle(targ_surface, color, (31, 31), 3, 3)
        elif number == '10':
            pygame.draw.circle(targ_surface, color, (17, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 31), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 31), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
        elif number == '11':
            pygame.draw.circle(targ_surface, color, (17, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 31), 3, 3)
            pygame.draw.circle(targ_surface, color, (31, 31), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 31), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
        elif number == '12':
            pygame.draw.circle(targ_surface, color, (17, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 31), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 31), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 31), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 31), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
        elif number == '13':
            pygame.draw.circle(targ_surface, color, (31, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 26), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 26), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 26), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 26), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 36), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 36), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 36), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 36), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
        elif number == '14':
            pygame.draw.circle(targ_surface, color, (26, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 26), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 26), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 26), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 26), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 36), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 36), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 36), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 36), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
        elif number == '15':
            pygame.draw.circle(targ_surface, color, (17, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (31, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 26), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 26), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 26), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 26), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 36), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 36), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 36), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 36), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
        elif number == '16':
            pygame.draw.circle(targ_surface, color, (17, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 26), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 26), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 26), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 26), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 36), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 36), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 36), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 36), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
        elif number == '17':
            pygame.draw.circle(targ_surface, color, (17, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (24, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 24), 3, 3)
            pygame.draw.circle(targ_surface, color, (24, 24), 3, 3)
            pygame.draw.circle(targ_surface, color, (31, 31), 3, 3)
            pygame.draw.circle(targ_surface, color, (38, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (38, 24), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 24), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 38), 3, 3)
            pygame.draw.circle(targ_surface, color, (24, 38), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (24, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (38, 38), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 38), 3, 3)
            pygame.draw.circle(targ_surface, color, (38, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
        elif number == '18':
            pygame.draw.circle(targ_surface, color, (17, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (24, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 24), 3, 3)
            pygame.draw.circle(targ_surface, color, (24, 24), 3, 3)
            pygame.draw.circle(targ_surface, color, (26, 31), 3, 3)
            pygame.draw.circle(targ_surface, color, (36, 31), 3, 3)
            pygame.draw.circle(targ_surface, color, (38, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 17), 3, 3)
            pygame.draw.circle(targ_surface, color, (38, 24), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 24), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 38), 3, 3)
            pygame.draw.circle(targ_surface, color, (24, 38), 3, 3)
            pygame.draw.circle(targ_surface, color, (17, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (24, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (38, 38), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 38), 3, 3)
            pygame.draw.circle(targ_surface, color, (38, 45), 3, 3)
            pygame.draw.circle(targ_surface, color, (45, 45), 3, 3)
        if rot:
            targ_surface = pygame.transform.rotate(targ_surface, 90)
        self.surface.blit(targ_surface, pos)

    def draw(self, dmn: list, pos, rot=False, inv=False): # that's how simple it should've been...
        '''Draws the domino'''
        if rot:
            pygame.draw.rect(self.surface, self.color_fill, (pos[0], pos[1], 55, 115))
            pygame.draw.rect(self.surface, self.color_outline, (pos[0]-2, pos[1]-2, 59, 119), 4)
            pygame.draw.rect(self.surface, self.color_div, (pos[0] + 5, pos[1] + 55, 47, 3))
        else:
            pygame.draw.rect(self.surface, self.color_fill, (pos[0], pos[1], 115, 55))
            pygame.draw.rect(self.surface, self.color_outline, (pos[0]-2, pos[1]-2, 119, 59), 4)
            pygame.draw.rect(self.surface, self.color_div, (pos[0] + 55, pos[1] + 5, 3, 47))
        if type(dmn) == str:
            dmn = dmn.split('-')
            dmn[0] = int(dmn[0])
            dmn[1] = int(dmn[1])
        if not rot and not inv:
            self._draw_number((pos[0] - 3, pos[1] - 3), dmn[0], self.color_numbers[dmn[0] - 1])
            self._draw_number((pos[0] + 55, pos[1] - 3), dmn[1], self.color_numbers[dmn[1] - 1])
        elif inv and not rot:
            self._draw_number((pos[0] + 55, pos[1] - 3), dmn[0], self.color_numbers[dmn[0] - 1])
            self._draw_number((pos[0] - 3, pos[1] - 3), dmn[1], self.color_numbers[dmn[1] - 1])
        elif rot and not inv:
            self._draw_number((pos[0] - 3, pos[1] - 3), dmn[0], self.color_numbers[dmn[0] - 1], True)
            self._draw_number((pos[0] - 3, pos[1] + 55), dmn[1], self.color_numbers[dmn[1] - 1], True)
        elif rot and inv:
            self._draw_number((pos[0] - 3, pos[1] + 55), dmn[0], self.color_numbers[dmn[0] - 1], True)
            self._draw_number((pos[0] - 3, pos[1] - 3), dmn[1], self.color_numbers[dmn[1] - 1], True)

    def draw_scaled(self, dmn, pos, scale=1.0, rot=False, inv=False):
        if scale == 1:
            self.draw(dmn, pos, rot, inv)
            return
        targ_surface = self.surface
        if rot:
            self.surface = pygame.Surface((62, 122)).convert_alpha()
            x, y = 62, 122
        else:
            self.surface = pygame.Surface((122, 62)).convert_alpha()
            x, y = 122, 62
        self.surface.fill(pygame.Color(0, 0, 0, 0))
        self.draw(dmn, (3, 3), rot, inv)
        pos = [pos[0] - 3, pos[1] - 3] # imitates the legacy behavior
        transformed = pygame.transform.smoothscale(self.surface, (int(x*scale), int(y*scale)))
        targ_surface.blit(transformed, pos)
        self.surface = targ_surface

## testing code
# if __name__ == '__main__':
#     pygame.init()
#     window = pygame.display.set_mode((1280, 720))
#     dmn = Domino(window, (127, 127, 127), (20, 20, 20), (127, 127, 127), [(255, 0, 0),
#                                                                         (255, 128, 0),
#                                                                         (255, 255, 0),
#                                                                         (0, 255, 0),
#                                                                         (0, 255, 255),
#                                                                         (0, 96, 255),
#                                                                         (128, 0, 255),
#                                                                         (255, 0, 255),
#                                                                         (255, 255, 255),
#                                                                         (255, 0, 0),
#                                                                         (255, 128, 0),
#                                                                         (255, 255, 0),
#                                                                         (0, 255, 0),
#                                                                         (0, 255, 255),
#                                                                         (0, 96, 255),
#                                                                         (128, 0, 255),
#                                                                         (255, 0, 255),
#                                                                         (255, 255, 255)])
#     while True:
#         dmn.draw('1-2', (100, 100), True, True)
#         dmn.draw('3-4', (175, 100), True, False)
#         dmn.draw('5-6', (250, 100), False, True)
#         dmn.draw('7-8', (250, 160), False, False)
#         dmn.draw('9-10', (100, 220), True, True)
#         dmn.draw('11-12', (175, 220), True, False)
#         dmn.draw('13-14', (250, 220), False, True)
#         dmn.draw('15-16', (250, 280), False, False)
#         dmn.draw('17-18', (375, 100), True, True)
#         pygame.display.update()
#         pygame.event.get()