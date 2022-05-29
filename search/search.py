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
import pdb

from game import Directions

S = Directions.SOUTH
W = Directions.WEST
N = Directions.NORTH
E = Directions.EAST

tinyMap: list = [[1, 1, 1, 1, 1],
                 [1, 0, 0, 0, 1],
                 [1, 1, 0, 1, 1],
                 [0, 1, 1, 1, 0],
                 [1, 1, 0, 0, 0]]


class Cell:
    row: int
    col: int
    g: int
    parents: list

    def __init__(self, row, col, g, parents):
        self.col = col
        self.row = row
        self.g = g
        self.parents = parents

    def reproduce(self, row, col, g, parents):
        return Cell(row, col, g, parents)

    def neighbors(self) -> list:
        myList: list = []
        #        pdb.set_trace()

        if self.row > 0 and tinyMap[self.row - 1][self.col]:
            myList.append(self.reproduce(self.row - 1, self.col, self.g + 1, self.parents + [self]))
        if self.row < 4 and tinyMap[self.row + 1][self.col]:
            myList.append(self.reproduce(self.row + 1, self.col, self.g + 1, self.parents + [self]))
        if self.col > 0 and tinyMap[self.row][self.col - 1]:
            myList.append(self.reproduce(self.row, self.col - 1, self.g + 1, self.parents + [self]))
        if self.col < 4 and tinyMap[self.row][self.col + 1]:
            myList.append(self.reproduce(self.row, self.col + 1, self.g + 1, self.parents + [self]))
        return myList

    def manhattanDistance(self) -> int:
        return abs(self.row - 4) + abs(self.col - 0)

    def cost(self) -> int:
        return self.manhattanDistance() + self.g

    def isGoal(self) -> bool:
        return self.row == 4 and self.col == 0

    def isEqualTo(self, cell) -> bool:
        return self.row == cell.row and self.col == cell.col

    def isIn(self, myList: list) -> bool:
        for cell in myList:
            if self.isEqualTo(cell):
                return True
        return False

    def directionTo(self, nextCell) -> str:
        if self.col == nextCell.col and nextCell.row == self.row + 1:
            return S
        if self.col == nextCell.col and nextCell.row == self.row - 1:
            return N
        if self.row == nextCell.row and nextCell.col == self.col + 1:
            return E
        return W

    def __str__(self):
        return '(' + str(self.row) + ', ' + str(self.col) + ', ' + str(self.g) + ')\n'


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


def directionsOf(cells: list[Cell]) -> list:
    directionList: list = []
    for i in range(len(cells) - 1):
        directionList.append(cells[i].directionTo(cells[i + 1]))
    return directionList


def depthFirstSearch(problem) -> list:
    """*** Question 9 - Part 1 ***"""

    start = Cell(0, 4, 0, [])
    frontier: list[Cell] = [start]

    while len(frontier) > 0:
        targetNode: Cell = frontier.pop(0)

        neighbors: list[Cell] = targetNode.neighbors()
        newNeighbors: list[Cell] = list(filter(lambda neighbor: not(neighbor.isIn(targetNode.parents)) and not(neighbor.isIn(frontier)), neighbors))
        frontier = newNeighbors + frontier
        if targetNode.isGoal():
            return directionsOf(targetNode.parents + [targetNode])
    return []


def aStarSearch(problem) -> list:
    """*** Question 9 - Part 2 ***"""

    start = Cell(0, 4, 0, [])
    frontier: list[Cell] = [start]
    bestGoal: Cell = Cell(4, 0, 1000, [])
    goalFound: bool = False

    while len(frontier) > 0:
        targetNode: Cell = frontier.pop(0)
        neighbors: list[Cell] = targetNode.neighbors()
        newNeighbors: list[Cell] = list(filter(lambda neighbor: not(neighbor.isIn(targetNode.parents)) and not(neighbor.isIn(frontier)), neighbors))

        for neighbor in newNeighbors:
            for i in range(len(frontier)):
                if neighbor.cost() < frontier[i].cost():
                    frontier.insert(i, neighbor)
                    break
            else:
                frontier.append(neighbor)

        if targetNode.isGoal() and targetNode.cost() < bestGoal.cost():
            bestGoal = targetNode
            goalFound = True

    return directionsOf(bestGoal.parents + [bestGoal]) if goalFound else []


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
