#
# @lc app=leetcode.cn id=1314 lang=python
#
# [1314] 矩阵区域和
#

# @lc code=start
class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        val_map = [[0]*(len(mat[0]) + 1) for _ in range(len(mat) + 1)]
        for i in range(len(mat)-1,-1,-1):
            for j in range(len(mat[0])-1,-1,-1):
                if i != len(mat)-1:
                    val_map[i][j] += val_map[i+1][j]
                if j != len(mat[0])-1:
                    val_map[i][j] += val_map[i][j+1]
                if i != len(mat)-1 and j != len(mat[0])-1:
                    val_map[i][j] -= val_map[i+1][j+1]
                val_map[i][j] += mat[i][j]
        res = [[0]*len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                left_x  = max(0, i-k)
                left_y  = max(0, j-k)
                right_x = min(len(mat), i+k + 1)
                right_y = min(len(mat[0]), j+k + 1)
                res[i][j] = val_map[left_x][left_y] - val_map[left_x][right_y] - val_map[right_x][left_y] + val_map[right_x][right_y]
        return res


# @lc code=end

