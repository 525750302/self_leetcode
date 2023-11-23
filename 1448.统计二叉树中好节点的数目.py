#
# @lc app=leetcode.cn id=1448 lang=python
#
# [1448] 统计二叉树中好节点的数目
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root,root.val)

    def dfs(self,root,max_val):
        if not root:
            return 0
        if root.val >= max_val:
            max_val = root.val
            return 1 + self.dfs(root.left,max_val) + self.dfs(root.right,max_val)
        else:
            return self.dfs(root.left,max_val) + self.dfs(root.right,max_val)

        
# @lc code=end

