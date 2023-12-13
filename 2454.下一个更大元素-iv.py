class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        q = []
        
        for i in range(len(nums)):
            while len(q) and q[0][0] < nums[i]:
                res[q[0][1]] = nums[i]
                heappop(q)
            while len(stack) and nums[stack[-1]] < nums[i]:
                heappush(q, (nums[stack[-1]], stack[-1]))
                stack.pop()
            stack.append(i)

        return res
