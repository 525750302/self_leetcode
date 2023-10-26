#
# @lc app=leetcode.cn id=113 lang=python
#
# [113] 路径总和 II
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
        :rtype: List[List[int]]
        """
        self.result = []
        path = []

        if root == None:
            return []
        def dfs(root,res):
            path.append(root.val)
            res -= root.val
            if res == 0 and root.left == None and root.right == None:
                self.result.append(path[:])
            
            if root.left != None:
                dfs(root.left,res)
            if root.right != None:
                dfs(root.right,res)
            path.pop(-1)
            res += root.val
        
        dfs(root,targetSum)

        return self.result
        
        
# @lc code=end

