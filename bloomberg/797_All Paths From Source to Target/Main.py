'''
source: https://leetcode.com/discuss/post/7049289/bloomberg-sse-ny-phone-screen-full-loop-rpn92/
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths
from node 0 to node n - 1 and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e.,
there is a directed edge from node i to node graph[i][j]).


Since the graph is a DAG, we can safely use DFS without worrying about cycles. We don’t need a visited set
I’ll perform DFS with backtracking from node 0, record the path when we reach node n-1, and explore all possible paths.
Clarify:
1.DAG stands for Directed Acyclic Graph, which means all edges are directed and there are no cycles in the graph.

path添加cur模板 进入时 append，离开时 pop；到终点时拷贝 path。
dfs(cur,path):
    path.append(cur)
    if dfs走到底/没路走   
        if 走到底：ans.append(path[::])
        path.pop() #return前一定要pop()这一层dfs添加的cur
        return 
    for nextval in graph[cur]:
        dfs()
    path.pop() #return前一定要pop
    return

解释下什么是DAG：
there are no directed cycles. it is impossible to start from a node and follow any directed edges to return to the same node.
DAG只要是有停止条件的，例如找到n-1停止：
In a DAG, along any DFS path, if the path does not reach the target, it must eventually reach a dead-end node/ node with no outgoing edges.


解释/确认题意：
So the it tells us..
Can I assume the graph is guaranteed to be a DAG with no directed cycles?
so the graph always represented as an adjacency list where graph[i] contains all outgoing neighbors of node i
Clarify:询问
If there is no path from node 0 to node n-1, should I return an empty list?
Can graph[i] be empty, indicating a node with no outgoing edges?

General idea:
I want to use dfs plus backtrack, because we want to explore and find all paths meeting the requiement.
Because the graph contains no cycles, DFS will always terminate, so we don’t need a visited set.
During DFS, we maintain a current path. When reaching the target, we add copy of path to the result. 
After exploring each branch from one node, we need to backtrack by removing the last node(so that other paths can be explored).

'''

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        '''
        backtracking
        '''
        ans = []

        n = len(graph)

        def dfs(cur, path): 
            nonlocal n
            path.append(cur)
            # leaf node or last node, end the dfs() process and return 
            if not graph[cur] or cur == n - 1:
                if cur == n - 1:
                    ans.append(path[::])
                path.pop() #
                return 
            for nextVal in graph[cur]:
                dfs(nextVal, path)
            path.pop()

        dfs(0, [])
        return ans

def main():
    sol = Solution()

    # Test case 1
    graph1 = [[1, 2], [3], [3], []]
    expected1 = [[0, 1, 3], [0, 2, 3]]
    result1 = sol.allPathsSourceTarget(graph1)
    print("Test case 1:")
    print("Input:", graph1)
    print("Expected:", expected1)
    print("Got:", result1)
    print("Pass:", sorted(result1) == sorted(expected1))
    print()

    # Test case 2
    graph2 = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    expected2 = [
        [0, 4],
        [0, 3, 4],
        [0, 1, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 4]
    ]
    result2 = sol.allPathsSourceTarget(graph2)
    print("Test case 2:")
    print("Input:", graph2)
    print("Expected:", expected2)
    print("Got:", result2)
    print("Pass:", sorted(result2) == sorted(expected2))
    print()

    # Test case 3 (edge case: single node)
    graph3 = [[]]
    expected3 = [[0]]
    result3 = sol.allPathsSourceTarget(graph3)
    print("Test case 3:")
    print("Input:", graph3)
    print("Expected:", expected3)
    print("Got:", result3)
    print("Pass:", sorted(result3) == sorted(expected3))
    print()


if __name__ == "__main__":
    main()


