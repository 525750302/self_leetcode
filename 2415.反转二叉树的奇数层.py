#
# @lc app=leetcode.cn id=2415 lang=python
#
# [2415] 反转二叉树的奇数层
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        stack  =[ root]
        level = 0
        while stack:
            new_stack = []
            for node in stack:
                if node:
                    if node.left:
                        new_stack.append(node.left)
                    if node.right:
                        new_stack.append(node.right)
            if new_stack and level % 2 == 0:
                val = []
                for node in new_stack:
                    val.append(node.val)
                for node in new_stack:
                    node.val = val.pop()
                stack = new_stack
            else:
                stack = new_stack
            level += 1
        return root
# @lc code=end

