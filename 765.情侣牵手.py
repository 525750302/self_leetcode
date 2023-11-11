#
# @lc app=leetcode.cn id=765 lang=python
#
# [765] 情侣牵手
#

# @lc code=start
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row)
        d = {row[i]: i for i in range(n)}
        res = 0
        for i in range(0,n,2):
            if row[i] == row[i] ^ 1:
                continue
            j = i ^ 1
            target = row[i] ^ 1
            while row[j] != target:
                res += 1
                a = row[j]
                b = d[target]
                row[j], row[d[target]] = row[d[target]], row[j]
                d[a] = b
                d[target] = j
                print(row)

        return res
# @lc code=end

