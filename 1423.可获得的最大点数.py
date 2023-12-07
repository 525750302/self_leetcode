#
# @lc app=leetcode.cn id=1423 lang=python
#
# [1423] 可获得的最大点数
#

# @lc code=start
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        pre = [0]
        ord = [0]
        sum = 0
        for i in range(len(cardPoints)):
            sum += cardPoints[i]
            pre.append(sum)
        sum = 0
        for i in range(len(cardPoints) - 1, -1 , -1):
            sum += cardPoints[i]
            ord.append(sum)
        res = 0
        for i in range(k + 1):
            res = max(pre[i] + ord[k-i], res)
        return res 
# @lc code=end

