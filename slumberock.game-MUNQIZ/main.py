import pygame
import random
import sys
import os

# Initialize Pygame and mixer
try:
    pygame.init()
    pygame.mixer.init()
except Exception as e:
    print(f"Pygame initialization error: {e}")
    sys.exit()

# Screen dimensions
WIDTH, HEIGHT = 1100, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('slumberRock')

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
default_font = pygame.font.SysFont(None, 50)
custom_font_path = r'c:\Users\lutfil\LTGYESSIR\slumberock.game\Robus-BWqOd.otf'
if os.path.isfile(custom_font_path):
    custom_font = pygame.font.Font(custom_font_path, 50)
else:
    custom_font = default_font

# Load background image
background_path = r'c:\Users\lutfil\LTGYESSIR\slumberock.game\background4.png'
try:
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except pygame.error as e:
    print(f"Error loading background image: {e}")
    sys.exit()

# Load character images
try:
    character1_img = pygame.image.load(r'c:\Users\lutfil\LTGYESSIR\slumberock.game\Ajim_00.png')
    character2_img = pygame.image.load(r'c:\Users\lutfil\LTGYESSIR\slumberock.game\yaiz_00.png')
    character3_img = pygame.image.load(r'c:\Users\lutfil\LTGYESSIR\slumberock.game\lut_00.png')
except pygame.error as e:
    print(f"Error loading character images: {e}")
    sys.exit()

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
music_path = r'c:\Users\lutfil\LTGYESSIR\slumberock.game\slumberock.mp3'
try:
    background_music = pygame.mixer.Sound(music_path)
    background_music.set_volume(0.5)
    background_music.play(-1)
except pygame.error as e:
    print(f"Error loading background music: {e}")
    sys.exit()

# Menu options
menu_options = [
    {'text': 'Start Game', 'rect': pygame.Rect(300, 200, 200, 50), 'action': 'start_game'},
    {'text': 'Options', 'rect': pygame.Rect(300, 300, 200, 50), 'action': 'options'},
    {'text': 'Exit', 'rect': pygame.Rect(300, 400, 200, 50), 'action': 'exit'}
]

# Game state
current_state = 'menu'

def draw_menu():
    menu_background = pygame.image.load(r'c:\Users\lutfil\LTGYESSIR\slumberock.game\background4.png').convert()
    menu_background = pygame.transform.scale(menu_background, (WIDTH, HEIGHT))
    screen.blit(menu_background, (0, 0))
    
    for option in menu_options:
        text = custom_font.render(option['text'], True, BLUE)
        screen.blit(text, (option['rect'].x + 10, option['rect'].y + 10))

def handle_menu_click(pos):
    global current_state
    for option in menu_options:
        if option['rect'].collidepoint(pos):
            if option['action'] == 'start_game':
                current_state = 'character_select'
            elif option['action'] == 'options':
                # Handle options action (add your logic here)
                pass
            elif option['action'] == 'exit':
                pygame.quit()
                sys.exit()

