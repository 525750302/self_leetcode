#
# @lc app=leetcode.cn id=2258 lang=python
#
# [2258] 逃离火灾
#

MAX_TIME = 10**9
# @lc code=start
class Solution(object):
    def maximumMinutes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.fire_map = [[MAX_TIME] * len(grid[0]) for _ in range(len(grid))]
        self.human_map = [[MAX_TIME] * len(grid[0]) for _ in range(len(grid))]
        self.ans_map = [[MAX_TIME] * len(grid[0]) for _ in range(len(grid))]
        self.direct = [[1,0],[-1,0],[0,1],[0,-1]]
        self.fire_bfs(grid)
        self.ans = 0
        self.human_bfs(grid)
        print(self.fire_map)
        print(self.human_map)
        if self.ans == MAX_TIME or self.ans == -1:
            return self.ans
        self.updata_ans(grid)
        return self.ans
    
    def fire_bfs(self,grid):
        stack = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    stack.append((i,j))
                    self.fire_map[i][j] = 0
                if grid[i][j] == 2:
                    self.fire_map[i][j] = -MAX_TIME
        
        while stack:
            x,y = stack.pop(0)
            for i in range(4):
                nx = x + self.direct[i][0]
                ny = y + self.direct[i][1]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and self.fire_map[nx][ny] == MAX_TIME:
                    self.fire_map[nx][ny] = min(self.fire_map[x][y] + 1,self.fire_map[nx][ny])
                    stack.append((nx,ny))

    def human_bfs(self,grid):
        stack = [[0,0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    self.human_map[i][j] = -MAX_TIME
        self.human_map[0][0] = 0
        flag = 0
        flag1 = 0
        while stack:
            x,y = stack.pop(0)
            for i in range(4):
                nx = x + self.direct[i][0]
                ny = y + self.direct[i][1]
                if nx == len(grid) -1 and ny == len(grid[0]) - 1 and self.human_map[nx][ny] == MAX_TIME and self.human_map[x][y]+ 1<=self.fire_map[nx][ny]:
                    flag = 1
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and self.human_map[nx][ny] == MAX_TIME:
                    if min(self.human_map[x][y]+ 1,self.human_map[nx][ny]) <= self.fire_map[nx][ny]:
                        if self.human_map[x][y]+ 1 == self.fire_map[nx][ny] and (nx != len(grid) -1 or ny != len(grid[0]) - 1 ):
                            continue
                        self.human_map[nx][ny] = min(self.human_map[x][y]+ 1,self.human_map[nx][ny])
                        if self.fire_map[nx][ny] == MAX_TIME:
                            flag1 = 1
                        stack.append((nx,ny))
        if flag == 0:
            self.ans = -1
        elif flag1 == 1:
            self.ans = MAX_TIME

    
    def updata_ans(self,grid):
        stack = [[0,0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    self.ans_map[i][j] = MAX_TIME
                else:
                    self.ans_map[i][j] = self.fire_map[i][j] - self.human_map[i][j]
        self.ans = 0
        used = [[0] * len(grid[0]) for _ in range(len(grid))]
        while stack:
            x,y = stack.pop(0)
            used[x][y] = 1
            for i in range(4):
                nx = x + self.direct[i][0]
                ny = y + self.direct[i][1]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 2 and used[nx][ny] == 0:
                    self.ans_map[nx][ny] = min(self.ans_map[x][y],self.ans_map[nx][ny])
                    stack.append([nx,ny])
                if nx == len(grid) -1 and ny == len(grid[0]) - 1  and used[nx][ny] == 0 :
                    print(self.fire_map[x][y],self.fire_map[nx][ny])
                    if self.fire_map[x][y] > self.fire_map[nx][ny]:
                        self.ans = max(self.ans,self.ans_map[nx][ny])
                    else:
                        self.ans = max(self.ans,self.ans_map[nx][ny] - 1)
        
        
# @lc code=end

