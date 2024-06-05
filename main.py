import pygame
import os

pygame.init()

SCR_HEIGHT = 600
SCR_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("assets/MainCharacters /VirtualGuy", "idle.png")), 
           pygame.image.load(os.path.join("assets/MainCharacters /VirtualGuy", "run.png")) ]
JUMPING = [pygame.image.load(os.path.join("assets/MainCharacters /VirtualGuy", "jump.png"))]
DOUBLE_JUMPING = [pygame.image.load(os.path.join("assets/MainCharacters /VirtualGuy", "double_jump.png"))]



