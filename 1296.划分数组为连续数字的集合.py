#
# @lc app=leetcode.cn id=1296 lang=python
#
# [1296] 划分数组为连续数字的集合
#

# @lc code=start
class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) % k != 0:
            return False
        nums.sort()
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        a = list(dic.keys())
        a.sort()
        for i in a:
            if  dic[i] != 0:
                for j in range(1,k):
                    if dic.get(i+j,0) < dic[i]:
                        return False
                    else:
                        dic[i+j] -= dic[i]
        return True

# @lc code=end

