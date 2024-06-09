import pygame
pygame.init()

win = pygame.display.set_mode((1100,700))
pygame.display.set_caption("slumberRock")
scr_width = 1100
scr_height = 700
x = 100
y = 600
width = 40
height = 60
vel =1/2
steps = 0 
gravity_direction = "down" 


run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if gravity_direction == "down":
        y += vel
    else:
        y -= vel    
    x += vel
    steps += 1
    if steps >= 10:
        x = 100
        y = 600
        steps = 0

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP] and y > vel and gravity_direction == "down":  
        y -= vel
    elif keys[pygame.K_DOWN] and y < scr_height - height - vel and gravity_direction == "down":
        y += vel
    elif keys[pygame.K_UP] and y < scr_height - height - vel and gravity_direction == "up":  
        y += vel
    elif keys[pygame.K_DOWN] and y > vel and gravity_direction == "up":
        y -= vel
    if keys[pygame.K_SPACE]:
        if gravity_direction == "down":
            gravity_direction = "up"
        else:
            gravity_direction = "down"
    
    win.fill((0,0,0)) 
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()