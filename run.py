# course: cs588
# assignment: Final Project
# date: 04/25/2020
# username: tleuen2
# name: Thomas Leuenberger
# description: this file prepares data and runs the simulation

import numpy as np
from random import seed
from random import random
import StatDisclosure
import TrafficGeneration

print('Now Starting Test Run')

mySenders = ['Beth', 'Bill', 'Clair', 'Charles']
myRecievers = ['Frank', 'Greg', 'Steven', 'Tyler', 'Ned', 'Bob', 'Stacey']
myTarget = ['Beth']
myTargetsReciever = ['Greg']
myBatchSize = 4 # num of senders
myNumOfIterations = 1000
 
myTraffic = TrafficGeneration.TrafficGenerator(mySenders, myRecievers,\
                myTarget, myTargetsReciever)
                
myStatDisclosure = StatDisclosure.StatDisclosure(myBatchSize, \
                    myNumOfIterations, myTraffic)
 
myStatDisclosure.simulate()