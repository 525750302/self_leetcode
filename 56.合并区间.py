#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])

        stack = []
        for i in range(len(intervals)):
            if len(stack) == 0:
                stack.append(intervals[i])
                continue
            a = intervals[i]
            if a[0]<=stack[-1][1]:
                stack[-1][1] = max(a[1],stack[-1][1])
            else:
                stack.append(a)
        
        return stack
# @lc code=end

