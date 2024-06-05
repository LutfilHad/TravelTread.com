import pygame
import os

pygame.init()

SCR_HEIGHT = 600
SCR_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("/Users/ahmadmunqiz/Documents/GitHub/Slumberock/assets/MainCharacters /VirtualGuy", "idle.png")), 
           pygame.image.load(os.path.join("/Users/ahmadmunqiz/Documents/GitHub/Slumberock/assets/MainCharacters/VirtualGuy", "run.png")) ]
JUMPING = [pygame.image.load(os.path.join("/Users/ahmadmunqiz/Documents/GitHub/Slumberock/assets/MainCharacters/VirtualGuy", "jump.png"))]
DOUBLE_JUMPING = [pygame.image.load(os.path.join("/Users/ahmadmunqiz/Documents/GitHub/Slumberock/assets/MainCharacters/VirtualGuy", "double_jump.png"))]


class mainchr:
  x_pos = 80
  y_pos = 310

  def __init__(self):
    self.run_img = RUNNING
    self.jump_img = JUMPING
    self.doublejump_img = DOUBLE_JUMPING

    self.mainchr_run =True
    self.mainchr_jump = False
    self.mainchr_doublejump = False

    self.stepindex = 0
    self.image = self.run_img[0]
    self.mainchr_rect = self.image.get_rect()
    self.mainchr_rect.x = self.x_pos
    self.mainchr_rect.y = self.y_pos

  def update(self, userInput):
    if self.mainchr_run:
      self.run()
    if self.mainchr_jump:
      self.jump()
    if self.mainchr_run:
      self.doublejump() 

    if self.stepindex >= 10:
      self.stepindex = 0


    if userInput[pygame.K_UP]and not self.mainchr_jump:
      self.mainchr_run = False
      self.mainchr_jump = True
      self.mainchr_doublejump = False
    elif userInput[pygame.K_DOWN]and not self.mainchr_jump:
      self.mainchr_run = False
      self.mainchr_jump = False
      self.mainchr_doublejump = True
    elif not (self.mainchr_jump or userInput[pygame.K_DOWN]) :
      self.mainchr_run = True
      self.mainchr_jump = False
      self.mainchr_doublejump = False

  def run(self):
    self.image = self.run_img[self.step_index // 5]
    self.mainchr_rect = self.image.get_rect()
    self.mainchr_rect.x = self.x_pos
    self.mainchr_rect.y = self.y_pos
    self.step_index += 1   

  def jump (self):
    pass
  
  def double_jump(self):
    pass    

def draw(self, screen):
    screen.blit(self.image, (self.mainchr_rect.x, self.mainchr_rect.y))

def main():
    run = True
    clock = pygame.time.Clock()
    player = mainchr()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userinput = pygame.key.get_pressed()

        player.update(userinput)
        player.draw(SCREEN)

        clock.tick(30)
        pygame.display.update()

main()
