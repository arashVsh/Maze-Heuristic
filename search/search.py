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
        بر اساس لیستی از حرکات که توسط این تابع برگردانده می شود,
         pacman به ترتیب دو خانه به جنوب یک خانه به غرب,
       1 خانه به جنوب, دو خانه به غرب, یک خانه به جنوب و در آخر
         یک خانه به غرب می رود تا به خانه هدف برسد
    """

    """
        در توابع depthFirstSearch و aStartSearch الگوریتم شما
         باید لیستی از حرکات مجاز را پیدا کند و برگرداند.
    """

    """
           جرکتی که باعث برخورد pacman با دیوار شود, غیر مجاز است.
            در صورتی که لیست برگردانده شده شامل حرکن غیر مجاز باشد,
           برنامه با اعلام خطا در خط 353 فایل pacman.py متوقف می شود. 
    """

    return [S, S, W, S, W, W, S, W]


def sampleSearch_2(problem) -> list:
    """
    مشابه با تابع sampleSearch لیستی از حرکات مجاز برای رسیدن به مقصد را بر می گرداند
    """

    return [W, W, W, W, S, S, E, S, S, W]


""" ******************************************************************************** """


def depthFirstSearch(problem) -> list:
    """*** سوال 9 تمرین بخش اول ***"""
    return []


def aStarSearch(problem) -> list:
    """*** سوال 9 تمرین بخش دوم ***"""
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
