import os
import sys
import time
from dobotapi import Dobot
from dobotapi.utils import get_coms_port
from utils import home_position, attach_fork_to_gripper, detach_fork_from_gripper, move_pallet_to_loading_area, return_empty_pallet_to_storage, bot_setup, bot_cleanup

bot = bot_setup()

# Return pallet 2 to its storage position
return_empty_pallet_to_storage(bot, '2')

# Move pallet 3 to the loading area
move_pallet_to_loading_area(bot, '3')

detach_fork_from_gripper(bot)

bot_cleanup(bot, home_position)
