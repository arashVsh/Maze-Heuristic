# textDisplay.py
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


import time
try: 
    import pacman
except:
    pass

DRAW_EVERY = 1
SLEEP_TIME = 0 # This can be overwritten by __init__
DISPLAY_MOVES = False
QUIET = False # Supresses output


def checkNullDisplay():
    return True


def draw(state):
    print(state)


def pause():
    time.sleep(SLEEP_TIME)


class NullGraphics:
    def initialize(self, state, isBlue = False):
        pass

    def update(self, state):
        pass

    def updateDistributions(self, dist):
        pass

    def finish(self):
        pass


def pause():
    time.sleep(SLEEP_TIME)


def draw(state):
    print(state)


class PacmanGraphics:
    def __init__(self, speed=None):
        self.turn = None
        self.agentCounter = None
        if speed is not None:
            global SLEEP_TIME
            SLEEP_TIME = speed

    def initialize(self, state, isBlue = False):
        draw(state)
        pause()
        self.turn = 0
        self.agentCounter = 0

    def update(self, state):
        numAgents = len(state.agentStates)
        self.agentCounter = (self.agentCounter + 1) % numAgents
        if self.agentCounter == 0:
            self.turn += 1
            if DISPLAY_MOVES:
                ghosts = [pacman.nearestPoint(state.getGhostPosition(i)) for i in range(1, numAgents)]
                print("%4d) P: %-8s" % (self.turn, str(pacman.nearestPoint(state.getPacmanPosition()))),
                      '| Score: %-5d' % state.score, '| Ghosts:', ghosts)
            if self.turn % DRAW_EVERY == 0:
                draw(state)
                pause()
        if state._win or state._lose:
            draw(state)

    def finish(self):
        pass
