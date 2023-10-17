
import queue
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        save_data = deque()
        save_data.clear()
        save_data.append(nums[0])
        result = []
        for i in range(1,k):
            target = nums[i]
            while len(save_data)>0 and target > save_data[-1]:
                save_data.pop()
            save_data.append(target)
        result.append(save_data[0])
        for j in range(k,len(nums)):
            target = nums[j-k]
            if target == save_data[0]:
                save_data.popleft()
            target = nums[j]
            while len(save_data)>0 and target > save_data[-1]:
                save_data.pop()
            save_data.append(target)
            result.append(save_data[0])
        return result
            
            