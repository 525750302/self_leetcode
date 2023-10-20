#
# @lc app=leetcode.cn id=54 lang=python
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        sum = len(matrix) * len(matrix[0])
        flag_matrix = [[1]*len(matrix[0]) for i in range(len(matrix))]
        x = 0
        y = 0
        direct = 0
        result = []
        while (len(result)<sum):
            result.append(matrix[y][x])
            flag_matrix[y][x] = 0
            if direct == 0:
                x = x + 1
            elif direct == 1:
                y = y + 1
            elif direct == 2:
                x = x - 1
            elif direct == 3:
                y = y - 1
            if x >=len(matrix[0]) or x<0 or y >=len(matrix) or y<0 or flag_matrix[y][x] == 0:
                if direct == 0:
                    x = x - 1
                    y = y + 1
                elif direct == 1:
                    y = y - 1
                    x = x - 1
                elif direct == 2:
                    x = x + 1
                    y = y - 1
                elif direct == 3:
                    y = y + 1
                    x = x + 1
                direct = (direct + 1)%4
        return result

# @lc code=end

