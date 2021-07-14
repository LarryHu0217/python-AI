from __future__ import division
from __future__ import print_function

import sys
import math
import time
import queue as Q
import resource
import heapq


#### SKELETON CODE ####
## The Class that Represents the Puzzle
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
        if n * n != len(config) or n < 2:
            raise Exception("The length of config is not correct!")
        if set(config) != set(range(n * n)):
            raise Exception("Config contains invalid/duplicate entries : ", config)

        self.n = n
        self.cost = cost
        self.parent = parent
        self.action = action
        self.config = tuple(config)
        self.children = []

        # Get the index and (row, col) of empty block
        self.blank_index = self.config.index(0)

    def display(self):
        """ Display this Puzzle state as a n*n board """
        for i in range(self.n):
            print(self.config[3 * i: 3 * (i + 1)])

    def move_up(self):
        """
        Moves the blank tile one row up.
        :return a PuzzleState with the new configuration
        """
        pos = self.config.index(0)
        if pos in (0, 1, 2):
            return None
        else:
            new_config = list(self.config)
            new_config[pos], new_config[pos - 3] = new_config[pos - 3], new_config[pos]
            return PuzzleState(new_config, self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self):
        """
        Moves the blank tile one row down.
        :return a PuzzleState with the new configuration
        """
        pos = self.config.index(0)
        if pos in (6, 7, 8):
            return None
        else:
            new_config = list(self.config)
            new_config[pos], new_config[pos + 3] = new_config[pos + 3], new_config[pos]
            return PuzzleState(new_config, self.n, parent=self, action="Down", cost=self.cost + 1)

    def move_left(self):
        """
        Moves the blank tile one column to the left.
        :return a PuzzleState with the new configuration
        """
        pos = self.config.index(0)
        if pos in (0, 3, 6):
            return None
        else:
            new_config = list(self.config)
            new_config[pos], new_config[pos - 1] = new_config[pos - 1], new_config[pos]
            return PuzzleState(new_config, self.n, parent=self, action="Left", cost=self.cost + 1)

    def move_right(self):
        """
        Moves the blank tile one column to the right.
        :return a PuzzleState with the new configuration
        """
        pos = self.config.index(0)
        if pos in (2, 5, 8):
            return None
        else:
            new_config = list(self.config)
            new_config[pos], new_config[pos + 1] = new_config[pos + 1], new_config[pos]
            return PuzzleState(new_config, self.n, parent=self, action="Right", cost=self.cost + 1)

    def expand(self):
        """ Generate the child nodes of this node """

        # Node has already been expanded
        if len(self.children) != 0:
            return self.children

        # Add child nodes in order of UDLR
        children = [
            self.move_up(),
            self.move_down(),
            self.move_left(),
            self.move_right()]

        # Compose self.children of all non-None children states
        self.children = [state for state in children if state is not None]
        return self.children



# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters
def writeOutput( actions,nodes_expanded,search_depth,MaxSearchDeep,max_memory,start_time,end_time):
    ### Student Code Goes here
    file = open('output1.txt', 'w')
    file.write("path_to_goal: " + str(actions))
    file.write("\ncost_of_path: " +str(len(actions)))
    file.write("\nnodes_expanded: " + str(nodes_expanded))
    file.write("\nsearch_depth: " + str(search_depth))
    file.write("\nmax_search_depth: " + str(MaxSearchDeep))
    file.write("\nrunning_time: " + str(end_time - start_time))
    file.write("\nmax_ram_usage: " +  str(max_memory / 1024 / 1024))
    file.close()


def bfs_search(initial_state):
    """BFS search"""
    ### STUDENT CODE GOES HERE ###
    start_time = time.time()
    MaxSearchDeep = 0
    nodes_expanded = 0
    frontier = [initial_state]
    frontierset = set()
    frontierset.add(initial_state.config)
    explored = set()
    max_memory = 0
    while len(frontier):
        state = frontier.pop(0)
        frontierset.remove(state.config)
        explored.add(state.config)
        if test_goal(state):
            break
        neighbors = state.expand()
        nodes_expanded += 1
        for neighbor in neighbors:
            if neighbor.config not in explored:
                if neighbor.config not in frontierset:
                    frontier.append(neighbor)
                    frontierset.add(neighbor.config)
                if neighbor.cost > MaxSearchDeep:
                    MaxSearchDeep = neighbor.cost
                total_mem = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
                if total_mem > max_memory:
                    max_memory = total_mem
    end_time = time.time()
    search_depth = state.cost
    actions = []
    while state != initial_state:
        actions.append(state.action)
        state = state.parent
    actions.reverse()
    writeOutput(actions, nodes_expanded, search_depth, MaxSearchDeep, max_memory, start_time, end_time)


