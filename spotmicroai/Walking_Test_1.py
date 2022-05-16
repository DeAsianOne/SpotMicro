# -*- coding: utf-8 -*-
import queue
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from config import motors_config_list
import time
import pygame
from IKUD import IKUD
from SpotClass import Spot

pygame.init()
done = False
clock = pygame.time.Clock()
pygame.joystick.init()

i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus, address = 0x42)
pca.frequency = 50

Spot = Spot()

from cmath import pi, sqrt
import math 

L1 = 11.5
L2 = 12

def find_angles(x, y, z, L1, L2):
    L3 = (x**2 + z**2)**(1/2)
    print(L3)
    angle_1 = math.atan(x/abs(z))
    angle_1 = (angle_1*180)/math.pi
    
    angle_2 = math.acos((L1**2+L3**2-L2**2)/(2*L1*L3))
    angle_2 = (angle_2*180)/math.pi
    
    angle_3 = 90 - (angle_1 + angle_2)
    
    angle_4 = math.acos((L1**2 + L2**2 - L3**2) / (2 * L1 * L2))
    angle_4 = (angle_4*180)/math.pi
    
    Shoulder_angle = 90
    Leg_angle = angle_3
    Feet_angle = angle_4

    return Shoulder_angle, Leg_angle, Feet_angle

def swing_phase(L1, L2):
    x = 0
    y = 0
    while x <= 8:
        z = ((16-(x-4)**2)**(1/2))-16
        Shoulder_angle, Leg_angle, Feet_angle = find_angles(x, y, z, L1, L2)
        print(Shoulder_angle, Leg_angle, Feet_angle)
        print(x, z)
        x += 0.5
        Spot.turn_rear_left(90, 180-Leg_angle, Feet_angle)
        time.sleep(0.5)

swing_phase(L1, L2)