class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        self.map = [[0] * len(land[0]) for i in range(len(land))]
        self.dicrection = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
        pool_num = 1
        ans = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if self.map[i][j] == 0 and land[i][j] == 0:
                    self.map[i][j] = pool_num
                    ans.append(self.dfs(i,j,land) + 1)
                    pool_num += 1
        ans.sort()
        return ans
    
    def dfs(self,x,y,land):
        area = 0
        for dx,dy in self.dicrection:
            tar_x = x + dx
            tar_y = y + dy
            if 0<=tar_x<len(self.map) and 0<=tar_y<len(self.map[0]) and land[tar_x][tar_y] == 0 and self.map[tar_x][tar_y] == 0:
                self.map[tar_x][tar_y] = self.map[x][y]
                area += 1
                area +=self.dfs(tar_x, tar_y, land)

        return area
