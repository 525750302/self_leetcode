class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        qp = [0] * n
        qp[0] = nums[0]
        for i in range(1,n):
            qp[i] = min(qp[i-1]+nums[i], nums[i])
        res1 = max(dp)
        if res1 < 0:
            return res1
        res2 = sum(nums)-min(qp)
        return max(res1, res2)