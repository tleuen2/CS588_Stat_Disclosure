# course: cs588
# assignment: Final Project
# date: 04/25/2020
# username: tleuen2
# name: Thomas Leuenberger
# description: traffic generation simulator

import numpy as np
from random import seed
from random import random

class TrafficGenerator:
    
    def __init__(self, senders, receivers, target, targetsReceivers):
        """Constructor for TrafficGenerator.

        The constructor for TrafficGenerator will prepare internal data members
        based on user passed parameters

        Args:
            self (int): The object calling this method
            senders (str[]): A python list of senders on the network
            receivers (str[]) : A python list of receivers on the network
            target (str[]) : A string of the target of the attack (must be an 
                           entry in "senders")

        Returns:
            void
            
        """
        self.sendersList = senders
        self.receiverList = receivers
        self.targetReceiverList = targetsReceivers
        self.numOfSenders = len(senders)
        self.numOfRecievers = len(receivers)
        self.numOfTargetsReceivers = len(targetsReceivers)
        self.targetProbVector = self.build_target_vector()
        self.trafficProbVector = self.build_traffic_vector()
        self.outputVector = np.array([])
        
    def build_target_vector(self):
        """Builds a vector of propbabilites representing who the victim is most
           likely to be talking too.

        Build a vector with one entry for each reciever in the network. Each 
        entry in this vector corresponds to the probability that the target is 
        communicating with that particular reciever. 
        
        Internally numpy arrays are used so that vector operations are made 
        simple.

        Args:
            void
            depends on class memebers

        Returns:
            np.array : (vector) of propbabilites representing who the victim 
            is most likely to be talking too
            
        """
        
        targetProbs = np.empty(len(self.receiverList))
        count = 0
        
        # At the start we just assign all recievers as equally likely
        initialProbability = 1 / self.numOfTargetsReceivers
        
        # Potential improvement : use dictionary rather than implicit indexing
        for receiver in self.receiverList:
            if receiver in self.targetReceiverList:
                targetProbs[count] = initialProbability
                count += 1
            else:
                targetProbs[count] = 0
                count += 1
            
        #print ('This is the target probability vector\n', targetProbs)
        return targetProbs
        
    def build_traffic_vector(self):
        """Builds a vector of propbabilites representing who the victim is most
           likely to be talking too.

        Build a vector with one entry for each reciever in the network. Each 
        entry in this vector corresponds to the probability that the target is 
        communicating with that particular reciever. 
        
        Internally numpy arrays are used so that vector operations are made 
        simple.

        Args:
            void
            depends on class memebers

        Returns:
            np.array : (vector) of propbabilites representing who the victim 
            is most likely to be talking too
            
        """
        
        targetProbs = np.empty(len(self.receiverList))
        count = 0
        
        # At the start we just assign all recievers as equally likely
        initialProbability = 1 / self.numOfRecievers
        
        # Potential improvement : use dictionary rather than implicit indexing
        for receiver in self.receiverList:
            targetProbs[count] = initialProbability
            count += 1
            
        #print ('This is the traffic probability vector\n', targetProbs)
        return targetProbs
    
    def set_target_vector(self, newVector):
        """Overwrites member variable for the target's probability vector
        
        Args:
            newVector (np.array) : The new target vector to be written

        Returns:
            void
            
        """
        self.targetProbVector = newVector
        
    def generate_observation(self):
        """Generates an observation of one iteration of communication on the 
            network
            
        The observation is a probability distribution. Each entry is the chance
        that the recipient at that entry is the target's receiver. The output
        must sum to 1 as it is a probability distribution. 
        
        Currently we are limited to only one target. This could be an 
        improvement for later work
        
        Args:
            void
            depends on class members

        Returns:
            np.array : (vector) representing the observation of one iteration 
            of network communication
            
        """
        
        output = np.empty(len(self.receiverList))
        count = 0
        coutn2 = 0
        
        # in order to create random traffic, we use a list of randomly generated
        # numbers between 0 and 1. Each of these number respresents the chance
        # that the recipient is the target's reciepient. 
        dist = np.random.random(self.numOfRecievers)
        
        # In oder to ensure that the observation vector sums to 1. Remeber that
        # this vector IS a probability disribution. It is generated randomly, 
        # and likely doesn't fit any known distribution, but that is okay. 
        # traffic on a network is highly sporatic
        normalizing_cosnt = np.sum(dist)
        dist = np.divide(dist, normalizing_cosnt)
        
        # We will assign the maximum likelihood in the distribution to the 
        # target's true recipient. 
        max_value = np.amax(dist)
        max_index = np.where(dist == max_value)
        
        # To make like easier later - remove the value from the distribution.
        # This is so that we can just iterate over the distribution without 
        # worrying about other recievers getting the maximum value
        dist = np.delete(dist, max_index[0][0])
        
        # Assign probabilities to receivers on the network
        for receiver in self.receiverList:
            if receiver not in self.targetReceiverList:
                value = dist[count]
                count += 1
            else:
                # the true reciever gets the maximum value
                value = max_value
            output[coutn2] = value
            coutn2 += 1
            
        return output
        
    def get_traffic_prob_vec(self):
        """Gets trafficProbVector
        
        Args:
            void
            depends on class members

        Returns:
            np.array : containing the class's traffic probability vector
            
        """
        
        return self.trafficProbVector
        
    def get_num_of_recievers(self):
        """Gets the number of receivers on the network
        
        Args:
            void
            depends on class members

        Returns:
            int : containing the number of receivers
            
        """
        return self.numOfRecievers