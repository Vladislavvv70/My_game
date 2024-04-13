from pygame import *
from random import randint, choice
from time import time as timer
mixer.init()

win_w = 1440
win_h = 980

main_win = display.set_mode((win_w,win_h))
display.set_caption('Шутер')

background = transform.scale(image.load('galaxy.jpg'), (win_w, win_h))



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
    def update1(self):
        key_pressed = key.get_pressed()     
        if key_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 778:
            self.rect.y += self.speed
    def update2(self):
        key_pressed = key.get_pressed()     
        if key_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 778:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.s2
        if self.rect.y >= 950:
            self.speed *= -1
        if self.rect.y <= 0:
            self.speed *= -1



player_1 = Player('white.png', 30, 196, 15, 100, 325, 0)
player_2 = Player('white.png', 30, 196, 15, 1340, 325, 0)
ball = Ball('white.png', 30, 30, choice([10, -10]), 690, 460, choice([10, -10]))

game = True
finish = False

clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    main_win.blit(background, (0, 0))
    
    player_1.update1()
    player_2.update2()
    ball.update()

    player_1.reset()
    player_2.reset()
    ball.reset()
    

    display.update()      
    clock.tick(FPS)              
