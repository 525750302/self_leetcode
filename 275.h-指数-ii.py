#
# @lc app=leetcode.cn id=275 lang=python
#
# [275] H 指数 II
#

# @lc code=start
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        right = max(citations)
        left = min(citations)
        if right == 0 :
            return 0
        if len(citations) == 1:
            return 1
        citations.sort()
        point = len(citations) - 1
        while left < right:
            mid = (left + right + 1) // 2
            while point > 0 and citations[point] >= mid:
                point -= 1
            while point < len(citations) and citations[point] < mid:
                point += 1
            if len(citations) - point >= mid:
                left = mid
            else:
                right = mid - 1
        
        return min(left,max(citations), len(citations))

            
# @lc code=end

