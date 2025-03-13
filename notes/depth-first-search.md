# Depth-First Search (DFS) 🔍

## **Overview**
- **DFS explores as far as possible along a branch before backtracking**
- Uses a **LIFO (Last In, First Out) stack**

<br>

---

## Algorithms

#### **Iterative Version**
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

#### **Recursive Version**
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

## BFS vs. DFS Comparison 

| Feature | BFS | DFS |
|---------|----|----|
| **Data Structure** | Queue (FIFO) | Stack (LIFO) |
| **Best for** | Finding the shortest path in an unweighted graph | Deep traversal of a graph |
| **Time Complexity** | \(O(V + E)\) | \(O(V + E)\) |
| **Space Complexity** | \(O(V)\) | \(O(V)\) (recursive depth) |
| **Completeness** | ✅ Yes (always finds solution if one exists) | ❌ No (may get stuck in infinite loops if cycles exist without detection) |
| **Optimality** | ✅ Yes (if costs are uniform) | ❌ No |

