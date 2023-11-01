class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        
        if len(nums) <2:
            return False

        if sum % 2 == 1:
            return  False
        
        dp = [[0] * (sum//2 + 1) for i in range(len(nums)+1)]
        dp[0][0] = 1
        for i in range(1,len(nums) + 1):
            for j in range(sum//2 + 1):
                if j >= nums[i-1] and dp[i-1][j-nums[i-1]] == 1:
                    dp[i][j] = 1
                elif dp[i-1][j] == 1:
                    dp[i][j] = 1
            if dp[i][sum//2] == 1:
                return True
                
        print(dp)
        return False