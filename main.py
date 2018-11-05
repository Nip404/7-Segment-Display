import engine
import pygame
import sys

pygame.init()
engine.init(4)

screen = pygame.display.set_mode(engine.windowsize,0,32)
engine.generate_Display(screen,[pygame.K_RETURN,pygame.K_SPACE,pygame.K_ESCAPE])

pygame.display.set_caption("7 Segment Display")

def main():
    while True:
        engine.Display.eventHandler()
        engine.Display.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()

