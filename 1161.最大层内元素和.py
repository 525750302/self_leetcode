#
# @lc app=leetcode.cn id=1161 lang=python
#
# [1161] 最大层内元素和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        queue = [root]
        level = 0
        max_level = 0
        max_sum = -float('inf')
        while queue:
            stack = []
            sum = 0
            level += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                sum += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if sum > max_sum:   
                max_sum = sum
                max_level = level
            queue = stack[0:]

        return max_level
        
# @lc code=end

