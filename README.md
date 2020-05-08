# CS588_Stat_Disclosure
This repo contains my final project for CS588. The project is focused on
statistical disclosure, and the code in this repo is an implementation of the
attack. This readme contains information about how to run the simulation, for
more information about the underpinnings of the attack please see the project
report.

## Requirements
### Python
This project requires Python version 3.8.2.   
Disclaimer - The project may run with other versions of Python 3, however the
project was built and tested with version 3.8.2
### Packages
The following Python packages are required -
* numpy
* random

## Usage
This simulator is run via the "run.py" script. First the script should be
updated with the attack parameters to be tested.

### Parameters of the attack
* mySenders -> Python list of the names of the senders on the network
  * Example input -> ['Beth', 'Bill', 'Clair', 'Charles']
* myRecievers -> Python list of the names of the receivers on the network
  * Example input -> ['Frank', 'Greg', 'Steven', 'Tyler', 'Ned', 'Bob',
  'Stacey']
* myTarget -> Python string of the name of the target of the attack. Note that
there can only be one target.
  * Example input -> 'Beth'
* myTargetsReciever -> Python list of the names of the target's recipients
  * Example input -> ['Frank', 'Bob']
* myNumOfIterations -> int of the number of communications rounds for which to
perform the attack
  * Example input -> 100000
* myNumOfTargetMessagesPerRound -> int of the number of messages that the
target sends each round
  * Example input -> 2

### Running the simulation
The simulation is run by invoking the run.py script via your local python
interpreter. For example "$ python run.py " from a bash terminal.

## Understanding the output
The output of the attack will look like this (using the example inputs for
simulation parameters)


    Now Starting Test Run
    The target of this attack was : Beth
    The targets receiver(s) was(were) : Frank, Bob
    The number of senders on the network was : 4
    The number of messages sent by that target each round was : 2
    The list of senders on the network was :
    ************************************
    Beth
    Bill
    Clair
    Charles
    ************************************
    The number of receivers on the network was : 11
    The list of recipients was :
    ************************************
    Beth
    Bill
    Clair
    Charles
    Frank
    Greg
    Steven
    Tyler
    Ned
    Bob
    Stacey
    ************************************
    The number of iterations the attack was run was : 100000
    The result of the attack was :
    ************************************
    Beth : 0.09979799469698866
    Bill : 0.04012515227833423
    Clair : 0.03310670466519659
    Charles : 0.01948090892837845
    Frank : 0.32525165788913657
    Greg : 0.08095724920731727
    Steven : 0.041487099290166446
    Tyler : 0.05205931223040469
    Ned : 0.08461957417217687
    Bob : 0.1679381718938153
    Stacey : 0.05519617474809045
    ************************************
First that parameters of the attack are reiterated for clarity, additionally
the actual values used for the attack are shown which should help quickly
uncover any mistakes.

The results section contains the probability that the target is communicating
with each possible recipient. In this attack the target is communicating with
Frank and Bob. From the results we can see that the probability of the target
communicating with Frank is 0.325 and the probability that the target is
communicating with Bob is 0.167. Note that these are the highest values in the
list of possible recipients, however we are still very unsure that these are
truly that target's recipients.  
