#
# @lc app=leetcode.cn id=73 lang=python
#
# [73] 矩阵置零
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = []
        col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        for i in range(len(row)):
            for j in range(len(matrix[0])):
                matrix[row[i]][j] = 0
        for i in range(len(col)):
            for j in range(len(matrix)):
                matrix[j][col[i]] = 0
# @lc code=end

