#
# @lc app=leetcode.cn id=1034 lang=python
#
# [1034] 边界着色
#

# @lc code=start
class Solution(object):
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """
        return_map = [[0]* len(grid[0]) for _ in range(len(grid))]
        target = grid[row][col]
        return_map = self.dfs(grid, row, col, color, return_map, target)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if return_map[i][j] == 0 or return_map[i][j] == -1 :
                    return_map[i][j] = grid[i][j]
        return return_map
    
    def dfs(self, grid, row, col, color, return_map, target):
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(4):
            dx = direction[i][0]
            dy = direction[i][1]
            count = 0
            if 0 > row + dx or row + dx >= len(grid) or 0 > col + dy or  col + dy >= len(grid[0]):
                return_map[row][col] = color
                continue
            if 0 <= row + dx < len(grid) and 0 <= col + dy < len(grid[0]):
                if grid[row+dx][col+dy] == target:
                    if return_map[row+dx][col+dy] == 0:
                        return_map[row+dx][col+dy] = -1
                        self.dfs(grid, row+dx, col+dy, color, return_map, target)
                if grid[row+dx][col+dy] != target:
                    count += 1
            if count > 0:
                return_map[row][col] = color
        return return_map


# @lc code=end

