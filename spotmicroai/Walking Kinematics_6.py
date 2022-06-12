import math 
import csv
L1 = 11.5
L2 = 12
x_swing = -0.5
y_swing = 0
x_stand = 3.5
y_stand = 0

def find_angles_n(x, y, z, L1, L2):
    L3 = (x**2 + z**2)**(1/2)
    angle_1 = math.atan(abs(x)/abs(z))
    angle_1 = (angle_1*180)/math.pi
    
    angle_2 = math.acos((L1**2+L3**2-L2**2)/(2*L1*L3))
    angle_2 = (angle_2*180)/math.pi
    
    angle_3 = 180 - (90 - (angle_2 + angle_1))
    
    angle_4 = math.acos((L1**2 + L2**2 - L3**2) / (2 * L1 * L2))
    angle_4 = (angle_4*180)/math.pi
    
    Shoulder_angle = 90
    Leg_angle = angle_3
    Feet_angle = angle_4

    return Shoulder_angle, Leg_angle, Feet_angle

def find_angles_p(x, y, z, L1, L2):
    L3 = (x**2 + z**2)**(1/2)
    angle_1 = math.atan(abs(x)/abs(z))
    angle_1 = (angle_1*180)/math.pi
    
    angle_2 = math.acos((L1**2+L3**2-L2**2)/(2*L1*L3))
    angle_2 = (angle_2*180)/math.pi
    
    angle_3 = 180 - (90 - (angle_2 - angle_1))
    
    angle_4 = math.acos((L1**2 + L2**2 - L3**2) / (2 * L1 * L2))
    angle_4 = (angle_4*180)/math.pi
    
    Shoulder_angle = 90
    Leg_angle = angle_3
    Feet_angle = angle_4

    return Shoulder_angle, Leg_angle, Feet_angle

def find_angles_swing(x_swing, y_swing, z_swing, L1, L2):
    if x_swing <= 0:
        Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing = find_angles_n(x_swing, y_swing, z_swing, L1, L2)
    elif x_swing > 0:
        Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing = find_angles_p(x_swing, y_swing, z_swing, L1, L2)
    return Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing 
            
def find_angles_stand(x_stand, y_stand, z_stand, L1, L2):
    if x_stand <= 0:
        Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand = find_angles_n(x_stand, y_stand, z_stand, L1, L2)
    elif x_stand > 0: 
        Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand = find_angles_p(x_stand, y_stand, z_stand, L1, L2)
    return Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand 

def swing_phase_rear(x_swing, L1, L2):
    z_swing = 2.5*(2.25-((x_swing)**2))**(1/2)-12
    Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing = find_angles_swing(x_swing, 0, z_swing, L1, L2)
    return Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing 

def swing_phase_front(x_swing, L1, L2):
    z_swing = 2.5*(2.25-((x_swing)**2))**(1/2)-10
    Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing = find_angles_swing(x_swing, 0, z_swing, L1, L2)
    return Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing 
            
def stand_phase_rear(x_stand, z_stand, L1, L2):
    Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand = find_angles_stand(x_stand, 0, z_stand, L1, L2)
    return Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand

def stand_phase_front(x_stand, z_stand, L1, L2):
    Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand = find_angles_stand(x_stand, 0, z_stand+2, L1, L2)
    return Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand
    
