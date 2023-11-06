#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.buildTreeRecu(preorder, inorder)
        
    def buildTreeRecu(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        root_in = inorder.index(preorder[0])
        root.left = self.buildTreeRecu(preorder[1:root_in+1], inorder[:root_in])
        root.right = self.buildTreeRecu(preorder[1+root_in:], inorder[root_in+1:])
        return root
                                    

        
# @lc code=end

