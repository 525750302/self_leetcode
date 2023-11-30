#
# @lc app=leetcode.cn id=1657 lang=python
#
# [1657] 确定两个字符串是否接近
#

# @lc code=start
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        dic_word1 = {}
        dic_word2 = {}
        if len(dic_word1) != len(dic_word2):
            return False
        for i in range(len(word1)):
            dic_word1[word1[i]] = dic_word1.get(word1[i], 0) + 1
            dic_word2[word2[i]] = dic_word2.get(word2[i], 0) + 1

        key_of_word1 = dic_word1.keys()
        key_of_word2 = dic_word2.keys()
        key_of_word1.sort()
        key_of_word2.sort()
        for i in range(len(key_of_word1)):
            if key_of_word1[i] != key_of_word2[i]:
                return False
        num_of_word1 = dic_word1.values()
        num_of_word2 = dic_word2.values()
        num_of_word1.sort()
        num_of_word2.sort()
        for i in range(len(num_of_word1)):
            if num_of_word1[i] != num_of_word2[i]:
                return False
        
        return True

# @lc code=end

