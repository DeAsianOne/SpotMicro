import math 
import csv
L1 = 11.5
L2 = 12

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
        
def leg_move(L1, L2):
    f = open('E:\Working From Home\__Sixth Form\Computer Science NEA\spotmicroai\Walk_Angles.csv', 'w')
    f.truncate()
    writer = csv.writer(f, lineterminator = '\n')
    x_swing = -0.5
    y_swing = 0
    z_stand = -12
    x_stand = 3.5
    y_stand = 0
    while x_swing <= 3.5:
        z_swing = 1.5*(4-((x_swing-1.5)**2))**(1/2)-12
        if x_swing <= 0:
            Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing = find_angles_n(x_swing, y_swing, z_swing, L1, L2)
        elif x_swing > 0:
            Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing = find_angles_p(x_swing, y_swing, z_swing, L1, L2) 
        if x_stand <= 0:
            Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand = find_angles_n(x_stand, y_stand, z_stand, L1, L2)
        elif x_stand > 0: 
            Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand = find_angles_p(x_stand, y_stand, z_stand, L1, L2)
        row = [Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing, 180 - Shoulder_angle_stand, 180 - Leg_angle_stand, 180 - Feet_angle_stand, Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand, 180 - Shoulder_angle_swing, 180 - Leg_angle_swing, 180 - Feet_angle_swing]
        writer.writerow(row)
        print(row)
        x_swing += 0.1
        x_stand -= 0.1
    x_swing = -0.5
    x_stand = 3.5
    while x_swing <= 3.5:
        z_swing = 1.5*(4-((x_swing-1.5)**2))**(1/2)-12
        if x_swing <= 0:
            Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing = find_angles_n(x_swing, y_swing, z_swing, L1, L2)
        elif x_swing > 0:
            Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing = find_angles_p(x_swing, y_swing, z_swing, L1, L2)
        if x_stand <= 0:
            Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand = find_angles_n(x_stand, y_stand, z_stand, L1, L2)
        elif x_stand > 0: 
            Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand = find_angles_p(x_stand, y_stand, z_stand, L1, L2)   
        row = [Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand, 180 - Shoulder_angle_swing, 180 - Leg_angle_swing, 180 - Feet_angle_swing, Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing, 180 - Shoulder_angle_stand, 180 - Leg_angle_stand, 180 - Feet_angle_stand]
        writer.writerow(row)
        print(row)
        x_swing += 0.1
        x_stand -= 0.1
    f.close()
    print("done")
        
leg_move(L1, L2)
