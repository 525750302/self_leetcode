#
# @lc app=leetcode.cn id=307 lang=python
#
# [307] 区域和检索 - 数组可修改
#

# @lc code=start
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.tree = {}
        self.build(0, len(nums) - 1, 1)

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.nums[index] = val
        self.update_val(index, val, 0, len(self.nums) - 1, 1)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        #print(self.tree)
        return self.search(left, right, 0, len(self.nums) - 1, 1)

    def update_val(self,index, val, left, right, root):
        if left == right:
            self.tree[root] = val
            return
        m = left + ((right - left) >> 1)
        if index <= m:
            self.update_val(index, val, left, m, root * 2)
        else:
            self.update_val(index, val, m + 1, right, root * 2 + 1)
        self.tree[root] = self.tree[root * 2] + self.tree[root * 2 + 1]


    def search(self,l, r, s, t, p):
        # [l, r] 为查询区间, [s, t] 为当前节点包含的区间, p 为当前节点的编号
        if l <= s and t <= r:
            return self.tree[p] # 当前区间为询问区间的子集时直接返回当前区间的和
        m = s + ((t - s) >> 1); sum = 0
        if l <= m:
            sum = sum + self.search(l, r, s, m, p * 2)
        # 如果左儿子代表的区间 [s, m] 与询问区间有交集, 则递归查询左儿子
        if r > m:
            sum = sum + self.search(l, r, m + 1, t, p * 2 + 1)
        # 如果右儿子代表的区间 [m + 1, t] 与询问区间有交集, 则递归查询右儿子
        return sum

    def build(self,s, t, p):
        # 对 [s,t] 区间建立线段树,当前根的编号为 p
        if s == t:
            self.tree[p] = self.nums[s]
            return
        m = s + ((t - s) >> 1)
        # 移位运算符的优先级小于加减法，所以加上括号
        # 如果写成 (s + t) >> 1 可能会超出 int 范围
        self.build(s, m, p * 2); self.build(m + 1, t, p * 2 + 1)
        # 递归对左右区间建树
        self.tree[p] = self.tree[p * 2] + self.tree[(p * 2) + 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end

