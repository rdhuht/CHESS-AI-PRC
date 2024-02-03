import pygame

from const import *


class Game:
    def __init__(self) -> None:
        pass

    
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # print(row, col)
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                if (row + col) % 2 == 0:
                    color = (200, 234, 123)
                else:
                    color = (234, 154,88)
                pygame.draw.rect(surface, color, rect)
