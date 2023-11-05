#
# @lc app=leetcode.cn id=274 lang=python
#
# [274] H 指数
#

# @lc code=start
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        point1 = 0
        point2 = 0
        result = max(min(len(citations),citations[point1]-1), 0)
        while point1 <= len(citations) - 1 and citations[point1] <= len(citations) - point2:
            result = min(citations[point1],len(citations) - point2)
            while point1 < len(citations) - 1 and citations[point1] == citations[point1+1]:
                point1 += 1
            point1 +=1
            if point1 >= len(citations):
                break
            while citations[point2] < citations[point1]:
                point2 += 1
        if point1 <= len(citations) - 1:
            result = max(result,len(citations) - point2)
        return result


# @lc code=end

