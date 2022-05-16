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

for joint in joints:
    joint = servo.Servo(pca.channels[motors_config_list[joint_counter]["channel"]])
    joint.set_pulse_width_range(motors_config_list[joint_counter]["min_pulse"],motors_config_list[joint_counter]["max_pulse"])
    joint.angle = int(motors_config_list[joint_counter]["rest_angle"])
    joint_counter += 1

time.sleep(0.03)

