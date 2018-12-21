import math
from pygame import *
import random

vec = math.Vector2

class Player(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = Surface((5,40))
        self.image.fill((100,100,100))
        self.rect = self.image.get_rect()
        self.rect.center = (250,700)
        self.pos = vec(250,570)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def update(self):
        changerx = random.randrange(-900,+900)
        changery = random.randrange(-900,900)
        changerx = changerx*0.001
        changery = changery*0.001
        self.acc = vec(changerx,changery)
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc
        self.rect.midbottom = self.pos

        # changer = random.randrange(-5, 0)
        # self.rect.y += changer