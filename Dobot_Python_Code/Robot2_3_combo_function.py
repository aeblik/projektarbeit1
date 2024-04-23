import os
import sys
from dobotapi import Dobot
from dobotapi.utils import get_coms_port
from time import sleep, time  # For sleep and time operations

# Initialize the Dobots and connect
bot2 = Dobot()
bot3 = Dobot()
bot2.port = get_coms_port()[0]
bot3.port = get_coms_port()[1]
bot2.connect()
bot3.connect()
bot2.clear_alarms()
bot3.clear_alarms()

# Function to move a block to a specified location
def move_block_to_location(bot3, from_pos, to_pos, above_pos):
    bot3.move_to_Joint(*from_pos)
    bot3.suction_cup.suck()
    sleep(0.5)
    bot3.move_to_Joint(*above_pos)
    bot3.move_to_Joint(*to_pos)
    bot3.suction_cup.idle()
    bot3.move_to_Joint(*above_pos)

# Function to check the color of the block (requires implementation)
def check_color():
    # Placeholder logic for color detection
    # Add your code to detect the block's color
    sleep(2)  # Placeholder sleep to simulate color detection
    return "red"  # Default return for testing

# Color counters and initialization
color_counters = {"red": 0, "green": 0, "blue": 0}

# Define starting positions and coordinates for sensors
start_position = [239.9078, 14.9822, 118.0104]
block_above = [259.8147, -2.6575, 60]
block_pick = [259.8147, -2.6575, 13]

color_sensor_above = [208.0257, -49.7464, 80]
color_sensor_on = [208.0257, -49.7464, 26]

# Dictionary for drop-off positions by color
drop_off_positions = {
    "red": {
        1: ([167.3237, 236.6798, 90], [167.3237, 236.6798, 14.4202]),
        2: ([167.3242, 203.5852, 90], [167.3242, 203.5852, 11.3766]),
        3: ([197.9035, 237.4073, 90], [197.9035, 237.4073, 14.7360]),
        4: ([197.9054, 203.2830, 90], [197.9054, 203.2830, 15.0241]),
    },
    "green": {
        1: ([56.3517, 180.7447, 90], [56.3517, 180.7447, 14.9375]),
        2: ([56.3523, 213.7935, 90], [56.3523, 213.7935, 15.7773]),
        3: ([90.8889, 214.8263, 90], [90.8889, 214.8263, 13.8238]),
        4: ([90.8894, 181.7295, 90], [90.8894, 181.7295, 15.1675]),
    },
    "blue": {
        1: ([53.7013, 291.9974, 90], [53.7013, 291.9974, 12.9593]),
        2: ([53.7018, 260.8730, 90], [53.7018, 260.8730, 14.2554]),
        3: ([88.5994, 293.2517, 90], [88.5994, 293.2517, 15.4802]),
        4: ([88.6007, 260.3268, 90], [88.6007, 260.3268, 15.1445]),
    },
}

# Movement of Robots and Conveyor Belt
bot2.ir_toggle()
# Initialize IR tracking variable
ir_false_start_time = None  # Avoid undefined state

while True:
    if bot2.get_ir() == False:
        if ir_false_start_time is None:
            ir_false_start_time = time()  # Record when IR first went 'False'
        elif time() - ir_false_start_time > 10:  # If IR remains 'False' for more than 10 seconds
            break  # Exit the loop
        else:
            bot2.conveyor_belt.move(speed=-0.5)  # Continue moving the conveyor belt
    else:
        ir_false_start_time = None  # Reset the timer when IR returns to 'True'
        bot2.conveyor_belt.idle()  # Stop the conveyor belt
        bot3.move_to_Joint(*start_position)  # Return to the starting position
        bot3.move_to_Joint(*block_above)
        bot3.move_to_Joint(*block_pick)
        bot3.suction_cup.suck()
        sleep(0.25)
        bot3.move_to_Joint(*block_above)
        bot3.move_to_Joint(*color_sensor_above)
        bot3.move_to_Joint(*color_sensor_on)
        bot3.suction_cup.idle()
        bot3.move_to_Joint(*color_sensor_above)

        # Check the block's color (ensure 'check_color' function works)
        color = check_color()  # Placeholder logic for color detection
        bot3.move_to_Joint(*start_position)  # Return to the starting position

        # Decide where to move the block based on its color
        if color == "red":
            color_counters["red"] += 1
            drop_off_above, drop_off_on = drop_off_positions["red"][color_counters["red"]]
            move_block_to_location(bot3, color_sensor_on, drop_off_on, drop_off_above)
        elif color == "green":
            color_counters["green"] += 1
            drop_off_above, drop_off_on = drop_off_positions["green"][color_counters["green"]]
            move_block_to_location(bot3, color_sensor_on, drop_off_on, drop_off_above)
        elif color == "blue":
            color_counters["blue"] += 1
            drop_off_above, drop_off_on = drop_off_positions["blue"][color_counters["blue"]]
            move_block_to_location(bot3, color_sensor_on, drop_off_on, drop_off_above)

# Return to the starting position and reset IR
bot3.move_to_Joint(*start_position)

# Properly disconnect Dobot devices and idle their components
bot2.ir_toggle()  # Reset IR sensor
bot2.conveyor_belt.idle()
bot2.suction_cup.idle()
bot3.suction_cup.idle()

# Disconnect the Dobot devices to prevent unexpected behavior
bot2.disconnect()  # Disconnect Dobot 2
bot3.disconnect()  # Disconnect Dobot 3