def dfs_search(initial_state):
    """DFS search"""
    ### STUDENT CODE GOES HERE ###
    start_time = time.time()
    MaxSearchDeep = 0
    nodes_expanded = 0
    frontier = [initial_state]
    frontierset= set()
    frontierset.add(initial_state.config)
    explored = set()
    max_memory = 0
    while len(frontier):
        state = frontier.pop()
        frontierset.remove(state.config)
        explored.add(state.config)
        if test_goal(state):
            break
        neighbors = state.expand()
        neighbors.reverse()
        nodes_expanded += 1
        for neighbor in neighbors:
            if neighbor.config not in explored:
                if neighbor.config not in frontierset:
                    frontier.append(neighbor)
                    frontierset.add(neighbor.config)
                if neighbor.cost > MaxSearchDeep:
                    MaxSearchDeep = neighbor.cost
            currentmem = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            if currentmem > max_memory:
                max_memory = currentmem
    end_time = time.time()
    search_depth = state.cost
    actions = []
    while state != initial_state:
        actions.append(state.action)
        state = state.parent
    actions.reverse()
    writeOutput(actions, nodes_expanded, search_depth, MaxSearchDeep, max_memory, start_time, end_time)


def A_star_search(initial_state):
    """A * search"""
    ### STUDENT CODE GOES HERE ###
    start_time = time.time()
    MaxSearchDeep = 0
    frontier = []
    nodes_expanded = 0
    idx = 0
    heapq.heappush(frontier, initial_state)
    idx += 1
    explored = set()
    max_memory = 0
    while len(frontier):
        state = heapq.heappop(frontier)
        explored.add(state.config)
        if test_goal(state):
            break
        nodes_expanded += 1
        neighbors = state.expand()
        for neighbor in neighbors:
            currency_mem = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            if currency_mem > max_memory:
                max_memory = currency_mem
            if (neighbor.config not in explored)and neighbor.config not in [x.config for x in frontier]:
                heapq.heappush(frontier, neighbor)
                idx += 1
                if neighbor.cost > MaxSearchDeep:
                    MaxSearchDeep = neighbor.cost
            elif neighbor.config in [x.config for x in frontier]:
                for x in frontier:
                    if neighbor.config == x.config:
                        frontier.remove(x)
    end_time = time.time()
    search_depth = state.cost
    actions = []
    while state != initial_state:
        actions.append(state.action)
        state = state.parent
    actions.reverse()
    writeOutput(actions, nodes_expanded, search_depth, MaxSearchDeep, max_memory, start_time, end_time)


def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    ### STUDENT CODE GOES HERE ###
    res = 0
    for idx, val in enumerate(state.config):
        res += calculate_manhattan_dist(idx, val, state.n)
    return res


def calculate_manhattan_dist(idx, value, n):
    """calculate the manhattan distance of a tile"""
    ### STUDENT CODE GOES HERE ###
    if value == 0:
        return 0
    idx_x = int(idx / n)
    idx_y = idx % n
    value_x = int(value / n)
    value_y = value % n
    return abs(idx_x - value_x) + abs(idx_y - value_y)


def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    ### STUDENT CODE GOES HERE ###
    for idx, val in enumerate(puzzle_state.config):
        if idx != val:
            return False
    return True


# Main Function that reads in Input and Runs corresponding Algorithm
def main():
    search_mode = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = list(map(int, begin_state))
    board_size = int(math.sqrt(len(begin_state)))
    hard_state = PuzzleState(begin_state, board_size)

    if search_mode == "bfs":
        bfs_search(hard_state)
    elif search_mode == "dfs":
        dfs_search(hard_state)
    elif search_mode == "ast":
        A_star_search(hard_state)
    else:
        print("Enter valid command arguments !")


if __name__ == '__main__':
    main()




