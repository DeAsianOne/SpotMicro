import math 
import csv
L1 = 11.5
L2 = 12
# Walking_Kinematics_2 implement trot gait
# two diagonal legs move in same motion, either swing or stand phase

# find angles when the x-coordinate of the leg was negative, behind the shoulder
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

# find angles when the x-coordinate of the leg was positive, in front of the shoulder
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

def swing_phase_1(L1, L2):
    x = -3
    y = 0
    while x <= 0:
        z = 2*(9-(x+2)**2)**(1/2)-16
        Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing = find_angles_n(x, y, z, L1, L2)
        return Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing 
        x += 0.25
        
def swing_phase_2(L1, L2):
    x = 0
    y = 0
    while x >= 3:
        z = 2*(9-(x+2)**2)**(1/2)-16
        Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing = find_angles_p(x, y, z, L1, L2)
        return Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing 
        x += 0.25
        
def stand_phase_1(L1, L2):
    z = -16
    x = 3
    y = 0
    while x >= 0:
        Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand = find_angles_p(x, y, z, L1, L2)
        return Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand 
        x -= 0.25
        
def stand_phase_2(L1, L2):
    z = -16
    x = 0
    y = 0
    while x >= -3:
        Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand = find_angles_n(x, y, z, L1, L2)
        return Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand 
        x -= 0.25
        
def leg_move(L1, L2):
    # opens csv and prepare to write motor angles to it
    f = open('E:\Working From Home\__Sixth Form\Computer Science NEA\spotmicroai/3_motors.csv', 'w')
    f.truncate()
    writer = csv.writer(f, lineterminator = '\n')
    # set initial phase conditions, intial x coordinate is 0.5 units behind shoulder
    # rear left and front right leg in swing phase first, rear right and front left leg in stand phase
    x_swing = -0.5
    y_swing = 0
    z_stand = -12
    x_stand = 3.5
    y_stand = 0
    while x_swing <= 3.5:
        z_swing = 1.5*(4-((x_swing-1.5)**2))**(1/2)-12
        # calculate swing phase when motor in negative x
        if x_swing <= 0:
            Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing = find_angles_n(x_swing, y_swing, z_swing, L1, L2)
        # calculate swing phase when motor in positive x
        elif x_swing > 0:
            Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing = find_angles_p(x_swing, y_swing, z_swing, L1, L2) 
        # calculate stand phase when motor in positive x
        if x_stand <= 0:
            Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand = find_angles_n(x_stand, y_stand, z_stand, L1, L2)
        # calculate stand phase when motor in negative x
        elif x_stand > 0: 
            Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand = find_angles_p(x_stand, y_stand, z_stand, L1, L2)
        row = [Shoulder_angle_swing, Leg_angle_swing, Feet_angle_swing, 180 - Shoulder_angle_stand, 180 - Leg_angle_stand, 180 - Feet_angle_stand, Shoulder_angle_stand, Leg_angle_stand, Feet_angle_stand, 180 - Shoulder_angle_swing, 180 - Leg_angle_swing, 180 - Feet_angle_swing]
        # write motor angles to csv file
        writer.writerow(row)
        print(row)
        # increment and decrement swing and stand phase respectively
        # swing phase moves leg forward by 0.1 units and stand phase move legs backwards by 0.1 units
        # this combination gives 40 coordinate pairs per phase
        x_swing += 0.1 
        x_stand -= 0.1
    # set initial conditions for second swing
    # after mutliple calculations Python seem to stray away from nice numbers
    # for example, x_stand may be 3.49999999 rather than 3.5
    # variables need to be reset or calculations may be unachieveable
    x_swing = -0.5
    x_stand = 3.5
    # second swing and stand phase
    # rear right and front left leg swing, rear left and front right leg stand phase
    # similar process to before
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
    # close csv so it can be used by another resource
    # only two swings written to csv to minimize size
    # when reading csv, it will be looped so the robot can move further than two steps
    f.close()
    # indicator process has stopped
    print("done")
        
leg_move(L1, L2)