import pygame
import random
import sys
from start_screen import start_screen
import os  

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Select Three Players')

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
default_font = pygame.font.SysFont(None, 50) 
custom_font_path = 'Robus-BWqOd.otf'  
if os.path.isfile(custom_font_path):
    custom_font = pygame.font.Font(custom_font_path, 50)  
else:
    custom_font = default_font  

# Load background image
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Load character images
character1_img = pygame.image.load('Ajim_00.png')
character2_img = pygame.image.load('yaiz_00.png')
character3_img = pygame.image.load('lut_00.png')

# Resize character images
character1_img = pygame.transform.scale(character1_img, (100, 100))
character2_img = pygame.transform.scale(character2_img, (100, 100))
character3_img = pygame.transform.scale(character3_img, (100, 100))

# Player data
players = [
    {'name': 'adjim', 'rect': pygame.Rect(100, 100, 200, 50), 'selected': False, 'img': character1_img, 'font': custom_font},
    {'name': 'yaizz', 'rect': pygame.Rect(100, 200, 200, 50), 'selected': False, 'img': character2_img, 'font': custom_font},
    {'name': 'LTG', 'rect': pygame.Rect(100, 300, 200, 50), 'selected': False, 'img': character3_img, 'font': custom_font},
]

# Load background music and play it continuously
background_music = pygame.mixer.Sound('slumberock.mp3')
background_music.set_volume(0.5)
background_music.play(-1)  # -1 makes the sound play indefinitely

# Play button
play_button_rect = pygame.Rect(270, 450, 200, 50)
play_text = custom_font.render('Play', True, RED)

# Game state
game_started = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pos = event.pos
                if play_button_rect.collidepoint(pos):
                    game_started = True  # Start the game or perform any other action
                else:
                    for player in players:
                        if player['rect'].collidepoint(pos):
                            if not player['selected']:
                                if sum(p['selected'] for p in players) < 3:
                                    player['selected'] = True
                            else:
                                player['selected'] = False

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

    # Draw background
    screen.blit(background, (0, 0))

    # Draw players
    for player in players:
        color = GREEN if player['selected'] else BLUE
        text = player['font'].render(player['name'], True, color)
        screen.blit(text, (player['rect'].x + 10, player['rect'].y + 10))
        screen.blit(player['img'], (player['rect'].x + 220, player['rect'].y))

    # Draw play button
    screen.blit(play_text, (play_button_rect.centerx - play_text.get_width() // 2, play_button_rect.centery - play_text.get_height() // 2))

    # Update the display
    pygame.display.flip()


if __name__ == "__main__":
    main()