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

i2c_bus = busio.I2C(SCL, SDA) # initiate the SCL and SDA pins on Raspberry Pi
pca = PCA9685(i2c_bus, address = 0x42) # set driver address
pca.frequency = 50 # set frequency of communication

while True:
        # list of all motors user can control
        options = {
        0: 'rear_shoulder_left - CHANNEL [' + str(motors_config_list[0]["channel"]) + ']',
        1: 'rear_leg_left - CHANNEL [' + str(motors_config_list[1]["channel"]) + ']',
        2: 'rear_feet_left - CHANNEL [' + str(motors_config_list[2]["channel"]) + ']',
        3: 'rear_shoulder_right - CHANNEL [' + str(motors_config_list[3]["channel"]) + ']',
        4: 'rear_leg_right - CHANNEL [' + str(motors_config_list[4]["channel"]) + ']',
        5: 'rear_feet_right - CHANNEL [' + str(motors_config_list[5]["channel"]) + ']',
        6: 'front_shoulder_left - CHANNEL [' + str(motors_config_list[6]["channel"]) + ']',
        7: 'front_leg_left - CHANNEL [' + str(motors_config_list[7]["channel"]) + ']',
        8: 'front_feet_left - CHANNEL [' + str(motors_config_list[8]["channel"]) + ']',
        9: 'front_shoulder_right - CHANNEL [' + str(motors_config_list[9]["channel"]) + ']',
        10: 'front_leg_right - CHANNEL [' + str(motors_config_list[10]["channel"]) + ']',
        11: 'front_feet_right - CHANNEL [' + str(motors_config_list[11]["channel"]) + ']'}
        
        # instructions displayed to instruct user
        title = 'Write "menu" or "m" and press Enter to return to the list of servos' + os.linesep + \
        'Write "exit" or "e" and press Enter to exit' + os.linesep + \
        '' + os.linesep + \
        'Please choose the servo to calibrate its rest position: '
        
        screen_options = list(options.values())

        # user chooses the option
        selected_option, selected_index = pick(screen_options, title)
        
        while True:
            # user enters angle for chosen motor
            user_input = int(input("Enter motor angle: "))
            # looks at config list and sets channel, min max pulse for chosen motor.
            active_joint = servo.Servo(pca.channels[motors_config_list[selected_index]["channel"]])
            active_joint.set_pulse_width_range(motors_config_list[selected_index]["min_pulse"],motors_config_list[selected_index]["max_pulse"])
            
            # processing user inputs
            if user_input == 'menu' or user_input == 'm':
                break
            elif user_input == 'exit' or user_input == 'e':
                sys.exit(0)
            else:
                active_joint.angle = int(user_input)
                print(selected_index)
            time.sleep(0.03)