#
# @lc app=leetcode.cn id=1583 lang=python
#
# [1583] 统计不开心的朋友
#

# @lc code=start
class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        res = 0
        dic = {}
        dic_pair = {}
        for i in range(len(preferences)):
            for j in range(len(preferences[i])):
                dic[(i,preferences[i][j])] = j

        for i, j in pairs:
            dic_pair[i] = j
            dic_pair[j] = i

        for i,j in pairs:
            for k in range(n):
                if preferences[i][k] == j:
                    break
                if dic[(preferences[i][k], i)] < dic[(preferences[i][k], dic_pair[preferences[i][k]])]:
                    res += 1
                    break
            for l in range(n):
                if preferences[j][l] == i:
                    break
                if dic[(preferences[j][l], j)] < dic[(preferences[j][l], dic_pair[preferences[j][l]])]:
                    res += 1
                    break
        return res 
# @lc code=end

