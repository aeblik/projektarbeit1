import time
from dobotapi import Dobot
from dobotapi.utils import get_coms_port

def connect_robot():
    """Establishes connection with Dobot robot."""
    bot = Dobot()
    bot.port = get_coms_port()[0]
    bot.connect()
    bot.clear_alarms()
    return bot

def handle_gripper(bot, positions):
    """Controls the gripper to pick or place objects based on specified positions."""
    bot.gripper.open()
    bot.move_to_Joint(*positions['above'])
    bot.move_to_Joint(*positions['pick'])
    bot.gripper.close()
    bot.move_to_Joint(*positions['lift'])

def handle_pallet(bot, positions):
    """Manages the sequence of moving a pallet from one position to another."""
    bot.move_to_Joint(*positions['front'])
    bot.move_to_Joint(*positions['loaded'])
    bot.move_to_Joint(*positions['lift'])

def handle_loading_area(bot, positions):
    """Handles the pallet movements in the loading area, including placement and retrieval of empty pallets."""
    bot.move_to_Joint(*positions['above'])
    bot.move_to_Joint(*positions['on'])
    bot.move_to_Joint(*positions['empty_fork'])
    time.sleep(5)
    bot.move_to_Joint(*positions['on'])
    bot.move_to_Joint(*positions['above'])

def return_fork_to_initial(bot, positions):
    """Returns the gripper fork to the initial position after operations."""
    bot.move_to_Joint(*positions['lift'])
    bot.move_to_Joint(*positions['pick'])
    bot.gripper.open()
    bot.move_to_Joint(*positions['above'])

def main():
    bot = connect_robot()

    # Gripper and pallet positions defined using dictionaries for better readability
    gripper_positions = {'above': [116.3743, -194.0146, 7.5, 57.408],
                         'pick': [116.3743, -194.0146, -17.6399, 57.408],
                         'lift': [116.3743, -194.0146, -2, 57.408]}

    pallet_positions = {
        '1': {'front': [158.6424, -183.6389, -6.6714, 55.6912],
              'loaded': [225.6311, -183.6389, -6.6714, 55.6912],
              'lift': [225.6311, -183.6389, 60.0, 55.6912]},
        '2': {'front': [147.123, -44.3675, -5.9256, 59.5793],
              'loaded': [227.8143, -44.3675, -5.9256, 59.5793],
              'lift': [227.8143, -44.3675, 60.0, 59.5793]},
        '3': {'front': [147.1234, 104.6730, -5.9256, 59.5793],
              'loaded': [225.2907, 104.6730, -5.9256, 59.5793],
              'lift': [225.2907, 104.6730, 60.0, 59.5793]}
    }

    loading_area_positions = {
        'above': [136.901, -240.906, 60.0, -28.5971],
        'on': [139.733, -240.906, 33.8178, -28.5971],
        'empty_fork': [139.733, -144.3046, 33.8178, -28.5971]
    }

    handle_gripper(bot, gripper_positions)
    for key in pallet_positions:
        handle_pallet(bot, pallet_positions[key])
        handle_loading_area(bot, loading_area_positions)
    return_fork_to_initial(bot, gripper_positions)

    bot.close()  # Properly close the connection

if __name__ == "__main__":
    main()
