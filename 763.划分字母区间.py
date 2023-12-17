#
# @lc app=leetcode.cn id=763 lang=python
#
# [763] 划分字母区间
#

# @lc code=start
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        stack = []
        dic_begin = {}
        dic_end = {}
        for i in range(len(s)):
            if s[i] not in dic_begin:
                dic_begin[s[i]] = i
                dic_end[s[i]] = i
            else:
                dic_end[s[i]] = i
        res = []
        last = -1
        for i in range(len(s)):
            if s[i] not in stack:
                stack.append(s[i])
            if dic_end[s[i]] <= i:
                stack.remove(s[i])
            if len(stack) == 0:
                res.append(i - last)
                last = i
        return res


# @lc code=end

