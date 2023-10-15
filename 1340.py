class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        check_flag = [0] * len(arr)
        flag = 0
        dp = [1]*len(arr)

        while flag < len(arr):
            for i in range(len(arr)):
                if check_flag[i] == 1:
                    continue
                
                left = max(0,i-d)
                right = min(len(arr)-1 , i+d)
                leap_able = 0
                for j in range(i-1,left-1,-1):
                    if arr[j]>= arr[i]:
                        break
                    if leap_able == 0 and check_flag[j] == 0:
                        leap_able = 1
                        break
                    dp[i] = max(dp[i],1+dp[j])
                for j in range(i+1,right+1):
                    if arr[j]>= arr[i]:
                        break
                    if leap_able == 0 and check_flag[j] == 0:
                        leap_able = 1
                        break
                    dp[i] = max(dp[i],1+dp[j])
                if leap_able == 0:
                    check_flag[i] = 1
                    flag = flag + 1
        return max(dp)
