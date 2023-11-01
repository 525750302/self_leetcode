#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        result = 0
        
        def draw_map(i,j,result):
            nonlocal grid
            grid[i][j] = result
            if i>0 and grid[i-1][j] == "1":
                draw_map(i-1,j,result)
            if j>0 and grid[i][j-1] == "1":
                draw_map(i,j-1,result)
            if i<len(grid)-1 and grid[i+1][j] == "1":
                draw_map(i+1,j,result)
            if j<len(grid[0])-1 and grid[i][j+1] == "1":
                draw_map(i,j+1,result)
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    result += 1
                    draw_map(i,j,result)
        
        return result
# @lc code=end

