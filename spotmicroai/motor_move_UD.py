import pygame
from IKUD import IKUD
from SpotClass import Spot

pygame.init()
done = False
clock = pygame.time.Clock()
pygame.joystick.init()

IKUD = IKUD()
Spot = Spot()

L0 = 5
shoulder_angle = 90
leg_angle = 180
feet_angle = 0

while not done:
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        hats = joystick.get_numhats()

        # Hat position. All or nothing for direction, not a float like
        # get_axis(). Position is a tuple of int values (x, y).
        for i in range(hats):
            hat = joystick.get_hat(i)
        
        if (joystick.get_hat(0) == (0,1)):
            L0 += 1
            leg_angle, feet_angle = IKUD.calculate_angle(L0)
        elif (joystick.get_hat(0) == (0,-1)):
            L0 -= 1
            leg_angle, feet_angle = IKUD.calculate_angle(L0)
            
    Spot.turn_motor(shoulder_angle, leg_angle, feet_angle)
    
    clock.tick(20)

pygame.close()
