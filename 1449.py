class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [[0,""]for i in range(target + 1)]
        dp[target][0] = 1
        dp[target][1] = "0"
        for i in range(len(cost)):
            if cost[i] > target:
                continue
            dp[cost[i]][0] = 1
            dp[cost[i]][1] = str(i + 1)
        for i in range(target):
            for j in range(len(cost)):
                if cost[j] > target:
                    continue
                if i >0 and dp[i][0] == 0:
                    continue
                if i + cost[j] > target:
                    continue
                add_t = i + cost[j]
                if dp[i][0] + 1 < dp[add_t][0]:
                    continue
                if dp[i][0] + 1 > dp[add_t][0]:
                    dp[add_t][0] = dp[i][0] + 1
                    dp[add_t][1] = dp[i][1] + str(j+1)
                    continue
                new_str = dp[i][1] + str(j+1)
                if new_str>dp[add_t][1]:
                    dp[add_t][1] = dp[i][1] + str(j+1)
        
        return dp[target][1]