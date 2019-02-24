# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent
import collections
from functools import reduce

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        for i in  range(self.iterations):
            v = util.Counter()
            for s0 in self.mdp.getStates():
                if self.mdp.isTerminal(s0):
                    continue
                v[s0] = -float("inf")
                for a in self.mdp.getPossibleActions(s0):
                    val = 0
                    for s, p in self.mdp.getTransitionStatesAndProbs(s0, a):
                        val += p * (self.mdp.getReward(s0, a, s) + self.discount * self.values[s])
                    v[s0] = max(v[s0], val)
            self.values = v.copy()


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        v = 0
        for s, p in self.mdp.getTransitionStatesAndProbs(state, action):
           v += p * (self.mdp.getReward(state, action, s) + self.discount * self.values[s])
        return v

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        action = None
        qVal = None
        for a in self.mdp.getPossibleActions(state):
            if action is None or self.getQValue(state, a) > qVal:
                action = a
                qVal = self.getQValue(state, a)
        return action


    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

class AsynchronousValueIterationAgent(ValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        An AsynchronousValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs cyclic value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 1000):
        """
          Your cyclic value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy. Each iteration
          updates the value of only one state, which cycles through
          the states list. If the chosen state is terminal, nothing
          happens in that iteration.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state)
              mdp.isTerminal(state)
        """
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        states = self.mdp.getStates()
        for i in range(self.iterations):
            v = self.values.copy()
            s0 = states[i % len(states)]
            if self.mdp.isTerminal(s0):
                continue
            v[s0] = -float("inf")
            for a in self.mdp.getPossibleActions(s0):
                val = 0
                for s, p in self.mdp.getTransitionStatesAndProbs(s0, a):
                    val += p * (self.mdp.getReward(s0, a, s) + self.discount * self.values[s])
                v[s0] = max(v[s0], val)
            self.values = v.copy()

class PrioritizedSweepingValueIterationAgent(AsynchronousValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A PrioritizedSweepingValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs prioritized sweeping value iteration
        for a given number of iterations using the supplied parameters.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100, theta = 1e-5):
        """
          Your prioritized sweeping value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        pred = self.generatePredecessors()
        pQ = util.PriorityQueue()
        states = self.mdp.getStates()
        for s in states:
            if self.mdp.isTerminal(s):
                continue
            pQ.push(s, -self.getDiff(s))
        for i in range(self.iterations):
            if pQ.isEmpty():
                break
            v = self.values.copy()
            s0 = pQ.pop()
            v[s0] = -float("inf")
            for a in self.mdp.getPossibleActions(s0):
                val = 0
                for s, p in self.mdp.getTransitionStatesAndProbs(s0, a):
                    val += p * (self.mdp.getReward(s0, a, s) + self.discount * self.values[s])
                v[s0] = max(v[s0], val)
            self.values = v.copy()
            for p in pred[s0]:
                diff = self.getDiff(p)
                if diff > self.theta:
                    pQ.update(p, -diff)


    def getDiff(self, s):
        qV = -float('inf')
        for a in self.mdp.getPossibleActions(s):
            qV = max(qV, self.getQValue(s, a))
        return abs(qV - self.values[s])

    def generatePredecessors(self):
        pred = {}
        for s in self.mdp.getStates():
            for a in self.mdp.getPossibleActions(s):
                for next, p in self.mdp.getTransitionStatesAndProbs(s, a):
                    if p > 0:
                        if next not in pred:
                            pred[next] = {s}
                        else:
                            pred[next].add(s)
        return pred