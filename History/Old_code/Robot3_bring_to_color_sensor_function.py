import os
from datetime import datetime
from time import sleep
from dobotapi import Dobot
from dobotapi.utils import get_coms_port

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


# Generate counters for each color
color_counters = {"red": 0, "green": 0, "blue": 0}


# Define starting positions
start_position = [239.9078, 14.9822, 118.0104]
block_above = [259.8147, -2.6575, 60]
block_pick = [259.8147, -2.6575, 13]

# Coordinates for color sensor
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

# Move the block from the conveyor belt to the color sensor
bot3.move_to_Joint(*start_position)
bot3.move_to_Joint(*block_above)
bot3.move_to_Joint(*block_pick)
bot3.suction_cup.suck()
sleep(0.5)
bot3.move_to_Joint(*block_above)
bot3.move_to_Joint(*color_sensor_above)
bot3.move_to_Joint(*color_sensor_on)
bot3.suction_cup.idle()
bot3.move_to_Joint(*color_sensor_above)

sleep(2)  # wait for the color sensor to detect the color
color = check_color()  # Assuming a function to get the detected color

# Determine drop-off location based on the block's color
color_counters[color] += 1
drop_off_above, drop_off_on = drop_off_positions[color][color_counters[color]]

# Move to the appropriate drop-off location and release the block
move_block_to_location(bot3, color_sensor_on, drop_off_on, drop_off_above)

# Return to the starting position
bot3.move_to_Joint(*start_position)

# Disconnect the Dobot
bot3.disconnect()
