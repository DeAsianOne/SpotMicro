# -*- coding: utf-8 -*-
import sys
import csv
import time

import SpotClass as sp

def main():
    Spot = sp.Spot()
    
    with open('789.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            angles = [float(row[0]),float(row[1]),float(row[2])]
            print(angles)
            Spot.rear_shoulder_left.angle = angles[0]
            Spot.rear_leg_left.angle = angles[1]
            Spot.rear_feet_left.angle = angles[2]
            time.sleep(1)
            
    
    return 0
    
if __name__ == '__main__':
    sys.exit(main())