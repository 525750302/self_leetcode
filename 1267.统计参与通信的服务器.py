#
# @lc app=leetcode.cn id=1267 lang=python
#
# [1267] 统计参与通信的服务器
#

# @lc code=start
class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        n = len(grid[0])
        m = len(grid)
        color_x = [0] * m
        color_y = [0] * n
        sum_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    color_x[i] += 1
                    color_y[j] += 1
                    sum_count += 1

        for i in range(m):
            for j in range(n):
                if (color_x[i] > 1 or color_y[j] > 1) and grid[i][j] > 0:
                    res += 1
        return res


# @lc code=end

