import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprite = []
        self.sprite.append(pygame.image.load('assets/MainCharacters /ajim/Ajim_00.png'))
        self.sprite.append(pygame.image.load('assets/MainCharacters /ajim/Ajim_01.png'))
        self.sprite.append(pygame.image.load('assets/MainCharacters /ajim/Ajim_02.png'))
        self.sprite.append(pygame.image.load('assets/MainCharacters /ajim/Ajim_03.png'))
        self.sprite.append(pygame.image.load('assets/MainCharacters /ajim/Ajim_04.png'))
        self.sprite.append(pygame.image.load('assets/MainCharacters /ajim/Ajim_05.png'))
        self.sprite.append(pygame.image.load('assets/MainCharacters /ajim/Ajim_06.png'))
        self.sprite.append(pygame.image.load('assets/MainCharacters /ajim/Ajim_07.png'))
        self.sprite.append(pygame.image.load('assets/MainCharacters /ajim/Ajim_08.png'))
        self.sprite.append(pygame.image.load('assets/MainCharacters /ajim/Ajim_09.png'))
        self.current_sprite = 0
        self.image = self.sprite[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.flipped_image = self.image


    def update(self, gravity_direction, x, y):
        self.current_sprite += 0.2  
        if self.current_sprite >= len(self.sprite):
            self.current_sprite = 0  

        self.image = self.sprite[int(self.current_sprite)]
        if gravity_direction == "up":
            self.flipped_image = pygame.transform.flip(self.image, False, True)
        else:
            self.flipped_image = self.image

        self.rect.topleft = [x, y]            

pygame.init()

win = pygame.display.set_mode((1100,700))
pygame.display.set_caption("slumberRock")
scr_width = 1100
scr_height = 700
x = 50
y = 600
width = 50
height = 70
vel =5
gravity_vel = 7
gravity_direction = "down" 
ajim = pygame.image.load('assets/MainCharacters /ajim/Ajim_00.png')
ajim = pygame.transform.scale(ajim, (width, height))
space_pressed = False

player = Player(x, y)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

background = pygame.image.load('assets/background/1BG.png').convert()
bg_width = scr_width
bg_height = scr_height
background = pygame.transform.scale(background, (bg_width, bg_height))
bg_x1 = 0
bg_x2 = bg_width

run = True

while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        if not space_pressed:
            if gravity_direction == "down":
                gravity_direction = "up"
            else:
                gravity_direction = "down"
            space_pressed = True
    else:
        space_pressed = False

    x += vel

    if gravity_direction == "down":
        y += gravity_vel
    else:
        y -= gravity_vel    

    if y > scr_height - height:
        y = scr_height - height
    elif y < 0:
        y = 0

    if x > scr_width - width:
        x = 0

    player.update(gravity_direction, x, y)

    bg_x1 -= vel
    bg_x2 -= vel

    if bg_x1 <= -bg_width:
        bg_x1 = bg_width
    if bg_x2 <= -bg_width:
        bg_x2 = bg_width


    win.fill((0,0,0))  
    win.blit(background, (bg_x1, 0))
    win.blit(background, (bg_x2, 0)) 
    win.blit(player.flipped_image, player.rect.topleft)
    pygame.display.update() 
    
pygame.quit()