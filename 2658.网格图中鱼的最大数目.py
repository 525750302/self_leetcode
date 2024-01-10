#
# @lc app=leetcode.cn id=2658 lang=python
#
# [2658] 网格图中鱼的最大数目
#

# @lc code=start
class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0 and not visited[i][j]:
                    value = self.dfs(grid, visited, i, j)
                    res = max(res, value)
        return res 

        
    def dfs(self, grid, visited, i, j):
        if visited[i][j] or grid[i][j] == 0:
            return 0
        visited[i][j] = True
        value = grid[i][j]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = i + dx, j + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                value += self.dfs(grid, visited, x, y)
        return value
# @lc code=end

