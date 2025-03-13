# 🔍 Breadth-First Search (BFS) 

## **Overview**
- **BFS explores all nodes at the present row/depth level before moving on to nodes at the next row**
- It guarantees the **shortest path** in an **unweighted** graph
- Uses a **FIFO (First In, First Out) queue**
  
<br>

---
## **Algorithm**

### **Pseudocode**
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
<br>

### **Time & Space Complexity**
- **Time Complexity:** \(O(V + E)\) (where \(V\) is vertices, \(E\) is edges)
- **Space Complexity:** \(O(V)\) due to the queue and visited set

<br>


---

> ### 📌 **NOTE**
> **Why is BFS an optimal algorithm?**
> <br>
> It visits all possible nodes that are one hop from the source, then checks all that are 2 hop, etc. until it reaches the destination 

---
