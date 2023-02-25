# -*- coding: utf-8 -*-
import sys
import csv
import time

import SpotClass as sp

def main():
    # instantiate class spot
    # initialise motors, and info
    Spot = sp.Spot()
    # loop through csv file so robot walks continuosly.
    while True:
        # opens Walk_Angles.csv
        with open('Walk_Angles.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                Spot.turn_motor(float(row[0]),float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7]),float(row[8]),float(row[9]),float(row[10]),float(row[11]))
                time.sleep(0.002)
            
    
    return 0
    
if __name__ == '__main__':
    sys.exit(main())