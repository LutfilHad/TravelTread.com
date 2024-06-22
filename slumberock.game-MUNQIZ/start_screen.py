import pygame
import sys

def start_screen(win, scr_width, scr_height):
    pygame.init()
    
    # Load custom fonts
    custom_font_path1 = 'assets/background/Robus-BWqOd.ttf'
    custom_font_path2 = 'assets/background/Atop-R99O3.ttf'
    font = pygame.font.Font(custom_font_path1, 150)
    button_font = pygame.font.Font(custom_font_path2, 30)
    
    title_text = font.render('SlumberRock', True, (192, 192, 192))
    button_text = button_font.render('Start Game', True, (255, 255, 255))
    
    button_rect = pygame.Rect((scr_width // 2) - 100, (scr_height // 2) + 50, 200, 50)
    
    # Load background image
    background = pygame.image.load('assets/background/City_Landscape_Background.jpg.webp')
    background = pygame.transform.scale(background, (scr_width, scr_height))
    
    run = True
    while run:
        win.fill((0, 0, 0))  # This line is optional as we'll cover the whole window with the background image
        win.blit(background, (0, 0))  # Draw the background image
        win.blit(title_text, ((scr_width // 2) - title_text.get_width() // 2, (scr_height // 2) - title_text.get_height() // 2 - 100))
        pygame.draw.rect(win, (0, 0, 255), button_rect)
        win.blit(button_text, (button_rect.x + (button_rect.width - button_text.get_width()) // 2, button_rect.y + (button_rect.height - button_text.get_height()) // 2))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    run = False

        pygame.display.update()


