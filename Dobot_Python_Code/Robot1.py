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
# Gripper open above claw
bot.gripper.open()
bot.move_to_Joint(116.3743,-194.0146,7.5,57.408)
print("Moved above claw")
# Gripper open around claw
bot.move_to_Joint(116.3743,-194.0146,-17.6399,57.408)
print("Moved around claw")
# Gripper closed
bot.gripper.close()
print("Gripper closed")
# Gripper lifted
bot.move_to_Joint(116.3743,-194.0146,-2,57.408)
print("Gripper lifted")
# fork in front pallet 1
bot.move_to_Joint(158.6424,-191.7747,-6.6714,55.6912)
print("Fork in front pallet 1")
bot.move_to_Joint(225.6311,-191.7791,-6.6714,55.6912)
print("Pallet 1 loaded")
bot.move_to_Joint(225.6311,-191.7791,60.0,55.6912)
print("Pallet 1 lifted")

#Move pallet 1 to loading area
bot.move_to_Joint(136.733,-162.0649,60.0,-33.5891)
print("Pallet 1 moved to loading area")
bot.move_to_Joint(136.901,-240.906,60.0,-28.5971)
# Move pallet onto loading area
bot.move_to_Joint(139.733,-240.906,33.8178,-28.5971)
print("Pallet 1 moved onto loading area")
bot.move_to_Joint(139.7321,-144.3046,33.8178,-28.5971)
print("Pallet 1 unloaded, waiting")
time.sleep(5)

bot.close() # Properly close the connection, also returns the gripper to idle
