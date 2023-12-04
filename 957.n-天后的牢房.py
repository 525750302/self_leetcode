#
# @lc app=leetcode.cn id=957 lang=python
#
# [957] N 天后的牢房
#

# @lc code=start
class Solution(object):
    def change_day(self, cells):
        new_cells = cells[0:]
        new_cells[0] = 0
        new_cells[-1] = 0
        for i in range(1, len(cells) - 1):
            if cells[i-1] == cells[i + 1]:
                new_cells[i] = 1
            else:
                new_cells[i] = 0
        return new_cells

    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        d = {}
        count = 0
        loop = 0
        key = tuple(cells)
        while d.get(key) is None:
            d[key] = count
            cells = self.change_day(cells)
            key = tuple(cells)
            count += 1
            if count == n:
                return cells
            
        loop = count - d[key]
        
        n = (n - count) % loop + d[key]
        for i in d.keys():
            if d[i] == n:
                return list(i)
    

# @lc code=end

