# course: cs588
# assignment: Final Project
# date: 04/25/2020
# username: tleuen2
# name: Thomas Leuenberger
# description: statistical disclosure implementation 

import numpy as np
from random import seed
from random import random

class StatDisclosure:

    def __init__(self, batchSizeInput, numOfIterationsInput, trafficGen):
        """Constructor for StatDisclosure.

        The constructor for StatDisclosure will prepare internal data members
        based on user passed parameters

        Args:
            self (int): The object calling this method
            batchSize (int): Size of one batch of messages in the network 
                             (usually the number of senders)
            numOfIterations (int) : The number of rounds of communication that 
                                    the attacker observes
            trafficGen (TrafficGeneration) : Class to hold traffic information 
                                             about the network

        Returns:
            void
            
        """
        self.batchSize = batchSizeInput
        self.numOfIterations = numOfIterationsInput
        self.trafficGenerator = trafficGen
        
    def simulate(self):
        """Runs simulation

        Performs the statistical disclsoure attack on simulated traffic

        Args:
            self (int): The object calling this method

        Returns:
            void
            
        """
        
        observations = self.generate_traffic()
        messagesPerRound = \
                    self.trafficGenerator.get_num_of_messages_sent_by_target()
        
        summationOfObservations = self.sum_vectors(observations)

        result = np.multiply(self.batchSize, \
                 (np.divide(summationOfObservations, \
                 self.numOfIterations)))

        result = np.subtract(result, \
                 np.multiply((self.batchSize - messagesPerRound), \
                 self.trafficGenerator.get_traffic_prob_vec()))
                    
        result = np.divide(result, messagesPerRound)
        
        self.print_result(result)
        return
        
        
    def sum_vectors(self, vectors):
        """Runs simulation

        Performs the statistical disclsoure attack on simulated traffic

        Args:
            self (int): The object calling this method
            vectors (np.array[]) : list of np.array's containing vectors to be 
                                   added

        Returns:
            np.array : (vector) of the result of the summation 
            
        """
        
        result = np.empty(self.trafficGenerator.get_num_of_receivers())
        
        for vec in vectors:
           result = np.add(result, vec)
            
        return result
        
    def generate_traffic(self):
        """Generates traffic observations for the simulator

        Performs the statistical disclsoure attack on simulated traffic

        Args:
            self (int): The object calling this method
            vectors (np.array[]) : list of np.array's containing vectors to be 
                                   added

        Returns:
            python array : of np.array's containing each generated observation
            
        """
        
        result = []
        
        for i in range(self.numOfIterations):
            result.append(self.trafficGenerator.generate_observation())
            
        return result
        
    def print_result(self, result):
        """Nicley print result for users

        Args:
            self (int): The object calling this method
            result (np.array[]) : vector containing the probability distribution
                                  from performing the attack

        Returns:
            void
            
        """
        
        outputString = 'The target of this attack was : '
        outputString += self.trafficGenerator.get_target()
        outputString += '\nThe targets receiver was : '
        outputString += self.trafficGenerator.get_target_receiver()
        outputString += '\nThe number of senders on the network was : '
        outputString += str(self.trafficGenerator.get_num_of_senders())
        outputString += '\nthe list of senders on the network was : '
        outputString += self.trafficGenerator.print_senders()
        outputString += '\nThe number of receivers on the network was : '
        outputString += str(self.trafficGenerator.get_num_of_receivers())
        outputString += '\nThe list of recipients was : '
        outputString += self.trafficGenerator.print_receivers()
        outputString += '\nThe number of iterations the attack was run was : '
        outputString += str(self.numOfIterations)
        outputString += '\nThe result of the attack was : '
        outputString += self.trafficGenerator.print_receivers(result)
        
        print(outputString)