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

S = Directions.SOUTH
W = Directions.WEST
N = Directions.NORTH
E = Directions.EAST


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


def sampleSearch(problem) -> list:
    """
       Based on the list of moves returned by this function, Pacman moves two cells to the south,
       one cell to the west, one cell to the south, two cells to the west, one cell to the south,
       and finally, one cell to the west. Pacman reached his goal.
    """

    """
        In the functions “depthFirstSearch” and “aStarSearch”, 
        your algorithm must find a sequence of legal moves and return it as a list.
    """

    """
         Any move that causes Pacman to hit the wall is illegal. 
         If the returned list contains any illegal moves, the program stops by 
         raising an exception in line 353 of the pacman.py file.
    """

    """
         Please, note the overall map, including the initial situation of Pacman, its goal, and walls, is always the same,
         however, it's on you to decide how to determine the coordinates of these elements.
         For example, we can say the initial coordinate of Pacman is (1, 5) because it's in the 1st row and 5th column.
         Similarly, we can say its goal's coordinate is (5, 1) because it's in the 5th row and 1st column.
         You must determine the coordinates of the walls and restrain Pacman from changing its state to one of these coordinates.
    """

    return [S, S, W, S, W, W, S, W]


def sampleSearch2(problem) -> list:
    return [W, W, W, W, S, S, E, S, S, W]


""" ******************************************************************************** """


def depthFirstSearch(problem) -> list:
    """*** Question 9 - Part 1 ***"""
    return []


def aStarSearch(problem) -> list:
    """*** Question 9 - Part 2 ***"""
    return []


""" ******************************************************************************** """


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of the least total cost first."""
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
