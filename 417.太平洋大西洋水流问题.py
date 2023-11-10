#
# @lc app=leetcode.cn id=417 lang=python
#
# [417] 太平洋大西洋水流问题
#

# @lc code=start
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        self.pacific = set()
        self.atlantic = set()
        m = len(heights)
        n = len(heights[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.dfs(heights, visited, i,j)
        for i in range(m):
            for j in range(n):
                if (i, j) in self.pacific and (i, j) in self.atlantic:
                    res.append([i, j])
        return res
    
    def dfs(self, heights, visited, i, j):
        m = len(heights)
        n = len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited[i][j] = True
        for d in directions:
            x = i + d[0]
            y = j + d[1]
            if x < 0 or y < 0:
                self.pacific.add((i, j))
            if x >= m or y >= n:
                self.atlantic.add((i, j))
            if x >= 0 and y >= 0 and x < m and y < n and not visited[x][y] and heights[x][y]<= heights[i][j]:
                if (x,y) in self.pacific and (x,y) in self.atlantic:
                    self.pacific.add((i, j))
                    self.atlantic.add((i, j))
                    break
                self.dfs(heights, visited, x, y)
                if (x,y) in self.pacific:
                    self.pacific.add((i, j))
                if (x,y) in self.atlantic:
                    self.atlantic.add((i, j))
        visited[i][j] = False

# @lc code=end

