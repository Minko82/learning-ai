"""
🚀 Value Iteration & Policy Iteration on Markov Decision Processes (MDPs)

This Python script performs MDP solving using algorithms like:
- Value Iteration
- Policy Iteration
- Q-value computation

It uses utilities from the AIMA `mdp4e` and `utils4e` modules.
"""

from mdp4e import *
from utils4e import print_table
import inspect



# In p1.png, solve for the optimal policy such that max reward is gained.
# The grid is a 2x2 map, where:
# - Diamond and fire are the terminal states with rewards(+1) and (-1) respectively
# - The non-terminal states have arrows in them defining the initial policy for the agent
# - All non-terminal states have a living reward of -0.05
# - Transitional probabilities in the policy direction would be 0.7, the directions perpendicular to policy direction would be 0.15 (As shown in figure)



# In p2.png, solve for the optimal policy such that max reward is gained.
# The grid is a 5X4 map, where:
# - Diamond and fire are the terminal states with rewards(+2) and (-2) respectively. 
# - All non-terminal states have a living reward of -0.035
# - The filled square at (2, 1) denotes a barrier, where it acts like a wall for all its neighboring states (Use `None` in the GridMDP definition)
# - Transitional probabilities in the policy direction would be 0.8, the directions perpendicular to policy direction would be 0.1 each (Already hard-coded into GridMDP)

# The possible actions for the agent at any state would be: UP(^), DOWN(v), LEFT(<) and RIGHT(>)


# - -0.4 
# - -4 
# - -0.07 
#

inspect.getsourcelines(GridMDP)


# As you can see in the above code snippet defining GridMDP, the transition probabilities are hard-coded into a variable named `T`, with probability 0.8 in the policy direction and probaility 0.1 each in directions perpendicular to the policy direction.



inspect.getsourcelines(policy_iteration)

inspect.getsourcelines(policy_evaluation)


grid = GridMDP([[+1, -1],
                [-0.05, -0.05]],
              terminals=[(0, 1), (1, 1)])

# The first parameter to GridMDP, is a 2-D matrix resembling the given diagram of MDP, 
# it is basically a list of list of rewards of each state in the given MDP.
# Notice the way terminals are denoted, in (column, row) format




grid = GridMDP([[-0.035, -0.035, -0.035, -0.035, +2], [-0.035, -0.035, -0.035, -0.035, -0.035], [-0.035, -2, None, -2, -0.035], [-0.035, -0.035, -0.035, -0.035, -0.035]], terminals=[(1,1), (3,1), (4,3)])
pi = policy_iteration(grid)


print_table(grid.to_arrows(pi))




#  -0.4

# This policy shows more arrows pointing toward the diamond, as the higher living reward encourages the agent to prioritize reaching the 
# goal quickly to maximize the reward. Only a few arrows differ, but the overall policy is similar. Its less worried about the fire

grid = GridMDP([[-0.4, -0.4, -0.4, -0.4, +2], [-0.4, -0.4, -0.4, -0.4, -0.4], [-0.4, -2, None, -2, -0.4], [-0.4, -0.4, -0.4, -0.4, -0.4]], terminals=[(1,1), (3,1), (4,3)])
pi = policy_iteration(grid)
print_table(grid.to_arrows(pi))




# 4
# This policy greatly differs from the one with a living reward of -0.35. In this case, the agent only heads toward the diamond when it's nearby. 
# Interestingly, here, more arrows point into the fire because entering the fire becomes more appealing than continuing to live

grid = GridMDP([[-4, -4, -4, -4, +2], [-4, -4, -4, -4, -4], [-4, -2, None, -2, -4], [-4, -4, -4, -4, -4]], terminals=[(1,1), (3,1), (4,3)])
pi = policy_iteration(grid)
print_table(grid.to_arrows(pi))




#  0.07

# Compared to the policy with a living reward of -0.35, this one is quite similar, but with a notable change: 
# the agent is no longer steered toward the wall. Instead, the strategy now encourages movement past the fire, accepting the risk of falling in as a trade-off.

grid = GridMDP([[-0.07, -0.07, -0.07, -0.07, +2], [-0.07, -0.07, -0.07, -0.07, -0.07], [-0.07, -2, None, -2, -0.07], [-0.07, -0.07, -0.07, -0.07, -0.07]], terminals=[(1,1), (3,1), (4,3)])
pi = policy_iteration(grid)
print_table(grid.to_arrows(pi))
