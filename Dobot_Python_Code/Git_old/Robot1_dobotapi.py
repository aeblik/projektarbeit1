import os
import sys
import time
from dobotapi import Dobot
from dobotapi.utils import get_coms_port

# Connect to Dobot
bot = Dobot()
bot.port = get_coms_port()[0]
bot.connect()

# Clear any existing alarms
bot.clear_alarms()

# Define the x, y, z, r coordinates for various positions
home_position = (225.6311, -191.7791, -6.6714, 55.6912)

gripper_positions = {
    'above': (116.3743, -194.0146, 7.5, 57.408),
    'pick': (116.3743, -194.0146, -17.6399, 57.408),
    'lift': (116.3743, -194.0146, -2, 57.408),
}

pallet_positions = {
    '1': {'front': (158.6424, -183.6389, -6.6714, 55.6912),
          'loaded': (225.6311, -183.6389, -6.6714, 55.6912),
          'lift': (225.6311, -183.6389, 60.0, 55.6912)},
    '2': {'front': (147.123, -44.3675, -5.9256, 59.5793),
          'loaded': (227.8143, -44.3675, -5.9256, 59.5793),
          'lift': (227.8143, -44.3675, 60.0, 59.5793)},
    '3': {'front': (147.1234, 104.6730, -5.9256, 59.5793),
          'loaded': (225.2907, 104.6730, -5.9256, 59.5793),
          'lift': (225.2907, 104.6730, 60.0, 59.5793)},
}

loading_area_positions = {
    'above': (136.901, -240.906, 60.0, -28.5971),
    'on': (139.733, -240.906, 33.8178, -28.5971),
    'empty_fork': (139.733, -144.3046, 33.8178, -28.5971),
    'in_front': (139.733, -126.1611, 60.0, -28.5971),
}

# Function to move to a specified location
def move_to(bot, position):
    bot.move_to_Joint(*position)

# Function to pick up and move a pallet to the loading area
def move_pallet_to_loading_area(bot, pallet_num):
    move_to(bot, pallet_positions[pallet_num]['front'])
    move_to(bot, pallet_positions[pallet_num]['loaded'])
    move_to(bot, pallet_positions[pallet_num]['lift'])
    move_to(bot, loading_area_positions['above'])
    move_to(bot, loading_area_positions['on'])
    move_to(bot, loading_area_positions['empty_fork'])
    time.sleep(5)  # Wait for unloading, replace with message to Bot 2

# Function to return an empty pallet to storage
def return_empty_pallet_to_storage(bot, pallet_num):
    move_to(bot, loading_area_positions['on'])
    move_to(bot, loading_area_positions['above'])
    move_to(bot, loading_area_positions['in_front'])
    move_to(bot, pallet_positions[pallet_num]['lift'])
    move_to(bot, pallet_positions[pallet_num]['loaded'])
    move_to(bot, pallet_positions[pallet_num]['front'])

# Function to attach the fork to gripper
def attach_fork_to_gripper(bot):
    move_to(bot, gripper_positions['above'])
    move_to(bot, gripper_positions['pick'])
    bot.gripper.close()
    move_to(bot, gripper_positions['lift'])

# Function to detach the fork from gripper
def detach_fork_from_gripper(bot):
    move_to(bot, gripper_positions['lift'])
    move_to(bot, gripper_positions['pick'])
    bot.gripper.open()
    move_to(bot, gripper_positions['above'])

# Open the gripper and lift the fork
bot.gripper.open()
move_to(bot, gripper_positions['above'])
move_to(bot, gripper_positions['pick'])
bot.gripper.close()
move_to(bot, gripper_positions['lift'])

###### Palette 1 ######
# Move pallet 1 to the loading area and return the empty pallet to storage
move_pallet_to_loading_area(bot, '1')
return_empty_pallet_to_storage(bot, '1')

###### Palette 2 ######
# Move pallet 2 to the loading area and return the empty pallet to storage
move_pallet_to_loading_area(bot, '2')
return_empty_pallet_to_storage(bot, '2')

###### Palette 3 ######
# Move pallet 3 to the loading area and return the empty pallet to storage
move_pallet_to_loading_area(bot, '3')
return_empty_pallet_to_storage(bot, '3')

# Return the fork to the initial position and open
detach_fork_from_gripper(bot)

# Return to the home position
move_to(bot, home_position)

# Properly close the connection and return to idle
bot.close()  # Properly close the connection
