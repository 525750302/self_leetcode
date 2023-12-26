class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:

        def isSingleRowCompliant(status: int, row: int) -> bool:
            for j in range(n):
                if ((status >> j) & 1) == 1:
                    if seats[row][j] == '#':
                        return False
                    if j > 0 and ((status >> (j - 1)) & 1) == 1:
                        return False
            return True

        def isCrossRowsCompliant(status: int, upperRowStatus: int) -> bool:
            for j in range(n):
                if ((status >> j) & 1) == 1:
                    if j > 0 and ((upperRowStatus >> (j - 1)) & 1) == 1:
                        return False
                    if j < n - 1 and ((upperRowStatus >> (j + 1)) & 1) == 1:
                        return False
            return True

        @cache
        def dp(row: int, status: int) -> int:
            if not isSingleRowCompliant(status, row):
                return -inf
            students = bin(status).count('1')
            if row == 0:
                return students
            mx = 0
            for upperRowStatus in range(2 ** n):
                if isCrossRowsCompliant(status, upperRowStatus):
                    mx = max(mx, dp(row - 1, upperRowStatus))
            return students + mx

        m, n = len(seats), len(seats[0])
        mx = 0
        for i in range(2 ** n):
            mx = max(mx, dp(m - 1, i))
        return mx