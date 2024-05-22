import os
import sys
import time
from dobotapi import Dobot
from dobotapi.utils import get_coms_port
from pydobot.lib.interface import Interface
from serial.tools import list_ports


available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port_pydobot = available_ports[0].device

bot_pydobot = Interface(port_pydobot)

print('Bot status:', 'connected' if bot_pydobot.connected() else 'not connected')
params = bot_pydobot.get_homing_paramaters()
print('Params:', params)

print('Homing')
bot_pydobot.set_homing_command(0)
time.sleep(25)


bot_dobotapi = Dobot()
bot_dobotapi.port = get_coms_port()[0]
bot_dobotapi.connect()

# Clear any existing alarms
bot_dobotapi.clear_alarms()

# Define the x, y, z, r coordinates for various positions
home_position = (200.0, 200.0, 80.0, 25.0)

bot_dobotapi.move_to_Joint(*home_position)
bot_dobotapi.close()

