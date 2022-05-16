import queue
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from config import motors_config_list
import time
import os
from pick import pick
import sys
from SpotClass import Spot
Spot = Spot()

while True:
        selected_option = int(input("Number leg:"))
        
        if selected_option == 1:
            while True:
                user_input = int(input("Enter shoulder angle: "))
                shoulder_angle = user_input
                user_input = int(input("Enter leg angle: "))
                leg_angle = user_input
                user_input = int(input("Enter feet angle: "))
                feet_angle = user_input
                if user_input == 'menu' or user_input == 'm':
                    break
                elif user_input == 'exit' or user_input == 'e':
                    sys.exit(0)
                else:
                    Spot.turn_rear_left(shoulder_angle, leg_angle, feet_angle)
                time.sleep(0.03)
                
        if selected_option == 2:
            while True:
                user_input = int(input("Enter shoulder angle: "))
                shoulder_angle = user_input
                user_input = int(input("Enter leg angle: "))
                leg_angle = user_input
                user_input = int(input("Enter feet angle: "))
                feet_angle = user_input
                
                if user_input == 'menu' or user_input == 'm':
                    break
                elif user_input == 'exit' or user_input == 'e':
                    sys.exit(0)
                else:
                    Spot.turn_rear_right(shoulder_angle, leg_angle, feet_angle)
                time.sleep(0.03)
                
        if selected_option == 3:
            while True:
                user_input = int(input("Enter shoulder angle: "))
                shoulder_angle = user_input
                user_input = int(input("Enter leg angle: "))
                leg_angle = user_input
                user_input = int(input("Enter feet angle: "))
                feet_angle = user_input
                
                if user_input == 'menu' or user_input == 'm':
                    break
                elif user_input == 'exit' or user_input == 'e':
                    sys.exit(0)
                else:
                    Spot.turn_front_left(shoulder_angle, leg_angle, feet_angle)
                time.sleep(0.03)
                
        if selected_option == 4:
            while True:
                user_input = int(input("Enter shoulder angle: "))
                shoulder_angle = user_input
                user_input = int(input("Enter leg angle: "))
                leg_angle = user_input
                user_input = int(input("Enter feet angle: "))
                feet_angle = user_input
                
                if user_input == 'menu' or user_input == 'm':
                    break
                elif user_input == 'exit' or user_input == 'e':
                    sys.exit(0)
                else:
                    Spot.turn_front_right(shoulder_angle, leg_angle, feet_angle)
                time.sleep(0.03)