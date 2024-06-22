import pygame
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
background_path = r'c:\Users\lutfil\LTGYESSIR\slumberock.game\background4.png'
try:
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except pygame.error as e:
    print(f"Error loading background image: {e}")
    sys.exit()

# Load character images
try:
    character1_img = pygame.image.load('c:\Users\lutfil\LTGYESSIR\slumberock.game\Ajim_00.png')
    character2_img = pygame.image.load('c:\Users\lutfil\LTGYESSIR\slumberock.game\yaiz_00.png')
    character3_img = pygame.image.load('c:\Users\lutfil\LTGYESSIR\slumberock.game\lut_00.png')
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
music_path = 'slumberock.mp3'
try:
    background_music = pygame.mixer.Sound(music_path)
    background_music.set_volume(0.5)
    background_music.play(-1)
except pygame.error as e:
    print(f"Error loading background music: {e}")
    sys.exit()

# Play button
play_button_rect = pygame.Rect(270, 450, 200, 50)
play_text = custom_font.render('Play', True, RED)

# Game state
game_started = False

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pos = event.pos
                if play_button_rect.collidepoint(pos):
                    game_started = True
                else:
                    for player in players:
                        if player['rect'].collidepoint(pos):
                            if not player['selected']:
                                if sum(p['selected'] for p in players) < 3:
                                    player['selected'] = True
                            else:
                                player['selected'] = False

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

    if game_started:
        # Add your game logic here after the game starts
        pass

