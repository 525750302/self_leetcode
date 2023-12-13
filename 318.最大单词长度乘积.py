#
# @lc app=leetcode.cn id=318 lang=python
#
# [318] 最大单词长度乘积
#

# @lc code=start
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len)
        res = 0
        words.reverse()
        set_words = [set(words[i]) for i in range(len(words))]
        for i in range(len(words) - 1):
            if len(set_words[i]) >= 26:
                continue
            if res > len(words[i]) * len(words[i + 1]):
                break
            for j in range(i + 1, len(words)):
                if not set_words[j] & set_words[i]:
                    res = max(res, len(words[i]) * len(words[j]))
        return res
# @lc code=end