def draw_character_select():
    # Draw background
    screen.blit(background, (0, 0))

    # Draw players
    for player in players:
        color = GREEN if player['selected'] else BLUE
        text = player['font'].render(player['name'], True, color)
        screen.blit(text, (player['rect'].x + 10, player['rect'].y + 10))
        screen.blit(player['img'], (player['rect'].x + 220, player['rect'].y))

    # Draw play button
    play_button_rect = pygame.Rect(270, 450, 200, 50)
    play_text = custom_font.render('Play', True, RED)
    screen.blit(play_text, (play_button_rect.centerx - play_text.get_width() // 2, play_button_rect.centery - play_text.get_height() // 2))

def handle_character_select_click(pos):
    global current_state
    play_button_rect = pygame.Rect(270, 450, 200, 50)
    if play_button_rect.collidepoint(pos):
        current_state = 'game'
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
        self.load_sprites()
        self.current_sprite = 0
        self.image = self.sprite[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.flipped_image = self.image
        self.health = 3
        self.max_health = 3

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
            'assets/MainCharacters/ajim/Ajim_09.png',
        ]
        for path in sprite_paths:
            image = pygame.image.load(path).convert_alpha()
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

    def hit_trap(self):
        self.health -= 1 # Decrease health when hit by a trap
        if self.health < 0:
            self.health = 0  # Ensure health doesn't go below zero

    def draw_health_bar(self, surface):
        # Calculate width of health bar based on current health
        bar_length = 100
        bar_height = 10
        fill = (self.health / self.max_health) * bar_length
        outline_rect = pygame.Rect(10, 10, bar_length, bar_height)
        fill_rect = pygame.Rect(10, 10, fill, bar_height)
        
        # Draw health bar
        pygame.draw.rect(surface, (255, 0, 0), fill_rect)
        pygame.draw.rect(surface, (0, 0, 0), outline_rect, 2)

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

class Trap(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image_path):
        super().__init__()
        self.image = pygame.image


        self.rect.topleft = [self.rect.x, y]  
    

    def hit_trap(self):
        self.health -= 1 # Decrease health when hit by a trap
        if self.health < 0:
            self.health = 0  # Ensure health doesn't go below zero

    def draw_health_bar(self, surface):
        # Calculate width of health bar based on current health
        bar_length = 100
        bar_height = 10
        fill = (self.health / self.max_health) * bar_length
        outline_rect = pygame.Rect(10, 10, bar_length, bar_height)
        fill_rect = pygame.Rect(10, 10, fill, bar_height)
        
        # Draw health bar
        pygame.draw.rect(surface, (255, 0, 0), fill_rect)
        pygame.draw.rect(surface, (0, 0, 0), outline_rect, 2)

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

class Trap(pygame.sprite.Sprite):
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

    def draw_game_over_screen(win):
        win.fill((0, 0, 0))

        font = pygame.font.Font('object/font.ttf', 50)
        text = font.render("YOU ARE DEAD", True, (255, 0, 0))
        text_rect = text.get_rect(center=(550, 300))
        win.blit(text, text_rect)

        font = pygame.font.Font('object/font.ttf', 20)
        restart_text = font.render("Press R if you want to restart or Q to quit the game", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(550, 400))
        win.blit(restart_text, restart_rect)

def generate_platform(platforms, traps, platform_image_path, trap_image_path, x, y, width, height):
    platform = Platform(x, y, width, height, platform_image_path)
    platforms.add(platform)

    if random.random() < 0.5:  # 50% chance to add a trap
        trap_x = x + random.randint(0, width - 30)  # Adjust the 30 to the width of the trap image
        trap_y = y - 30  # Adjust the 30 to the height of the trap image
        trap = Trap(trap_x, trap_y, 30, 30, trap_image_path)  # Adjust the width and height to the trap image dimensions
        traps.add(trap)

def main_game():
    pygame.init()

    win = pygame.display.set_mode((1100, 700))
    pygame.display.set_caption("SlumbeRock")
    scr_width = 1099 
    scr_height = 700
    player_x = 350
    y = 400
    width = 50
    height = 70
    vel = 5
    gravity_vel = 7
    gravity_direction = "down" 
    ajim = pygame.image.load('assets/MainCharacters/ajim/Ajim_00.png') 
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
    trap_image_path = 'assets/Traps/Idle.png'
    platforms = pygame.sprite.Group()
    traps = pygame.sprite.Group()
    y_positions = [600, 400, 300, 200]

    # Generate initial platform under the player
    initial_platform_width = 300  # Added variable for initial platform width
    initial_platform_height = 30  # Added variable for initial platform height
    generate_platform(platforms, traps, platform_image_path, trap_image_path, player_x - initial_platform_width // 2, y + height, initial_platform_width, initial_platform_height)  # Generate initial platform

    # Generate additional platforms
    for steps in range(1, 10):  # Corrected loop range and function call
        generate_platform(platforms, traps, platform_image_path, trap_image_path, scr_width + steps * 100, random.choice(y_positions), random.randint(200, 400), 30)

    run = True
    platform_timer = 0
    game_time = 0  # Initialize game time
    speed_increase_interval = 500
    game_over = False
    while run:
        pygame.time.delay(20)
        game_time += 1  # Increment game time

        # Increase speed every 500 frames (adjust as needed)
        if game_time % speed_increase_interval == 0:
            gravity_vel += 0.5
            vel += 0.5

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
        traps.update(vel)

        platform_timer += 1
        if platform_timer >= 20:
            platform_timer = 0
            generate_platform(platforms, traps, platform_image_path, trap_image_path, scr_width + random.randint(200, 300), random.choice(y_positions), random.randint(200, 400), 30)  # Generate platforms periodically

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

        collided_traps = pygame.sprite.spritecollide(player, traps, False)
        if collided_traps:
            game_over()  # Call game_over function when player collides with trap
            break  # Exit the main game loop on game over

        player.update(gravity_direction, y)

        win.fill((0, 0, 0))
        win.blit(background, (bg_x1, 0))
        win.blit(background, (bg_x2, 0))
        win.blit(player.flipped_image, player.rect.topleft)
        platforms.draw(win)
        traps.draw(win)

        pygame.display.update()

    pygame.quit()


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pos = event.pos
                if current_state == 'menu':
                    handle_menu_click(pos)
                elif current_state == 'character_select':
                    handle_character_select_click(pos)

    if current_state == 'menu':
        draw_menu()
    elif current_state == 'character_select':
        draw_character_select()

    pygame.display.flip()

    if current_state == 'game':
        main_game()
        current_state = 'menu'  # Reset to menu after game ends
