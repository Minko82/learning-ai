#!/usr/bin/env python
# coding: utf-8

# 

# In[15]:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from collections import deque
import heapq


# SCENARIO: A robotics group needs some help designing a path planning algorithm that can navigate around the engineering center. To get started they have designed two test environments for you to implement breadth-first, depth-first, and uniform-cost search.
# 
# - In the first environment, every movement to an adjacent cell has a cost of 1. The first environment will be represented by the `edge_weights_1` dictionary. 
# 
# - In the second enviornment, traveling to adjacent cells has a random int cost between 1 and 100. The second environment will be represented by the `edge_weights_2` dictionary. 
# 
# - Both setups have the same obstacles, free space, and goal. The code below creates and gives a visual representation of the robot's environment. 
# 
# - The first figure shows the environment itself with free spaces, barriers, robot start, and goal point. 
# 
# - The second image shows an example of what a path might look like as the robot moves through the environment.
# 
# ### Color representation
# yellow = obstacle
# 
# teal = free space
# 
# pink = goal
# 
# grey = robot start
# 
# red = part of the path

# In[16]:

# Given code
def show_path(env, path):
    env_copy = np.copy(env)
    for cell in path:
        if(env_copy[cell[0]][cell[1]] >= 5 and env_copy[cell[0]][cell[1]] < 20):
            env_copy[cell[0]][cell[1]] = 41
    show_env(env_copy)

def show_env(env):
    cmap = colors.ListedColormap(['yellow', 'teal', 'pink', 'grey', 'red'])
    bounds = [0,5,20,30,40,41]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(env, cmap=cmap, norm=norm)
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    ax.set_xticks(np.arange(-.5, 10, 1));
    ax.set_yticks(np.arange(-.5, 10, 1));
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])

    plt.show()

np.random.seed(303)
env = np.random.rand(10, 10) * 20
#set robot start position, grey color spot
start = (0, 0)
env[start[0]][start[1]] = 31

#set goal position pink square
goal = (8, 9)

env[goal[0]][goal[1]] = 21

# show the original graph
show_env(env)

# show an example path in the original graph, not a valid path

example_path = [(1,1), (1,2), (1,3), (1,4), (2,4), (3,4), (4,4), (5,4), (6,4), (7,4), (8,4), (8,5),(8,6),(8,7),(8,8)]
show_path(env, example_path)

# ### Graph Representation
# We represent the graph above as an adjacency dict in the following code. You can see what edges any cell has by indexing into the two dicts: 
# - `edge_weights_1`
# - `edge_weights_2`
# 
# For indexing, the top left of the graph is (row=0, col=0). Row values increase downward and column values increase to the right. 
# 
# So for example, if you wanted to look at the pink cell's (the goal location) connections you can call `print(edge_weights_2[(8,9)])` 

# In[17]:

# create dictionary
edge_weights_1 = {}
edge_weights_2 = {}

for row, row_vals in enumerate(env):
    for col, val in enumerate(env[row]):
        # create dictionary
        edge_weights_1[(row, col)] = {}
        edge_weights_2[(row, col)] = {}

        #set all 6 direction options in edge_wights
        # 1) up
        if(row > 0):
            edge_weights_1[(row, col)][(row-1, col)] = 1
            edge_weights_2[(row, col)][(row-1, col)] = np.random.randint(101)
            if(col > 0):
                edge_weights_1[(row, col)][(row-1, col-1)] = 1
                edge_weights_2[(row, col)][(row-1, col-1)] = np.random.randint(101)
            if(col < 9):
                edge_weights_1[(row, col)][(row-1, col+1)] = 1
                edge_weights_2[(row, col)][(row-1, col+1)] = np.random.randint(101)

        #2) left
        if(col > 0):
            edge_weights_1[(row, col)][(row, col-1)] = 1
            edge_weights_2[(row, col)][(row, col-1)] = np.random.randint(101)
            if(row < 9):
                edge_weights_1[(row, col)][(row+1, col-1)] = 1
                edge_weights_2[(row, col)][(row+1, col-1)] = np.random.randint(101)

        #3) down 
        if(row < 9):
                edge_weights_1[(row, col)][(row+1, col)] = 1
                edge_weights_2[(row, col)][(row+1, col)] = np.random.randint(101)
                if(col < 9): 
                    edge_weights_1[(row, col)][(row+1, col+1)] = 1
                    edge_weights_2[(row, col)][(row+1, col+1)] = np.random.randint(101)

        #) right
        if(col < 9):
                edge_weights_1[(row, col)][(row, col+1)] = 1
                edge_weights_2[(row, col)][(row, col+1)] = np.random.randint(101)

