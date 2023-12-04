#
# @lc app=leetcode.cn id=1038 lang=python
#
# [1038] 从二叉搜索树到更大和树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.re_dfs(root, 0)
        return root
    
    def re_dfs(self, root, sum):
        if root.right != None :
            sum = self.re_dfs(root.right, sum)
        sum += root.val
        root.val = sum
        if root.left != None :
            sum = self.re_dfs(root.left, sum)
        return sum
            
        
# @lc code=end

