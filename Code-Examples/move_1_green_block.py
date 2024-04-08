import os
import sys
import time
from dobotapi import Dobot
from dobotapi.utils import get_coms_port

bot = Dobot()
# In case of multipe Dobots connected to one device choose the port to adress once specific Dobot
bot.port = get_coms_port()[0]
bot.connect()


bot.clear_alarms()

# print(bot.get_alarms())


# Block 1

bot.move_to_Joint(118,227,0,100)
bot.move_to_Joint(118,227,-40,100)

bot.suction_cup.suck()


bot.move_to_Joint(118,227,50,100)

bot.move_to_Joint(277,-35,50,100)

bot.move_to_Joint(277,-35,5,100)

bot.suction_cup.idle()

bot.move_to_Joint(277,-35,50,100)

bot.move_to_Joint(200,0,80,0)

print("2 green Block moved")

bot.close() # Properly close the connection, also returns the gripper to idle


