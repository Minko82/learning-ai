# 🔍 Depth-First Search (DFS)  

<br>

## 🔎 **Overview**  
- **DFS explores as far as possible along a branch before backtracking**.  
- Uses a **LIFO (Last In, First Out) stack** for traversal.  

 <br>
 
 **Key Properties** 
- ✔ **Efficient for exploring deep graphs**.  
- ✔ **Uses less memory than BFS for dense graphs**.  
- ❌ **Not guaranteed to find the shortest path**.  
- ❌ **Can get stuck in cycles without proper checks**.  

---

<br>

## 🛠 **How DFS Works**  
1. Start from the **initial node**, mark it as visited.  
2. Expand the **last added node** (LIFO order).  
3. If no more neighbors exist, **backtrack** to the previous node.  
4. Repeat until all reachable nodes are visited or the goal is found.  

<br>

**Example Graph**  

```css
    A
   / \
  B   C
 / \   \
D   E   F
```

DFS Traversal (Starting from A):

A → B → D → E → C → F

---

 <br>

## ⚡ **BFS vs. DFS Comparison**  

| Feature | 🏁 **BFS** | 🔍 **DFS** |
|---------|-----------|-----------|
| **Data Structure** | Queue (FIFO) | Stack (LIFO) |
| **Best for** | Finding the shortest path in an unweighted graph | Deep traversal of a graph |
| **Time Complexity** | \(O(V + E)\) | \(O(V + E)\) |
| **Space Complexity** | \(O(V)\) | \(O(V)\) (recursive depth) |
| **Completeness** | ✅ Yes (always finds a solution if one exists) | ❌ No (may get stuck in infinite loops without cycle detection) |
| **Optimality** | ✅ Yes (if costs are uniform) | ❌ No |
