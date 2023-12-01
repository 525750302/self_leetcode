#
# @lc app=leetcode.cn id=2661 lang=python
#
# [2661] 找出叠涂元素
#

# @lc code=start
class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        dic_index = {}
        for i in range(len(arr)):
            dic_index[arr[i]] = i
        max_line = [0] * len(mat)
        max_col = [0] * len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                max_line[i] = max(max_line[i], dic_index[mat[i][j]])
                max_col[j] = max(max_col[j], dic_index[mat[i][j]])
        ans = 10**9
        for i in range(len(mat)):
            ans = min(ans,max_line[i])
        for j in range(len(mat[0])):
            ans = min(ans,max_col[j])
        return ans 

# @lc code=end

