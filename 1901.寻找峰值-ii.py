class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        low, high = 0, m - 1
        while low <= high:
            i = (low + high) // 2
            j = mat[i].index(max(mat[i]))
            if i - 1 >= 0 and mat[i][j] < mat[i - 1][j]:
                high = i - 1
                continue
            if i + 1 < m and mat[i][j] < mat[i + 1][j]:
                low = i + 1
                continue
            return [i, j]
        return None # impossible
