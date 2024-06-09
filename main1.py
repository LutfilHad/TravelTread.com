import pygame
pygame.init()

win = pygame.display.set_mode((1100,700))
pygame.display.set_caption("slumberRock")
scr_width = 1100
scr_height = 700
x = 50
y = 600
width = 50
height = 70
vel =10
gravity_vel = 10
gravity_direction = "down" 
ajim = pygame.image.load('assets/MainCharacters /ajim/Ajim_00.png')
ajim = pygame.transform.scale(ajim, (width, height))
space_pressed = False

run = True

while run:
    pygame.time.delay(30)

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

    if gravity_direction == "down":
        flipped_ajim = ajim
    else:
        flipped_ajim = pygame.transform.flip(ajim, False, True)  


    win.fill((0,0,0))  
    win.blit(flipped_ajim, (x,y)) 
    pygame.display.update() 
    
pygame.quit()