#
# @lc app=leetcode.cn id=2178 lang=python
#
# [2178] 拆分成最多数目的正偶数之和
#

# @lc code=start
class Solution(object):
    def maximumEvenSplit(self, finalSum):
        """
        :type finalSum: int
        :rtype: List[int]
        """
        if finalSum % 2 == 1:
            return []
        res = []
        count = 2
        sum = 0
        while sum < finalSum:
            sum += count
            res.append(count)
            count += 2
        if sum > finalSum:
            res.pop(int((sum - finalSum)/2 - 1))

        return res

# @lc code=end

