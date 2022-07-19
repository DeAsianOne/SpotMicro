import pygame

pygame.init()

done = False
clock = pygame.time.Clock()
pygame.joystick.init()

import queue
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from config import motors_config_list
import time

i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus, address = 0x42)
pca.frequency = 50
joint_counter = 0

while not done:
    
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.

    joystick_count = pygame.joystick.get_count()

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        buttons = joystick.get_numbuttons()

        for i in range(buttons):
            button = joystick.get_button(i)
        
        if (joystick.get_button(0) == True):
            while joint_counter 12:
                joint = servo.Servo(pca.channels[motors_config_list[joint_counter]["channel"]])
                joint.set_pulse_width_range(motors_config_list[joint_counter]["min_pulse"],motors_config_list[joint_counter]["max_pulse"])
                joint.angle = int(motors_config_list[joint_counter]["rest_angle"])
                joint_counter += 1

    clock.tick(20)
    
pygame.quit()