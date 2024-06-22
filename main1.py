import pygame
import random
import sys
from start_screen import start_screen

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
            'assets/MainCharacters /ajim/Ajim_00.png',
            'assets/MainCharacters /ajim/Ajim_01.png',
            'assets/MainCharacters /ajim/Ajim_02.png',
            'assets/MainCharacters /ajim/Ajim_03.png',
            'assets/MainCharacters /ajim/Ajim_04.png',
            'assets/MainCharacters /ajim/Ajim_05.png',
            'assets/MainCharacters /ajim/Ajim_06.png',
            'assets/MainCharacters /ajim/Ajim_07.png',
            'assets/MainCharacters /ajim/Ajim_08.png',
            'assets/MainCharacters /ajim/Ajim_09.png'
        ]
        for path in sprite_paths:
            image = pygame.image.load(path)
            width = int(image.get_width() * 2)
            height = int(image.get_height() * 2)
            scaled_image = pygame.transform.scale(image, (width, height))
            self.sprite.append(scaled_image)

    def update(self, gravity_direction, y):
        self.current_sprite += 0.2  
        if self.current_sprite >= len(self.sprite):
            self.current_sprite = 0  

        self.image = self.sprite[int(self.current_sprite)]
        if gravity_direction == "up":
            self.flipped_image = pygame.transform.flip(self.image, False, True)
        else:
            self.flipped_image = self.image

        self.rect.topleft = [self.rect.x, y]           

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

def generate_platform(platforms, image_path, x, y, width, height):
    platform = Platform(x, y, width, height, image_path)
    platforms.add(platform)

def main():

    pygame.init()

    win = pygame.display.set_mode((1100,700))
    pygame.display.set_caption("slumberRock")
    scr_width = 1099 
    scr_height = 700
    player_x = 350
    y = 400
    width = 50
    height = 70
    vel = 5
    gravity_vel = 7
    gravity_direction = "down" 
    ajim = pygame.image.load('assets/MainCharacters /ajim/Ajim_00.png') 
    ajim = pygame.transform.scale(ajim, (width, height))
    space_pressed = False

    player = Player(player_x, y)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    background = pygame.image.load('assets/background/1BG.png').convert()
    bg_width = scr_width
    bg_height = scr_height
  
    bg_x1 = 1100
    bg_x2 = 0.01
    platform_image_path = 'assets/Terrain/platform3.png'
    platforms = pygame.sprite.Group()
    y_positions = [600, 400, 300, 200]

    # Generate initial platform under the player
    initial_platform_width = 300  # Added variable for initial platform width
    initial_platform_height = 30  # Added variable for initial platform height
    generate_platform(platforms, platform_image_path, player_x - initial_platform_width // 2, y + height, initial_platform_width, initial_platform_height)  # Generate initial platform

    # Generate additional platforms
    for steps in range(1, 10):  # Corrected loop range and function call
        generate_platform(platforms, platform_image_path, scr_width + steps * 100, random.choice(y_positions), random.randint(200, 400), 30)

    start_screen(win, scr_width, scr_height)

    run = True
    platform_timer = 0
    game_time = 0  # Initialize game time

    while run:
        pygame.time.delay(20)
        game_time += 1  # Increment game time

        # Increase speed every 500 frames (adjust as needed)
        if game_time % 100 == 0:
            gravity_vel += 0
            vel += 0.05

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

        if gravity_direction == "down":
            y += gravity_vel
        else:
            y -= gravity_vel

        if y > scr_height - height:
            y = scr_height - height
        elif y < 0:
            y = 0

        # Check if player touches top or bottom of screen
        if y <= 0 or y >= scr_height - height:
            run = False

        # Clamp y within screen boundaries
        y = max(0, min(y, scr_height - height))

        player.rect.topleft = [player_x, y]

        platforms.update(vel)

        platform_timer += 1
        if platform_timer >= 20:
            platform_timer = 0
            generate_platform(platforms, platform_image_path, scr_width + random.randint(200, 300), random.choice(y_positions), random.randint(200, 400), 30)  # Generate platforms periodically

        bg_x1 -= vel
        bg_x2 -= vel

        # Reset background images to maintain continuous scrolling
        if bg_x1 <= -bg_width:
            bg_x1 = bg_width
        if bg_x2 <= -bg_width:
            bg_x2 = bg_width

        collided_platforms = pygame.sprite.spritecollide(player, platforms, False)
        for platform in collided_platforms:
            if gravity_direction == "down":
                if player.rect.bottom > platform.rect.top and player.rect.top < platform.rect.top:
                    y = platform.rect.top - height
            elif gravity_direction == "up":
                if player.rect.top < platform.rect.bottom and player.rect.bottom > platform.rect.bottom:
                    y = platform.rect.bottom

        player.update(gravity_direction, y)

        win.fill((0, 0, 0))
        win.blit(background, (bg_x1, 0))
        win.blit(background, (bg_x2, 0))
        win.blit(player.flipped_image, player.rect.topleft)
        platforms.draw(win)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()