import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("SlumberRock")


WIDTH, HEIGHT = 1220, 600
FPS = 40
PLAYER_VEL = 8
GRAVITY = 0.8
FLAP = -10
window = pygame.display.set_mode((WIDTH, HEIGHT))

def flip(sprites):
    return[pygame.transform.flip(sprites, True, True) for sprite in sprites]
def load_sprite_sheets()
class Player(pygame.sprite.Sprite):
    COLOR = (255, 231, 0)

    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(self.COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x_vel = 0
        self.y_vel = 0
        self.gravity = GRAVITY
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    def update(self):
        self.y_vel += self.gravity
        self.rect.y += self.y_vel

        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            self.rect.y -= self.y_vel
            self.y_vel = 0

    def flap(self):
        self.y_vel = FLAP
        self.gravity *= -1

        
        
def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image

def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)
    
    window.blit(player.image, player.rect)
    pygame.display.update()
  

def main(window):
  clock = pygame.time.Clock()
  background, bg_image = get_background("srbg.png")
  player = Player(WIDTH // 4, HEIGHT // 2, 50, 50)



  run = True
  while run :
     clock.tick(FPS)

     for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
           break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.flap()


     draw(window, background, bg_image, player)
  pygame.quit()
  quit()  

if __name__ == "__main__" :
    main(window) 
