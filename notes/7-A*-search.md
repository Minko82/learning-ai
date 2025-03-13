# 🌟 A* Search Algorithm  

<br>

## 🔍 **Overview**  
- A **graph traversal algorithm** that finds the **shortest path** by combining **Uniform Cost Search (UCS)** and **Greedy Best-First Search**.  
- Uses both **actual cost \( g(n) \)** and **estimated cost \( h(n) \)** to prioritize nodes.  
  - **\( g(n) \)** → The cost from the start node to \( n \) (actual cost).  
  - **\( h(n) \)** → The estimated cost from \( n \) to the goal (heuristic).  
- More efficient than **UCS** and more reliable than **GBFS**, as it guarantees an optimal path if the heuristic is admissible.  

<br>

> ### **Formula:**
> $f(n) = g(n) + h(n)$

<br>

**Key Properties**  
- ✅ **Complete** → Will find a solution if one exists.  
- ✅ **Optimal** → Finds the shortest path if the heuristic is **admissible** (never overestimates).  
- ✅ **More efficient than UCS** → Expands fewer nodes in most cases.  
- ❌ **Memory-intensive** → Stores many nodes in the priority queue.  

---
<br>

## 🛠 **How A* Works**  
1. Start at the **initial node** and add it to a priority queue.  
2. Expand the node with the **lowest total estimated cost**:  
$f(n) = g(n) + h(n)$
   - **\( g(n) \)** → Cost from the start to node \( n \) (actual cost).  
   - **\( h(n) \)** → Estimated cost from \( n \) to the goal (heuristic).  
3. Add its neighbors to the queue with their updated **\( f(n) \)** values.  
4. If the goal node is reached, return the path.  
5. Repeat until the goal is found or the queue is empty.  

<br>

**Example:**  

```css
    A
   / \
  1   4
 /     \
B --2-- C
       /
      G
```

**Goal:** Find the shortest path from A to G.

**Heuristic values:**
- h(A) = 6
- h(B) = 3
- h(C) = 2
- h(G) = 0

**A* Path**: A → B → C → G 
