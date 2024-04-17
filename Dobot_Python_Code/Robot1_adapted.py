import os
import sys
import time
from dobotapi import Dobot
from dobotapi.utils import get_coms_port

bot = Dobot()
# Select the port for a specific Dobot when multiple are connected
bot.port = get_coms_port()[0]
bot.connect()

# Clear any existing alarms
bot.clear_alarms()

###### Palette 1 ######
# Open the gripper above the claw
bot.gripper.open()
bot.move_to_Joint(116.3743,-194.0146,7.5,57.408)
# Move the gripper around the claw
bot.move_to_Joint(116.3743,-194.0146,-17.6399,57.408)
# Close the gripper to grasp the claw
bot.gripper.close()
# Lift the gripper with the claw
bot.move_to_Joint(116.3743,-194.0146,-2,57.408)
# Move to the position in front of pallet 1
bot.move_to_Joint(158.6424,-191.7747,-6.6714,55.6912)
bot.move_to_Joint(225.6311,-191.7791,-6.6714,55.6912)
# Lift pallet 1
bot.move_to_Joint(225.6311,-191.7791,60.0,55.6912)

# Move pallet 1 to the loading area
bot.move_to_Joint(136.733,-162.0649,60.0,-33.5891)
bot.move_to_Joint(136.901,-240.906,60.0,-28.5971)
# Move pallet 1 onto the loading area
bot.move_to_Joint(139.733,-240.906,33.8178,-28.5971)
bot.move_to_Joint(139.733,-144.3046,33.8178,-28.5971)
# Wait after unloading pallet 1
time.sleep(5)

# Pick up empty pallet from loading area
bot.move_to_Joint(139.733,-240.906,33.8178,-28.5971)
bot.move_to_Joint(139.733,-240.906,60.0,-28.5971)
# Move the empty pallet slightly back
bot.move_to_Joint(139.733,-126.1611,60.0,-28.5971)

# Move empty pallet 1 to pallet storage
bot.move_to_Joint(225.6311,-191.7791,60.0,55.6912)
bot.move_to_Joint(225.6311,-191.7791,-6.6714,55.6912)
bot.move_to_Joint(147.1219,-191.5112,-6.6714,55.6912)

###### Palette 2 ######
# Fork in front of pallet 2
bot.move_to_Joint(147.123,-50.1275,-5.9256,59.5793)
# Load pallet 2 onto the fork
bot.move_to_Joint(227.8143,-50.1278,-5.9256,59.5793)
# Lift pallet 2
bot.move_to_Joint(227.8143,-50.1278,60.0,59.5793)

# Move pallet 2 to the loading area
bot.move_to_Joint(136.733,-162.0649,60.0,-33.5891)
bot.move_to_Joint(136.901,-240.906,60.0,-28.5971)
# Move pallet 2 onto the loading area
bot.move_to_Joint(139.733,-240.906,33.8178,-28.5971)
bot.move_to_Joint(139.733,-144.3046,33.8178,-28.5971)
# Wait after unloading pallet 2
time.sleep(5)

# Pick up empty pallet from loading area
bot.move_to_Joint(139.733,-240.906,33.8178,-28.5971)
bot.move_to_Joint(139.733,-240.906,60.0,-28.5971)
# Move the empty pallet slightly back
bot.move_to_Joint(139.733,-126.1611,60.0,-28.5971)

# Move empty pallet 2 to pallet storage
bot.move_to_Joint(227.8143,-50.1278,60.0,59.5793)
bot.move_to_Joint(227.8143,-50.1278,-5.9256,59.5793)
bot.move_to_Joint(147.123,-50.1278,-5.9256,59.5793)

###### Palette 3 ######
# Fork in front of pallet 3
bot.move_to_Joint(147.123,92.0485,-5.9256,59.5793)
# Load pallet 3 onto the fork
bot.move_to_Joint(225.2907,92.0485,-5.9256,59.5793)
# Lift pallet 3
bot.move_to_Joint(225.2907,92.0485,60.0,59.5793)

# Move pallet 3 to the loading area
bot.move_to_Joint(136.733,-162.0649,60.0,-33.5891)
bot.move_to_Joint(136.901,-240.906,60.0,-28.5971)
# Move pallet 3 onto the loading area
bot.move_to_Joint(139.733,-240.906,33.8178,-28.5971)
bot.move_to_Joint(139.733,-144.3046,33.8178,-28.5971)
# Wait after unloading pallet 3
time.sleep(5)

# Pick up empty pallet from loading area
bot.move_to_Joint(139.733,-240.906,33.8178,-28.5971)
bot.move_to_Joint(139.733,-240.906,60.0,-28.5971)
# Move the empty pallet slightly back
bot.move_to_Joint(139.733,-126.1611,60.0,-28.5971)

# Move empty pallet 3 to pallet storage
bot.move_to_Joint(225.2907,92.0485,60.0,59.5793)
bot.move_to_Joint(225.2907,92.0485,-5.9256,59.5793)
bot.move_to_Joint(147.123,92.0485,-5.9256,59.5793)

bot.close() # Properly close the connection, also returns the gripper to idle
