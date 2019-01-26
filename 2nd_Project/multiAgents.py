# multiAgents.py
# --------------
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


from util import manhattanDistance
# from game import Directions
from game import Agent
import random
import util as util


class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best
        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    @staticmethod
    def evaluationFunction(currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"

        foodPos = getPositions(newFood)
        ghostPos = successorGameState.getGhostPositions()
        scaredGhostPos = [g for i, g in enumerate(ghostPos)
                          if (newScaredTimes[i] > 0 and manhattanDistance(newPos, g) < newScaredTimes[i])]
        notScaredGhostPos = [g for g in ghostPos if g not in scaredGhostPos]
        score = successorGameState.getScore()

        if len(foodPos) == 0:
            return 9999

        ns = minManhattanDistance(newPos, notScaredGhostPos)
        s = minManhattanDistance(newPos, scaredGhostPos)
        f = minManhattanDistance(newPos, foodPos)

        if currentGameState.getNumFood() > successorGameState.getNumFood():
            score += 10
        if ns == 1:
            score -= 10
        else:
            score += ns / 10
        score -= s
        score -= f

        if newPos == currentGameState.getPacmanPosition():
            score -= 10

        return score

def getPositions(board):
    pos = []
    for i in range(len([row for row in board])):
        for j in range(len(board[0])):
            if board[i][j]:
                pos.append((i, j))
    return pos

def minManhattanDistance(origin, targets):
    if len(targets) == 0:
        return 0
    d = 9999
    for t in targets:
        d = min(d, manhattanDistance(origin, t))
    return d


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game

          gameState.isWin():
            Returns whether or not the game state is a winning state

          gameState.isLose():
            Returns whether or not the game state is a losing state
        """

        "*** YOUR CODE HERE ***"
        actions = gameState.getLegalActions(0)
        score = None
        bestAction = None
        for act in actions:
            successor = gameState.generateSuccessor(0, act)
            actScore = self.minMax(successor, self.depth, 1)
            if score is None:
                score = actScore
                bestAction = act
            elif score < actScore:
                score = actScore
                bestAction = act
        return bestAction

    def minMax(self, state, depth, agentIndex):

        if agentIndex == state.getNumAgents():
            depth -= 1
            agentIndex = 0

        if state.isWin():
            return self.evaluationFunction(state)
        elif state.isLose():
            return self.evaluationFunction(state)

        if depth == 0:
            return self.evaluationFunction(state)

        score = None
        actions = state.getLegalActions(agentIndex)

        for act in actions:
            successor = state.generateSuccessor(agentIndex, act)
            actScore = self.minMax(successor, depth, agentIndex + 1)
            if score is None:
                score = actScore
            elif agentIndex == 0:
                score = max(score, actScore)
            else:
                score = min(score, actScore)
        return score


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        actions = gameState.getLegalActions(0)
        score = None
        bestAction = None
        alpha = None
        for act in actions:
            successor = gameState.generateSuccessor(0, act)
            actScore = self.alphaBeta(successor, self.depth, 1, alpha, None)
            if score is None:
                score = actScore
                alpha = score
                bestAction = act
            elif score < actScore:
                score = actScore
                alpha = score
                bestAction = act
        return bestAction

    def alphaBeta(self, state, depth, agentIndex, alpha, beta):

        if agentIndex == state.getNumAgents():
            depth -= 1
            agentIndex = 0

        if state.isWin():
            return self.evaluationFunction(state)
        elif state.isLose():
            return self.evaluationFunction(state)

        if depth == 0:
            return self.evaluationFunction(state)

        score = None
        actions = state.getLegalActions(agentIndex)

        for act in actions:
            successor = state.generateSuccessor(agentIndex, act)
            actScore = self.alphaBeta(successor, depth, agentIndex + 1, alpha, beta)
            if score is None:
                score = actScore
                if agentIndex == 0:
                    if beta is not None:
                        if actScore > beta:
                            return actScore
                    if alpha is not None:
                        alpha = max(actScore, alpha)
                    else:
                        alpha = actScore
                else:
                    if alpha is not None:
                        if actScore < alpha:
                            return actScore
                    if beta is not None:
                        beta = min(beta, actScore)
                    else:
                        beta = actScore
            elif agentIndex == 0:
                if beta is not None:
                    if actScore > beta:
                        return actScore
                score = max(score, actScore)
                alpha = max(score, alpha)
            else:
                if alpha is not None:
                    if actScore < alpha:
                        return actScore
                score = min(score, actScore)
                beta = min(score, beta)
        return score

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()


def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

