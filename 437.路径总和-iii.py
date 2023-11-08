#
# @lc app=leetcode.cn id=437 lang=python
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        self.dfs(root, targetSum)
        return self.res
    
    def dfs(self, root, targetSum):
        if not root:
            return []

        sum_save = [root.val]
        left_sum = self.dfs(root.left, targetSum)
        for i in range(len(left_sum)):
            left_sum[i] = left_sum[i] + root.val
        right_sum = self.dfs(root.right, targetSum)
        for i in range(len(right_sum)):
            right_sum[i] = right_sum[i] + root.val
            
        sum_save = sum_save + left_sum + right_sum
        if targetSum in sum_save:
            self.res += sum_save.count(targetSum)
        return sum_save
# @lc code=end

