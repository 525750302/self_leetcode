def dfs(i, cur_sum):
    if i == n and cur_sum == j:
            return True
    x = 0
    for k in range(i, n):
        x = x*10 + int(s[k])
        if dfs(k+1, cur_sum + x):
            return True 
    return False

NUM_SUM = [0] * 1001
for j in range(1001):
    s = str(j**2)
    n = len(s)
    NUM_SUM[j] = NUM_SUM[j-1] + j**2 if dfs(0, 0) else NUM_SUM[j-1]

class Solution:
    def punishmentNumber(self, n: int) -> int:
        return NUM_SUM[n]