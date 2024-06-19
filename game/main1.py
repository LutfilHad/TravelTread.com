import pygame
import random

pygame.init()

win = pygame.display.set_mode((1100,700))
pygame.display.set_caption("slumberRock")
scr_width = 1100
scr_height = 700
x = 50
y = 400
width = 50
height = 70
vel =5
gravity_vel = 7
gravity_direction = "down" 
ajim = pygame.image.load('assets/MainCharacters/ajim/Ajim_00.png')
ajim = pygame.transform.scale(ajim, (width, height))
space_pressed = False
game_over = False
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)

player_health = 300

background = pygame.image.load('assets/background/1BG.png').convert()
bg_width = scr_width
bg_height = scr_height
background = pygame.transform.scale(background, (bg_width, bg_height))
bg_x1 = 0
bg_x2 = bg_width
button_img = pygame.image.load('object/restart.png')


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprite = []
        self.load_sprites ()
        self.current_sprite = 0
        self.image = self.sprite[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.flipped_image = self.image

    def load_sprites(self):
        sprite_paths = [
            'assets/MainCharacters/ajim/Ajim_00.png',
            'assets/MainCharacters/ajim/Ajim_01.png',
            'assets/MainCharacters/ajim/Ajim_02.png',
            'assets/MainCharacters/ajim/Ajim_03.png',
            'assets/MainCharacters/ajim/Ajim_04.png',
            'assets/MainCharacters/ajim/Ajim_05.png',
            'assets/MainCharacters/ajim/Ajim_06.png',
            'assets/MainCharacters/ajim/Ajim_07.png',
            'assets/MainCharacters/ajim/Ajim_08.png',
            'assets/MainCharacters/ajim/Ajim_09.png'
        ]
        for path in sprite_paths:
            image = pygame.image.load(path)
            width = int(image.get_width() * 2)
            height = int(image.get_height() * 2)
            scaled_image = pygame.transform.scale(image, (width, height))
            self.sprite.append(scaled_image)


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

    def draw(self):
        pygame.draw.rect(win, GREY, self.rect, 2)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def update(self, vel):
        self.rect.x -= vel
        if self.rect.right < 0:
            self.kill()

def generate_platform(platforms, image_path, scr_width, scr_height, y_positions):
    platform_width = random.randint(200, 400)
    platform_height = 30
    platform_x = scr_width + random.randint(200, 300)
    platform_y = random.choice(y_positions)
    platform = Platform(platform_x, platform_y, platform_width, platform_height, image_path)
    platforms.add(platform)

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

player = Player(x, y)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

ajim = Player(100, int(scr_height / 2))

platform_image_path = 'assets/Terrain/platform3.png'
platforms = pygame.sprite.Group()
y_positions = [500, 400, 300, 200] 
for _ in range(4):
    generate_platform(platforms, platform_image_path, scr_width, scr_height, y_positions)

#character restart
button = Button(scr_width // 2 - 50, scr_height // 2 - 100, button_img)

run = True
platform_timer = 0 

while run:
    pygame.time.delay(30)

    

    
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

    platforms.update(vel)

    platform_timer += 1
    if platform_timer >= 60: 
        platform_timer = 0
        generate_platform(platforms, platform_image_path, scr_width, scr_height, y_positions)


    bg_x1 -= vel
    bg_x2 -= vel

    if bg_x1 <= -bg_width:
        bg_x1 = bg_width
    if bg_x2 <= -bg_width:
        bg_x2 = bg_width

    if pygame.sprite.spritecollide(player, platforms, False):
        if gravity_direction == "down":
            y -= gravity_vel  
        else:
            y += gravity_vel  

    win.fill((0,0,0))  
    win.blit(background, (bg_x1, 0))
    win.blit(background, (bg_x2, 0)) 
    win.blit(player.flipped_image, player.rect.topleft)
    platforms.draw(win)
    
    player.draw()
    pygame.draw.rect(win, RED,(20,20,300,15))
    pygame.draw.rect(win, GREEN,(20,20,player_health,15))
    
    if ajim.rect.left >= 0:
        game_over = True

    #check game over
    if game_over == True:
       if button.draw() == True:
             game_over = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            player_health -= 40
    
    pygame.display.update() 
    
pygame.quit()