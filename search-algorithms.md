# 🚀 Chapter 2: Search Algorithms 

## 1️⃣ Introduction to Search Problems
- **Search algorithms** →  Used when an agent needs to find a sequence of actions that **leads to a goal**
  - These algorithms help **navigate problem spaces** efficiently
- **Complete Search Algorithm** → An algorithm that finds the destination if it exists and notifies the caller if the destination doesn't exist

<br>

---

## 2️⃣ Components of a Search Problem
1. **Initial State** → The starting point of the agent.
2. **Actions** → All possible actions the agent can take.
3. **Transition Model** → A description of how each action changes the state.
4. **Goal Test** → Determines if the current state is the goal.
5. **Path Cost** → The numerical cost of a path from the start to a goal.

<br>

---

## 3️⃣ Understanding Time & Space Complexity ⏳💾
### **Time Complexity**
- Measures how the **running time of an algorithm** increases as the input size grows
- Expressed using **Big-O notation** (e.g., \(O(n)\), \(O(n^2)\), etc.)

### **Space Complexity**
- Measures the **amount of memory** an algorithm uses in relation to input size
- Also expressed using **Big-O notation**

📌 **Example:**
- A loop running through **n** elements has **O(n) time complexity**
- A recursive function storing **n** recursive calls has **O(n) space complexity**

<br>

---

## 4️⃣ Types of Search Algorithms
Search algorithms are categorized into two types:

### **Uninformed Search (Blind Search)**
- No additional information about the goal except how to determine if a state is a goal
  
  📌 Example algorithms:
  - **Breadth-First Search (BFS)**
  - **Depth-First Search (DFS)**
  - **Uniform-Cost Search (UCS)**

### **Informed Search (Heuristic Search)**
- Uses heuristics to estimate the cost to the goal, making search more efficient
  
  📌 Example algorithms:
  - **Greedy Best-First Search**
  - A* **Search**
  - **Hill Climbing**
 
<br>

---

## 5️⃣ Breadth-First Search (BFS) 🔍
### **Overview**
- **BFS explores all nodes at the present depth level before moving on to nodes at the next depth level**
- It guarantees the **shortest path** in an **unweighted** graph
- Uses a **FIFO (First In, First Out) queue**

### **Algorithm (Pseudocode)**
```python
BFS(graph, start_node, end_node):
    frontier = new Queue()
    frontier.enqueue(start_node)
    explored = new Set()

    while frontier is not empty:
        current_node = frontier.dequeue()
        if current_node in explored:
            continue
        if current_node == end_node:
            return success

        for neighbor in graph.get_neighbors(current_node):
            frontier.enqueue(neighbor)

        explored.add(current_node)
```

### **Time & Space Complexity**
- **Time Complexity:** \(O(V + E)\) (where \(V\) is vertices, \(E\) is edges)
- **Space Complexity:** \(O(V)\) due to the queue and visited set

<br>

---

## 6️⃣ Depth-First Search (DFS) 🔍
### **Overview**
- **DFS explores as far as possible along a branch before backtracking**
- It can be implemented using **recursion** (implicit stack) or **iteration with an explicit stack**
- Uses a **LIFO (Last In, First Out) stack**

### **Algorithm (Iterative Version)**
```python
def dfs_iterative(graph, start):
    stack = [start]
    visited = set()
    while stack:
        v = stack.pop()
        if v not in visited:
            print(v, end=' ')
            visited.add(v)
            for neighbor in graph[v]:
                if neighbor not in visited:
                    stack.append(neighbor)
```

### **Algorithm (Recursive Version)**
```python
def dfs_recursive(graph, s, visited=set()):
    print(s, end=' ')
    visited.add(s)
    for neighbor in graph[s]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
```

### **Time & Space Complexity**
- **Time Complexity:** \(O(V + E)\)  
- **Space Complexity:**
  - **Recursive:** \(O(V)\) (due to recursion stack)
  - **Iterative:** \(O(V)\) (due to explicit stack)
    
<br>

---

## 7️⃣ BFS vs. DFS Comparison 

| Feature | BFS | DFS |
|---------|----|----|
| **Data Structure** | Queue (FIFO) | Stack (LIFO) |
| **Best for** | Finding the shortest path in an unweighted graph | Deep traversal of a graph |
| **Time Complexity** | \(O(V + E)\) | \(O(V + E)\) |
| **Space Complexity** | \(O(V)\) | \(O(V)\) (recursive depth) |
| **Completeness** | ✅ Yes (always finds solution if one exists) | ❌ No (may get stuck in infinite loops if cycles exist without detection) |
| **Optimality** | ✅ Yes (if costs are uniform) | ❌ No |

