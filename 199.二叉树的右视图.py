#
# @lc app=leetcode.cn id=199 lang=python
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        self.result = []
        self.check_right_tree(root,0)
    
        return  self.result

    def check_right_tree(self,root,storey):
        if not root:
            return
        if storey >= len(self.result):
            self.result.append(root.val)
        
        if root.right:
            self.check_right_tree(root.right,storey+1)
        
        if root.left:
            self.check_right_tree(root.left,storey+1)
        
# @lc code=end

