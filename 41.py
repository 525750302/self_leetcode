class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i]< len(nums) and nums[i]>0 and nums[i]!= i+1 and nums[nums[i]-1]!=nums[i] :
                self.swap(i,nums)
                i = i-1
            i =i+1
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums) + 1
    
    def swap(self,location,nums):
        target = nums[location] - 1
        if nums[target]!= target + 1:
            a = nums[target]
            nums[target] = nums[location]
            nums[location] = a
        
