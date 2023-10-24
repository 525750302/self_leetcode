#
# @lc app=leetcode.cn id=315 lang=python
#
# [315] 计算右侧小于当前元素的个数
#

# @lc code=start

class Solution(object):
    def lowbit(self,x):
        return (x)&(-x)

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) + 1
        self.MAXN = n
        self.tree = [0] * n
        self.dic = {}
        sorted = []
        for i in range(n-1):
            sorted.append(nums[i])
        sorted.sort()
        for i in range(n-1):
            self.dic[sorted[i]] = i + 1
        
        result = [0] * (n-1)
        for i in range(n-2,-1,-1):
            result[i] = (self.query(self.dic[nums[i]]))
            self.update(self.dic[nums[i]],1)
        
        return result

    def update(self,i, x):
        pos = i
        while pos < self.MAXN:
            self.tree[pos] += x
            pos  += self.lowbit(pos)  
        
    def query(self,n):
        ans = 0
        pos = n - 1
        while pos:
            ans += self.tree[pos]
            pos -= self.lowbit(pos)
        return ans


# @lc code=end

input = [5,2,6,1]
a = Solution()
print(a.countSmaller(input))

