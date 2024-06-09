import pygame
pygame.init()

win = pygame.display.set_mode((1100,700))
pygame.display.set_caption("slumberRock")
scr_width = 1100
scr_height = 700
x = 50
y = 600
width = 40
height = 60
vel =5
gravity_vel = 5 
gravity_direction = "down" 

space_pressed = False

run = True

while run:
    pygame.time.delay(50)

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
        x=0


    win.fill((0,0,0)) 
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()