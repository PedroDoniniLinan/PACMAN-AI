# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
import searchAgents as sa


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


class Node:
    """
    This class outlines the structure of a node containing a state, parent, action and
    a path-cost. It is used as the unitary element for the searches developed below.
    """
    def __init__(self, state, parent, action, cost, info=[]):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.info = info


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def reconstructPath(problem, goal):
    """
    Reconstructs path from search node of the goal.

    :param problem:
    :param goal: Search node of the goal
    :return: The list of directions to be taken from the start to
    arrive to the goal
    """

    actions = []
    current = goal
    while current.state != problem.getStartState():
        actions.append(current.action)
        current = current.parent
    return list(reversed(actions))


def initializeFrontier(problem, strategy='dfs', heuristic=nullHeuristic):
    """
    Initialize frontier according to strategy and data structure.

    :param problem:
    :param strategy: Type of search
    :return: frontier
    """
    frontiers = {
        'dfs': util.Stack(),
        'bfs': util.Queue(),
        'ucs': util.PriorityQueue(),
        'astar': util.PriorityQueue()
    }
    frontier = frontiers[strategy]
    if strategy == 'dfs' or strategy == 'bfs':
        frontier.push(Node(problem.getStartState(), None, None, 0))
    elif strategy == 'ucs':
        frontier.push(Node(problem.getStartState(), None, None, 0), 0)
    else:
        frontier.push(Node(problem.getStartState(), None, None, 0),
                      heuristic(problem.getStartState(), problem) + 0)
    return frontier


def pushIntoFrontier(frontier, s, current, problem, strategy='dfs', heuristic=nullHeuristic):
    """
    Add to the frontier, states to be treat in the next iteration.

    :param frontier:
    :param s: One of successor
    :param current: Current State
    :param problem:
    :param strategy: Type of search
    """
    if strategy == 'ucs':
        frontier.push(Node(s[0], current, s[1], s[2] + current.cost), s[2] + current.cost)
    elif strategy == 'astar':
        frontier.push(Node(s[0], current, s[1], s[2] + current.cost), s[2] + current.cost
                      + heuristic(s[0], problem))
    else:
        frontier.push(Node(s[0], current, s[1], s[2] + current.cost))


def graphSearch(problem, strategy='dfs', heuristic=nullHeuristic):
    """
    Generic graph search algorithm.

    :param problem:
    :param strategy: Type of search to be used
    :return: The list of directions necessary to build the solution's path
    """

    visited = set()
    frontier = initializeFrontier(problem, strategy, heuristic)
    while not frontier.isEmpty():
        current = frontier.pop()
        if problem.isGoalState(current.state):
            return reconstructPath(problem, current)
        if current.state not in visited:
            visited.add(current.state)
            for s in problem.getSuccessors(current.state):
                pushIntoFrontier(frontier, s, current, problem, strategy, heuristic)
    return None


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    "*** YOUR CODE HERE ***"

    stop = Directions.STOP

    solution = graphSearch(problem)

    if solution is not None:
        return solution

    return [stop]


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    "*** YOUR CODE HERE ***"

    stop = Directions.STOP

    solution = graphSearch(problem, 'bfs')

    if solution is not None:
        return solution

    print("NONE")
    return [stop]


def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    "*** YOUR CODE HERE ***"

    stop = Directions.STOP

    solution = graphSearch(problem, 'ucs')

    if solution is not None:
        return solution

    return [stop]


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    "*** YOUR CODE HERE ***"

    stop = Directions.STOP

    solution = graphSearch(problem, 'astar', heuristic)

    if solution is not None:
        return solution

    return [stop]


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
