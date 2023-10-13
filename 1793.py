class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        min_value = nums[k]
        length = 1
        max_result = min_value * length
        pre = nums[:k]
        pro = nums[k+1:]
        count1 = k-1
        count2 = 0
        while length < len(nums):
            if count1 >= 0:
                while count1 >= 0 and pre[count1] >= min_value:
                    count1 -= 1
                    length += 1
                    if count1 <= -1:
                        break
            if count2 < len(pro):
                while count2 <= len(pro)-1 and pro[count2] >= min_value:
                    count2 += 1
                    length += 1
                    if count2 >= len(pro):
                        break
            max_result = max(min_value * length, max_result)
            if count1 <= 0:
                left = -1
            else:
                left = pre[count1]

            if count2 >= len(pro)-1:
                right = -1
            else:
                right = pro[count2]
            
            if left > right:
                min_value = min(min_value,left)
                count1 -= 1
            if left <= right:
                min_value = min(min_value,right)
                count2 += 1
            length += 1
        
        return max_result


