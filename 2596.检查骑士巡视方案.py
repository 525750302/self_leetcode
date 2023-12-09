#
# @lc app=leetcode.cn id=2596 lang=python
#
# [2596] 检查骑士巡视方案
#

# @lc code=start
class Solution(object):
    def checkValidGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        visited[0][0] = 1
        direc = [[1,2],[2,1],[-1,2],[-2,1],[-1,-2],[-2,-1],[1,-2],[2,-1]]
        return self.dfs(grid, 0, 0, direc, visited , 1)
    def dfs(self, grid, x, y, direc, visited, step):
        if step == len(grid) * len(grid[0]):
            return True
        for dx, dy in direc:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and visited[nx][ny] == 0 and grid[nx][ny] == step:
                visited[nx][ny] = 1
                if self.dfs(grid, nx, ny, direc, visited, step + 1):
                    return True
                visited[nx][ny] = 0
        return False
# @lc code=end

