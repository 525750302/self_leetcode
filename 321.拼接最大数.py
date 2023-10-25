#
# @lc app=leetcode.cn id=321 lang=python
#
# [321] 拼接最大数
#

# @lc code=start
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_list = [0] * k
        for i in range(k+1):
            if len(nums1) < i or len(nums2) < k- i:
                continue
            list1 = self.creatlist(nums1,i)
            list2 = self.creatlist(nums2,k - i)
            result = self.merge(list1,list2)
            if self.compare(result,max_list)> 0:
                max_list = result
        
        return max_list
    
    def creatlist(self,line,num):
        if num == 0:
            return []
        stack = []
        for i in range(len(line)):
            if len(stack) == 0:
                stack.append(line[i])
                continue
            while len(stack) > 0 and stack[-1] < line[i] and len(stack) + len(line) - i >num:
                stack.pop(-1)
            stack.append(line[i])
        result = []
        for i in range(num):
            result.append(stack[i])
        return result
    
    def merge(self,line1,line2):
        p1 = 0
        p2 = 0
        result = []
        check1 = 0
        check2 = 0
        while p1 < len(line1) or p2 < len(line2):
            if p2 >= len(line2) or self.compare(line1[p1::],line2[p2::]) > 0:
                result.append(line1[p1])
                p1 += 1
            else:
                result.append(line2[p2])
                p2 += 1

        return result
    
    def compare(self,line1,line2):
        x, y = len(line1), len(line2)
        p1 = 0
        p2 = 0
        while p1 < x and p2 < y:
            difference = line1[p1] - line2[p2]
            if difference != 0:
                return difference
            p1 += 1
            p2 += 1
        
        return (x - p1) - (y - p2)

# @lc code=end

