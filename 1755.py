class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        def state_compress(lst):
            m = len(lst)
            bit ={1<<i: lst[i] for i in range(m)}
            dp = [0]*(1<<m)
            for i in range(1,1<<m):
                dp[i] = dp[i^i&-i] + bit[i&-i]
                print(i^i&-i)
            return sorted(list(set(dp)))
        pre = state_compress(nums[:n//2])
        post = state_compress(nums[n//2:])
        ans = abs(goal)
        i = 0
        j = len(post)-1
        while i < len(pre) and j >= 0:
            ans = min(ans, abs(goal-pre[i]-post[j]))
            if not ans:
                return ans
            if pre[i]+post[j] > goal:
                j -= 1
            elif pre[i]+post[j] < goal:
                i += 1
        return ans