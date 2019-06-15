# *Subject* : Reinforcement Learning

**Problem** : Agents are tested first on a Gridworld, then applied to a simulated Pacman. Agents will have
policies giving the action they should take in a state based on their future reward which takes into account a discount for not immediate
rewards and a noise in their actions (this means that with a given probability they may take a random action).

In this project, value iteration (Markov Decision Process - MDP) and Q-learning (Reinforcement learning) were implemented. This is the description for the **value iteration**.

All algorithms can be found in the "valueIterationAgents.py.py" and "analysis.py" files.

# **Value iteration**

## **Value iteration agent**

Agent in valueIterationAgents.py which is an offline planner, not a reinforcement learning agent, and so 
the relevant training option is the number of iterations of value iteration it should run (option -i) in its initial planning phase. 
ValueIterationAgent takes an MDP on construction and runs value iteration for the specified number of iterations before the constructor 
returns.

**Commands**

* python gridworld.py -a value -i 100 -k 10

* python gridworld.py -a value -i 5

## **Bridge crossing analysis**

BridgeGrid is a grid world map with the a low-reward terminal state and a high-reward terminal state 
separated by a narrow "bridge", on either side of which is a chasm of high negative reward. The agent starts near the low-reward state.
With the default discount of 0.9 and the default noise of 0.2, the optimal policy does not cross the bridge. But a noise of 0 makes it 
possible.

**Commands**

* python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.9 --noise 0.2

* python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.9 --noise 0


## **Asynchronous Value Iteration Agent**

In valueIterationAgents.py this is also an offline planner and will update only one state in each 
iteration, as opposed to doing a batch-style update. In the first iteration, only update the value of the first state in the states list. 
In the second iteration, only update the value of the second. Keep going until you have updated the value of each state once, then start 
back at the first state for the subsequent iteration. If the state picked for updating is terminal, nothing happens in that iteration. 

**Commands**

* python gridworld.py -a asynchvalue -i 1000 -k 10


## **Prioritized Sweeping Value Iteratio**

In valueIterationAgents.py this agent derives from AsynchronousValueIterationAgent.Prioritized 
sweeping attempts to focus updates of state values in ways that are likely to change the policy. First, we define the predecessors of 
a state s as all states that have a nonzero probability of reaching s by taking some action theta, which is passed in as a parameter,
represents our tolerance for error when deciding whether to update the value of a state. 

**Commands**

* python gridworld.py -a priosweepvalue -i 1000
