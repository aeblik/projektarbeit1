import os
import sys
from time import sleep
from dobotapi import Dobot
from dobotapi.utils import get_coms_port

# Define starting positions
start_position = [239.9078, 14.9822, 118.0104]
block_above = [259.8147, -2.6575, 60]
block_pick = [259.8147, -2.6575, 13]
color_sensor_above = [208.0257, -49.7464, 80]

bot2 = Dobot()
bot3 = Dobot()
# In case of multipe Dobots connected to one device choose the port to adress once specific Dobot
bot2.port = get_coms_port()[0]
bot3.port = get_coms_port()[1]
print(bot3.port)
bot2.connect()
bot3.connect()
bot2.clear_alarms()
bot3.clear_alarms()


bot3.move_to_Joint(*color_sensor_above)                                                                                                                                       
