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

rear_shoulder_left = None 
rear_leg_left = None 
rear_feet_left = None
rear_shoulder_right = None
rear_leg_right = None 
rear_feet_right = None  
front_shoulder_left = None 
front_leg_left = None 
front_feet_left = None
front_shoulder_right = None 
front_leg_right = None 
front_feet_right = None 

# motor instances, list contains empty instances
joints = [rear_shoulder_left, rear_leg_left, rear_feet_left, rear_shoulder_right, rear_leg_right, rear_feet_right, front_shoulder_left, front_leg_left, front_feet_left, front_shoulder_right, front_leg_right, front_feet_right]
joint_counter = 0

while not done:
    
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.

    joystick_count = pygame.joystick.get_count()

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        
        axis = joystick.get_numaxes()
            
        for i in range(axis):
            axis = joystick.get_axis(i)

        buttons = joystick.get_numbuttons()

        for i in range(buttons):
            button = joystick.get_button(i)

        hats = joystick.get_numhats()

        for i in range(hats):
            hat = joystick.get_hat(i)
        
        if (joystick.get_button(0) == True):
            while joint_counter < len(joints):
                joint = servo.Servo(pca.channels[motors_config_list[joint_counter]["channel"]])
                joint.set_pulse_width_range(motors_config_list[joint_counter]["min_pulse"],motors_config_list[joint_counter]["max_pulse"])
                joint.angle = int(motors_config_list[joint_counter]["rest_angle"])
                joint_counter += 1

    clock.tick(20)
    
pygame.quit()