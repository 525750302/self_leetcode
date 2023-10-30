class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-999999] * len(nums)
        dp[0] = nums[0]
        #print(dp)
        for i in range(1,len(nums)):
            dp[i] = max(nums[i],dp[i-1]  + nums[i])
        
        return max(dp)
