# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result1, result2 = self.cal_path(root)
        if result2 == 0:
            return result1
        return max(result1,result2, root.val)


    def cal_path(self, root):

        if root.left == None and root.right == None:
            result = max(0,root.val)
            return root.val,result        

        result_left_single = -99999
        result_left_connect = 0
        if root.left != None:
            result_left_single,result_left_connect = self.cal_path(root.left)
        
        result_right_single = -99999
        result_right_connect = 0
        if root.right != None:
            result_right_single,result_right_connect = self.cal_path(root.right)

        conenct_singal = result_left_connect + result_right_connect + root.val
        if result_right_connect > 0:
            conenct_singal = max(conenct_singal,result_right_connect)        
        if result_left_connect > 0:
            conenct_singal = max(conenct_singal,result_left_connect)    
        
        return max(result_left_single,result_right_single,conenct_singal), max(result_left_connect, result_right_connect)+ root.val




a = Solution()
input = [0,1,0,2,1,0,1,3,2,1,2,1]
result = a.maxPathSum(input)
print(result)