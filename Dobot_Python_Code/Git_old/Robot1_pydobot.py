import os
import sys
import time
from pydobot import Dobot
from serial.tools import list_ports

# Automatically detect the first available COM port
port = list_ports.comports()[0].device  # Get the first available COM port
bot1 = Dobot(port=port, verbose=False)  # Initialize the Dobot with the detected port

# Clear any existing alarms
bot1.clear_alarms()

# Set the speed of the Dobot
bot1.speed(50, 50)

# Define the x, y, z, r coordinates for various positions
home_position = (225.6311, -191.7791, -6.6714, 55.6912)

gripper_positions = {
    'above': (116.3743, -194.0146, 7.5, 57.408),
    'pick': (116.3743, -194.0146, -17.6399, 57.408),
    'lift': (116.3743, -194.0146, -2, 57.408),
}

pallet_positions = {
    '1': {'front': (158.6421, -183.6389, -6.6714, 55.6912),
          'loaded': (225.6311, -183.6389, -6.6714, 55.6912),
          'lift': (225.6311, -183.6389, 60.0, 55.6912)},
    '2': {'front': (147.123, -44.3675, -5.9256, 59.5793),
          'loaded': (227.8143, -44.3675, -5.9256, 59.5793),
          'lift': (227.8143, -44.3675, 60.0, 59.5793)},
    '3': {'front': (147.1234, 104.6730, -5.9256, 59.5793),
          'loaded': (226.6, 104.6730, -5.9256, 59.5793),
          'lift': (226.6, 104.6730, 60.0, 59.5793)},
}

loading_area_positions = {
    'above': (136.901, -244.2901, 60.0, -31.4771),
    'on': (136.901, -244.2901, 33.8178, -31.4771),
    'empty_fork': (136.901, -144.3046, 33.8178, -31.4771),
    'in_front': (136.901, -126.1611, 60.0, -31.4771),
}

# Function to move to a specified location
def move_to(bot, position):
    bot.move_to(*position)

# Function to move a pallet to the loading area
def move_pallet_to_loading_area(bot, pallet_num):
    move_to(bot, pallet_positions[pallet_num]['front'])
    move_to(bot, pallet_positions[pallet_num]['loaded'])
    move_to(bot, pallet_positions[pallet_num]['lift'])
    move_to(bot, loading_area_positions['above'])
    move_to(bot, loading_area_positions['on'])
    move_to(bot, loading_area_positions['empty_fork'])
    time.sleep(5)  # Wait for unloading, replace with a message to another bot if needed

# Function to return an empty pallet to storage
def return_empty_pallet_to_storage(bot, pallet_num):
    move_to(bot, loading_area_positions['on'])
    move_to(bot, loading_area_positions['above'])
    move_to(bot, loading_area_positions['in_front'])
    move_to(bot, pallet_positions[pallet_num]['lift'])
    move_to(bot, pallet_positions[pallet_num]['loaded'])
    move_to(bot, pallet_positions[pallet_num]['front'])

# Function to attach the gripper to the claw
def attach_fork_to_gripper(bot):
    move_to(bot, gripper_positions['above'])
    move_to(bot, gripper_positions['pick'])
    bot.grip(enable=False)  # Close gripper
    move_to(bot, gripper_positions['lift'])

# Function to detach the gripper from the claw
def detach_fork_from_gripper(bot):
    move_to(bot, gripper_positions['lift'])
    move_to(bot, gripper_positions['pick'])
    bot.grip(enable=True)  # Open gripper
    move_to(bot, gripper_positions['above'])

# Attach the gripper to the claw and lift it
attach_fork_to_gripper(bot1)

###### Palette 1 ######
# Move pallet 1 to the loading area and return the empty pallet to storage
move_pallet_to_loading_area(bot1, '1')
return_empty_pallet_to_storage(bot1, '1')

###### Palette 2 ######
# Move pallet 2 to the loading area and return the empty pallet to storage
move_pallet_to_loading_area(bot1, '2')
return_empty_pallet_to_storage(bot1, '2')

###### Palette 3 ######
# Move pallet 3 to the loading area and return the empty pallet to storage
move_pallet_to_loading_area(bot1, '3')
return_empty_pallet_to_storage(bot1, '3')

# Detach the gripper from the claw
detach_fork_from_gripper(bot1)

# Return to the home position
move_to(bot1, home_position)

# Properly close the connection and return to idle
bot1.close()  # Properly close the connection
