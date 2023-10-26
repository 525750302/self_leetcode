#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        max_val = 0
        for i in range(len(nums)):
            max_val = (max_val<<1 )+1
        for j in range(1,max_val+1):
            target = j
            data = []
            count1 = 0
            while target > 0:
                if target % 2 == 1:
                    data.append(nums[count1])
                count1 += 1
                target = int(target >> 1)
            result.append(data)
        
        return result
# @lc code=end

a = Solution()
input = [1,2,3,4,5,6,7,8,9]
print(a.subsets(input))