for first_node in list(edge_weights_2.keys()):
    for second_node in list(edge_weights_2[first_node].keys()):

        # if first_node is yellow (an obstacle) the connection going both ways should be removed
        if(env[first_node[0]][[first_node[1]]] < 5):
            edge_weights_2[first_node].pop(second_node)
            edge_weights_2[second_node].pop(first_node)
            edge_weights_1[first_node].pop(second_node)
            edge_weights_1[second_node].pop(first_node)
        # if there is a connection, make sure both edges are the same
        else:
            w1 = edge_weights_2[first_node][second_node]
            w2 = edge_weights_2[second_node][first_node]
            if(w1 != w2):
                edge_weights_2[first_node][second_node] = edge_weights_2[second_node][first_node]

# These represent the same location
print('goal:   ', edge_weights_2[goal])
print('(8, 9): ', edge_weights_2[(8,9)])

# ### Useful helper routines for searching
# 

# In[18]:

def path(previous, s): 
    '''
    `previous` is a dictionary chaining together the predecessor state that led to each state
    `s` will be None for the initial state
    otherwise, start from the last state `s` and recursively trace `previous` back to the initial state,
    constructing a list of states visited as we go
    '''
    if s is None:
        return []
    else:
        return path(previous, previous[s])+[s]

def pathcost(path, step_costs):
    '''
    add up the step costs along a path, which is assumed to be a list output from the `path` function above
    '''
    cost = 0
    for s in range(len(path)-1):
        cost += step_costs[path[s]][path[s+1]]
    return cost

# In[19]:

def check_map(step_costs):
    ''' function to check if all the path costs are at least symmetric '''
    check_states = []
    for state1 in step_costs.keys():
        for state2 in step_costs[state1].keys():
            uh_oh = step_costs[state2][state1]!=step_costs[state1][state2]
            if uh_oh:
                print('Check the costs between states {} and {}'.format(state1,state2))
                check_states.append([state1,state2])
    if len(check_states)==0:
        print('all okay! (symmetric at least)')
    return check_states



#### Breadth-first search

# In[20]:

def breadth_first(start, goal, state_graph, return_cost):
    # Deque documentation: https://docs.oracle.com/javase/7/docs/api/java/util/Deque.html
    frontier = deque([start]) 
    reached = set()  
    previous = {start: None}  

    while frontier:
        # O(1) removal from front
        current = frontier.popleft()  

        if current == goal:
            solution_path = path(previous, current)
            if return_cost:
                return solution_path, pathcost(solution_path, state_graph)
            return solution_path

        reached.add(current)

        for neighbor in state_graph.get(current, {}):
            if neighbor not in reached and neighbor not in frontier:
                previous[neighbor] = current
                frontier.append(neighbor)

    return None


#### Uniform-cost search
#
# In[21]:

# Used the following heapq documentation for syntax reference: https://docs.python.org/3/library/heapq.html
class Frontier_PQ:
    def __init__(self, start, cost):
        self.states = {start: cost}  
        self.q = [(cost, start)]  
        self.q.sort() 

# add(state, cost): add the (cost, state) tuple to the frontier
    def add(self, state, cost):
        if state not in self.states:
            self.states[state] = cost
            heapq.heappush(self.q, (cost, state))

# pop(): return the lowest-cost (cost, state) tuple, and pop it off the frontier
    def pop(self):
        if self.q:
            cost, state = heapq.heappop(self.q)
            self.states.pop(state, None)  
            return cost, state
        return None  

# replace(state, cost): if you find a lower-cost path to a state that's already on the frontier, it should be replaced using this method.
    def replace(self, state, cost):
        if state in self.states:
            if cost < self.states[state]:  
                self.states[state] = cost
                heapq.heappush(self.q, (cost, state))

# * **start**: initial state
# * **goal**: goal state
# * **state_graph**: graph representing the connectivity and step costs of the state space (e.g., **edge_weights_1** or **edge_weights_2**)
# * **return_cost**: logical input representing whether or not to return the solution path cost
#   * If **True**, then the output should be a tuple where the first value is the list representing the solution path and the second value is the path cost
#   * If **False**, then the only output is the solution path list object

