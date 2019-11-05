import pygame

'''
11111
2   3    1: 3, 6
2   3    2: 1, 3, 4, 5, 7
2   3    3: 1, 3, 4, 6, 7
44444    4: 2, 3, 4, 6
5   6    5: 1, 2, 4, 6, 7
5   6    6: 1, 2, 4, 5, 6, 7
5   6    7: 1, 3, 6
77777
'''

configs = [
    [0, 1, 2, 4, 5, 6],
    [2, 5],
    [0, 2, 3, 4, 6],
    [0, 2, 3, 5, 6],
    [1, 2, 3, 5],
    [0, 1, 3, 5, 6],
    [0, 1, 3, 4, 5, 6],
    [0, 2, 5],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 5, 6]
]

class Digit:
    def __init__(self,segments):
        self.segments = segments

class Segment:
    def __init__(self,position):
        self.position = position
        self.start = [0, 0]
        self.end = [0, 0]
        self.on = False

    @property
    def a(self):
        return self.start
    
    @a.setter
    def a(self, new):
        self.start = new if (isinstance(new, list) and len(new) == 2) else self.start

    @property
    def b(self):
        return self.end

    @b.setter
    def b(self, new):
        self.end = new if (isinstance(new, list) and len(new) == 2) else self.end

def init(amount):
    global digits
    
    digits = [Digit({i:Segment(i) for i in range(7)}) for _ in range(amount)]

    for i,digit in enumerate(digits):
        digit.segments[0].a = [_boundary + (i * _width) + (i * _gap), _boundary]
        digit.segments[0].b = [_boundary + ((i+1) * _width) + (i * _gap), _boundary]

        digit.segments[1].a = [_boundary + (i * _width) + (i * _gap) , _boundary]
        digit.segments[1].b = [_boundary + (i * _width) + (i * _gap) , _boundary + _width]

        digit.segments[2].a = [_boundary + ((i+1) * _width) + (i * _gap), _boundary]
        digit.segments[2].b = [_boundary + ((i+1) * _width) + (i * _gap), _boundary + _width]

        digit.segments[3].a = [_boundary + (i * _width) + (i * _gap), _boundary + _width]
        digit.segments[3].b = [_boundary + ((i+1) * _width) + (i * _gap), _boundary + _width]

        digit.segments[4].a = [_boundary + (i * _width) + (i * _gap), _boundary + _width]
        digit.segments[4].b = [_boundary + (i * _width) + (i * _gap), _boundary + (2 * _width)]

        digit.segments[5].a = [_boundary + ((i+1) * _width) + (i * _gap), _boundary + _width]
        digit.segments[5].b = [_boundary + ((i+1) * _width) + (i * _gap), _boundary + (2 * _width)]

        digit.segments[6].a = [_boundary + (i * _width) + (i * _gap), _boundary + (2 * _width)]
        digit.segments[6].b = [_boundary + ((i+1) * _width) + (i * _gap), _boundary + (2 * _width)]

def draw(num):
    surf.fill((0, 0, 0))
    
    while len(num) > len(digits):
        num = str(int(num) - 10**len(digits))

    num = ((len(digits) - len(num)) * "0") + num

    for displayed, digit in list(reversed(list(zip(list(map(int, str(num)[::-1])), reversed(digits))))):
        for p, s in digit.segments.items():
            if p in configs[displayed]:
                s.on = True
            else:
                s.on = False
    
    for d in digits:
        for s in d.segments.values():
            pygame.draw.line(surf, (255 if s.on else 69, 0, 0), s.a, s.b, _bar_size)
