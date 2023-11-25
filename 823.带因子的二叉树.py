#
# @lc app=leetcode.cn id=823 lang=python
#
# [823] 带因子的二叉树
#

# @lc code=start
class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mod = (10 ** 9 + 7)
        arr.sort()
        dic = {v : i for i, v in enumerate(arr)}
        f = [1] * len(arr)

        for i , a in enumerate(arr):
            for j in range(i):
                b = arr[j]
                if a % b == 0 and a // b in dic:
                    f[i] = (f[i] + f[j] * f[dic[a//b]]) % mod
        return sum(f) % mod
# @lc code=end

