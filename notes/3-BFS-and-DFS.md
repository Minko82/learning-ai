# 🚀 BFS and DFS

## 1️⃣ Breadth-First Search (BFS) 🔍
### **Overview**
- **BFS explores all nodes at the present row/depth level before moving on to nodes at the next row**
- It guarantees the **shortest path** in an **unweighted** graph
- Uses a **FIFO (First In, First Out) queue**
  

#### **Algorithm (Pseudocode)**
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

#### **Time & Space Complexity**
- **Time Complexity:** \(O(V + E)\) (where \(V\) is vertices, \(E\) is edges)
- **Space Complexity:** \(O(V)\) due to the queue and visited set



#### **Why is BFS an optimal algorithm?**
It visits all possible nodes that are one hop from the source, then checks all that are 2 hop, etc. until it reaches the destination

<br>

---

## 2️⃣ Depth-First Search (DFS) 🔍
### **Overview**
- **DFS explores as far as possible along a branch before backtracking**
- Uses a **LIFO (Last In, First Out) stack**

#### **Algorithm (Iterative Version)**
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

#### **Algorithm (Recursive Version)**
```python
def dfs_recursive(graph, s, visited=set()):
    print(s, end=' ')
    visited.add(s)
    for neighbor in graph[s]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
```

#### **Time & Space Complexity**
- **Time Complexity:** \(O(V + E)\)  
- **Space Complexity:**
  - **Recursive:** \(O(V)\) (due to recursion stack)
  - **Iterative:** \(O(V)\) (due to explicit stack)
    
<br>

---

## 3️⃣ BFS vs. DFS Comparison 

| Feature | BFS | DFS |
|---------|----|----|
| **Data Structure** | Queue (FIFO) | Stack (LIFO) |
| **Best for** | Finding the shortest path in an unweighted graph | Deep traversal of a graph |
| **Time Complexity** | \(O(V + E)\) | \(O(V + E)\) |
| **Space Complexity** | \(O(V)\) | \(O(V)\) (recursive depth) |
| **Completeness** | ✅ Yes (always finds solution if one exists) | ❌ No (may get stuck in infinite loops if cycles exist without detection) |
| **Optimality** | ✅ Yes (if costs are uniform) | ❌ No |

