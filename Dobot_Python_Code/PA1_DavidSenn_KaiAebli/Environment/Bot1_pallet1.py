import os
import sys
import time
from dobotapi import Dobot
from dobotapi.utils import get_coms_port
from utils import home_position, attach_fork_to_gripper, move_pallet_to_loading_area, bot_setup, bot_cleanup

bot = bot_setup()

# Attach the fork to the gripper
attach_fork_to_gripper(bot)

# Move pallet 1 to the loading area
move_pallet_to_loading_area(bot, '1')

#bot_cleanup(bot, home_position)
