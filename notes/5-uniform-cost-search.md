# 🌟 Uniform Cost Search (UCS)  

## 🔍 **What is UCS?**  
- Uniform Cost Search (UCS) is a **graph traversal algorithm** that finds the least-cost path from a start node to a goal node. 
- Unlike BFS, which prioritizes depth, UCS expands the **least costly** node first, making it optimal for weighted graphs.  

<br>

---

## 🛠 **How UCS Works**  
1. Start at the **initial node** and add it to a priority queue with cost = 0.  
2. Expand the node with the **lowest path cost**.  
3. Add its neighbors to the queue with their **cumulative cost**.  
4. If a goal node is reached, return the path.  
5. Repeat until the goal is found or the queue is empty.

<br>

---

## ⚖ **Key Properties**  
- ✅ **Complete** → Always finds a solution if one exists.  
- ✅ **Optimal** → Always finds the least-cost path.  
- ❌ **Expensive** → Can be slow if costs are high.  
- ❌ **Memory-intensive** → Stores many nodes in the queue.  

<br>

---

## 🔢 **Algorithm (Pseudocode)**  
```python
def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [])]  # (Cost, Node, Path)
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)  # Pop lowest-cost node
        
        if node in visited:
            continue
        
        visited.add(node)
        path = path + [node]
        
        if node == goal:
            return path, cost  # Return optimal path and cost
        
        for neighbor, step_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + step_cost, neighbor, path))
    
    return None  # No path found
