#
# @lc app=leetcode.cn id=1444 lang=python
#
# [1444] 切披萨的方案数
#

# @lc code=start
class Solution(object):
    def ways(self, pizza, k):
        """
        :type pizza: List[str]
        :type k: int
        :rtype: int
        """
        nums = [[0]*(len(pizza[0]) +1) for _ in range(len(pizza) + 1)]
        for i in range(len(pizza)-1,-1,-1):
            for j in range(len(pizza[0])-1,-1,-1): 
                if pizza[i][j] == 'A':
                    nums[i][j] = nums[i][j+1] + nums[i+1][j] + 1 - nums[i+1][j+1]
                else:
                    nums[i][j] = nums[i][j+1] + nums[i+1][j] - nums[i+1][j+1]
        if nums[0][0] == 0:
            return 0
        MAX_NUM = 10**9 + 7
        #三维dp
        dp = [[[0]*(len(pizza[0]) + 1) for _ in range(len(pizza) + 1)] for z in range(k)]
        dp[0][0][0] = 1
        for i in range(1,k):
            for j in range(len(pizza)):
                for k in range(len(pizza[0])):
                    if nums[j][k] <=0:
                        continue
                    # 纵切
                    for z in range(k):
                        if nums[j][z] - nums[j][k] > 0:
                            dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][z]) % MAX_NUM   
                    # 横切
                    for z in range(j):
                        if nums[z][k] - nums[j][k] > 0:
                            dp[i][j][k] = (dp[i][j][k] + dp[i-1][z][k]) % MAX_NUM
            #print(dp[i])
        sum = 0
        for i in range(len(pizza)):
            for j in range(len(pizza[0])):
                sum = (sum + dp[-1][i][j]) % MAX_NUM

        return sum 
# @lc code=end

