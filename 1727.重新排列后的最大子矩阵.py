#
# @lc app=leetcode.cn id=1727 lang=python
#
# [1727] 重新排列后的最大子矩阵
#

# @lc code=start
class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        pre_map = [[0] * (len(matrix[0]) + 1) for _ in range(1 + len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    pre_map[i + 1][j] = matrix[i][j] + pre_map[i][j]
                else:
                    pre_map[i + 1][j] = 0

        max_val = 0
        for i in range(len(pre_map)):
            height = pre_map[i][0:]
            height.sort()

            for j in range(len(height) - 1, -1 ,-1):
                max_val = max(max_val, height[j] * (len(height) - j))
        return max_val

                
        
 # @lc code=end

