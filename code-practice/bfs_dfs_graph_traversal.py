# Graph Search Exploration in Python

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import heapq
import unittest
import copy
import random
np.random.seed(3)

# Implementing Breadth-First and Depth-First Search on a Graph

class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, key):
        if key not in self.vertices:
            self.vertices[key] = []
        else:
            print("Vertex already exists")

    def addEdge(self, key1, key2):
        if key1 not in self.vertices or key2 not in self.vertices:
            print("One or more vertices not found.")
        else:
            self.vertices[key1].append(key2)
            self.vertices[key2].append(key1)

    def findVertex(self, key):
        return self.vertices.get(key, None)

    def breadth_first_search(self, start, goal):
        print("\nBreadth First Search (BFS) Traversal:")
        queue = deque([start])
        explored = set()
        bfs_path = []

        while queue:
            node = queue.popleft()
            if node not in explored:
                explored.add(node)
                bfs_path.append(node)
                queue.extend(self.vertices[node])
                print(f"Visited: {node}, Queue: {list(queue)}")
                
                if node == goal:
                    print("Goal reached!")
                    return bfs_path
        return bfs_path

    def depth_first_search(self, start, goal):
        print("\nDepth First Search (DFS) Traversal:")
        stack = [start]
        explored = set()
        dfs_path = []

        while stack:
            node = stack.pop()
            if node not in explored:
                explored.add(node)
                dfs_path.append(node)
                stack.extend(reversed(self.vertices[node]))
                print(f"Visited: {node}, Stack: {list(stack)}")
                
                if node == goal:
                    print("Goal reached!")
                    return dfs_path
        return dfs_path

    def visualize_graph(self):
        G = nx.Graph()
        for key, edges in self.vertices.items():
            for edge in edges:
                G.add_edge(key, edge)
        
        plt.figure(figsize=(8,6))
        nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
        plt.title("Graph Visualization")
        plt.show()

# Initializing and Testing the Graph
g = Graph()
for i in range(10):
    g.addVertex(i)

edges = [(0,1), (0,2), (1,9), (1,5), (1,4), (2,4), (2,6), (2,3), (3,8), (4,6), (5,6), (5,7), (6,7), (6,8), (7,9), (7,8)]
for e in edges:
    g.addEdge(*e)

g.visualize_graph()

# Running Searches
bfs_path = g.breadth_first_search(1, 7)
dfs_path = g.depth_first_search(1, 7)

print("\nBFS Path:", bfs_path)
print("DFS Path:", dfs_path)
