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

while joint_counter < 12:
    joint = servo.Servo(pca.channels[motors_config_list[joint_counter]["channel"]])
    joint.set_pulse_width_range(motors_config_list[joint_counter]["min_pulse"],motors_config_list[joint_counter]["max_pulse"])
    joint.angle = int(motors_config_list[joint_counter]["rest_angle"])
    joint_counter += 1

time.sleep(0.03)

