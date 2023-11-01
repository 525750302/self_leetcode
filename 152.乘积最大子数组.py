class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_po = [0] * len(nums)
        dp_neg = [0] * len(nums)
        for i in range(len(nums)):
            dp_po[i] = nums[i]
            dp_neg[i] = -nums[i]

        for i in range(1,len(nums)):
            if nums[i] >= 0:
                dp_po[i] = max(dp_po[i-1] * nums[i],dp_po[i])
                dp_neg[i] = max(dp_neg[i-1] * nums[i],dp_neg[i])
            else:
                dp_neg[i] = max(dp_po[i-1] * (-nums[i]),dp_neg[i])
                dp_po[i] = max(dp_neg[i-1] *(-nums[i]),dp_po[i])
       
        return max(max(dp_po),-min(dp_neg))