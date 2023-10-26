class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = set()
        dig1 = set()
        dig2 = set()

        def dfs(row):
            if row == n:
                return 1

            else:
                count = 0
                for i in range(n):
                    if i in col or row - i in dig1 or row + i in dig2:
                        continue
                    col.add(i)
                    dig1.add(row-i)
                    dig2.add(row + i)
                    count += dfs(row + 1)
                    col.remove(i)
                    dig1.remove(row-i)
                    dig2.remove(row + i)
            return count
       
        return dfs(0)
