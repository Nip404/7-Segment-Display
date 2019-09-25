import engine
from engine import pygame
import time
import sys

def counter():
    total = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                total += 1
            
        engine.Display.update(total)

if __name__ == "__main__":
    engine.init(2)
    engine.caption("Example - Counter display")

    counter()
