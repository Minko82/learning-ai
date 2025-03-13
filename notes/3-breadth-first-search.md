# 🔍 Breadth-First Search (BFS) 

## **Overview**
- **BFS explores all nodes at the present row/depth level before moving on to nodes at the next row**
- It guarantees the **shortest path** in an **unweighted** graph
- Uses a **FIFO (First In, First Out) queue**

<br>

---
> #### 📌 **NOTE**
> **Why is BFS an optimal algorithm?**
> <br>
> It visits all possible nodes that are one hop from the source, then checks all that are 2 hop, etc. until it reaches the destination 
---

<br>

---

<br>

## 🛠 **How BFS Works**  
1. Start from the **initial node**, mark it as visited.  
2. Add it to a **queue** (FIFO order).  
3. Expand the **front node** of the queue and add its unvisited neighbors.  
4. Continue until the goal node is found or all nodes are visited.  

<br>

**Example Graph**  

```css
    A
   / \
  B   C
 / \   \
D   E   F
```

BFS Traversal (Starting from A):

A → B → C → D → E → F

<br>

---

<br>

## ⏳ **Time & Space Complexity**  

| Complexity | BFS |
|------------|----|
| **Time Complexity** | \(O(V + E)\) |
| **Space Complexity** | \(O(V)\) (queue & visited set) |

> **📌 Why \(O(V + E)\)?**  
> - BFS **visits each node once** → \(O(V)\)  
> - BFS **traverses each edge once** → \(O(E)\)  
