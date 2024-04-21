from time import sleep
from dobotapi import Dobot
from dobotapi.utils import get_coms_port

bot = Dobot()
bot.port = get_coms_port()[0]
bot.connect()

bot.clear_alarms()

# Definition of x,y,z coordinates for the robot to move to
start_position = [239.9078, 14.9822, 118.0104]
block_above = [259.8147, -2.6575, 60]
block_pick = [259.8147, -2.6575, 13]

color_sensor_above = [208.0257, -49.7464, 80]
color_sensor_on = [208.0257, -49.7464, 26]

# Definition of x,y,z coordinates for the robot to drop off the yellow blocks
yellow_above_pos1 = [111.2305, -191.8447, 60]
yellow_on_pos1 = [111.2305, -191.8447, -26.6404]
yellow_above_pos2 = [114.7853, -222.4699, 60]
yellow_on_pos2 = [114.7853, -222.4699, -28.1023]
yellow_above_pos3 = [76.6503, -222.4704, 60]
yellow_on_pos3 = [76.6503, -222.4704, -24]
yellow_above_pos4 = [80.0833, -189.9268, 60]
yellow_on_pos4 = [80.0833, -189.9268, -24.0455]

# Definition of x,y,z coordinates for the robot to drop off the red blocks
red_above_pos1 = [167.3237, 236.6798, 90]
red_on_pos1 = [167.3237, 236.6798, 14.4202]
red_above_pos2 = [167.3242, 203.5852, 90]
red_on_pos2 = [167.3242, 203.5852, 11.3766]
red_above_pos3 = [197.9035, 237.4073, 90]
red_on_pos3 = [197.9035, 237.4073, 14.7360]
red_above_pos4 = [197.9054, 203.2830, 90]
red_on_pos4 = [197.9054, 203.2830, 15.0241]

# Definition of x,y,z coordinates for the robot to drop off the green blocks
green_above_pos1 = [56.3517, 180.7447, 90]
green_on_pos1 = [56.3517,180.7447, 14.9375]
green_above_pos2 = [56.3523, 213.7935, 90]
green_on_pos2 = [56.3523, 213.7935, 15.7773]
green_above_pos3 = [90.8889, 214.8263, 90]
green_on_pos3 = [90.8889, 214.8263, 13.8238]
green_above_pos4 = [90.8894, 181.7295, 90]
green_on_pos4 = [90.8894, 181.7295, 15.1675]

# Definition of x,y,z coordinates for the robot to drop off the blue blocks
blue_above_pos1 = [53.7013, 291.9974, 90]
blue_on_pos1 = [53.7013, 291.9974, 12.9593]
blue_above_pos2 = [53.7018, 260.8730, 90]
blue_on_pos2 = [53.7018, 260.8730, 14.2554]
blue_above_pos3 = [88.5994, 293.2517, 90]
blue_on_pos3 = [88.5994, 293.2517, 15.4802]
blue_above_pos4 = [88.6007, 260.3268, 90]
blue_on_pos4 = [88.6007, 260.3268, 15.1445]

# Initialize a counter for each color of the blocks
yellow_counter = 0
red_counter = 0
green_counter = 0
blue_counter = 0

# Move the blocks from the conveyor belt to the color sensor
bot.move_to_Joint(*start_position)
bot.move_to_Joint(*block_above)
bot.move_to_Joint(*block_pick)
bot.suction_cup.suck()
sleep(0.5)
bot.move_to_Joint(*block_above)
bot.move_to_Joint(*color_sensor_above)
bot.move_to_Joint(*color_sensor_on)
bot.suction_cup.idle()
bot.move_to_Joint(*color_sensor_above)

sleep(2)  # wait for the color sensor to detect the color
# Insert a function to check the color and return the color => color = check_color()
color = check_color()  # assuming a function to get the detected color

# Determine where to drop off the block based on its color
bot.move_to_Joint(*color_sensor_on)
bot.suction_cup.suck()
sleep(0.5)
bot.move_to_Joint(*color_sensor_above)

