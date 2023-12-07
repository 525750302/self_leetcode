#
# @lc app=leetcode.cn id=1094 lang=python
#
# [1094] 拼车
#

# @lc code=start
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        stack = []
        curr = 0
        trips.sort(key=lambda x: x[1])
        for i in range(len(trips)):
            if stack:
                while stack and stack[0][2] <= trips[i][1]:
                    curr -= stack[0][0]
                    stack.pop(0)
            if trips[i][1] != trips[i][2]:

                if trips[i][0] > capacity - curr:
                    return False
                if trips[i][1] > trips[i][2]:
                    return False
                curr = curr + trips[i][0]
                stack.append(trips[i])
                stack.sort(key=lambda x: x[2])
        return True

# @lc code=end

