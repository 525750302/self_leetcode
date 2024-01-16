class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def dfs(num, i, j, limit) -> int:
            if j > max_sum:
                return 0
            if i == -1:
                return j >= min_sum
            if not limit and d[i][j] != -1:
                return d[i][j]
            res = 0
            up = ord(num[i]) - ord('0') if limit > 0 else 9
            for x in range(up + 1):
                res = (res + dfs(num, i - 1, j + x, limit and x == up)) % MOD
            if not limit:
                d[i][j] = res
            return res

        def get(num):
            num = num[::-1]
            return dfs(num, len(num) - 1, 0, True)

        # 求解 num - 1，先把最后一个非 0 字符减去 1，再把后面的 0 字符变为 9
        def sub(num):
            i = len(num) - 1
            arr = list(num)
            while arr[i] == '0':
                i -= 1
            arr[i] = chr(ord(arr[i]) - 1)
            i += 1
            while i < len(num):
                arr[i] = '9'
                i += 1
            return ''.join(arr)

        N, M = 23, 401
        MOD = 10**9 + 7
        d = [[-1] * M for _ in range(N)]
        return (get(num2) - get(sub(num1)) + MOD) % MOD

