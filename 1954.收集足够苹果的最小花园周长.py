class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        left, right = 1, 100000
        res = 1
        while left <= right:
            mid = (right - left) // 2 + left
            total = 2 * mid * (mid + 1) * (2 * mid + 1)
            if total >= neededApples:
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        return res * 8