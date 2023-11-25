#
# @lc app=leetcode.cn id=1457 lang=python
#
# [1457] 二叉树中的伪回文路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        ans = self.dfs(root, stack)
        return ans 

    def dfs(self, root, stack):
        if root == None:
            return 0
        ans = 0
        if root.val in stack:
            stack.remove(root.val)
        else:
            stack.append(root.val)
        if root.left == None and root.right == None:
            if len(stack) <= 1:
                ans += 1
        
        if root.left != None:
            ans += self.dfs(root.left, stack)
        if root.right != None:
            ans += self.dfs(root.right, stack)
        if root.val in stack:
            stack.remove(root.val)
        else:
            stack.append(root.val)
        return ans



# @lc code=end

