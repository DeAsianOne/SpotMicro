# -*- coding: utf-8 -*-
import sys
import csv
import time

import SpotClass as sp

def main():
    Spot = sp.Spot()
    while True:
        with open('3_motors.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                angles = [float(row[0]),float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7]),float(row[8]),float(row[9]),float(row[10]),float(row[11])]
                print(angles)
                Spot.rear_shoulder_left.angle = angles[0]
                Spot.rear_leg_left.angle = angles[1]
                Spot.rear_feet_left.angle = angles[2]
                
                Spot.rear_shoulder_right.angle = angles[3]
                Spot.rear_leg_right.angle = angles[4]
                Spot.rear_feet_right.angle = angles[5]
                
                Spot.front_shoulder_left.angle = angles[6]
                Spot.front_leg_left.angle = angles[7]
                Spot.front_feet_left.angle = angles[8]
                
                Spot.front_shoulder_right.angle = angles[9]
                Spot.front_leg_right.angle = angles[10]
                Spot.front_feet_right.angle = angles[11]
                time.sleep(0.001)
            
    
    return 0
    
if __name__ == '__main__':
    sys.exit(main())