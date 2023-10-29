#
# @lc app=leetcode.cn id=498 lang=python
#
# [498] 对角线遍历
#

# @lc code=start
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        target = 0
        flag = 0
        result = []
        while target < len(mat) + len(mat[0]):
            if flag == 0:
                x = min(len(mat)-1, target)
                y = target - x
                while y< len(mat[0]) and y != target + 1:
                    #print(result,x,y)
                    result.append(mat[x][y])
                    x-=1
                    y+=1 

                flag = 1
            else:
                y = min(len(mat[0])-1, target)
                x = target - y
                while x < len(mat) and x != target + 1:
                    result.append(mat[x][y])
                    x+=1
                    y-=1 

                flag = 0
            
            target += 1
        
        return result
# @lc code=end

