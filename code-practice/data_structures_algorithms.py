# Exploring Data Structures and Algorithms in Python

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import heapq
import unittest
from scipy import stats
import copy
import random
np.random.seed(3)

# List Maker Function

def listmaker(length, value):
    return [value] * length

# Test cases
if (listmaker(10,1) == [1,1,1,1,1,1,1,1,1,1]) & (listmaker(1,10) == [10]):
    print('Passed test case')
else:
    print('Failed test case')

assert listmaker(10,1) == [1,1,1,1,1,1,1,1,1,1], 'Failed test case'
assert listmaker(1,10) == [10], 'Failed test case'

# Visualizing Graphs

def visualize_graph(graph):
    G = nx.Graph()
    for key, edges in graph.vertices.items():
        for edge in edges:
            G.add_edge(key, edge)
    
    plt.figure(figsize=(8,6))
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
    plt.title("Graph Visualization")
    plt.show()

# Exploring Graphs

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

# Initializing and Testing the Graph

g = Graph()
for i in range(10):
    g.addVertex(i)

edges = [(0,1), (0,2), (1,9), (1,5), (1,4), (2,4), (2,6), (2,3), (3,8), (4,6), (5,6), (5,7), (6,7), (6,8), (7,9), (7,8)]
for e in edges:
    g.addEdge(*e)

print("Graph exploration complete!")
visualize_graph(g)
