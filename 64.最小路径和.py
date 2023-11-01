class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[999999] * len(grid[0]) for i in range(len(grid))]
        dp[0][0] = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0:
                    alternative1 = 9999999
                else:
                    alternative1 = dp[i-1][j]
                if j == 0:
                    alternative2 = 9999999
                else:
                    alternative2 = dp[i][j-1]
                
                dp[i][j] = min(alternative1, alternative2, dp[i][j])  + grid[i][j]
                
        return dp[-1][-1]