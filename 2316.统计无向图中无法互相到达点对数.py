#
# @lc app=leetcode.cn id=2316 lang=python
#
# [2316] 统计无向图中无法互相到达点对数
#

# @lc code=start
class Solution(object):
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            else:
                self.parent[px] = py
                if self.rank[px] == self.rank[py]:
                    self.rank[py] += 1

    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.parent = list(range(n))
        self.rank = [0] * n

        for i , j in edges:
            a = self.find(i)
            b = self.find(j)
            if a != b:
                self.union(a,b)
        for i in range(len(self.parent)):
            self.find(i)
        dic = {}
        for i in range(len(self.parent)):
            dic[self.parent[i]] = dic.get(self.parent[i],0)+1

        if len(dic.keys()) == 1:
            return 0
        res = 0
        for i in dic:
            if dic[i] >= 1:
                res += (dic[i] * (n - dic[i]))
        res = res // 2
        return res


# @lc code=end

