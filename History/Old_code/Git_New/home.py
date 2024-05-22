import os
import sys
import time

sys.path.insert(1, '/home/control2/dobot_python') #If run from script
#sys.path.insert(0, os.path.abspath('.')) #If run from command

from lib.interface import Interface
from serial.tools import list_ports

available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')

port = available_ports[0].device

bot = Interface(port)

print('Bot status:', 'connected' if bot.connected() else 'not connected')
params = bot.get_homing_paramaters()
print('Params:', params)

print('Homing')
bot.set_homing_command(0)

time.sleep(25)
print('reset')

