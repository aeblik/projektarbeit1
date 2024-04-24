import os
from datetime import datetime
from time import sleep
from dobotapi import Dobot
from dobotapi.utils import get_coms_port

# Function to move a block to a specified location
def move_block_to_location(bot3, from_pos, to_pos, above_pos):
    bot3.move_to_Joint(*from_pos)
    bot3.suction_cup.suck()
    sleep(0.5)
    bot3.move_to_Joint(*above_pos)
    bot3.move_to_Joint(*to_pos)
    bot3.suction_cup.idle()
    bot3.move_to_Joint(*above_pos)

# Create a new folder with a timestamp for this run
run_folder = datetime.now().strftime("run_%Y-%m-%d_%H-%M-%S")
os.makedirs(run_folder, exist_ok=True)

# Path to the counter file
counter_file_path = os.path.join(run_folder, "color_counters.txt")

# Initialize the Dobot and connect
bot3 = Dobot()
bot3.port = get_coms_port()[0]
bot3.connect()
bot3.clear_alarms()

# Read existing counters from the file, if it exists
color_counters = {"yellow": 0, "red": 0, "green": 0, "blue": 0}
if os.path.isfile(counter_file_path):
    with open(counter_file_path, "r") as f:
        for line in f:
            color, count = line.strip().split(":")
            color_counters[color] = int(count)

# Define starting positions
start_position = [239.9078, 14.9822, 118.0104]
block_above = [259.8147, -2.6575, 60]
block_pick = [259.8147, -2.6575, 13]

# Coordinates for color sensor
color_sensor_above = [208.0257, -49.7464, 80]
color_sensor_on = [208.0257, -49.7464, 26]

# Dictionary for drop-off positions by color
drop_off_positions = {
    "yellow": {
        1: ([111.2305, -191.8447, 60], [111.2305, -191.8447, -26.6404]),
        2: ([114.7853, -222.4699, 60], [114.7853, -222.4699, -28.1023]),
        3: ([76.6503, -222.4704, 60], [76.6503, -222.4704, -24]),
        4: ([80.0833, -189.9268, 60], [80.0833, -189.9268, -24.0455]),
    },
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

# Save the updated color counters to the file
with open(counter_file_path, "w") as f:
    for color, count in color_counters.items():
        f.write(f"{color}:{count}\n")

# Disconnect the Dobot
bot3.disconnect()
