#
# @lc app=leetcode.cn id=2079 lang=python
#
# [2079] 给植物浇水
#

# @lc code=start
class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        count = 0
        ans = 0
        for i in range(len(plants)):
            if count + plants[i]  > capacity:
                count = 0
                ans += i * 2
            ans += 1
            count += plants[i]

        return ans 

# @lc code=end

