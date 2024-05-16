from dobotapi import Dobot
from dobotapi.utils import get_coms_port

# Define the x, y, z, r coordinates for various positions
home_position = (200.0, 200.0, 80.0, 25.0)

gripper_positions = {
    'above': (116.3743, -194.0146, 7.5, 57.408),
    'pick': (116.3743, -194.0146, -17.6399, 57.408),
    'lift': (116.3743, -194.0146, -2, 57.408),
}

pallet_positions = {
    '1': {'front': (152.8339, -183.6392, -6.6714, 57.0592),
          'loaded': (225.6311, -183.6389, -6.6714, 57.0592),
          'lift': (225.6311, -183.6389, 60.0, 57.0592)},
    '2': {'front': (147.123, -44.3675, -5.9256, 59.5793),
          'loaded': (228.5, -44.3675, -5.9256, 59.5793),
          'lift': (228.5, -44.3675, 60.0, 59.5793)},
    '3': {'front': (147.1234, 104.6730, -5.9256, 59.5793),
          'loaded': (226.6, 104.6730, -5.9256, 59.5793),
          'lift': (226.6, 104.6730, 60.0, 59.5793),
          'front_lifted': (147.1234, 104.6730, 60, 59.5793)}
}

loading_area_positions = {
    'above': (136.901, -244.0, 60.0, -29.7491),
    'on': (136.901, -244.0, 33.8178, -29.7491),
    'empty_fork': (136.901, -144.3046, 33.8178, -29.7491),
    'in_front': (136.901, -126.1611, 60.0, -29.7491),
}
def bot_setup():
    # Connect to Dobot
    bot = Dobot()
    bot.port = get_coms_port()[0]
    bot.connect()
    bot.clear_alarms()
    print("bot connected")
    return bot

def move_pallet_to_loading_area(bot, pallet_num):
    for position in ['front', 'loaded', 'lift']:
        bot.move_to_Linear(*pallet_positions[pallet_num][position])
    bot.move_to_Linear(*loading_area_positions['above'])
    bot.move_to_Linear(*loading_area_positions['on'])
    bot.move_to_Linear(*loading_area_positions['empty_fork'])
    print(f"Pallet {pallet_num} has been placed on the loading area.")

def return_empty_pallet_to_storage(bot, pallet_num):
    bot.move_to_Linear(*loading_area_positions['on'])
    bot.move_to_Linear(*loading_area_positions['above'])
    bot.move_to_Linear(*loading_area_positions['in_front'])
    bot.move_to_Joint(*pallet_positions[pallet_num]['lift'])
    bot.move_to_Linear(*pallet_positions[pallet_num]['loaded'])
    bot.move_to_Linear(*pallet_positions[pallet_num]['front'])
    if pallet_num == '3':
        bot.move_to_Joint(*pallet_positions[pallet_num]['front_lifted'])

def attach_fork_to_gripper(bot):
    bot.move_to_Joint(*gripper_positions['above'])
    bot.gripper.open()
    bot.gripper.idle()
    bot.move_to_Linear(*gripper_positions['pick'])
    bot.gripper.close()
    bot.gripper.idle()
    bot.move_to_Linear(*gripper_positions['lift'])

def detach_fork_from_gripper(bot):
    bot.move_to_Joint(*gripper_positions['lift'])
    bot.move_to_Joint(*gripper_positions['pick'])
    bot.gripper.open()
    bot.gripper.idle()
    bot.move_to_Joint(*gripper_positions['above'])
    
def bot_cleanup(bot, home_position):
    # Move to home position and close the connection
    bot.move_to_Joint(*home_position)
    bot.close()
