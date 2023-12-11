#
# @lc app=leetcode.cn id=96 lang=python
#
# [96] 不同的二叉搜索树
#

# @lc code=start
num = [0] * 20
num[0] = 1
num[1] = 1
num[2] = 2
num[3] = 5
for i in range(4, 20):
    for j in range(0,i):
        num[i] += num[j] * num[i-1-j]

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return num[n]
        
# @lc code=end

