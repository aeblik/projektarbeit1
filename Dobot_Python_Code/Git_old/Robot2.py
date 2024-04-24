from time import sleep
from dobotapi import Dobot
from dobotapi.utils import get_coms_port

bot = Dobot()
# In case of multipe Dobots connected to one device choose the port to adress once specific Dobot
bot.port = get_coms_port()[0]
bot.connect()

bot.clear_alarms()

#First block
bot.move_to_Joint(13.8287, -267.374, 46.5712)
bot.move_to_Joint(13.8287, -267.374, 15.4)
bot.suction_cup.suck()
time.sleep(0.5)
bot.move_to_Joint(13.8287, -267.374, 92)
bot.move_to_Joint(174.7025, -197.5623, 92)
bot.move_to_Joint(174.7029, -212.0127, 13.4273)
bot.suction_cup.idle()
bot.move_to_Joint(174.7029, -197.523, 92)
# Speed can range from -1.0 to 1.0 (negative values move the belt in the opposite direction)
bot.conveyor_belt.move(speed= (-0.5))
sleep(0.5) # move belt for 0.5 seconds
bot.conveyor_belt.idle() # Stop the conveyor belt

#Second block
bot.move_to_Joint(49.325, -270.2565, 46.5712)
bot.move_to_Joint(49.325, -270.2565, 13.4)
bot.suction_cup.suck()
time.sleep(0.5)
bot.move_to_Joint(49.325, -270.2565, 92)
bot.move_to_Joint(174.7025, -197.5623, 92)
bot.move_to_Joint(174.7029, -212.0127, 13.4273)
bot.suction_cup.idle()
bot.move_to_Joint(174.7029, -197.523, 92)
# Speed can range from -1.0 to 1.0 (negative values move the belt in the opposite direction)
bot.conveyor_belt.move(speed= (-0.5))
sleep(0.5) # move belt for 0.5 seconds
bot.conveyor_belt.idle() # Stop the conveyor belt

#Third block
bot.move_to_Joint(49.3254, -300.8365, 46.5712)
bot.move_to_Joint(46.3254, -300.8365, 12.4)
bot.suction_cup.suck()
time.sleep(0.5)
bot.move_to_Joint(46.3254, -300.8365, 92)
bot.move_to_Joint(174.7025, -197.5623, 92)
bot.move_to_Joint(174.7029, -212.0127, 13.4273)
bot.suction_cup.idle()
bot.move_to_Joint(174.7029, -197.523, 92)
# Speed can range from -1.0 to 1.0 (negative values move the belt in the opposite direction)
bot.conveyor_belt.move(speed= (-0.5))
sleep(0.5) # move belt for 0.5 seconds
bot.conveyor_belt.idle() # Stop the conveyor belt

#Fourth block
bot.move_to_Joint(14.4295, -300.84, 46.5712)
bot.move_to_Joint(14.4295, -300.84, 12.4)
bot.suction_cup.suck()
time.sleep(0.5)
bot.move_to_Joint(14.4295, -300.84, 92)
bot.move_to_Joint(174.7025, -197.5623, 92)
bot.move_to_Joint(174.7029, -212.0127, 13.4273)
bot.suction_cup.idle()
bot.move_to_Joint(174.7029, -197.523, 92)
# Speed can range from -1.0 to 1.0 (negative values move the belt in the opposite direction)
bot.conveyor_belt.move(speed= (-0.5))
sleep(0.5) # move belt for 0.5 seconds
bot.conveyor_belt.idle() # Stop the conveyor belt

bot.disconnect()