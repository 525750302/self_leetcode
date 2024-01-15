#
# @lc app=leetcode.cn id=1338 lang=python
#
# [1338] 数组大小减半
#

# @lc code=start
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dic = {}
        for i in arr:
            dic[i] = dic.get(i, 0) + 1
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        count = 0
        res = 0
        for i in dic:
            count += i[1]
            res += 1
            if count * 2 >= len(arr):
                break
        return res
# @lc code=end

