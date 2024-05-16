from serial.tools import list_ports
import time
import pydobot


available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = available_ports[0].device

bot = pydobot.Dobot(port=port, verbose=False)





# Clear any existing alarms
#bot.home()
#bot.home()
#bot.set_point_to_point_joint_params(velocity=0.6, acceleration = 20)
#bot.set_point_to_point_joint_params(20, 20)
bot.speed(velocity=80, acceleration=60)

bot.grip(False)
time.sleep(1)
bot.move_to(116.3743,-194.0146,7.5,57.408, wait=True)
bot.grip(True)
time.sleep(1)
#bot.gripper.disable()
bot.close()

#bot.move_to_Joint(116.3743, -194.0146, 7.5, 57.408)
