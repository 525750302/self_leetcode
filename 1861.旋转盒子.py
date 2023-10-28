#
# @lc app=leetcode.cn id=1861 lang=python
#
# [1861] 旋转盒子
#

# @lc code=start
class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        col = len(box)
        row = len(box[0])
        self.new_box = [["."] * col for i in range(row)]
        for i in range(col):
            for j in range(row):
                self.new_box[j][col -1 - i] = box[i][j]
        
        for now_location in range(col):
            point = row-1
            while point >=0 and (self.new_box[point][now_location] != "."):
                point -= 1
            if point <0:
                continue
            i = point
            while i > -1:
                if self.new_box[i][now_location] == "#":
                    self.swap(i,now_location,point)
                    point -= 1
                elif self.new_box[i][now_location] == "*":
                    point = i
                    while point >=0 and (self.new_box[point][now_location] != "."):
                        point -= 1
                        i -= 1
                i -= 1
        
        return self.new_box

    
    def swap(self,i,now_location,point):
        a = self.new_box[i][now_location]
        self.new_box[i][now_location] = self.new_box[point][now_location]
        self.new_box[point][now_location] = a

# @lc code=end

