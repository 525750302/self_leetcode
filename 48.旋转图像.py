#
# @lc app=leetcode.cn id=48 lang=python
#
# [48] 旋转图像
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        def swap (begin,target):
            a = matrix[begin[0]][begin[1]]
            matrix[begin[0]][begin[1]] = matrix[target[0]][target[1]]
            matrix[target[1]][target[0]] = a
        
        for i in range(n):
            for j in range(i,m):
                swap([i,j],[j,i])
            
        for i in range(n):
            for j in range(m/2,m):
                swap([i,j],[i,m-1-j])

        return matrix
# @lc code=end

