
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = []
        begin_dp = []

        for i in range(rows):
            dp.append(0)
            begin_dp.append([])
        
        result = 0
        for i in range(rows):
            line_counter = 0
            for j in range(cols):
                if matrix[i][j] == '1':
                    begin_dp[i].append(j)
            
            max_connect_part = 0
            for k in range(i,-1,-1):
                if len(begin_dp) == 0:
                    break
                
                j = 0
                while j < len(begin_dp[i]):
                    if matrix[k][begin_dp[i][j]] == '0':
                        del begin_dp[i][j]
                        j = j - 1
                    j = j + 1
                
                connect_part = self.cal_connect_part(begin_dp[i])
                max_connect_part = max(max_connect_part,connect_part * (i - k + 1))
            result = max(result,max_connect_part)

        return result

    def cal_connect_part(self,line):
        if len(line) == 0:
            return 0
        counter = line[0]
        connect_part = 1
        max_connect_part = 1
        for i in range(1,len(line)):
            if line[i] == counter + 1:
                connect_part = connect_part + 1
            else:
                connect_part = 1
            counter = line[i]
            max_connect_part = max(max_connect_part, connect_part)
        
        return max_connect_part



