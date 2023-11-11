#
# @lc app=leetcode.cn id=133 lang=python
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        visited = {}
        stack = [node]
        
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited[cur] = Node(cur.val)
            for n in cur.neighbors:
                if n in visited:
                    visited[cur].neighbors.append(visited[n])
                    if visited[n].neighbors.count(visited[cur]) == 0:
                        visited[n].neighbors.append(visited[cur])
                else:
                    stack.append(n)
        return visited[node]
        
# @lc code=end

