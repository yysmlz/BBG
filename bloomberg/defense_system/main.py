"""
vo2 是 alien defense system，有个 2D grid，
你要放置一个炮塔保护最多的 house，炮塔能保护曼哈顿距离 k 里的 house，面试官说实现太难，
听我讲完思路就下一题了


Let me restate the problem to make sure I understand it correctly.

We are given a 2D grid where 1 represents a house and 0 represents an empty cell.
We want to place exactly one turret on an empty cell.
The turret can protect all houses whose Manhattan distance from the turret is at most k.

Our goal is to find the placement that 
maximizes the number of protected houses, and return either the maximum count or the position



What are the range for grid size and k? 
is there any blocks


pre[r2][c2] gives the entire top-left rectangle.
Then we subtract the top strip and the left strip.
Since the top-left overlap is subtracted twice, we add it back once.
This leaves exactly the target rectangle.



"""