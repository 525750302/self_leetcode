#
# @lc app=leetcode.cn id=130 lang=python
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.board = board
        m, n = len(board), len(board[0])
        self.map = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(i,0)
            if board[i][n-1] == 'O':
                self.dfs(i,n-1)
        for j in range(n):
            if board[0][j] == 'O':
                self.dfs(0,j)
            if board[m-1][j] == 'O':
                self.dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not self.map[i][j]:
                    board[i][j] = 'X'
        return board

    def dfs(self,i,j):
        if i<0 or i>=len(self.board) or j<0  or j>=len(self.board[0]) or self.board[i][j] != 'O' or self.map[i][j] == True:
            return
        self.map [i][j] = True
        self.dfs(i-1,j)
        self.dfs(i+1,j)
        self.dfs(i,j-1)
        self.dfs(i,j + 1)


# @lc code=end

