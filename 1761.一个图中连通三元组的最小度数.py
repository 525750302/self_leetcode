#
# @lc app=leetcode.cn id=1761 lang=python
#
# [1761] 一个图中连通三元组的最小度数
#

# @lc code=start
class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        dic = {}
        degree = [[] for i in range(n+1)]
        for i, j in edges:
            dic[(i,j)] = 1
            dic[(j,i)] = 1
            degree[i].append(j)
            degree[j].append(i)
        length = [0] * (n+1)
        for i in range(1,n+1):
            length[i] = len(degree[i])

        min_val = 10**9
        visted = {}
        for u, v in edges:
            i = min(u,v)
            j = max(u,v)
            for k in degree[i]:
                if k <i or k <j or dic.get((j,k),0) == 0:
                    continue
                min_val = min(min_val, length[i] + length[j] + length[k] - 6)
        return -1 if min_val == 10**9 else min_val

# @lc code=end

