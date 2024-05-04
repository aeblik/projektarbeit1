import os
import sys
import time

sys.path.insert(1, '/home/control2/dobot_python') #If run from script
#sys.path.insert(0, os.path.abspath('.')) #If run from command

from lib.interface import Interface
from serial.tools import list_ports

available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')

port1 = available_ports[0].device

bot1 = Interface(port1)

print('Bot status:', 'connected' if bot1.connected() else 'not connected')
params = bot1.get_homing_paramaters()
print('Params:', params)

print('Homing')
bot1.set_homing_command(0)

print('Homing complete')

port2 = available_ports[1].device

bot2 = Interface(port2)

print('Bot status:', 'connected' if bot2.connected() else 'not connected')
params = bot2.get_homing_paramaters()
print('Params:', params)

print('Homing')
bot2.set_homing_command(0)

print('reset')
