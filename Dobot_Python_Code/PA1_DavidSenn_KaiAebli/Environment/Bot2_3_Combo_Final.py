import os
import sys
from dobotapi.dobot import Dobot
from serial.tools import list_ports
from dobotapi.utils import get_coms_port
from time import sleep, time
from pydobot.lib.interface import Interface

# Initialize the Dobots and connect
bot2 = Dobot()
bot3 = Dobot()
#bot2.port = get_coms_port()[0]
#bot3.port = get_coms_port()[1]
available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')

bot2.port = available_ports[0].device
bot3.port = available_ports[1].device
bot2.connect()
bot3.connect()
bot2.clear_alarms()
bot3.clear_alarms()



# Connect bot 3 also via pydobot
bot3_col = Interface(available_ports[1].device)


def read_color (bot):
    bot.set_color_sensor(0, enable=1, port=1, version = 1)
    sleep(1)
    try:
        colors = bot.get_color_sensor(index=0)
        print(colors)
    except Exception as e:
        print(f"an error occured: {e}")
        colors = None
    bot.set_color_sensor(0, enable=0, port=1, version = 1)
    return colors




# Function to move a block to a specified location
def move_block_to_location(bot3, from_pos, from_pos_above, to_pos, above_pos):
    bot3.move_to_Joint(*from_pos)  # Fixed syntax error
    bot3.suction_cup.suck()
    sleep(0.25)  # Short suction delay
    bot3.move_to_Joint(*from_pos_above)  # Ensure correct variable usage
    bot3.move_to_Joint(*above_pos)
    bot3.move_to_Joint(*to_pos)  # Move block to drop-off
    bot3.suction_cup.idle()  # Release block
    bot3.move_to_Joint(*above_pos)  # Return to initial above position


# Color counters and initialization
color_counters = {"red": 0, "green": 0, "blue": 0}

# Define starting positions and coordinates for sensors
start_position = [239.9078, 14.9822, 118.0104]
block_above = [287.8147, -2.6575, 60]
block_pick = [287.8147, -2.6575, 13]

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

# Recycling position for error-handling and overflow
recycling_pos = [180, 120, 90]

# Movement of Robots and Conveyor Belt
bot2.ir_toggle()  # Enable IR sensor

# Initialize IR tracking variable
ir_false_start_time = None  # Initialization to avoid undefined state

while True:
    if bot2.get_ir() == False:
        if ir_false_start_time is None:
            ir_false_start_time = time()  # Record when IR first went 'False'
        elif time() - ir_false_start_time > 5:  # If IR remains 'False' for more than 5 seconds
            print('There are no more blocks to sort.')
            break  # Exit the loop
        else:
            bot2.conveyor_belt.move(speed=-0.5)  # Continue moving the conveyor belt
    else:
        ir_false_start_time = None  # Reset the timer when IR returns to 'True'
        bot2.conveyor_belt.idle()  # Stop the conveyor belt
        bot3.move_to_Joint(*start_position)  # Return to initial position
        bot3.move_to_Joint(*block_above)  # Move to block above position
        bot3.move_to_Joint(*block_pick)  # Move to block pick-up
        bot3.suction_cup.suck()  # Start suction
        sleep(0.25)  # Short delay for suction
        bot3.move_to_Joint(*block_above)  # Move above block
        bot3.move_to_Joint(*color_sensor_above)  # Move to color sensor position
        bot3.move_to_Joint(*color_sensor_on)  # Move to sensor on position
        bot3.suction_cup.idle()  # Idle suction cup
        bot3.move_to_Joint(*color_sensor_above)  # Move back to sensor above position

        # Check the block's color
        color = read_color(bot3_col)  # Placeholder logic for color detection
        #print(color)
        #print(type(color))

        # Return to starting position after color check
        #bot3.move_to_Joint(*start_position)  # Return to initial position

        # Determine where to move the block based on its color
        if color[0] == 1:
            color_counters["red"] += 1
            if color_counters["red"] <= 4:
                drop_off_above, drop_off_on = drop_off_positions["red"][color_counters["red"]]
                move_block_to_location(bot3, color_sensor_on, color_sensor_above, drop_off_on, drop_off_above)
            else:
                move_block_to_location(bot3, color_sensor_on, color_sensor_above, recycling_pos, recycling_pos)
                print("No more space for red blocks")
                
        elif color[1] == 1:
            color_counters["green"] += 1
            if color_counters["green"] <= 4:
                drop_off_above, drop_off_on = drop_off_positions["green"][color_counters["green"]]
                move_block_to_location(bot3, color_sensor_on, color_sensor_above, drop_off_on, drop_off_above)
            else:
                move_block_to_location(bot3, color_sensor_on, color_sensor_above, recycling_pos, recycling_pos)
                print("No more space for green blocks")
        elif color[2] == 1:
            color_counters["blue"] += 1
            if color_counters["blue"] <=4:
                drop_off_above, drop_off_on = drop_off_positions["blue"][color_counters["blue"]]
                move_block_to_location(bot3, color_sensor_on, color_sensor_above, drop_off_on, drop_off_above)
            else:
                move_block_to_location(bot3, color_sensor_on, color_sensor_above, recycling_pos, recycling_pos)
                print("No more space for green blocks")
        else:
            move_block_to_location(bot3, color_sensor_on, color_sensor_above, recycling_pos, recycling_pos)
            print("Unknown color detected. Block will be moved to recycling-bin")

# Return to the starting position
bot3.move_to_Joint(*start_position)  # Ensure correct return position

# Properly disconnect Dobot devices and idle their components
bot2.ir_toggle()  # Reset IR sensor
bot2.conveyor_belt.idle()  # Idle conveyor belt
bot2.suction_cup.idle()  # Idle suction cup
bot3.suction_cup.idle()  # Idle suction cup

# Disconnect the Dobot devices to prevent unexpected behavior
bot2.close()  # Disconnect Dobot 2
bot3.close()  # Disconnect Dobot 3
print('All blocks have been sorted and the Dobots went to sleep.')
