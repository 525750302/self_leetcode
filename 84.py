class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = [0] * len(heights)
        right = [0] * len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1
            stack.append(i)
        stack.clear()
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            else:
                right[i] = len(heights)
            stack.append(i)
        max_result = 0
        for i in range(len(heights)):
            max_result = max(max_result,(right[i] - left[i]-1) * heights[i])
        return max_result

            