#
# @lc app=leetcode.cn id=116 lang=python
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        result = []
        stack = [root]
        result = self.bfs(result,stack)
        return root

    def bfs(self,result, stack):
        new_stack = []
        while stack:
            node = stack.pop(0)
            if node == None:
                continue 
            result.append(node.val)
            #print(result)
            if node.left:
                new_stack.append(node.left)
            if node.right:
                new_stack.append(node.right)
            if stack:
                node.next = stack[0]
            else:
                node.next = None
                stack = new_stack[:]
                result.append("#")
                new_stack = []
        return result


        
# @lc code=end