if color == 'yellow':
    # Increment the counter for yellow blocks
    yellow_counter += 1

    # Determine the drop-off position based on the counter
    if yellow_counter == 1:
        bot.move_to_Joint(*yellow_above_pos1)
        bot.move_to_Joint(*yellow_on_pos1)
        bot.suction_cup.idle()
        bot.move_to_Joint(*yellow_above_pos1)
    elif yellow_counter == 2:
        bot.move_to_Joint(*yellow_above_pos2)
        bot.move_to_Joint(*yellow_on_pos2)
        bot.suction_cup.idle()
        bot.move_to_Joint(*yellow_above_pos2)
    elif yellow_counter == 3:
        bot.move_to_Joint(*yellow_above_pos3)
        bot.move_to_Joint(*yellow_on_pos3)
        bot.suction_cup.idle()
        bot.move_to_Joint(*yellow_above_pos3)
    elif yellow_counter == 4:
        bot.move_to_Joint(*yellow_above_pos4)
        bot.move_to_Joint(*yellow_on_pos4)
        bot.suction_cup.idle()
        bot.move_to_Joint(*yellow_above_pos4)

elif color == 'red':
    # Increment the counter for red blocks
    red_counter += 1

    # Determine the drop-off position based on the counter
    if red_counter == 1:
        bot.move_to_Joint(*red_above_pos1)
        bot.move_to_Joint(*red_on_pos1)
        bot.suction_cup.idle()
        bot.move_to_Joint(*red_above_pos1)
    elif red_counter == 2:
        bot.move_to_Joint(*red_above_pos2)
        bot.move_to_Joint(*red_on_pos2)
        bot.suction_cup.idle()
        bot.move_to_Joint(*red_above_pos2)
    elif red_counter == 3:
        bot.move_to_Joint(*red_above_pos3)
        bot.move_to_Joint(*red_on_pos3)
        bot.suction_cup.idle()
        bot.move_to_Joint(*red_above_pos3)
    elif red_counter == 4:
        bot.move_to_Joint(*red_above_pos4)
        bot.move_to_Joint(*red_on_pos4)
        bot.suction_cup.idle()
        bot.move_to_Joint(*red_above_pos4)

elif color == 'green':
    # Increment the counter for green blocks
    green_counter += 1

    # Determine the drop-off position based on the counter
    if green_counter == 1:
        bot.move_to_Joint(*green_above_pos1)
        bot.move_to_Joint(*green_on_pos1)
        bot.suction_cup.idle()
        bot.move_to_Joint(*green_above_pos1)
    elif green_counter == 2:
        bot.move_to_Joint(*green_above_pos2)
        bot.move_to_Joint(*green_on_pos2)
        bot.suction_cup.idle()
        bot.move_to_Joint(*green_above_pos2)
    elif green_counter == 3:
        bot.move_to_Joint(*green_above_pos3)
        bot.move_to_Joint(*green_on_pos3)
        bot.suction_cup.idle()
        bot.move_to_Joint(*green_above_pos3)
    elif green_counter == 4:
        bot.move_to_Joint(*green_above_pos4)
        bot.move_to_Joint(*green_on_pos4)
        bot.suction_cup.idle()
        bot.move_to_Joint(*green_above_pos4)

elif color == 'blue':
    # Increment the counter for blue blocks
    blue_counter += 1

    # Determine the drop-off position based on the counter
    if blue_counter == 1:
        bot.move_to_Joint(*blue_above_pos1)
        bot.move_to_Joint(*blue_on_pos1)
        bot.suction_cup.idle()
        bot.move_to_Joint(*blue_above_pos1)
    elif blue_counter == 2:
        bot.move_to_Joint(*blue_above_pos2)
        bot.move_to_Joint(*blue_on_pos2)
        bot.suction_cup.idle()
        bot.move_to_Joint(*blue_above_pos2)
    elif blue_counter == 3:
        bot.move_to_Joint(*blue_above_pos3)
        bot.move_to_Joint(*blue_on_pos3)
        bot.suction_cup.idle()
        bot.move_to_Joint(*blue_above_pos3)
    elif blue_counter == 4:
        bot.move_to_Joint(*blue_above_pos4)
        bot.move_to_Joint(*blue_on_pos4)
        bot.suction_cup.idle()
        bot.move_to_Joint(*blue_above_pos4)

# Move the robot back to the starting position
bot.move_to_Joint(*start_position)

bot.disconnect()
