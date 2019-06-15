# *Subject* : Reinforcement Learning

**Problem** : Agents are tested first on a Gridworld, then applied to a simulated Pacman. Agents will have
policies giving the action they should take in a state based on their future reward which takes into account a discount for not immediate
rewards and a noise in their actions (this means that with a given probability they may take a random action).

In this project, value iteration (Markov Decision Process - MDP) and Q-learning (Reinforcement learning) were implemented. This is the description for the **reinforcement learning**.

All algorithms can be found in the "qLearningAgents.py.py" and "analysis.py" files.

# **Reinforcement Learning**

## **Q-Learning**

The value iteration agent does not actually learn from experience. Rather, it ponders its MDP model to arrive at a complete policy 
before ever interacting with a real environment. When it does interact with the environment, it simply follows the precomputed policy. 
This distinction may be subtle in a simulated environment like a Gridword, but it's very important in the real world, where the real 
MDP is not available.

The Q-learning agent, which does very little on construction, but instead learns by trial and error from interactions with the 
environment through its update(state, action, nextState, reward) method. The update is done by computeValueFromQValues, getQValue, 
and computeActionFromQValues methods.

**Commands**

* python gridworld.py -a q -k 5 -m (uses keyboard to show how the agent learns)

## **Epsilon greedy**

The epsilon-greedy action selection in getAction, means the agent chooses random actions an epsilon fraction (e) of the time, and 
follows its current best Q-values otherwise. Note that choosing a random action may result in choosing the best action.

**Commands**

* python gridworld.py -a q -k 100 

* python gridworld.py -a q -k 100 --noise 0.0 -e 0.1

* python gridworld.py -a q -k 100 --noise 0.0 -e 0.9

## **Bridge Crossing Revisited**

**Commands**

* python gridworld.py -a q -k 50 -n 0 -g BridgeGrid -e 1

* python gridworld.py -a q -k 50 -n 0 -g BridgeGrid -e 0

## **Q-Learning and Pacman**

Pacman will play games in two phases. In the first phase, training, Pacman will begin to learn about the values of positions and actions.
Because it takes a very long time to learn accurate Q-values even for tiny grids, Pacman's training games run in quiet mode by default, 
with no GUI (or console) display. Once Pacman's training is complete, he will enter testing mode. When testing, Pacman's self.epsilon 
and self.alpha will be set to 0.0, effectively stopping Q-learning and disabling exploration, in order to allow Pacman to exploit his 
learned policy.

**Commands**

* python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid ( 10 test games after the 2000 training games )

* python pacman.py -p PacmanQAgent -n 10 -l smallGrid -a numTraining=10 (10 training games)
