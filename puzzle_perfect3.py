
from __future__ import division
from __future__ import print_function

import copy
import sys
import math
import time
import queue as Q


#### SKELETON CODE ####
## The Class that Represents the Puzzle
from collections import deque, Set

from pip._vendor.progress.counter import Stack


class PuzzleState(object):
    """
        The PuzzleState stores a board configuration and implements
        movement instructions to generate valid children.
    """
    def __init__(self, config, n, parent=None, action="Initial", cost=0):
        """
        :param config->List : Represents the n*n board, for e.g. [0,1,2,3,4,5,6,7,8] represents the goal state.
        :param n->int : Size of the board
        :param parent->PuzzleState
        :param action->string
        :param cost->int
        """
        if n*n != len(config) or n < 2:
            raise Exception("The length of config is not correct!")
        if set(config) != set(range(n*n)):
            raise Exception("Config contains invalid/duplicate entries : ", config)

        self.n        = n
        self.cost     = cost
        self.parent   = parent
        self.action   = action
        self.config   = config
        self.children = []

        # Get the index and (row, col) of empty block
        self.blank_index = self.config.index(0)

GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
GoalNode = PuzzleState()  # at finding solution
NodesExpanded = 0  # total nodes visited
MaxSearchDeep = 0  # max deep
initial_state = list()
moves=list()
cost=set()

def display(self):
    """ Display this Puzzle state as a n*n board """
    for i in range(self.n):
        print(self.config[3*i : 3*(i+1)])

def move_up(self):
    """
    Moves the blank tile one row up.
    :return a PuzzleState with the new configuration
    """
    pos = self.config.index(0)
    if pos in (0, 1, 2):
        return None
    else:
        new_val = list(self.config)
        new_val[pos], new_val[pos - 3] = new_val[pos - 3], new_val[pos]
        return new_val

def move_down(self):
    """
    Moves the blank tile one row down.
    :return a PuzzleState with the new configuration
    """
    pos = self.config.index(0)
    if pos in (6, 7, 8):
        return None
    else:
        new_val = list(self.config)
        new_val[pos], new_val[pos + 3] = new_val[pos + 3], new_val[pos]
        return new_val

def move_left(self):
    """
    Moves the blank tile one column to the left.
    :return a PuzzleState with the new configuration
    """
    pos = self.config.index(0)
    if pos in (0, 3, 6):
        return None
    else:
        new_val = list(self.config)
        new_val[pos], new_val[pos - 1] = new_val[pos - 1], new_val[pos]
        return new_val

def move_right(self):
    """
    Moves the blank tile one column to the right.
    :return a PuzzleState with the new configuration
    """
    pos = self.config.index(0)
    if pos in (2, 5, 8):
        return None
    else:
        new_val = list(self.config)
        new_val[pos], new_val[pos + 1] = new_val[pos + 1], new_val[pos]
        return new_val

def expand(self):
    """ Generate the child nodes of this node """
    global nodes_expanded
    nodes_expanded += 1
    neighbors = list()
    neighbors.append(PuzzleState(move_up(self.n),parent=self,cost=self.cost+1,action="move")


# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters
def writeOutput():
    ### Student Code Goes here
    pass

def bfs_search(initial_state):
    """BFS search"""
    ### STUDENT CODE GOES HERE ###
    global MaxFrontierSize, GoalNode, MaxSearchDeep
    boardVisited = set()
    Queue = deque(initial_state.config)
    while Queue:
        node = Queue.popleft()
        boardVisited.add(node.map)
        if node.state == GoalState:
            GoalNode = node
            return Queue
        possiblePaths = expand(node)
        for path in possiblePaths:
            if path.map not in boardVisited:
                Queue.append(path)
                boardVisited.add(path.map)
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = MaxSearchDeep + 1
    print("max_search_depth:", MaxSearchDeep)
    print(boardVisited)

def dfs_search(initial_state):
    """DFS search"""
    Visited=set()
    stack=list( initial_state.config)
    while stack:
        node=stack.pop()
        Visited.add(node.map)
        if node.state==GoalState:
            GoalNode=node
            return stack
        neighbors=reversed(expand(node))
        for neighbor in neighbors:
            if neighbor.map not in Visited:
                stack.append(neighbor)
                Visited.add(neighbor.map)

                if len(neighbor)>MaxSearchDeep:
                    MaxSearchDeep+=1
    print("max_search_depth:", MaxSearchDeep)
    print(Visited)




    Visited=set()
    stack=list( initial_state.config)
    while stack:
        node=stack.pop()
        Visited.add(node.map)
        if node.state==GoalState:
            GoalNode=node
            return stack
        neighbors=reversed(expand(node))
        for neighbor in neighbors:
            if neighbor.map not in Visited:
                stack.append(neighbor)
                Visited.add(neighbor.map)

                if len(neighbor)>MaxSearchDeep:
                    MaxSearchDeep+=1
    print("max_search_depth:", MaxSearchDeep)
    print(Visited)


def A_star_search(initial_state):
    """A * search"""
    ### STUDENT CODE GOES HERE ###
    pass

def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    ### STUDENT CODE GOES HERE ###
    pass

def calculate_manhattan_dist(idx, value, n):
    """calculate the manhattan distance of a tile"""
    ### STUDENT CODE GOES HERE ###
    pass

def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    ### STUDENT CODE GOES HERE ###
    return sum(abs(b%side-g%side)+abs(b//side-g //side)
                for b,g in (())
    pass

def backtrace():

    current_node = GoalNode

    while initial_state != current_node.state:

        if current_node.move == 1:
            movement = 'Up'
        elif current_node.move == 2:
            movement = 'Down'
        elif current_node.move == 3:
            movement = 'Left'
        else:
            movement = 'Right'

        moves.insert(0, movement)
        current_node = current_node.parent

    return moves

# Main Function that reads in Input and Runs corresponding Algorithm
def main():
    search_mode = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = list(map(int, begin_state))
    board_size  = int(math.sqrt(len(begin_state)))
    hard_state  = PuzzleState(begin_state, board_size)
    start_time  = time.time()

    if   search_mode == "bfs": bfs_search(hard_state)
    elif search_mode == "dfs": dfs_search(hard_state)
    elif search_mode == "ast": A_star_search(hard_state)
    else:
        print("Enter valid command arguments !")

    end_time = time.time()
    print("Program completed in %.3f second(s)"%(end_time-start_time))

if __name__ == '__main__':
    main()