class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # solve(mx) 返回最大金额为 mx 时，最多可以偷多少间房子
        def solve(mx: int) -> int:
            f = [0] * len(nums)
            for x in range(len(nums)):
                if nums[x] > mx:
                    f[x] = f[x-1]
                else:
                    f[x] = max(f[x-1], f[x-2] + 1)
            return f[-1]
        return bisect_left(range(min(nums), max(nums)), k, key=solve) + min(nums)
