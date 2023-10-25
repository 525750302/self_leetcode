#
# @lc app=leetcode.cn id=327 lang=python
#
# [327] 区间和的个数
#

# @lc code=start
from sortedcontainers import SortedSet
class Solution(object):
    def lowbit(self,x):
        return (x)&(-x)
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        self.q = []
        count1 = 0
        
        sum = 0
        presum = [0]
        for i in range(len(nums)):
            sum += nums[i]
            presum.append(sum)
        all_num = SortedSet()
        for i in presum:
            all_num.add(i)
            all_num.add(i-lower)
            all_num.add(i - upper)

        dic = {}
        count = 0
        for i in all_num:
            dic[i] = count
            count += 1
        n = len(dic) + 1
        self.MAXN = n
        self.tree = [0] * n
        result = 0
        for i in presum:
            left = dic[i - upper]
            right = dic[i-lower]
            result += self.query(right+1) - self.query(left)
            self.update(dic[i]+1,1)

        return result

    def update(self,i, x):
        pos = i
        while pos < self.MAXN:
            self.tree[pos] += x
            pos  += self.lowbit(pos)  
        
    def query(self,n):
        ans = 0
        pos = n 
        while pos>0:
            ans += self.tree[pos]
            pos -= self.lowbit(pos)
        return ans
    
    def sum(self,i,j):
        return self.q[j] - self.q[i]
# @lc code=end

