import pygame
import random

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
        self.health = 3  # Health attribute
        self.heart_image = pygame.image.load('assets/heart.webp')  # Load heart image
        self.heart_image = pygame.transform.scale(self.heart_image, (30, 30))  # Scale heart image

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

    def draw_health_bar(self, win):
        heart_size = 30  # Size of the heart image
        heart_spacing = 5  # Spacing between hearts
        for i in range(self.health):
            heart_x = 10 + i * (heart_size + heart_spacing)
            heart_y = 10
            win.blit(self.heart_image, (heart_x, heart_y))

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
    win.fill((0, 0, 0))  # Fill screen with black background

    font = pygame.font.Font('object/font.ttf', 50)
    text = font.render("YOU ARE DEAD", True, (255, 0, 0))
    text_rect = text.get_rect(center=(550, 300))
    win.blit(text, text_rect)

    font = pygame.font.Font('object/font.ttf', 20)
    restart_text = font.render("Press R if you want to restart or Q to quit the game", True, (255, 255, 255))
    restart_rect = restart_text.get_rect(center=(550, 400))
    win.blit(restart_text, restart_rect)

def generate_platform(platforms, image_path, scr_width, scr_height, y_positions):
    platform_width = random.randint(200, 400)
    platform_height = 30
    platform_x = scr_width + random.randint(200, 300)
    platform_y = random.choice(y_positions)
    platform = Platform(platform_x, platform_y, platform_width, platform_height, image_path)
    platforms.add(platform)

def generate_trap(traps, platforms, image_path):
    if platforms:
        platform = random.choice(platforms.sprites())
        trap_width = 50
        trap_height = 50
        trap_x = random.randint(platform.rect.left, platform.rect.right - trap_width)
        trap_y = platform.rect.top - trap_height
        trap = Trap(trap_x, trap_y, trap_width, trap_height, image_path)
        traps.add(trap)

pygame.init()

win = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("slumberRock")
scr_width = 1100
scr_height = 700
x = 100  # Adjusted starting position
y = 400
width = 50
height = 70
vel = 8  # Increased player horizontal velocity
gravity_vel = 10
gravity_direction = "down"
ajim = pygame.image.load('assets/MainCharacters/ajim/Ajim_00.png')
ajim = pygame.transform.scale(ajim, (width, height))

player = Player(x, y)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

background = pygame.image.load('assets/background/1BG.png').convert()
bg_width = scr_width
bg_height = scr_height
background = pygame.transform.scale(background, (bg_width, bg_height))
bg_x1 = 0
bg_x2 = bg_width
platform_image_path = 'assets/Terrain/platform3.png'
platforms = pygame.sprite.Group()
traps = pygame.sprite.Group()
trap_image_path = 'assets/Traps/Idle.png'  # Path to your trap image
y_positions = [600, 400, 300, 200]
for _ in range(4):
    generate_platform(platforms, platform_image_path, scr_width, scr_height, y_positions)

run = True
platform_timer = 0
trap_timer = 0
bg_vel = 11 # Adjusted background scroll velocity
game_over = False

while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gravity_direction == "down":
                    gravity_direction = "up"
                else:
                    gravity_direction = "down"
            if event.key == pygame.K_r and game_over:
                # Restart game
                player.health = 3
                player.rect.topleft = (100, 400)
                traps.empty()
                platforms.empty()
                for _ in range(4):
                    generate_platform(platforms, platform_image_path, scr_width, scr_height, y_positions)
                game_over = False
            elif event.key == pygame.K_q and game_over:
                run = False

    if not game_over:
        if gravity_direction == "down":
            y += gravity_vel
        else:
            y -= gravity_vel

        if y > scr_height - height:
            y = scr_height - height
        elif y < 0:
            y = 0

        # Check collisions with platforms
        player.rect.y = y  # Update player's rect position
        collisions = pygame.sprite.spritecollide(player, platforms, False)
        if collisions:
            if gravity_direction == "down":
                y = collisions[0].rect.top - height
            else:
                y = collisions[0].rect.bottom
            player.rect.y = y  # Update player's rect position after adjustment

        player.update(gravity_direction, x, y)

        platforms.update(vel)
        traps.update(vel)

        platform_timer += 1
        if platform_timer >= 60:
            platform_timer = 0
            generate_platform(platforms, platform_image_path, scr_width, scr_height, y_positions)

        trap_timer += 1
        if trap_timer >= 50:  # Adjust as needed for trap generation frequency
            trap_timer = 0
            generate_trap(traps, platforms, trap_image_path)

        bg_x1 -= bg_vel  # Update background scroll speed
        bg_x2 -= bg_vel

        if bg_x1 <= -bg_width:
            bg_x1 = bg_width
        if bg_x2 <= -bg_width:
            bg_x2 = bg_width

        if pygame.sprite.spritecollide(player, traps, True):
            player.health -= 1
            if player.health <= 0:
                game_over = True

        win.fill((0, 0, 0))
        win.blit(background, (bg_x1, 0))
        win.blit(background, (bg_x2, 0))
        win.blit(player.flipped_image, player.rect.topleft)
        platforms.draw(win)
        traps.draw(win)
        player.draw_health_bar(win)

    else:
        draw_game_over_screen(win)

    pygame.display.update()

pygame.quit()
