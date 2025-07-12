#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from collections import deque
import heapq
import unittest
from scipy import stats
import copy
np.random.seed(3)

def listmaker(length, value):
    return [value] * length

# You can execute the cell below to run a simple test case for your `listmaker` function

if (listmaker(10,1)==[1,1,1,1,1,1,1,1,1,1]) & (listmaker(1,10)==[10]):
        print('Passed test case') 
else:
    print('Failed test case')

# These test cases could have also been executed using a couple `assert` statements as follows
# below and see what happens when you intentionally fail a test case.

assert listmaker(10,1)==[1,1,1,1,1,1,1,1,1,1], 'Failed test case'
assert listmaker(1,10)==[10], 'Failed test case'

# Those test cases could have also been implemented using Python's `unittest` package. Below is a simple example. 
# set up the tests to run, as a sub-class of the unittest 'TestCase' class
import unittest

class Tests_Problem1(unittest.TestCase):
    def test_listmaker(self):
        self.assertEqual(listmaker(10,1), [1,1,1,1,1,1,1,1,1,1])
        self.assertEqual(listmaker(1,10), [10])

# instantiation of your tests
tests = Tests_Problem1()

# load the tests
tests_to_run = unittest.TestLoader().loadTestsFromModule(tests)

# run the tests
unittest.TextTestRunner().run(tests_to_run)


class Mandalorian:
#     Note to self: init is a constructor
    def __init__(self, name):
        self.name = name # New mandalorians have a character string attribute name, which is assigned the 
        # value passed into the instantiation.
        self.isAlive = True # New mandalorians have a Boolean attribute isAlive
        self.defense = [] # New mandalorians have an attribute defense which will be a list of their defense skills.

#   push a new defense skill to the end of the Mandalorian's list of defenses.
    def learn(self, skill):
        self.defense.append(skill)

#   push a long forgotten but suddenly remembered defense skill to the beginning of the Mandalorian's list of defenses.
#   Used this source to learn about "insert": https://bobbyhadz.com/blog/python-move-item-in-list
    def remember(self, skill):
        self.defense.insert(0, skill)

#   sometimes mandalorians forget things. Remove the last defense mechanism the Mandalorian gained. 
#   If the Mandalorian has no defense mechanisms, return "Mandalorian is defenseless!"
    def forget(self):
        if len(self.defense) <= 0:
            return "Mandalorian is defenseless!"
        else:
            return self.defense.pop()

#   returns an integer representing the number of unique defense skills that the Mandalorian has
#   Set syntax resource: https://www.geeksforgeeks.org/python-get-unique-values-list/
    def checkDefense(self):
        return len(set(self.defense))

#   The winner of the fight is the individual who possesses more (unique) defense skills
    def fight(self, bounty_hunters):
        mandelorian_stats = self.checkDefense()
        bounty_hunter_stats = bounty_hunters.checkDefense()

        if mandelorian_stats > bounty_hunter_stats:
            bounty_hunters.isAlive = False
            print(f"{self.name} wins the fight.")
            return self.name
        elif mandelorian_stats < bounty_hunter_stats:
            self.isAlive = False
            print(f"{bounty_hunters.name} wins the fight.")
            return bounty_hunters.name
        else:
            print("The fight results in a tie.")
            return "Tie"


import random

mando = Mandalorian("Mando")
greef = Mandalorian("Greef")

defense_skills = ['sword fighting', 'jet packs', 'strong armor', 'extra helmet', 'grogu help', 
                    'the force', 'sandcrawler', 'spaceship']

# Random numbers in python documentation: https://www.geeksforgeeks.org/random-numbers-in-python/

# Mando
num_skills = random.choice([1, 2, 3])
mando_selected_skills = []

for _ in range(num_skills):
    while True:
        skill = random.choice(defense_skills)
        if skill not in mando_selected_skills:
            mando_selected_skills.append(skill)
            mando.learn(skill)
            break 

# Greef
greef_selected_skills = []

for _ in range(2):
    while True:
        greef_skill = random.choice(defense_skills)
        if greef_skill not in greef_selected_skills:
            greef_selected_skills.append(greef_skill)
            greef.learn(greef_skill)
            break  

if random.random() <= 0.1:
    skill = random.choice(defense_skills)
    mando.remember(skill)

print(f"Mando's defense skills: {mando.defense}")
print(f"Greef's defense skills: {greef.defense}")


if random.random() <= 0.3:
    greef.forget()

if random.random() <= 0.05:
    mando.forget()

print(f"Mando's defense skills: {mando.defense}")
print(f"Greef's defense skills: {greef.defense}")

mando.fight(greef)



class Node:
#     Setting default parameters to None in case it's childless
#     Learned how to implement it using: https://note.nkmk.me/en/python-argument-default/

    def __init__(self, key, l=None, r=None, p=None):
        self.key = key  
        self.left_child = l 
        self.right_child = r  
        self.parent = p  

    def getChildren(self):
        return [self.left_child, self.right_child]

# This is just so I test my code. Doing it like I do leetcode exercises lol
# I did the template offirst testing method that was shown in Question 1

# Test case 1: A node with no children or parent
node1 = Node(1)
node2 = Node(2) 

assert node1.key == 1
assert node1.left_child is None
assert node1.right_child is None
assert node1.parent is None
assert node1.getChildren() == [None, None]

# Test case 3: A node with two children
node3 = Node(3, l=node1, r=node2)

assert node3.key == 3
assert node3.left_child == node1
assert node3.right_child == node2
assert node3.parent is None
assert node3.getChildren() == [node1, node2]

