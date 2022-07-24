import queue
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from config import motors_config_list


class Spot():
    i2c_bus = busio.I2C(SCL, SDA)
    pca = PCA9685(i2c_bus, address = 0x42)
    pca.frequency = 50 
    
    rear_shoulder_left = servo.Servo(pca.channels[motors_config_list[0]["channel"]])
    rear_shoulder_left.set_pulse_width_range(motors_config_list[0]["min_pulse"],motors_config_list[0]["max_pulse"])
    
    rear_leg_left = servo.Servo(pca.channels[motors_config_list[1]["channel"]])
    rear_leg_left.set_pulse_width_range(motors_config_list[1]["min_pulse"],motors_config_list[1]["max_pulse"])
    
    rear_feet_left = servo.Servo(pca.channels[motors_config_list[2]["channel"]])
    rear_feet_left.set_pulse_width_range(motors_config_list[2]["min_pulse"],motors_config_list[2]["max_pulse"])
    
    rear_shoulder_right = servo.Servo(pca.channels[motors_config_list[3]["channel"]])
    rear_shoulder_right.set_pulse_width_range(motors_config_list[3]["min_pulse"],motors_config_list[3]["max_pulse"])
    
    rear_leg_right = servo.Servo(pca.channels[motors_config_list[4]["channel"]])
    rear_leg_right.set_pulse_width_range(motors_config_list[4]["min_pulse"],motors_config_list[4]["max_pulse"])
    
    rear_feet_right = servo.Servo(pca.channels[motors_config_list[5]["channel"]])  
    rear_feet_right.set_pulse_width_range(motors_config_list[5]["min_pulse"],motors_config_list[5]["max_pulse"])
    
    front_shoulder_left = servo.Servo(pca.channels[motors_config_list[6]["channel"]])
    front_shoulder_left.set_pulse_width_range(motors_config_list[6]["min_pulse"],motors_config_list[6]["max_pulse"])
    
    front_leg_left = servo.Servo(pca.channels[motors_config_list[7]["channel"]])
    front_leg_left.set_pulse_width_range(motors_config_list[7]["min_pulse"],motors_config_list[7]["max_pulse"])
    
    front_feet_left = servo.Servo(pca.channels[motors_config_list[8]["channel"]])
    front_feet_left.set_pulse_width_range(motors_config_list[8]["min_pulse"],motors_config_list[8]["max_pulse"])
    
    front_shoulder_right = servo.Servo(pca.channels[motors_config_list[9]["channel"]])
    front_shoulder_right.set_pulse_width_range(motors_config_list[9]["min_pulse"],motors_config_list[9]["max_pulse"])
    
    front_leg_right = servo.Servo(pca.channels[motors_config_list[10]["channel"]])
    front_leg_right.set_pulse_width_range(motors_config_list[10]["min_pulse"],motors_config_list[10]["max_pulse"])
    
    front_feet_right = servo.Servo(pca.channels[motors_config_list[11]["channel"]])
    front_feet_right.set_pulse_width_range(motors_config_list[11]["min_pulse"],motors_config_list[11]["max_pulse"])
    
    
    def turn_rear_left(self, shoulder_angle, leg_angle, feet_angle):
        
        self.rear_shoulder_left.angle = shoulder_angle
        self.rear_leg_left.angle = leg_angle
        self.rear_feet_left.angle = feet_angle

    def turn_rear_right(self, shoulder_angle, leg_angle, feet_angle):
        
        self.rear_shoulder_right.angle = 180 - shoulder_angle
        self.rear_leg_right.angle = 180 - leg_angle
        self.rear_feet_right.angle = 180 - feet_angle
        
    def turn_front_left(self, shoulder_angle, leg_angle, feet_angle):
        
        self.front_shoulder_left.angle = shoulder_angle
        self.front_leg_left.angle = leg_angle
        self.front_feet_left.angle = feet_angle
    
    def turn_front_right(self, shoulder_angle, leg_angle, feet_angle):
        
        self.front_shoulder_right.angle = 180 - shoulder_angle
        self.front_leg_right.angle = 180 - leg_angle
        self.front_feet_right.angle = 180 - feet_angle
    
    def turn_motor(self, shoulder_angle, leg_angle, feet_angle):
        
        self.rear_shoulder_left.angle = shoulder_angle
        self.rear_leg_left.angle = leg_angle
        self.rear_feet_left.angle = feet_angle
        
        self.rear_shoulder_right.angle = 180 - shoulder_angle
        self.rear_leg_right.angle = 180 - leg_angle
        self.rear_feet_right.angle = 180 - feet_angle
        
        self.front_shoulder_left.angle = shoulder_angle
        self.front_leg_left.angle = leg_angle
        self.front_feet_left.angle = feet_angle
        
        self.front_shoulder_right.angle = 180 - shoulder_angle
        self.front_leg_right.angle = 180 - leg_angle
        self.front_feet_right.angle = 180 - feet_angle
        
