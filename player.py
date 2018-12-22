import math
from pygame import *
import random
WIDTH = 600
HEIGHT = 720
counter = 0
vec = math.Vector2


class Player(sprite.Sprite):
    def __init__(self,game):
        sprite.Sprite.__init__(self)
        self.image = Surface((5,40))
        self.image.fill((100,100,100))
        self.game = game
        # draw.circle(self.image,(100,100,100),)
        self.rect = self.image.get_rect()
        self.rect.center = (250,700)
        self.pos = vec(250,570)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    # def respawn(self):
    #     global  counter
    #     counter = 0



    def update(self):
        changerx = random.randrange(-900,+900)
        changery = random.randrange(-900,900)
        changerx = changerx*0.001
        changery = changery*0.001
        self.acc = vec(changerx,changery)
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc
        self.rect.midbottom = self.pos
        if self.rect.x>WIDTH or self.rect.x<0 or self.rect.y>HEIGHT or self.rect.y<0:
            self.kill()
            global counter
            counter= counter+1
            print(counter)
            if counter > 99:
                counter= 0
                self.game.new()
        # changer = random.randrange(-5, 0)
        # self.rect.y += changer


class Target(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = Surface((20,20))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (250,100)

    def update(self):
        pass