from time import sleep
from dobotapi import Dobot
from dobotapi.utils import get_coms_port

# Define a function to perform the operations for moving and picking up a block, then placing it on the conveyor
def operate_block(bot, block_above, block_pick, conveyor_positions):
    # Move to the position directly above the block to be picked
    bot.move_to_Joint(*block_above)
    # Move down to the exact position to pick up the block
    bot.move_to_Joint(*block_pick)
    # Activate the suction cup to pick up the block
    bot.suction_cup.suck()
    # Pause to ensure the block is securely attached
    sleep(0.5)
    # Move back up to the initial position above the block
    bot.move_to_Joint(*block_above)
    # Move to a position above the conveyor belt to place the block
    bot.move_to_Joint(*conveyor_positions['above'])
    # Move down to place the block on the conveyor belt
    bot.move_to_Joint(*conveyor_positions['on'])
    # Deactivate the suction cup to release the block
    bot.suction_cup.idle()
    # Move back up to the position above the conveyor
    bot.move_to_Joint(*conveyor_positions['above'])
    # Start the conveyor belt to move the block away
    bot.conveyor_belt.move(speed=-0.5)
    # Allow the belt to move for a short duration
    sleep(0.5)
    # Stop the conveyor belt
    bot.conveyor_belt.idle()

# Initialize the Dobot API
bot = Dobot()
# Set the port to connect to the first available Dobot
bot.port = get_coms_port()[0]
# Establish connection to the Dobot
bot.connect()
# Clear any existing alarms in the Dobot system
bot.clear_alarms()

# Define the coordinates for positions directly above each block
blocks_above = [
    [13.8287, -270.8062, 90], # Block 1
    [53.1174, -268.0737, 90], # Block 2
    [53.3576, -299.855, 90], # Block 3
    [18.1257, -300.1451, 90] # Block 4
]
# Define the Z-coordinates for picking up each block
pick_z_coords = [14.4, 13.4, 12.4, 12.4]
# Calculate the full picking coordinates for each block using the above coordinates and the specific Z-coordinates
blocks_pick = [[x, y, z_pick] for (x, y, _), z_pick in zip(blocks_above, pick_z_coords)]

# Define conveyor positions in a dictionary to be passed as parameters
conveyor_positions = {
    'above': [174.7025, -184.3191, 90],  # Position above the conveyor belt
    'on': [174.7025, -184.3191, 13.4273]  # Exact position on the conveyor belt
}

# Iterate over each block to perform the picking and placing operations
for block_above, block_pick in zip(blocks_above, blocks_pick):
    operate_block(bot, block_above, block_pick, conveyor_positions)

# Disconnect the Dobot after operations are complete
bot.disconnect()
