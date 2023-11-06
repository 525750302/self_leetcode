#
# @lc app=leetcode.cn id=208 lang=python
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie(object):

    def __init__(self):
        self.tree = {}
        self.dic = {}
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        str = ""
        for i in range(len(word)):
            str = str + word[i]
            if self.tree.get(str) == None:
                self.tree[str] = []
            if i > 0:
                self.tree[last].append(str)
            last = str
        self.dic[word] = 1
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if self.dic.get(word) is None:
            return False
        return True


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        str = ""
        for i in range(len(prefix)):
            str = str + prefix[i]
            if self.tree.get(str) == None:
                return False
            if i > 0:
                if self.tree[last].count(str) == 0:
                    return False
            last = str
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

