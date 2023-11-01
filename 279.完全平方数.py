class Solution:
    def numSquares(self, n: int) -> int:
        stack = []
        count = 1
        while 1:
            if count ** 2 <= n:
                stack.append(count**2)
            else:
                break
            count += 1
        
        dp = [999999]* (n + 1)
        dp[0] = 0
        for i in range(1,len(stack) + 1):
            add_num = stack[len(stack) - i]
            for j in range(n+1):
                if j - add_num >= 0 and dp[j-add_num] < 999999:
                    dp[j] = min(dp[j-add_num] + 1, dp[j])

        return dp[-1]
