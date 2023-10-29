#
# @lc app=leetcode.cn id=419 lang=python
#
# [419] 甲板上的战舰
#

# @lc code=start
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        col = len(board[0])
        row = len(board)
        check_map = [[0]*(col + 2) for i in range(row + 2)]
        num = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] =="X":
                    if check_map[i][j+1] == 0 and check_map[i+1][j] == 0:
                        num += 1
                        check_map[i+1][j+1] = num
                    else:
                        check_map[i+1][j+1] = max(check_map[i][j+1],check_map[i + 1][j])
        
        return num
# @lc code=end

