
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for i,row in enumerate(nums):
            for j,c in enumerate(row):
                ans.append([i+j, j, c])
        ans.sort()
        return [c[2] for c in ans]
