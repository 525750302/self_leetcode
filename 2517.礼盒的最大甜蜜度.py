#
# @lc app=leetcode.cn id=2517 lang=python
#
# [2517] 礼盒的最大甜蜜度
#

# @lc code=start
class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        price.sort()
        result = 0

        left, right =- 0, price[-1] - price[0]
        while left < right:
            mid = (left + right + 1) //2
            if self.check(price,k,mid):
                left = mid
            else:
                right = mid-1
        return left

    def check(self,price,k,distance):
        pre = - inf 
        count = 0
        for i in price:
            if i - pre >= distance:
                count += 1
                if count >= k:
                    break
                pre = i
        return count >= k
# @lc code=end

