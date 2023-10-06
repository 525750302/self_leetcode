class Solution(object):
    sum_result = []
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        usable = [[1]*n for i in range(n)]
        self.sum_result = []
        solution = []
        usable_rows = [1]*n
        for i in range(n):
            solution.append(i)
            usable[0][i] = 0
            usable_rows[i] = 0
            
            for j in range(1, n):
                if i-j >= 0:
                    usable[j][i-j] = 0
            for j in range(1, n):
                if i+j < n:
                    usable[j][i+j] = 0
            self.search_location(usable_rows,usable,1,n,solution)
            solution.pop(-1)
            usable[0][i] = 1
            usable_rows[i] = 1
            for j in range(1, n):
                if i-j >= 0:
                    usable[j][i-j] = 1
            for j in range(1, n):
                if i+j < n:
                    usable[j][i+j] = 1
        
        return self.sum_result

    
    def search_location(self, usable_rows, usable, no, n, solution):
        if no == n:
            result = self.draw(solution,n)
            self.sum_result.append(result)
            return
    
        for i in range(n):
            if usable[no][i] <= 0 or usable_rows[i] <= 0:
                continue
            solution.append(i)
            usable[no][i] = usable[no][i] - 1
            usable_rows[i] = 0
                        
            for j in range(1, n - no):
                if i-j >= 0:
                    usable[j + no][i-j] = usable[j + no][i-j] - 1
            for j in range(1, n - no):
                if i+j < n:
                    usable[j + no][i+j] = usable[j + no][i+j] - 1
            self.search_location(usable_rows,usable,no + 1,n,solution)

            solution.pop(-1)
            usable[no][i] = usable[no][i] + 1
            usable_rows[i] = 1
            for j in range(1, n - no):
                if i-j >= 0:
                    usable[j + no][i-j] = usable[j + no][i-j] + 1
            for j in range(1, n - no):
                if i+j < n:
                    usable[j + no][i+j] = usable[j + no][i+j] + 1

    def draw(self,line,n):
        result = []
        for i in range(len(line)):
            a = line[i]
            str_line = str()
            for j in range(a):
                str_line = str_line + "."
            str_line = str_line + "Q"
            for j in range(a + 1, n):
                str_line = str_line + "."
            result.append(str_line)
        
        return result

a = Solution()
input = 6
result = a.solveNQueens(input)
print(result)