import os
import sys
import time
from dobotapi import Dobot
from dobotapi.utils import get_coms_port

bot = Dobot()
# Select the port for a specific Dobot when multiple are connected
bot.port = get_coms_port()[0]
bot.connect()

# Clear any existing alarms
bot.clear_alarms()

# Define the x, y, z, r coordinates for various positions
gripper_positions = {
    'above': (116.3743, -194.0146, 7.5, 57.408),
    'pick': (116.3743, -194.0146, -17.6399, 57.408),
    'lift': (116.3743, -194.0146, -2, 57.408),
}

pallet_positions = {
    '1': {
        'front': (158.6424, -183.6389, -6.6714, 55.6912),
        'loaded': (225.6311, -183.6389, -6.6714, 55.6912),
        'lift': (225.6311, -183.6389, 60.0, 55.6912),
    },
    '2': {
        'front': (147.123, -44.3675, -5.9256, 59.5793),
        'loaded': (227.8143, -44.3675, -5.9256, 59.5793),
        'lift': (227.8143, -44.3675, 60.0, 59.5793),
    },
    '3': {
        'front': (147.1234, 104.6730, -5.9256, 59.5793),
        'loaded': (225.2907, 104.6730, -5.9256, 59.5793),
        'lift': (225.2907, 104.6730, 60.0, 59.5793),
    },
}

loading_area_positions = {
    'above': (136.901, -240.906, 60.0, -28.5971),
    'on': (139.733, -240.906, 33.8178, -28.5971),
    'empty_fork': (139.733, -144.3046, 33.8178, -28.5971),
    'in_front': (139.733,-126.1611,60.0,-28.5971),
}


# Function to move to a specified location
def move_to(bot, position):
    bot.move_to_Joint(*position)


###### Palette 1 ######
# Open the gripper above the claw
bot.gripper.open()
# Move the gripper above the claw
move_to(bot, gripper_positions['above'])
# Move the gripper around the claw
move_to(bot, gripper_positions['pick'])
# Close the gripper to grasp the claw
bot.gripper.close()
# Lift the gripper with the claw
move_to(bot, gripper_positions['lift'])

# Pick up pallet 1
move_to(bot, pallet_positions['1']['front'])
move_to(bot, pallet_positions['1']['loaded'])
move_to(bot, pallet_positions['1']['lift'])

# Move pallet to the loading area
move_to(bot, loading_area_positions['above'])
move_to(bot, loading_area_positions['on'])
move_to(bot, loading_area_positions['empty_fork'])
time.sleep(5) # Wait for unloading of pallet
move_to(bot, loading_area_positions['on'])
move_to(bot, loading_area_positions['above'])
move_to(bot, loading_area_positions['in_front'])

# Move empty pallet 1 to pallet storage
move_to(bot, pallet_positions['1']['lift'])
move_to(bot, pallet_positions['1']['loaded'])
move_to(bot, pallet_positions['1']['front'])

###### Palette 2 ######
# Fork in front of pallet 2
move_to(bot, pallet_positions['2']['front'])
move_to(bot, pallet_positions['2']['loaded'])
move_to(bot, pallet_positions['2']['lift'])

# Move pallet to the loading area
move_to(bot, loading_area_positions['above'])
move_to(bot, loading_area_positions['on'])
move_to(bot, loading_area_positions['empty_fork'])
time.sleep(5) # Wait for unloading of pallet
move_to(bot, loading_area_positions['on'])
move_to(bot, loading_area_positions['above'])
move_to(bot, loading_area_positions['in_front'])

# Move empty pallet 2 to pallet storage
move_to(bot, pallet_positions['2']['lift'])
move_to(bot, pallet_positions['2']['loaded'])
move_to(bot, pallet_positions['2']['front'])

###### Palette 3 ######
# Pick up pallet 3
move_to(bot, pallet_positions['3']['front'])
move_to(bot, pallet_positions['3']['loaded'])
move_to(bot, pallet_positions['3']['lift'])

# Move pallet to the loading area
move_to(bot, loading_area_positions['above'])
move_to(bot, loading_area_positions['on'])
move_to(bot, loading_area_positions['empty_fork'])
time.sleep(5) # Wait for unloading of pallet
move_to(bot, loading_area_positions['on'])
move_to(bot, loading_area_positions['above'])
move_to(bot, loading_area_positions['in_front'])

# Move empty pallet 3 to pallet storage
move_to(bot, pallet_positions['3']['lift'])
move_to(bot, pallet_positions['3']['loaded'])
move_to(bot, pallet_positions['3']['front'])

# Return the fork to the initial position
move_to(bot, gripper_positions['lift'])
move_to(bot, gripper_positions['pick'])
bot.gripper.open()
move_to(bot, gripper_positions['above'])

# Move the robot to the home position
#move_to(bot, (0, 0, 0, 0))

bot.close() # Properly close the connection
