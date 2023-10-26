#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        stack = [root]
        deep = []
        if root == None:
            return []
        new_stack = []
        while (stack):
            a = stack.pop(0)
            if stack!= None:
                deep.append(a.val)
            if a.left != None:
                new_stack.append(a.left)
            
            if a.right != None:
                new_stack.append(a.right)
            if not stack:
                stack = new_stack
                new_stack = []
                result.append(deep)
                deep = []
        return result
# @lc code=end

