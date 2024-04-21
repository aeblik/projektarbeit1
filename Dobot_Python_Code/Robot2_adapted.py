from time import sleep
from dobotapi import Dobot
from dobotapi.utils import get_coms_port

bot = Dobot()
# In case of multipe Dobots connected to one device choose the port to adress once specific Dobot
bot.port = get_coms_port()[0]
bot.connect()

bot.clear_alarms()

# Definition of x,y,z coordinates for the robot to move to
# blocks on pallett
first_block_above = [13.8287, -267.374, 90]
second_block_above = [49.325, -270.2565, 90]
third_block_above = [49.3254, -300.8365, 90]
fourth_block_above = [14.4295, -300.84, 90]

first_block_pick = [first_block_above[0], 
                    first_block_above[1], 
                    first_block_above[2] - (first_block_above[2]- 15.4)
                    ]

second_block_pick = [second_block_above[0], 
                     second_block_above[1], 
                     second_block_above[2] - (second_block_above[2]- 13.4)
                     ]

third_block_pick = [third_block_above[0],
                    third_block_above[1], 
                    third_block_above[2] - (third_block_above[2]- 12.4)
                    ]

fourth_block_pick = [fourth_block_above[0], 
                     fourth_block_above[1], 
                     fourth_block_above[2] - (fourth_block_above[2]- 12.4)
                     ]


# Drop of point of the blocks on the conveyor belt
above_conveyor_belt = [174.7025, -212.0127, 90] # Above the conveyor belt

on_conveyor_belt = [above_conveyor_belt[0], 
                    above_conveyor_belt[1], 
                    above_conveyor_belt[2] - (above_conveyor_belt[2] - 13.4273)] # On the conveyor belt


#First block
bot.move_to_Joint(first_block_above[0], first_block_above[1], first_block_above[2]) # Move above the first block
bot.move_to_Joint(first_block_pick[0], first_block_pick[1], first_block_pick[2]) # Pick the first block
bot.suction_cup.suck()
sleep(0.5)
bot.move_to_Joint(first_block_above[0], first_block_above[1], first_block_above[2]) # Lift the first block
bot.move_to_Joint(above_conveyor_belt[0],above_conveyor_belt[1],above_conveyor_belt[2])
bot.move_to_Joint(on_conveyor_belt[0],on_conveyor_belt[1],on_conveyor_belt[2])
bot.suction_cup.idle()
bot.move_to_Joint(above_conveyor_belt[0],above_conveyor_belt[1],above_conveyor_belt[2])
# Speed can range from -1.0 to 1.0 (negative values move the belt in the opposite direction)
bot.conveyor_belt.move(speed= (-0.5))
sleep(0.5) # move belt for 0.5 seconds
bot.conveyor_belt.idle() # Stop the conveyor belt

#Second block
bot.move_to_Joint(second_block_above[0], second_block_above[1], second_block_above[2])
bot.move_to_Joint(second_block_pick[0], second_block_pick[1], second_block_pick[2])
bot.suction_cup.suck()
sleep(0.5)
bot.move_to_Joint(second_block_above[0], second_block_above[1], second_block_above[2])
bot.move_to_Joint(above_conveyor_belt[0],above_conveyor_belt[1],above_conveyor_belt[2])
bot.move_to_Joint(on_conveyor_belt[0],on_conveyor_belt[1],on_conveyor_belt[2])
bot.suction_cup.idle()
bot.move_to_Joint(above_conveyor_belt[0],above_conveyor_belt[1],above_conveyor_belt[2])
# Speed can range from -1.0 to 1.0 (negative values move the belt in the opposite direction)
bot.conveyor_belt.move(speed= (-0.5))
sleep(0.5) # move belt for 0.5 seconds
bot.conveyor_belt.idle() # Stop the conveyor belt

#Third block
bot.move_to_Joint(third_block_above[0], third_block_above[1], third_block_above[2])
bot.move_to_Joint(third_block_pick[0], third_block_pick[1], third_block_pick[2])
bot.suction_cup.suck()
sleep(0.5)
bot.move_to_Joint(third_block_above[0], third_block_above[1], third_block_above[2])
bot.move_to_Joint(above_conveyor_belt[0],above_conveyor_belt[1],above_conveyor_belt[2])
bot.move_to_Joint(on_conveyor_belt[0],on_conveyor_belt[1],on_conveyor_belt[2])
bot.suction_cup.idle()
bot.move_to_Joint(above_conveyor_belt[0],above_conveyor_belt[1],above_conveyor_belt[2])
# Speed can range from -1.0 to 1.0 (negative values move the belt in the opposite direction)
bot.conveyor_belt.move(speed= (-0.5))
sleep(0.5) # move belt for 0.5 seconds
bot.conveyor_belt.idle() # Stop the conveyor belt

#Fourth block
bot.move_to_Joint(fourth_block_above[0], fourth_block_above[1], fourth_block_above[2])
bot.move_to_Joint(fourth_block_pick[0], fourth_block_pick[1], fourth_block_pick[2])
bot.suction_cup.suck()
sleep(0.5)
bot.move_to_Joint(fourth_block_above[0], fourth_block_above[1], fourth_block_above[2])
bot.move_to_Joint(above_conveyor_belt[0],above_conveyor_belt[1],above_conveyor_belt[2])
bot.move_to_Joint(on_conveyor_belt[0],on_conveyor_belt[1],on_conveyor_belt[2])
bot.suction_cup.idle()
bot.move_to_Joint(above_conveyor_belt[0],above_conveyor_belt[1],above_conveyor_belt[2])
# Speed can range from -1.0 to 1.0 (negative values move the belt in the opposite direction)
bot.conveyor_belt.move(speed= (-0.5))
sleep(0.5) # move belt for 0.5 seconds
bot.conveyor_belt.idle() # Stop the conveyor belt

bot.disconnect()