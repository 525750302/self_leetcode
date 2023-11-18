class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_point = 0
        left_height = height[left_point]
        right_point = len(height) - 1
        right_height = height[right_point]
        sum = 0
        while(left_point != right_point):
            if right_height >= left_height:
                left_point = left_point + 1
                sum = sum + max(0,min(left_height,right_height) - height[left_point])
                if height[left_point]> left_height:
                    left_height = height[left_point]
            else:
                right_point = right_point - 1
                sum = sum + max(0,min(left_height,right_height) - height[right_point])
                if height[right_point]> right_height:
                    right_height = height[right_point]
            

        return sum

a = Solution()
input = [0,1,0,2,1,0,1,3,2,1,2,1]
result = a.trap(input)
print(result)