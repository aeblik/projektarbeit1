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


###### Palette 1 ######
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

#Move pallet to loading area
bot.move_to_Joint(136.733,-162.0649,60.0,-33.5891)
print("Pallet moved to loading area")
bot.move_to_Joint(136.901,-240.906,60.0,-28.5971)
# Move pallet onto loading area
bot.move_to_Joint(139.733,-240.906,33.8178,-28.5971)
print("Pallet moved onto loading area")
bot.move_to_Joint(139.733,-144.3046,33.8178,-28.5971)
print("Pallet unloaded, waiting")
time.sleep(5)

# Pick up empty pallet from loading area
bot.move_to_Joint(139.733,-240.906,33.8178,-28.5971)
print("empty pallet picked up")
bot.move_to_Joint(139.733,-240.906,60.0,-28.5971)
print("empty pallet lifted")
# Move empty pallet back a bit
bot.move_to_Joint(139.733,-126.1611,60.0,-28.5971)
print("empty pallet moved back")

# Move empty pallet 1 to pallet storage
bot.move_to_Joint(225.6311,-191.7791,60.0,55.6912)
print("Pallet 1 above starting position")
bot.move_to_Joint(225.6311,-191.7791,-6.6714,55.6912)
print("Pallet 1 lowered")
bot.move_to_Joint(147.1219,-191.5112,-6.6714,55.6912)
print("Pallet 1 unloaded")

###### Palette 2 ######
# Fork in front of pallet 2
bot.move_to_Joint(147.123,-50.1275,-5.9256,59.5793)
print("Fork in front of pallet 2")
# palett 2 on fork
bot.move_to_Joint(227.8143,-50.1278,-5.9256,59.5793)
print("Pallet 2 loaded")
bot.move_to_Joint(227.8143,-50.1278,60.0,59.5793)
print("Pallet 2 lifted")

#Move pallet to loading area
bot.move_to_Joint(136.733,-162.0649,60.0,-33.5891)
print("Pallet moved to loading area")
bot.move_to_Joint(136.901,-240.906,60.0,-28.5971)
# Move pallet onto loading area
bot.move_to_Joint(139.733,-240.906,33.8178,-28.5971)
print("Pallet moved onto loading area")
bot.move_to_Joint(139.733,-144.3046,33.8178,-28.5971)
print("Pallet unloaded, waiting")
time.sleep(5)

# Pick up empty pallet from loading area
bot.move_to_Joint(139.733,-240.906,33.8178,-28.5971)
print("empty pallet picked up")
bot.move_to_Joint(139.733,-240.906,60.0,-28.5971)
print("empty pallet lifted")
# Move empty pallet back a bit
bot.move_to_Joint(139.733,-126.1611,60.0,-28.5971)
print("empty pallet moved back")

# Move empty pallet 2 to pallet storage
bot.move_to_Joint(227.8143,-50.1278,60.0,59.5793)
print("Pallet 2 above starting position")
bot.move_to_Joint(227.8143,-50.1278,-5.9256,59.5793)
print("Pallet 2 lowered")
bot.move_to_Joint(147.123,-50.1278,-5.9256,59.5793)
print("Pallet 2 unloaded")

###### Palette 3 ######
# Fork in front of pallet 3
bot.move_to_Joint(147.123,92.0485,-5.9256,59.5793)
print("Fork in front of pallet 3")
bot.move_to_Joint(225.2907,92.0485,-5.9256,59.5793)
print("Pallet 3 loaded")
bot.move_to_Joint(225.2907,92.0485,60.0,59.5793)
print("Pallet 3 lifted")

#Move pallet to loading area
bot.move_to_Joint(136.733,-162.0649,60.0,-33.5891)
print("Pallet moved to loading area")
bot.move_to_Joint(136.901,-240.906,60.0,-28.5971)
# Move pallet onto loading area
bot.move_to_Joint(139.733,-240.906,33.8178,-28.5971)
print("Pallet moved onto loading area")
bot.move_to_Joint(139.733,-144.3046,33.8178,-28.5971)
print("Pallet unloaded, waiting")
time.sleep(5)

# Pick up empty pallet from loading area
bot.move_to_Joint(139.733,-240.906,33.8178,-28.5971)
print("empty pallet picked up")
bot.move_to_Joint(139.733,-240.906,60.0,-28.5971)
print("empty pallet lifted")
# Move empty pallet back a bit
bot.move_to_Joint(139.733,-126.1611,60.0,-28.5971)
print("empty pallet moved back")

# Move empty pallet 3 to pallet storage
bot.move_to_Joint(225.2907,92.0485,60.0,59.5793)
print("Pallet 3 above starting position")
bot.move_to_Joint(225.2907,92.0485,-5.9256,59.5793)
print("Pallet 3 lowered")
bot.move_to_Joint(147.123,92.0485,-5.9256,59.5793)
print("Pallet 3 unloaded")

bot.close() # Properly close the connection, also returns the gripper to idle
