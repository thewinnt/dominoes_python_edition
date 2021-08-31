import pygame

pygame.init()
window = pygame.display.set_mode((1280, 720))

class Domino:
    def __init__(self, surface, color_outline=(0, 0, 0), color_fill=(240, 240, 240), color_div=(0, 0, 0), color_numbers=[(0, 0, 0)] * 9):
        self.surface = surface
        self.color_outline = color_outline
        self.color_div = color_div
        self.color_fill = color_fill
        self.color_numbers = color_numbers
    def _draw_number(self, pos, number, color, rot=False):
        if number == '0':
            return
        if not rot:
            if number == '1':
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+31), 3, 3)
            elif number == '2':
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+45), 3, 3)
            elif number == '3':
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+31), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+45), 3, 3)
            elif number == '4':
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+45), 3, 3)
            elif number == '5':
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+31), 3, 3)
            elif number == '6':
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+45), 3, 3)
            elif number == '7':
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+31), 3, 3)
            elif number == '8':
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+31), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+31), 3, 3)
            elif number == '9':
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+31), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+31), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+31), 3, 3)
        else:
            if number == '1':
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+31), 3, 3)
            elif number == '2':
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+45), 3, 3)
            elif number == '3':
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+31), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+45), 3, 3)
            elif number == '4':
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+45), 3, 3)
            elif number == '5':
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+31), 3, 3)
            elif number == '6':
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+31), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+31), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+17), 3, 3)
            elif number == '7':
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+31), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+31), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+31), 3, 3)
            elif number == '8':
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+31), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+31), 3, 3)
            elif number == '9':
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+17), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+45), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+17, pos[1]+31), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+45, pos[1]+31), 3, 3)
                pygame.draw.circle(self.surface, color, (pos[0]+31, pos[1]+31), 3, 3)

    def draw(self, type, pos, rot=False, inv=False): # that's how simple it should've been...
        '''Draws the domino'''
        if rot:
            pygame.draw.rect(self.surface, self.color_fill, (pos[0], pos[1], 55, 115))
            pygame.draw.rect(self.surface, self.color_outline, (pos[0]-2, pos[1]-2, 59, 119), 4)
            pygame.draw.rect(self.surface, self.color_div, (pos[0] + 5, pos[1] + 55, 47, 3))
        else:
            pygame.draw.rect(self.surface, self.color_fill, (pos[0], pos[1], 115, 55))
            pygame.draw.rect(self.surface, self.color_outline, (pos[0]-2, pos[1]-2, 119, 59), 4)
            pygame.draw.rect(self.surface, self.color_div, (pos[0] + 55, pos[1] + 5, 3, 47))
        if not rot and not inv:
            self._draw_number((pos[0] - 3, pos[1] - 3), type[0], self.color_numbers[int(type[0]) - 1])
            self._draw_number((pos[0] + 55, pos[1] - 3), type[1], self.color_numbers[int(type[1]) - 1])
        elif inv and not rot:
            self._draw_number((pos[0] + 55, pos[1] - 3), type[0], self.color_numbers[int(type[0]) - 1])
            self._draw_number((pos[0] - 3, pos[1] - 3), type[1], self.color_numbers[int(type[1]) - 1])
        elif rot and not inv:
            self._draw_number((pos[0] - 3, pos[1] - 3), type[0], self.color_numbers[int(type[0]) - 1], True)
            self._draw_number((pos[0] - 3, pos[1] + 55), type[1], self.color_numbers[int(type[1]) - 1], True)
        elif rot and inv:
            self._draw_number((pos[0] - 3, pos[1] + 55), type[0], self.color_numbers[int(type[0]) - 1], True)
            self._draw_number((pos[0] - 3, pos[1] - 3), type[1], self.color_numbers[int(type[1]) - 1], True)

    def draw_scaled(self, type, pos, scale=1.0, rot=False, inv=False):
        targ_surface = self.surface
        if rot:
            self.surface = pygame.Surface((59, 119))
            x, y = 59, 119
        else:
            self.surface = pygame.Surface((119, 59))
            x, y = 119, 59
        self.draw(type, (2, 2), rot, inv)
        pos = [pos[0] - 2, pos[1] - 2] # imitates the legacy behavior
        transformed = pygame.transform.smoothscale(self.surface, (int(x*scale), int(y*scale)))
        targ_surface.blit(transformed, pos)

## testing code
# if __name__ == '__main__':
#     dmn = domino(window, (127, 127, 127), (20, 20, 20), (127, 127, 127), [(255, 0, 0),
#                                                                         (255, 128, 0),
#                                                                         (255, 255, 0),
#                                                                         (0, 255, 0),
#                                                                         (0, 255, 255),
#                                                                         (0, 0, 255),
#                                                                         (128, 0, 255),
#                                                                         (255, 0, 255),
#                                                                         (255, 255, 255)])

#     while True:
#         dmn.draw('09', (100, 100), True, True)
#         dmn.draw('34', (175, 100), True, False)
#         dmn.draw('56', (250, 100), False, True)
#         dmn.draw('78', (250, 160), False, False)
#         pygame.display.update()
#         pygame.event.get()