#
# @lc app=leetcode.cn id=2304 lang=python
#
# [2304] 网格中的最小路径代价
#

# @lc code=start
class Solution(object):
    def minPathCost(self, grid, moveCost):
        """
        :type grid: List[List[int]]
        :type moveCost: List[List[int]]
        :rtype: int
        """
        dp_val = [[99999999] * len(grid[0]) for _ in range(len(grid))

        for i in range(len(grid[0])):
            dp_val[0][i] = grid[0][i]
        for i in range(len(grid)):
            for j in range(1,len(grid[0])):
                for k in range(len(grid[0])):
                    dp_val[i][j] = min(dp_val[i][j], dp_val[i - 1][k] + moveCost[i][j] + grid[i][j])
            
        return min(dp_val[-1])

# @lc code=end

