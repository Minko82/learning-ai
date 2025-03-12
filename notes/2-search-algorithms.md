# 🚀 Search Algorithms 

## 1️⃣ Introduction to Search Problems
- **Search algorithms** →  Used when an agent needs to find a sequence of actions that **leads to a goal**
  - These algorithms help **navigate problem spaces** efficiently
    
<br>

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

## 3️⃣ Time & Space Complexity ⏳💾
**Time Complexity**  → Measures how the **running time of an algorithm** increases as the input size grows
- A loop running through **n** elements has **O(n) time complexity**
  
<br>

**Space Complexity** → Measures the **amount of memory** an algorithm uses in relation to input size
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

_BFS and DFS are covered in the next page_
