#
# @lc app=leetcode.cn id=2336 lang=python
#
# [2336] 无限集中的最小数字
#

# @lc code=start
class SmallestInfiniteSet(object):

    def __init__(self):
        self.poped_stack = []
        self.pop_target = [1]


    def popSmallest(self):
        """
        :rtype: int
        """
        Target = self.pop_target.pop(0)
        self.poped_stack.append(Target)
        self.poped_stack.sort()
        if self.pop_target == []:
            self.pop_target.append(self.poped_stack[-1] + 1)
        return Target


    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.poped_stack:
            return None
        else:
            self.poped_stack.remove(num)
            self.pop_target.append(num)
            self.pop_target.sort()



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end

