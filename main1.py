import pygame
import random
import sys
from start_screen import start_screen

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

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, control_flip, sprite_paths):
        super().__init__()
        self.sprite = []
        self.load_sprites(sprite_paths)
        self.current_sprite = 0
        self.image = self.sprite[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.flipped_image = self.image
        self.control_flip = control_flip
        self.gravity_direction = "down"  # Start with downward gravity

    def load_sprites(self, sprite_paths):
        for path in sprite_paths:
            image = pygame.image.load(path)
            width = int(image.get_width() * 2)
            height = int(image.get_height() * 2)
            scaled_image = pygame.transform.scale(image, (width, height))
            self.sprite.append(scaled_image)

    def update(self, y, gravity_vel):
        self.current_sprite += 0.1  # Adjust the increment for smoother animation
        if self.current_sprite >= len(self.sprite):
            self.current_sprite = 0

        self.image = self.sprite[int(self.current_sprite)]
        if self.gravity_direction == "up":
            self.flipped_image = pygame.transform.flip(self.image, False, True)
        else:
            self.flipped_image = self.image

        self.rect.topleft = [self.rect.x, y]

    def flip_gravity(self):
        if self.gravity_direction == "down":
            self.gravity_direction = "up"
        else:
            self.gravity_direction = "down"

def generate_platform(platforms, image_path, x, y, width, height):
    platform = Platform(x, y, width, height, image_path)
    platforms.add(platform)

def main():
    pygame.init()

    win = pygame.display.set_mode((1100, 700))
    pygame.display.set_caption("Slumberock")
    scr_width = 1100 
    scr_height = 700
    player1_x = 350
    player2_x = 700
    y1 = 400  # Vertical position for player 1
    y2 = 400  # Vertical position for player 2
    width = 50
    height = 70
    vel = 5
    gravity_vel = 7

    player1_flip = pygame.K_SPACE  # Player 1 control (Space to flip gravity)
    player2_flip = pygame.K_UP     # Player 2 control (Up arrow to flip gravity)

    player1_sprite_paths = [
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

    player2_sprite_paths = [
        'assets/MainCharacters /yaiz/yaiz_00.png',
        'assets/MainCharacters /yaiz/yaiz_01.png',
        'assets/MainCharacters /yaiz/yaiz_02.png',
        'assets/MainCharacters /yaiz/yaiz_03.png',
        'assets/MainCharacters /yaiz/yaiz_04.png',
        'assets/MainCharacters /yaiz/yaiz_05.png',
        'assets/MainCharacters /yaiz/yaiz_06.png',
        'assets/MainCharacters /yaiz/yaiz_07.png',
        'assets/MainCharacters /yaiz/yaiz_08.png',
        'assets/MainCharacters /yaiz/yaiz_09.png'
    ]

    player1 = Player(player1_x, y1, player1_flip, player1_sprite_paths)
    player2 = Player(player2_x, y2, player2_flip, player2_sprite_paths)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player1, player2)

    background = pygame.image.load('assets/background/1BG.png').convert()
    bg_width = scr_width
    bg_height = scr_height
    bg_x1 = 0
    bg_x2 = bg_width
    platform_image_path = 'assets/Terrain/platform3.png'
    platforms = pygame.sprite.Group()
    y_positions = [600, 400, 300, 200]

    # Generate initial platform under each player
    initial_platform_width = 300
    initial_platform_height = 30
    generate_platform(platforms, platform_image_path, player1_x - initial_platform_width // 2, y1 + height, initial_platform_width, initial_platform_height)
    generate_platform(platforms, platform_image_path, player2_x - initial_platform_width // 2, y2 + height, initial_platform_width, initial_platform_height)

    # Generate additional platforms
    for steps in range(1, 10):
        generate_platform(platforms, platform_image_path, scr_width + steps * 100, random.choice(y_positions), random.randint(200, 400), 30)

    start_screen(win, scr_width, scr_height)

    run = True
    platform_timer = 0
    game_time = 0

    while run:
        pygame.time.delay(20)
        game_time += 1

        if game_time % 500 == 0:
            gravity_vel += 1
            vel += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        # Player 1 controls
        if keys[player1.control_flip]:
            player1.flip_gravity()

        # Player 2 controls
        if keys[player2.control_flip]:
            player2.flip_gravity()

        # Update player positions based on gravity direction
        if player1.gravity_direction == "up":
            y1 -= gravity_vel
        else:
            y1 += gravity_vel

        if player2.gravity_direction == "up":
            y2 -= gravity_vel
        else:
            y2 += gravity_vel

        # Ensure player1 stays within screen boundaries
        if y1 > scr_height - height:
            y1 = scr_height - height
        elif y1 < 0:
            y1 = 0

        # Ensure player2 stays within screen boundaries
        if y2 > scr_height - height:
            y2 = scr_height - height
        elif y2 < 0:
            y2 = 0

        player1.rect.topleft = [player1_x, y1]
        player2.rect.topleft = [player2_x, y2]

        platforms.update(vel)

        platform_timer += 1
        if platform_timer >= 20:
            platform_timer = 0
            generate_platform(platforms, platform_image_path, scr_width + random.randint(200, 300), random.choice(y_positions), random.randint(200, 400), 30)

        bg_x1 -= vel
        bg_x2 -= vel

        if bg_x1 <= -bg_width:
            bg_x1 = bg_width
        if bg_x2 <= -bg_width:
            bg_x2 = bg_width

        # Collision handling for player 1
        collided_platforms1 = pygame.sprite.spritecollide(player1, platforms, False)
        for platform in collided_platforms1:
            if player1.gravity_direction == "down":
                if player1.rect.bottom > platform.rect.top and player1.rect.top < platform.rect.top:
                    y1 = platform.rect.top - height
            elif player1.gravity_direction == "up":
                if player1.rect.top < platform.rect.bottom and player1.rect.bottom > platform.rect.bottom:
                    y1 = platform.rect.bottom

        # Collision handling for player 2
        collided_platforms2 = pygame.sprite.spritecollide(player2, platforms, False)
        for platform in collided_platforms2:
            if player2.gravity_direction == "down":
                if player2.rect.bottom > platform.rect.top and player2.rect.top < platform.rect.top:
                    y2 = platform.rect.top - height
            elif player2.gravity_direction == "up":
                if player2.rect.top < platform.rect.bottom and player2.rect.bottom > platform.rect.bottom:
                    y2 = platform.rect.bottom

        player1.update(y1, gravity_vel)
        player2.update(y2, gravity_vel)

        win.fill((0, 0, 0))
        win.blit(background, (bg_x1, 0))
        win.blit(background, (bg_x2, 0))
        win.blit(player1.flipped_image, player1.rect.topleft)
        win.blit(player2.flipped_image, player2.rect.topleft)
        platforms.draw(win)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()