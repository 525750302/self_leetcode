class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        i = 0
        res = list(dominoes)
        pre = 'L'
        while i < n:
            j = i
            while j < n and dominoes[j] == '.': 
                j += 1
            right = dominoes[j] if j < n else 'R'
            if pre == right:
                while i < j:
                    res[i] = right
                    i += 1
            elif pre == 'R' and right == 'L':
                k = j - 1
                while i < k:
                    res[i] = pre
                    res[k] = right
                    i += 1
                    k -= 1
            pre = right
            i = j + 1
        return "".join(res)