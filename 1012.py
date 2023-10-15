class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        return n - self.cal(n)
    
    def cal(self,n):
        nums = []
        while n:
            nums.append(n%10)
            n = int(n/10)
        
        return self.dp(len(nums)-1,0,True,True,nums)
    
    def dp(self,position, mask, lead, limit,nums):
        if position < 0:
            return int(lead)^1
        up = nums[position] if limit else 9
        ans = 0
        repeat = -1
        for i in range(up + 1):
            if mask >> i &1:
                continue
            if i == 0 and lead:
                ans += self.dp(position -1, mask,lead,limit and i == up,nums)
            elif limit == False and i != up:
                if repeat == -1:
                    repeat= self.dp(position-1, mask|1<<i, False, limit and i == up,nums)
                    ans += repeat
                else:
                    ans += repeat
                
            else:
                ans += self.dp(position-1, mask|1<<i, False, limit and i == up,nums)
        
        return ans
       
