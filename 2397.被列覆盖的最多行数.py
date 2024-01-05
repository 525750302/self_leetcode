class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0])
        mask = [sum(v << j for j, v in enumerate(row)) for i, row in enumerate(matrix)]
        res, limit = 0, 1 << n
        for cur in range(1, limit):
            if cur.bit_count() != numSelect:
                continue
            t = sum((mask[j] & cur) == mask[j] for j in range(m))
            res = max(res, t)
        return res
