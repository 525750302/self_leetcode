#
# @lc app=leetcode.cn id=337 lang=python
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.select = {}
        self.nonselect = {}
        self.dfs(root)
        return max(self.select[root],self.nonselect[root])
    
    def dfs(self, root):
        if root == None:
            return 
        if root.left == None:
            a = 0
            c = 0
        else:
            self.dfs(root.left)
            a = self.nonselect[root.left]
            c = self.select[root.left]
        if root.right == None:
            b= 0
            d = 0
        else:
            self.dfs(root.right)
            b = self.nonselect[root.right]
            d = self.select[root.right]
        
        self.select[root] = root.val  + a + b
        self.nonselect[root] = max(a,c) + max(b,d)

        
# @lc code=end

