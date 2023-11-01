#
# @lc app=leetcode.cn id=79 lang=python
#
# [79] 单词搜索
#

# @lc code=start
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.direct = [[-1,0],[1,0],[0,-1],[0,1]]
        used_map = [[0]*len(board) for i in range(board[0])]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    used_map[i][j] = 1
                    if self.check(board,i,j,used_map,word,1) == True:
                        return True
                    used_map[i][j] = 0
        
        return False
    
    def check(self,board,begin_i,begin_j,used_map,word,now_num):
        if now_num == len(word):
            return True
        for d in self.direct:
            if begin_i + d[0] >=0 and begin_i + d[0] < len(board):
                if begin_j + d[1] >=0 and begin_j + d[1] < len(board[0]):
                    if used_map[begin_i+d[0]][begin_j+d[1]] == 0 and board[begin_i+d[0]][begin_j+d[1]] == word[now_num]:
                        used_map[i][j] = 1
                        if self.check(board,i,j,used_map,word,1) == True:
                            return True
                        used_map[i][j] = 0
        return False

        
# @lc code=end

