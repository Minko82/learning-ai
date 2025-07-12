# 🌟 Minimax Algorithm  

<br>

## 🔍 **Overview**  
- Minimax is an adversarial search  strategy for two-player games like chess, tic-tac-toe, and checkers.  
- **Players take turns**:  
  - **`Max`** → Tries to get the **highest possible score**.  
  - **`Min`** → Tries to **make `Max's` score as low as possible**.   

> 🔎 **Why does `Min` try to lower the score?**  
> - `Min` is your opponent—it wants to **make the game as hard as possible for you**.  
> - If `Min` played randomly, it would be **too easy to win**
> - Minimax assumes Min will **always** pick the move that is worst for Max.  

<br>

**Key Properties**  
- ✅ **Complete** → Always finds a solution if the game has an ending.  
- ✅ **Optimal** → Always finds the best move if the opponent plays perfectly.  
- ❌ **Slow for big games** → Looks at every possible move, making it **very slow**.  
- ❌ **Needs lots of calculations** → Tries out every move **before deciding**.  

---
<br>

## 🛠 **How Minimax Works (Step by Step)**  
1️⃣ **Look at all possible moves** and build a game tree.  
2️⃣ **`Min` makes its move first** (in its own subtrees).  
3️⃣ **`Max` makes a move last**, choosing the best option from what `Min` left behind.  
4️⃣ **The best choice is picked**, and the game moves forward.  

> 🔎 **Think of `Min` as an annoying player:**  
> - `Min` **only plays to mess with `Max`**.  
> - `Max` has to **think ahead** and choose the move that is **best even in the worst-case scenario**.  

<br>

#### **Example:**  
```css
     (Max)
    /     \
  ?         ?
 / \       / \
3   5     2   5
```

**Step 1:** `Min's` Turn (`Min` Picks from Its Own Branch)
```css
     (Max)
    /     \
  3         2
 / \       / \
3   5     2   5
```

- ``Left Min node`` picks the lowest from (3, 5) → Chooses 3.  
- `Right Min node` picks the lowest from (2, 5) → Chooses 2  

**Step 2:** `Max’s` Turn (Max Picks the Highest Option Left)
```css
     (Max)
    /     \
  3         2
```

- `Max` now picks the highest number left: max(3, 2) → `3`  

**Final Minimax Decision: `3`**  
