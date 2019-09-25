import graphics
import pygame
import time
import sys

def init(_amount):
    global amount, windowsize, surf

    pygame.init()
    amount = _amount

    try:
        windowsize = [(graphics._width * amount) + (graphics._gap * (amount-1)) + (graphics._boundary * 2),\
        graphics._height + (graphics._boundary * 2) + graphics._bar_size]
    except:
        pre_init()
        init(amount)

    screen = pygame.display.set_mode(windowsize, 0, 32)
    generate_Display(screen)

# sets dimensions
def pre_init(width=50, height=100, gap=10, bar_size=5, boundary=10):
    graphics._width = width
    graphics._height = height
    graphics._gap = gap
    graphics._bar_size = bar_size
    graphics._boundary = boundary

def caption(title):
    pygame.display.set_caption(title)

def generate_Display(surf):
    global Display
    Display = _Display(surf)

class _Display:
    def __init__(self, surf):
        graphics.surf = surf
        graphics.init(amount)

    def update(self, num, update_surf=True):
        if not isinstance(num, int):
            raise ValueError("Input to display must be type <int>.")

        graphics.draw(str(num))

        if update_surf:
            pygame.display.flip()
