#
# @lc app=leetcode.cn id=447 lang=python
#
# [447] 回旋镖的数量
#

# @lc code=start
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)<3:
            return 0
        
        res = 0
        for i in range(len(points)):
            dic = {}
            for j in range(len(points)):
                if i==j:
                    continue
                dic[(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2] = 1 if dic.get((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)!=None else dic[(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2] + 1
            for k in dic:
                res += dic[k]*(dic[k]-1)
        return res
            
    
# @lc code=end

