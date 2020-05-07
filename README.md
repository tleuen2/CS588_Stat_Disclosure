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
