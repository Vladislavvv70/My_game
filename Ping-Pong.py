from pygame import *
from random import randint
from time import time as timer
mixer.init()

win_w = 1440
win_h = 980

main_win = display.set_mode((win_w,win_h))
display.set_caption('Шутер')

background = transform.scale(image.load('Background.png'), (win_w, win_h))



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, size_x, size_y, player_speed, player_x, player_y, s2):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.s2 = s2
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.image_name = player_image
    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()     
        if key_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < 625:
            self.rect.x += self.speed

game = True
finish = False

clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    main_win.blit(background, (0, 0))


    display.update()      
    clock.tick(FPS)              