# **Subject**: Adversarial agents

All agents algorithms can be found in the "multiAgents.py" file.

**Reflex Agent**: A reflex agent chooses an action at each choice point by examining its alternatives via a state evaluation function. 
It only considers immediate results.

**Commands**: 

* python pacman.py -p ReflexAgent -l testClassic

* python pacman.py --frameTime 0 -p ReflexAgent -k 1

* python pacman.py --frameTime 0 -p ReflexAgent -k 2

* python autograder.py -q q1

* python autograder.py -q q1 --no-graphics

**MinMax Agent**: Implements the MinMax algorithm for a given state evaluation function and depth parameter.

**Commands**: 

* python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4

* python pacman.py -p MinimaxAgent -l trappedClassic -a depth=3

* python autograder.py -q q2

* python autograder.py -q q2 --no-graphics

**AlphaBeta Agent**: Implements the AlphaBeta algorithm (improved MinMax which avoids running through unecessary nodes) for a given state evaluation function and depth parameter.

**Commands**: 

* python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic

* python pacman.py -p AlphaBetaAgent -l trappedClassic -a depth=3 -q -n 10

* python autograder.py -q q3

* python autograder.py -q q3 --no-graphics

**EspectiMax Agent**: Implements the MinMax algorithm (MinMax which contains random nodes) for a given state evaluation function and 
depth parameter.

**Commands**: 

* python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3

* python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q -n 10

* python autograder.py -q q4

* python autograder.py -q q4 --no-graphics

**Better evaluation function**: developed heuristic to improve the agents performance.

**Commands**: 

* python autograder.py -q q5

* python autograder.py -q q5 --no-graphics
