# 🌟 Uniform Cost Search (UCS)  

<br>

## 🔍 **Overview**  
- Graph traversal algorithm that finds the **least-cost path**. 
    - Unlike BFS, which prioritizes depth, UCS expands the **least costly** node first, making it optimal for weighted graphs.  

<br>

**Key Properties**  
- ✅ **Complete** → Always finds a solution if one exists.  
- ✅ **Optimal** → Always finds the least-cost path.  
- ❌ **Expensive** → Can be slow if costs are high.  
- ❌ **Memory-intensive** → Stores many nodes in the queue.  

<br>

---
<br>

## 🛠 **How UCS Works**  
1. Start at the **initial node** and add it to a priority queue with cost = 0.  
2. Expand the node with the **lowest path cost**.  
3. Add its neighbors to the queue with their **cumulative cost**.  
4. If a goal node is reached, return the path.  
5. Repeat until the goal is found or the queue is empty.

<br>

**Example:**  

```css
    A
   / \
  1   4
 /     \
B --2-- C

```
**Goal:** Run UCS from A to C
<br>
**UCS Path:** A → B → C 