print("All tests passed!")

class Tree:

    def __init__(self, rootkey):
        #create a new tree while setting root
        self.root = Node(rootkey, None, None, None)

    def checkTree(self, key, parentKey, root):
        #Recursive function that searches through tree to find if parentKey exists
        # note that 'root' input is not necessarily the root of the tree ('self')
        # 'root' is just where to start looking for the right parentKey to add this new node
        if root == None:
            #if there is no root in tree
            return False
        if root.key == parentKey:
            if root.left_child == None or root.right_child == None:
                # the node 'root' is the parent you should add the new child node to
                return root 
            else:
                print("Parent has two children, node not added.")
                return False
        else:
            for child in root.getChildren():
                # check 'root' node's children if they are the parent you're looking for
                add_temp = self.checkTree(key, parentKey, child)
                if add_temp:
                    return add_temp

    def add(self, key, parentKey):
        parent_node = self.checkTree(key , parentKey, self.root)

        # if parentKey is not found in the tree, then print the message: "Parent not found."
        if parent_node is None:
            print("Parent not found.")
            return False
        else:
            new_node = Node(key, None, None, parent_node)

            if parent_node.left_child is None:
                parent_node.left_child = new_node  
                return True

            elif parent_node.right_child is None:
                parent_node.right_child = new_node  
                return True

            # don’t add the node if the parent already has two children. 
            # Instead, print the message: "Parent has two children, node not added."
            else:
                print("Parent has two children, node not added.")
                return False

    def findNodeDelete(self, key, root):
        if root == None:
            return False
        if key == root.key:
            if root.left_child == None and root.right_child == None:
                if root.parent.left_child.key == key:
                    root.parent.left_child = None
                elif root.parent.right_child.key == key:
                    root.parent.right_child = None
                root = None
                return True
            else:
                print("Node not deleted, has children")
                return False
        else:
            for child in root.getChildren():
                delete_node = self.findNodeDelete(key, child)
                if delete_node:
                    return delete_node

    def delete(self, key):
        if self.root == None:
            self.root = Node(key, None, None, None)
        if key == self.root.key:
            if self.root.left_child == None and self.root.right_child == None:
                self.root = None
                return True
            else:
                print("Node not deleted, has children")
                return False
        else:
            for child in self.root.getChildren():
                delete_node = self.findNodeDelete(key, child)
                if delete_node:
                    return delete_node

        print("Parent not found." )
        return False

    def printTree(self):
        if self.root != None:
            print(self.root.key)
            for child in self.root.getChildren():
                self.printBranch(child)
        else: 
            return

    def printBranch(self, root):
        if root == None:
            return
        else:
            print(root.key)
            for child in root.getChildren():
                self.printBranch(child)

tree = Tree('A')

# Adding nodes to the tree
tree.add('B', 'A') 
tree.add('C', 'A') 

tree.add('D', 'B')  
tree.add('E', 'B')  

tree.add('F', 'C')  
tree.add('G', 'C')  

tree.add('H', 'D')  
tree.add('I', 'D')

tree.add('M', 'H')  
tree.add('N', 'H')  

# Adding an empty node to the left of I, then adding O to the right
# Idk if it matters which side the child is on??
# tree.add('NULL', 'I') 
tree.add('O', 'I') 

tree.add('J', 'F')  
# tree.add('NULL', 'F')

tree.add('K', 'G')  
tree.add('L', 'G')

tree.add('P', 'L')  
tree.add('Q', 'L')

#  I wish I could create a test to visualize the code, but I'm not quite sure how to do that with Python yet. 
# Turtle maybe?
tree.printTree()

# tree.printBranch()

testTree = Tree('A')

# Test case 1:
testTree.add('B', 'A')
testTree.add('C', 'A')
assert testTree.root.left_child.key == 'B'
assert testTree.root.right_child.key == 'C'
print("Passed test!")


class Graph:

    def __init__(self):
        self.vertices = {}

    def addVertex(self, key):
        # check if key value already exists
        if key in self.vertices:
            print("Vertex already exists")
        else:
            self.vertices[key] = []



# Edge: An edge is a line segment between faces (A face is a single flat surface).
    def addEdge(self, key1, key2):
        if (key1 not in self.vertices) or (key2 not in self.vertices):
            print("One or more vertices not found.")
        else: # I believe this'll connect the two vertices 
            self.vertices[key1].append(key2)
            self.vertices[key2].append(key1)

# Vertex: A vertex is a corner.
    def findVertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

g = Graph()

g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)
g.addVertex(8)
g.addVertex(9)

g.addEdge(0, 1)  
g.addEdge(0, 2)  

g.addEdge(1, 9)  
g.addEdge(1, 5)  
g.addEdge(1, 4) 

g.addEdge(2, 4)  
g.addEdge(2, 6)  
g.addEdge(2, 3)

g.addEdge(3, 8) 

g.addEdge(4, 6)  

g.addEdge(5, 6)
g.addEdge(5, 7) 

g.addEdge(6, 7) 
g.addEdge(6, 8)

g.addEdge(7, 9)  
g.addEdge(7, 8)  

# Test 0
g.findVertex(0)  

# Test 1
g.findVertex(1)  

# Test 2
g.findVertex(2)  

# Test 3
g.findVertex(3)  

# Test 4
g.findVertex(4)  

# Test 5
g.findVertex(5)

# Test 6
g.findVertex(6)

# Test 7
g.findVertex(7)

# Test 8
g.findVertex(8) 

# Test 9
g.findVertex(9) 

