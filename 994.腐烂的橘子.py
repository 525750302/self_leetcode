#
# @lc app=leetcode.cn id=994 lang=python
#
# [994] 腐烂的橘子
#

# @lc code=start
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        stack = []
        num_of_origin = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    stack.append([i,j])
                if grid[i][j] == 1:
                    num_of_origin += 1
        if num_of_origin == 0:
            return 0
        time = -1
        while(stack):
            time += 1
            new_stack = []
            while(stack):
                [x,y] = stack.pop()
                if x -1>=0 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    new_stack.append([x-1,y])
                    num_of_origin -= 1
                if x +1<len(grid) and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    new_stack.append([x+1,y])
                    num_of_origin -= 1                
                if y -1>=0 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    new_stack.append([x,y-1])
                    num_of_origin -= 1
                if y +1<len(grid[0]) and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    new_stack.append([x,y+1])
                    num_of_origin -= 1      
            stack = new_stack
        if num_of_origin <=0:
            return time
        return -1          

# @lc code=end

