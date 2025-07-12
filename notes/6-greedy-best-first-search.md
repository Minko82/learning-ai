# 🌟 Greedy Best-First Search  

<br>

## 🔍 **Overview**  
- A graph traversal algorithm that expands the node that appears **closest to the goal** based on a **heuristic function h(n)**.
  - **Heuristic $h(n)$** → A function that estimates the cost from a given node to the goal
      - Helps guide the search more efficiently by prioritizing nodes that appear closer to the goal
- Often faster than **UCS and A*** but **not guaranteed to find the shortest path**.  

<br>

**Key Properties**  
- ✅ **Complete** → Will find a solution if one exists (with cycle detection).  
- ❌ **Not Optimal** → May not find the shortest path.  
- ✅ **Faster than UCS & A*** → Expands fewer nodes in most cases.  
- ❌ **Can get stuck** → May loop indefinitely if the heuristic is misleading.  

---
<br>

## 🛠 **How Greedy Best-First Search Works**  
1. Start at the **initial node** and add it to a priority queue.  
2. Expand the node with the **lowest heuristic cost**:  
   $f(n) = h(n)$
   - **\( h(n) \)** → Estimated cost from node \( n \) to the goal (heuristic).  
3. Add its neighbors to the queue based only on **\( h(n) \)**.  
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

**GBFS Path:** A → C → G
