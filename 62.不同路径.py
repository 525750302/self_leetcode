#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = 1 
        bigger = max(m,n)
        smaller = min(m,n)
        dive = 1
        for i in range(1, smaller):
            count *= (smaller + bigger - 1 - i) 
            dive *= i
        return count//dive
# @lc code=end