def rear_left_swing(L1, L2, f):
    writer = csv.writer(f, lineterminator = '\n')
    x_rear_left = -1.5
    x_rear_right = 0.5
    x_front_left = 1.5
    x_front_right = -0.5
    shoulder_rear = 80
    shoulder_front = 100
    leg_height_right = -10
    leg_height_left = -14
    while x_rear_left <= 1.5:
        rear_shoulder_left, rear_leg_left, rear_feet_left = swing_phase_rear(x_rear_left, L1, L2)
        rear_shoulder_right, rear_leg_right, rear_feet_right = stand_phase_rear(x_rear_right, leg_height_right, L1, L2)
        front_shoulder_left, front_leg_left, front_feet_left = stand_phase_front(x_front_left, leg_height_left, L1, L2)
        front_shoulder_right, front_leg_right, front_feet_right = stand_phase_front(x_front_right, leg_height_right, L1, L2)
        x_rear_left += 0.03
        x_rear_right -= 0.01
        x_front_left -= 0.01
        x_front_right -= 0.01
        row = [shoulder_front, rear_leg_left, rear_feet_left, shoulder_front, 180 - (rear_leg_right), 180 - (rear_feet_right), shoulder_rear, front_leg_left, front_feet_left, shoulder_rear, 180 - (front_leg_right), 180 - (front_feet_right)]
        writer.writerow(row)
        print(row)
    while shoulder_rear <= 90:
        rear_shoulder_left, rear_leg_left, rear_feet_left = stand_phase_rear(x_rear_left, leg_height_left, L1, L2)
        rear_shoulder_right, rear_leg_right, rear_feet_right = stand_phase_rear(x_rear_right, leg_height_right, L1, L2)
        front_shoulder_left, front_leg_left, front_feet_left = stand_phase_front(x_front_left, leg_height_left, L1, L2)
        front_shoulder_right, front_leg_right, front_feet_right = stand_phase_front(x_front_right, leg_height_right, L1, L2)
        shoulder_rear += 1
        shoulder_front -= 1
        leg_height_right -= 0.2
        leg_height_left += 0.2
        row = [shoulder_front, rear_leg_left, rear_feet_left, shoulder_front, 180 - (rear_leg_right), 180 - (rear_feet_right), shoulder_rear, front_leg_left, front_feet_left, shoulder_rear, 180 - (front_leg_right), 180 - (front_feet_right)]
        writer.writerow(row)
        print(row)
        
def front_right_swing(L1, L2, f):
    writer = csv.writer(f, lineterminator = '\n')
    x_rear_left = 1.5
    x_rear_right = -0.5
    x_front_left = 0.5
    x_front_right = -1.5
    shoulder_rear = 90
    shoulder_front = 90
    leg_height_right = -12
    leg_height_left = -12
    while shoulder_rear <= 100:
        rear_shoulder_left, rear_leg_left, rear_feet_left = stand_phase_rear(x_rear_left, leg_height_left, L1, L2)
        rear_shoulder_right, rear_leg_right, rear_feet_right = stand_phase_rear(x_rear_right, leg_height_right, L1, L2)
        front_shoulder_left, front_leg_left, front_feet_left = stand_phase_front(x_front_left, leg_height_left, L1, L2)
        front_shoulder_right, front_leg_right, front_feet_right = stand_phase_front(x_front_right, leg_height_right, L1, L2)
        shoulder_rear += 1
        shoulder_front -= 1
        leg_height_right -= 0.2
        leg_height_left += 0.2
        row = [shoulder_front, rear_leg_left, rear_feet_left, shoulder_front, 180 - (rear_leg_right), 180 - (rear_feet_right), shoulder_rear, front_leg_left, front_feet_left, shoulder_rear, 180 - (front_leg_right), 180 - (front_feet_right)]
        writer.writerow(row)
        print(row)
    while x_front_right <= 1.5:
        rear_shoulder_left, rear_leg_left, rear_feet_left = stand_phase_rear(x_rear_left, leg_height_left, L1, L2)
        rear_shoulder_right, rear_leg_right, rear_feet_right = stand_phase_rear(x_rear_right, leg_height_right, L1, L2)
        front_shoulder_left, front_leg_left, front_feet_left = stand_phase_front(x_front_left, leg_height_left, L1, L2)
        front_shoulder_right, front_leg_right, front_feet_right = swing_phase_front(x_front_right, L1, L2)
        x_rear_left -= 0.01
        x_rear_right -= 0.01
        x_front_left -= 0.01
        x_front_right += 0.03
        row = [shoulder_front, rear_leg_left, rear_feet_left, shoulder_front, 180 - (rear_leg_right), 180 - (rear_feet_right), shoulder_rear, front_leg_left, front_feet_left, shoulder_rear, 180 - (front_leg_right), 180 - (front_feet_right)]
        writer.writerow(row)
        print(row)
        
