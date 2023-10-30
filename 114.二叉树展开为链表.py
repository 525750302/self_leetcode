# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        point = root
        if point != None:
            self.dfs(point)
    
    def dfs(self,point):
        left = point.left
        point.left = None
        right = point.right
        if left!= None:
            point.right = left
            point = self.dfs(left)
        
        if right != None:
            point.right = right
            point = self.dfs(right)
        
        return point

        