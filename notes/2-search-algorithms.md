# 🚀 Search Algorithms 

## Introduction to Search Problems
- **Search algorithms** →  Used when an agent needs to find a sequence of actions that **leads to a goal**
  - These algorithms help **navigate problem spaces** efficiently
    
<br>

- **Complete Search Algorithm** → An algorithm that finds the destination if it exists and notifies the caller if the destination doesn't exist

<br>

---

## Components of a Search Problem
1. **Initial State** → The starting point of the agent.
2. **Actions** → All possible actions the agent can take.
3. **Transition Model** → A description of how each action changes the state.
4. **Goal Test** → Determines if the current state is the goal.
5. **Path Cost** → The numerical cost of a path from the start to a goal.

<br>

---

## Time & Space Complexity ⏳💾
**Time Complexity**  → Measures how the **running time of an algorithm** increases as the input size grows
- A loop running through **n** elements has **O(n) time complexity**
  
<br>

**Space Complexity** → Measures the **amount of memory** an algorithm uses in relation to input size
- A recursive function storing **n** recursive calls has **O(n) space complexity**


<br>

---

## Types of Search Algorithms
Search algorithms are categorized into two types:

### **Uninformed Search (Blind Search)**
- No additional information about the goal except how to determine if a state is a goal
    - Example algorithms:
        - **[Breadth-First Search (BFS)](https://github.com/Minko82/learning-ai/blob/main/notes/3-breadth-first-search.md)**
        - **[Depth-First Search (DFS)](https://github.com/Minko82/learning-ai/blob/main/notes/4-depth-first-search.md)**
        - **[Uniform-Cost Search (UCS)](https://github.com/Minko82/learning-ai/blob/main/notes/5-uniform-cost-search.md)**

### **Informed Search (Heuristic Search)**
- Uses heuristics to estimate the cost to the goal, making search more efficient
    - Example algorithms:
      - **Greedy Best-First Search**
      - A* **Search**

<br>

### ⚡ **Comparisons**  

| Algorithm | Uses Costs? | Guarantees Optimality? | Time Complexity |
|-----------|------------|------------------------|-----------------|
| **BFS**  | ❌ No  | ✅ Yes (for unweighted graphs) | O(b^d) |
| **DFS**  | ❌ No  | ❌ No  | O(b^d) |
| **UCS**  | ✅ Yes | ✅ Yes | O((b^d)) |
| **A\***  | ✅ Yes | ✅ Yes (with an admissible heuristic) | O((b^d)) |

> 🔎 Note:
> - **\( b \) = Branching Factor** → The average number of child nodes each node has.  
> - **\( d \) = Depth** → The shortest distance from the root (starting node) to the goal node.  

