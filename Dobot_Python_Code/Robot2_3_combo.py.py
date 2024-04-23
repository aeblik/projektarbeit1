import os
import sys
from dobotapi import Dobot
from dobotapi.utils import get_coms_port
from time import sleep, time  # Importing 'time' for timing operations

# Define starting positions
start_position = [239.9078, 14.9822, 118.0104]
block_above = [259.8147, -2.6575, 60]
block_pick = [259.8147, -2.6575, 13]

bot2 = Dobot()
bot3 = Dobot()
bot2.port = get_coms_port()[0]
bot3.port = get_coms_port()[1]
bot2.connect()
bot3.connect()
bot2.clear_alarms()
bot3.clear_alarms()

bot2.ir_toggle()

# Keep track of the time when the IR sensor last detected 'True'
ir_false_start_time = None

while True:
    if bot2.get_ir() == False:
        if ir_false_start_time is None:
            ir_false_start_time = time()  # Record the current time
        elif time() - ir_false_start_time > 10:  # Check if more than 10 seconds passed
            break  # Exit the loop
        else:
            bot2.conveyor_belt.move(speed=-0.5)  # Move the conveyor belt
    else:
        ir_false_start_time = None  # Reset the timer when IR is 'True'
        bot2.conveyor_belt.idle()  # Stop the conveyor belt
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

        sleep(2)
        break  # Exit the loop after processing a block

bot2.ir_toggle()  # Reset IR sensor
bot2.close()  # Properly close the connection
bot3.close()  # Properly close the connection
