# SpotMicro
CAD model 1: https://www.thingiverse.com/thing:3445283
CAD model 2 (currently used): https://www.thingiverse.com/thing:4559827
- can be printed without support
- stronger joints, 3D prints less likely to break
- doesn't need superglue
        
SpotMicroAI community - https://spotmicroai.readthedocs.io/en/latest/

This repository contains code written by myself for an independent project. It is definitely not perfect.
The content of each file is as below:
- config.py: stores dictionaries for each leg containing channel number, min_pulse, max_pulse and rest angle. Also contains list storing all 12 dictionaries. 
- SpotClass.py: creates the class Spot() used in many other files. Stores min, max pulse of motors, its channels (imported in from config.py), and basic turning instructions for each leg.
- motor_move.py: allows user to select an specific motor and move that motor to a specific angle.
- motor_move.py: robot moves to rest position instantly.
- controller_Rest_position.py: robot moves to rest position when a button on controller is pressed.
- IKUD.py: calculates angles for moving up and down using trigonometry. Robot doesn't actually move.
- motor_move_UD.py: robot stays stationary, but moves up and down along the vertical axis. Controlled using D-Pad of controller.
- motor_move_leg.py: user chooses a leg and can move the motors of that leg to specific angles. Similar to motor_move.py but for 3 instead of 1 motor.
- Walk_Angles.csv: stores list of angles created by Walking Kinematics files.
- move_leg_test.py: moves motors to angles in Walk_Angles.csv. Run this for robot to walk.
- Walking_Kinematics.py: first attempt at walking algorithm. Robot  moves its legs in semi-circular motion, but forward biased so keeps on falling backwards. Diagonal legs move together.
- Walking_Kinematics_2.py: robot moves legs in semi-circular motion but is now more central, moves under shoulder instead of in front of it, maths is slightly more complicated.
