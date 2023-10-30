#
# @lc app=leetcode.cn id=236 lang=python
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.father = [root]
        self.search(p,root)
        p_father = self.father.copy()
        self.father = [root]
        self.search(q,root)
        q_father = self.father.copy()

        for i in range(min(len(q_father),len(p_father))):
            if q_father[i] != p_father[i]:
                return q_father[i-1] 
        
        if len(q_father) < len(p_father):
            return q_father[-1]
        else:
            return p_father[-1]

    
    def search(self,target,root):
        if root == target:
            return True
        
        flag = False
        if root.left != None:
            self.father.append(root.left)
            flag = self.search(target,root.left)
            if flag == True:
                return True
            self.father.pop(-1)
        flag = False
        if root.right != None:
            self.father.append(root.right)
            flag = self.search(target,root.right)
            if flag == True:
                return True
            self.father.pop(-1)
        
        return False
        

        
        
# @lc code=end

