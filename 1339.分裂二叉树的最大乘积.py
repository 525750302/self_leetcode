#
# @lc app=leetcode.cn id=1339 lang=python
#
# [1339] 分裂二叉树的最大乘积
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sums = {}
        sum = self.dfs(root)
        self.max_val = 0
        self.cal(root, sum)
        return (self.max_val)%(10**9 + 7)

    def dfs(self,root):
        if root is None:
            return 0
        self.sums[root]=self.dfs(root.left)+self.dfs(root.right)+root.val
        return self.sums[root]
    
    def cal(self,root,sum):
        if root is None:
            return 0
        left = self.cal(root.left,sum)
        self.max_val = max(self.max_val,(sum - left) * left)
        right = self.cal(root.right,sum)
        self.max_val = max(self.max_val,(sum - right) * right)
        return left+right+root.val
# @lc code=end

