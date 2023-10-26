#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root,-99999999999,99999999999)

    
    def check(self,root,min_val,max_val):
        if root == None:
            return True
        if root.left != None and (root.left.val >= root.val or root.left.val <= min_val):
            return False
        
        if  root.right != None and (root.right.val <= root.val or root.right.val >= max_val):
             return False


        if root.left !=None:
            if self.check(root.left,min_val,root.val) == False:
                return False
        
        if root.right !=None:
            if self.check(root.right,root.val,max_val) == False:
                return False
            
        return True
# @lc code=end

