class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        right = left
        dic = {}
        res = 0
        while right < len(nums):
            dic[nums[right]] = dic.get(nums[right], 0) + 1
            if dic[nums[right]] > k:
                while nums[left] != nums[right]:
                    dic[nums[left]] -= 1
                    left += 1
                    
                dic[nums[left]] -= 1
                left += 1
            if right - left + 1 >res:
                res = right - left + 1
            #print(right,left)
            right += 1
        return res
