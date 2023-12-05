#
# @lc app=leetcode.cn id=2221 lang=python
#
# [2221] 数组的三角和
#

# @lc code=start
class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return (nums[0] + nums[1])% 10
        
        count = [1]

        for i in range(1,n - 1):
            if (n - i) % i == 0:
                count.append(count[i - 1]*((n - i) // i))
            else:
                count.append((count[i - 1])*(n - i)//i)
            #print(count, i , n-i)
        count.append(1)
        #print(count)
        res = sum((nums[i] * count[i])% 10 for i in range(n))
        res = res - res // 10 * 10
        return res


# @lc code=end

