#
# @lc app=leetcode.cn id=212 lang=python
#
# [212] 单词搜索 II
#

# @lc code=start
from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        self.used_map = [[0] * (len(board[0])+2) for i in range(len(board) + 2)]
        for i in range(len(board[0])+1):
            self.used_map[0][i] = 1
            self.used_map[len(board)+1][i] = 1
        for j in range(len(board) + 1):
            self.used_map[j][0] = 1
            self.used_map[j][len(board[0])+1] = 1
        self.n = len(board)
        self.m = len(board[0])
        self.directs = [[-1,0],[1,0],[0,-1],[0,1]]

        self.result = []
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                self.search(trie, i, j,board)
        
        return self.result
    
    def search(self,head,begin_x,begin_y,board):
        if board[begin_x][begin_y] not in head.children:
            return
        target = board[begin_x][begin_y]
        nxt = head.children[target]
        if nxt.word != "":
            self.result.append(nxt.word)
            nxt.word = ""
        if nxt.children:
            for dicrect in self.directs:
                target_x = begin_x + dicrect[0]
                target_y = begin_y + dicrect[1]
                if self.used_map[target_x+1][target_y+1] == 0:
                    self.used_map[begin_x+1][begin_y+1] = 1
                    self.search(nxt,target_x,target_y,board)
                    self.used_map[begin_x+1][begin_y+1] = 0
        if not nxt.children:
                head.children.pop(target)

# @lc code=end

