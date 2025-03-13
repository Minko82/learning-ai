# 🌟 Minimax Algorithm  

<br>

## 🔍 **Overview**  
- **Minimax is an adversarial search algorithm** used in **turn-based two-player games** like chess, tic-tac-toe, and checkers.  
- Assumes both players **play optimally**:  
  - **Maximizing player** → Tries to get the highest possible score.  
  - **Minimizing player** → Tries to force the lowest possible score.  
- **Explores the entire game tree** up to a given depth and assigns values to game states.  

<br>

**Key Properties**  
- ✅ **Complete** → Finds a solution if the game tree is finite.  
- ✅ **Optimal** → Guarantees the best strategy against an optimal opponent.  
- ❌ **Exponential time complexity** → \( O(b^d) \), making it slow for large games.  
- ❌ **Computationally expensive** → Evaluates all possible moves.  

---
<br>

## 🛠 **How Minimax Works**  
1. **Generate the game tree** up to a certain depth.  
2. **Apply an evaluation function** to assign values to terminal nodes.  
3. **Propagate values up the tree**:  
   - **Maximizing player** picks the **highest** value.  
   - **Minimizing player** picks the **lowest** value.  
4. **Repeat until the root node is reached**, selecting the best move.  

<br>

**Example Minimax Tree:**  

```css
         (Max)
        /     \
      3         5
     / \       / \
    3   5     2   5
   (Min)     (Min)
```

Max chooses 5 because Min picks the smallest value from its children.
