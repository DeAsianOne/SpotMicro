import pygame

pygame.init()

done = False

pygame.joystick.init()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 

    joystick_count = pygame.joystick.get_count()

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        buttons = joystick.get_numbuttons()

        for i in range(buttons):
            button = joystick.get_button(i)

        hats = joystick.get_numhats()

        for i in range(hats):
            hat = joystick.get_hat(i)
        
        if (joystick.get_hat(0) == (0,1)):
            print("A was pressed")
    
pygame.close()