# In[22]:

# Used the following heapq documentation for syntax reference: https://docs.python.org/3/library/heapq.html

def uniform_cost(start, goal, state_graph, return_cost):
    # Referenced from my 1a answer
    frontier = Frontier_PQ(start, 0)  
    reached = {start: 0} 
    previous = {start: None}  

    while frontier.q:
        cost, current = frontier.pop()

        if current == goal:
            solution_path = path(previous, goal)
            if return_cost:
                return solution_path, pathcost(solution_path, state_graph)
            return solution_path

        for neighbor, step_cost in state_graph.get(current, {}).items():
            new_cost = cost + step_cost

            if neighbor not in reached or new_cost < reached[neighbor]:
                reached[neighbor] = new_cost
                previous[neighbor] = current
                frontier.add(neighbor, new_cost)

    return None  



# Edge Weights 1
print("\n")
print("===== EDGE WEIGHTS 1 =====")
print("\n")

bfs_weight_1 = breadth_first(start, goal, edge_weights_1, return_cost=True)
if bfs_weight_1:
    print("--- Breadth-First Search ---")
    print("Path:", bfs_weight_1[0])
    print("Cost:", bfs_weight_1[1])
    show_path(env, bfs_weight_1[0])
else:
    print("Breadth-First Search did not find a path.")

ucs_weight_1 = uniform_cost(start, goal, edge_weights_1, return_cost=True)
if ucs_weight_1:
    print("--- Uniform-Cost Search ---")
    print("Path:", ucs_weight_1[0])
    print("Cost:", ucs_weight_1[1])
    show_path(env, ucs_weight_1[0])
else:
    print("Uniform-Cost Search did not find a path.")

# Edge Weights 2
print("\n")
print("===== EDGE WEIGHTS 2 =====")
print("\n")

bfs_weight_2 = breadth_first(start, goal, edge_weights_2, return_cost=True)
if bfs_weight_2:
    print("--- Breadth-First Search ---")
    print("Path:", bfs_weight_2[0])
    print("Cost:", bfs_weight_2[1])
    show_path(env, bfs_weight_2[0])
else:
    print("Breadth-First Search did not find a path.")

ucs_weight_2 = uniform_cost(start, goal, edge_weights_2, return_cost=True)
if ucs_weight_2:
    print("--- Uniform-Cost Search ---")
    print("Path:", ucs_weight_2[0])
    print("Cost:", ucs_weight_2[1])
    show_path(env, ucs_weight_2[0])
else:
    print("Uniform-Cost Search did not find a path.")


# 

# In[51]:

def a_star(start, goal, state_graph, return_cost):
    frontier = []
    # (total_cost, path_cost, node)
    heapq.heappush(frontier, (0, 0, start)) 
    came_from = {start: None}
    path_costs = {start: 0}
    visited = set()  

    while frontier:
        _, current_path_cost, current_node = heapq.heappop(frontier)

        if current_node == goal:
            solution_path = path(came_from, goal)
            if return_cost:
                return solution_path, path_costs[goal]
            return solution_path

        visited.add(current_node)

        for neighbor, move_cost in state_graph[current_node].items():
            new_path_cost = current_path_cost + move_cost
            # Euclidean heuristic
            estimated_cost = ((goal[0] - neighbor[0]) ** 2 + (goal[1] - neighbor[1]) ** 2) ** 0.5  
            total_cost = new_path_cost + estimated_cost

            if neighbor not in visited and (neighbor not in path_costs or new_path_cost < path_costs[neighbor]):
                path_costs[neighbor] = new_path_cost
                heapq.heappush(frontier, (total_cost, new_path_cost, neighbor))
                came_from[neighbor] = current_node

    return None

# In[52]:

# Solution path for edge_weights_2
start = (0,0)
goal = (8,9)
graph_1 = edge_weights_1
graph_2 = edge_weights_2
a_star_ret_1 = a_star(start, goal, graph_1, True)
a_star_ret_2 = a_star(start, goal, graph_2, True)

print("---------------------------------")
print("A* solution edge_weights_1: ", a_star_ret_1)
print("---------------------------------")
print("A* solution edge_weights_2:", a_star_ret_2)
print("---------------------------------")

show_env(env)
print('A* edge_weights_1')
show_path(env, a_star_ret_1[0])
print('A* edge_weights_2')
show_path(env, a_star_ret_2[0])
