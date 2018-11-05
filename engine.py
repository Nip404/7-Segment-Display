import graphics
import pygame
import time
import sys

def init(_amount):
    global amount,windowsize
    
    amount = _amount

    try:
        windowsize = [(graphics._width*amount)+(graphics._gap*(amount-1))+(graphics._boundary*2),graphics._height+(graphics._boundary*2)+graphics._bar_size]
    except:
        pre_init()
        init(amount)

# sets dimensions
def pre_init(width=50,height=100,gap=10,bar_size=5,boundary=10):
    graphics._width = width
    graphics._height = height
    graphics._gap = gap
    graphics._bar_size = bar_size
    graphics._boundary = boundary

def generate_Display(surf,keys):
    global Display
    
    for key in keys:
        assert isinstance(key,int), "Keys must be valid pygame events"
        
    Display = _Display(surf,keys)

class _Display:
    def __init__(self,surf,keys):
        self.time = []
        
        self.started = False
        self.running = False

        self.start,self.pause,self.close = keys
        graphics.surf = surf
        graphics.init(amount)

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                try:
                    if event.key == self.start and not self.started:
                        self.started = True
                        self.running = True
                        self.time.append([time.time()]*2)
                        
                    elif event.key == self.pause:
                        self.running = not self.running

                        if self.running:
                            self.time.append([time.time()]*2)

                    elif event.key == self.close:
                        pygame.quit()
                        sys.exit()
                            
                except:
                    print(f"{event} not valid.")

    def update(self):
        if self.running:
            self.time[-1][-1] = time.time()
        graphics.draw(int(sum(i[1]-i[0] for i in self.time)))
