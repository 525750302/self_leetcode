#
# @lc app=leetcode.cn id=1944 lang=python
#
# [1944] 队列中可以看到的人数
#

# @lc code=start
class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[i] >= stack[-1]:
                res[i] +=1
                stack.pop()
            if stack:
                res[i] += 1
            stack.append(heights[i])
        return res
# @lc code=end

