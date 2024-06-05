import os
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

RUNNING = [pygame.image.load(os.path.join("/Users/ahmadmunqiz/Documents/GitHub/Slumberock/assets/MainCharacters /VirtualGuy", "run.png"))]
JUMPING = [pygame.image.load(os.path.join("/Users/ahmadmunqiz/Documents/GitHub/Slumberock/assets/MainCharacters /VirtualGuy", "jump.png"))]

class Character:
    x_pos = 80
    y_pos = 300

    def __init__(self):
        self.run_imgs = RUNNING
        self.jump_imgs = JUMPING

        self.mc_run = True
        self.mc_jump = False

        self.step_index = 0 
        self.image = self.run_imgs[0]
        self.mc_rect = self.image.get_rect()
        self.mc_rect.x = self.x_pos
        self.mc_rect.y = self.y_pos

    def update(self, userinput):
        if self.mc_run :
            self.run
        if self.mc_jump :
            self.mc_jump

        if self.step_index >= 10:
            self.step_index = 0

        if userinput[pygame.K_UP] and not self.mc_jump:
            self.mc_run = False 
            self.mc_jump = True
        elif userinput[pygame.K_UP] and not self.mc_jump:  
            self.mc_run = True    
            self.mc_jump = False

    def run(self) :
        self.image = self.run_imgs[self.step_index // 5]
        self.mc_rect = self.image.get_rect()
        self.mc_rect.x = self.x_pos
        self.mc_rect.y = self.y_pos

    def jump(self):
        pass

def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image

def draw(window, background, bg_image, self):
    for tile in background:
        window.blit(bg_image, tile, (self.mc_rect.x, self.mc_rect.y))
    
    pygame.display.update()
  

def main(window):
  clock = pygame.time.Clock()
  background, bg_image = get_background("srbg.png")
  player = Character()


  run = True
  while run :
     clock.tick(FPS)

     for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
           break
     draw(window, background, bg_image, player )
     userinput = pygame.key.get_pressed()

     player.draw(window)
     player.update(userinput)
  pygame.quit()
  quit()  

if __name__ == "__main__" :
    main(window) 
