#!/usr/bin/env python
# 

import search
import utils4e
import numpy as np

# For inhertience
from search import Problem, Node 
from search import Problem

class GraphSearchProblem(Problem):
    """
    Note to self:

    initial : starting node value/state
    goal    : destination node value
    graph   : dictionary of vertexes and theirs neighbors
    """
    def __init__(self, initial, goal, graph):
        super().__init__(initial, goal)
        self.graph = graph

    def actions(self, A):
        return list(self.graph.get(A))

    def result(self, state, action):
        return action

graph = {
    1: [2, 3],
    2: [4],
    3: [1, 4, 5],
    4: [2, 3, 8, 9],
    5: [3, 6, 7],
    6: [5],
    7: [5],
    8: [4],
    9: [4]
}


# CUstom functions so the output looks prettyyyyy

def print_header():
    print("{:<10} {:<25} {:<40} {}".format("Step", "Frontier", "Reached", "Actions"))
    print("{:<10} {:<25} {:<40} {}".format("----", "--------", "-------", "-------"))

def print_status(step, frontier, explored, actions=None):
    step_str = f"{step}"
    frontier_str = f"{[n.state for n in frontier]}"
    explored_str = f"{[v for v in explored]}"
    actions_str = f""

    if actions:
        actions_str += f"{actions}"

    print("{:<10} {:<25} {:<40} {}".format(
        step_str,
        frontier_str,
        explored_str,
        actions_str
    ))

# In[4]:

from collections import deque
from search import Node

bfs_search_tree = {}

def breadth_first_graph_search(problem):
    print_header()

    node = Node(problem.initial)
    frontier = deque([node])
    explored = dict()

    # Initial display
    print_status(0, frontier, explored)

    if problem.goal_test(node.state):
        return node

    step = 1

    while frontier:
        node = frontier.popleft()
        bfs_search_tree[node] = []
        add_children = []
        explored[node.state] = None

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                explored[child.state] = None
                bfs_search_tree[node].append(child)

                if problem.goal_test(child.state):
                    print_status(step, frontier, explored, f"pop {node.state} -> add {[add_child.state for add_child in add_children]}, found {child.state}")
                    return child

                add_children.append(child)
                frontier.append(child)

        print_status(step, frontier, explored, f"pop {node.state} -> add {[add_child.state for add_child in add_children]}")
        step += 1
    return None

dfs_search_tree = {}

def depth_first_graph_search(problem):
    print_header()

    frontier = [(Node(problem.initial))]  # Stack
    explored = dict()

    # Initial display
    print_status(0, frontier, explored)

    step = 1
    while frontier:
        node = frontier.pop()

        explored[node.state] = None
        dfs_search_tree[node] = []

        if problem.goal_test(node.state):
            print_status(step, frontier, explored, f"pop {node.state} -> found {node.state}")
            return node

        add_children = []

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
                add_children.append(child)
                dfs_search_tree[node].append(child)

        print_status(step, frontier, explored, f"pop {node.state} -> add {[add_child.state for add_child in add_children]}")
        step += 1
    return None 

# Tested this with the goal of 8, and it works!!

problem = GraphSearchProblem(1, 7, graph)

print("Breadth First Search (BFS):")
bfs_solution = breadth_first_graph_search(problem)

print()

print("Depth First Search (DFS):")
dfs_solution = depth_first_graph_search(problem)
# In[5]:

print()
print("Breath First Graph Search:")
print("BFS search tree: ")
for parent, children in bfs_search_tree.items():
    print(f"{parent.state} -> {[child.state for child in children]}")

print()

print(f"Path from source to destination (BFS): {[node.state for node in bfs_solution.path()]}")

print()

print("Depth First Graph Search:")
print("DFS search tree: ")
for parent, children in dfs_search_tree.items():
    print(f"{parent.state} -> {[child.state for child in children]}")

print()

print(f"Path from source to destination (DFS): {[node.state for node in dfs_solution.path()]}")
