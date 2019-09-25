import engine
import pygame
import time
import sys

def timer():
    t0 = time.time()
    paused = False
    paused_time_elapsed = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                    
                    if paused:
                        paused_time_elapsed.append([time.time()]*2)
                    else:
                        paused_time_elapsed[-1][-1] = time.time()

        if not paused:
            engine.Display.update(int(time.time() - t0 - sum(map(lambda i: i[1]-i[0], paused_time_elapsed))))

if __name__ == "__main__":
    engine.init(4)
    engine.caption("7 Segment Display")

    timer()
