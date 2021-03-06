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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

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
    closed = []
    fringe = util.Stack()
    current_state = problem.getStartState()
    current_node = dict()
    current_node["state"]  = current_state
    current_node["parent"] = None
    current_node["action"] = None
    fringe.push(current_node)
    flag = bool()


    while not fringe.isEmpty():
        current_node = fringe.pop()
        current_state = current_node["state"]
        for nodeClosed in closed:
            if nodeClosed["state"] == current_state:
                flag = True
                break

        if flag:
            flag = False
            continue

        if problem.isGoalState(current_state):
            break

        tempStck = util.Stack()
        for child in  problem.getSuccessors(current_state):
            tempStck.push({"state":child[0],"parent":current_node,"action":child[1]})

        while not tempStck.isEmpty():#bra dorost kardane tartibe azafe shodane child ha
            fringe.push(tempStck.pop())

        closed.insert(0,current_node)

    actions = []
    while True:
        if current_node["action"] == None:
            break
        actions.insert(0,current_node["action"])
        current_node=current_node["parent"]

    return  actions

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    closed = []
    fringe = util.Queue();
    current_state = problem.getStartState()
    current_node = dict()
    current_node["state"] = current_state
    current_node["parent"] = None
    current_node["action"] = None
    fringe.push(current_node)
    flag = bool()

    while not fringe.isEmpty():
        current_node = fringe.pop()
        current_state = current_node["state"]

        for nodeClosed in closed:
            if nodeClosed["state"] == current_state:
                flag = True
                break

        if flag:
            flag = False
            continue

        if problem.isGoalState(current_state):
            break

        for child in  problem.getSuccessors(current_state):
            fringe.push({"state":child[0],"parent":current_node,"action":child[1]})

        closed.insert(0,current_node)

    actions = []
    while True:
        if current_node["action"] == None:
            break
        actions.insert(0, current_node["action"])
        current_node = current_node["parent"]

    return actions



    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    closed = []
    fringe = util.PriorityQueue()
    current_state = problem.getStartState()
    current_node = dict()
    current_node["state"] = current_state
    current_node["parent"] = None
    current_node["action"] = None
    current_node["cost"] = 0
    fringe.push(current_node,current_node["cost"])
    flag = bool()

    while not fringe.isEmpty():
        current_node = fringe.pop()
        current_state = current_node["state"]

        for nodeClosed in closed:
            if nodeClosed["state"] == current_state:
                flag = True
                break

        if flag:
            flag = False
            continue

        if problem.isGoalState(current_state):
            break

        for child in problem.getSuccessors(current_state):
            fringe.push({"state": child[0], "parent": current_node, "action": child[1],"cost":child[2]+current_node["cost"]},child[2]+current_node["cost"])

        closed.insert(0, current_node)

    actions = []
    while True:
        if current_node["action"] == None:
            break
        actions.insert(0, current_node["action"])
        current_node = current_node["parent"]

    return actions



    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    closed = []
    closed = []
    fringe = util.PriorityQueue()
    current_state = problem.getStartState()
    current_node = dict()
    current_node["state"] = current_state
    current_node["parent"] = None
    current_node["action"] = None
    current_node["g"] = 0
    current_node["h"] = heuristic(current_state,problem)
    current_node["f"] = heuristic(current_state,problem)
    fringe.push(current_node, current_node["f"])
    flag = bool()

    while not fringe.isEmpty():
        current_node = fringe.pop()
        current_state = current_node["state"]

        for nodeClosed in closed:
            if nodeClosed["state"] == current_state:
                flag = True
                break

        if flag:
            flag = False
            continue

        if problem.isGoalState(current_state):
            break

        for child in problem.getSuccessors(current_state):
            fringe.push({"state": child[0], "parent": current_node, "action": child[1],
                         "g": child[2] + current_node["g"],"h":heuristic(child[0],problem),
                         "f":child[2] + current_node["g"]+heuristic(child[0],problem)},
                        child[2] + current_node["g"]+heuristic(child[0],problem))

        closed.insert(0, current_node)

    actions = []
    while True:
        if current_node["action"] == None:
            break
        actions.insert(0, current_node["action"])
        current_node = current_node["parent"]

    return actions


    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
