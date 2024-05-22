import os
import sys
import time
from dobotapi import Dobot
from dobotapi.utils import get_coms_port
from utils import home_position, attach_fork_to_gripper, move_pallet_to_loading_area, return_empty_pallet_to_storage, bot_setup, bot_cleanup

bot = bot_setup()

# Return pallet 1 to its storage position
return_empty_pallet_to_storage(bot, '1')

# Move pallet 2 to the loading area
move_pallet_to_loading_area(bot, '2')

#bot_cleanup(bot, home_position)
