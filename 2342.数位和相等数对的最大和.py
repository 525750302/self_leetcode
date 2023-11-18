#
# @lc app=leetcode.cn id=2342 lang=python
#
# [2342] 数位和相等数对的最大和
#

# @lc code=start
class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        max_result = 0
        for i in range(len(nums)):
            target = self.sum_of_location(nums[i])
            if dic.get(target) == None:
                dic[target] = nums[i]
            else:
                max_result = max(dic[target] + nums[i], max_result)
                dic[target] = max(dic[target] , nums[i])
        return max_result
    
    def sum_of_location(self,num):
        count = 0
        while num:
            count = count + (num % 10)
            num = num // 10
        return count
# @lc code=end

