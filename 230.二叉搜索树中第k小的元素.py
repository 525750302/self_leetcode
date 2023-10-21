#
# @lc app=leetcode.cn id=230 lang=python
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = 0
        self.result = 0
        self.target = k


        self.find(root,count)
        return self.result
    def find(self,r,count):
        if r.left !=None:
            count = self.find(r.left,count)
        count = count + 1
        if count == self.target :
            self.result = r.val
            return count
        if count > self.target :
            return count
        if r.right !=None:
            count = self.find(r.right,count)

        return count
# @lc code=end

