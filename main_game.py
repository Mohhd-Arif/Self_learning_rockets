from pygame import *
import random
from rockets.player import *


class Game:
    def __init__(self):
        init()
        mixer.init()
        self.screen = display.set_mode((500,720))
        display.set_caption("rocket genetic algorithm")
        self.animation_time = time.Clock()
        self.running = True

    def new(self):
        self.all_sprites = sprite.Group()
        self.player = sprite.Group()
        for x in range(50):
            x = Player()
            self.all_sprites.add(x)
            self.player.add(x)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.draw()
            self.update()
            self.animation_time.tick(60)

    def update(self):
        self.all_sprites.update()

    def events(self):
        for e in event.get():
            if e.type == QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill((0,0,0))
        self.all_sprites.draw(self.screen)
        display.update()
        display.flip()


game = Game()
while game.running:
    game.new()

quit()