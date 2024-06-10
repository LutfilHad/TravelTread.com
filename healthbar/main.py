import pygame, sys

pygame.init()

WIDTH = 1280
HEIGTH = 720

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption('Slumber Rock')

GRAVITY = 1
game_over = False

RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)

bg_image = pygame.image.load('graphics/teal.jpg').convert_alpha()
player_health = 400

player_image = pygame.image.load('graphics/Ajim_00.png').convert_alpha()

class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(player_image, (145, 145)) 
        self.width = 140
        self.heigth = 140
        self.rect = pygame.Rect(0, 0, self.width, self.heigth)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False

    def move(self):

        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx = - 10
            self.flip = True
        if key[pygame.K_d]:
            dx = 10
            self.flip = False
        if key[pygame.K_SPACE]:
            jumping = True

        #gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        #player dont go off
        if self.rect.left + dx < 0:
            dx = -self.left
        if self.rect.right + dx > WIDTH:
            dx = WIDTH - self.rect.right
        if self.rect.bottom +dy >HEIGTH:
            dy = 0

        
        #update rect position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 5, self.rect.y))
        pygame.draw.rect(screen, GREY, self.rect, 2)

player = Player(WIDTH //2 ,HEIGTH - 150)

run = True
while run:
  
    player.move() 

    clock.tick(60)
    screen.blit(bg_image, (0, 0))

    player.draw()
    pygame.draw.rect(screen, RED,(50,50,400,15))
    pygame.draw.rect(screen, GREEN,(50,50,player_health,15))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.QUIT
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            player_health -= 40

    pygame.display.update()