def rear_right_swing(L1, L2, f):
    writer = csv.writer(f, lineterminator = '\n')
    x_rear_left = 0.5
    x_rear_right = -1.5
    x_front_left = -0.5
    x_front_right = 1.5
    shoulder_rear = 100
    shoulder_front = 80
    leg_height_right = -14
    leg_height_left = -10
    while x_rear_right <= 1.5:
        rear_shoulder_left, rear_leg_left, rear_feet_left = stand_phase_rear(x_rear_left, leg_height_left, L1, L2)
        rear_shoulder_right, rear_leg_right, rear_feet_right = swing_phase_rear(x_rear_right, L1, L2)
        front_shoulder_left, front_leg_left, front_feet_left = stand_phase_front(x_front_left, leg_height_left, L1, L2)
        front_shoulder_right, front_leg_right, front_feet_right = stand_phase_front(x_front_right, leg_height_right, L1, L2)
        x_rear_left -= 0.01
        x_rear_right += 0.03
        x_front_left -= 0.01
        x_front_right -= 0.01
        row = [shoulder_front, rear_leg_left, rear_feet_left, shoulder_front, 180 - (rear_leg_right), 180 - (rear_feet_right), shoulder_rear, front_leg_left, front_feet_left , shoulder_rear, 180 - (front_leg_right), 180 - (front_feet_right)]
        writer.writerow(row)
        print(row)
    while shoulder_rear >= 90:
        rear_shoulder_left, rear_leg_left, rear_feet_left = stand_phase_rear(x_rear_left, leg_height_left, L1, L2)
        rear_shoulder_right, rear_leg_right, rear_feet_right = stand_phase_rear(x_rear_right, leg_height_right, L1, L2)
        front_shoulder_left, front_leg_left, front_feet_left = stand_phase_front(x_front_left, leg_height_left, L1, L2)
        front_shoulder_right, front_leg_right, front_feet_right = stand_phase_front(x_front_right, leg_height_right, L1, L2)
        shoulder_rear -= 1
        shoulder_front += 1
        leg_height_right += 0.2
        leg_height_left -= 0.2
        row = [shoulder_front, rear_leg_left, rear_feet_left, shoulder_front, 180 - (rear_leg_right), 180 - (rear_feet_right), shoulder_rear, front_leg_left, front_feet_left , shoulder_rear, 180 - (front_leg_right), 180 - (front_feet_right)]
        writer.writerow(row)
        print(row)
    
def front_left_swing(L1, L2, f):
    writer = csv.writer(f, lineterminator = '\n')
    x_rear_left = -0.5
    x_rear_right = 1.5
    x_front_left = -1.5
    x_front_right = 0.5
    shoulder_rear = 90
    shoulder_front = 90
    leg_height_right = -12
    leg_height_left = -12
    while shoulder_rear >= 80:
        rear_shoulder_left, rear_leg_left, rear_feet_left = stand_phase_rear(x_rear_left, leg_height_left, L1, L2)
        rear_shoulder_right, rear_leg_right, rear_feet_right = stand_phase_rear(x_rear_right, leg_height_right, L1, L2)
        front_shoulder_left, front_leg_left, front_feet_left = stand_phase_front(x_front_left, leg_height_left, L1, L2)
        front_shoulder_right, front_leg_right, front_feet_right = stand_phase_front(x_front_right, leg_height_right, L1, L2)
        shoulder_rear -= 1
        shoulder_front += 1
        leg_height_right += 0.2
        leg_height_left -= 0.2
        row = [shoulder_front, rear_leg_left, rear_feet_left, shoulder_front, 180 - (rear_leg_right), 180 - (rear_feet_right), shoulder_rear, front_leg_left, front_feet_left, shoulder_rear, 180 - (front_leg_right), 180 - (front_feet_right)]
        writer.writerow(row)
        print(row)
    while x_front_left <= 1.5:
        rear_shoulder_left, rear_leg_left, rear_feet_left = stand_phase_rear(x_rear_left, leg_height_left, L1, L2)
        rear_shoulder_right, rear_leg_right, rear_feet_right = stand_phase_rear(x_rear_right, leg_height_right, L1, L2)
        front_shoulder_left, front_leg_left, front_feet_left = swing_phase_front(x_front_left, L1, L2)
        front_shoulder_right, front_leg_right, front_feet_right = stand_phase_front(x_front_right, leg_height_right, L1, L2)
        x_rear_left -= 0.01
        x_rear_right -= 0.01
        x_front_left += 0.03
        x_front_right -= 0.01
        row = [shoulder_front, rear_leg_left, rear_feet_left, shoulder_front, 180 - (rear_leg_right), 180 - (rear_feet_right), shoulder_rear, front_leg_left, front_feet_left, shoulder_rear, 180 - (front_leg_right), 180 - (front_feet_right)]
        writer.writerow(row)
        print(row)
    
def leg_move(L1, L2):
    f = open('E:\Working From Home\__Sixth Form\Computer Science NEA\spotmicroai/3_motors.csv', 'w')
    f.truncate()
    rear_left_swing(L1, L2, f)
    front_right_swing(L1, L2, f)
    rear_right_swing(L1, L2, f)
    front_left_swing(L1, L2, f)
    f.close()
    
leg_move(L1, L2)
    