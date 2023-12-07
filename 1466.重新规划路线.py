#
# @lc app=leetcode.cn id=1466 lang=python
#
# [1466] 重新规划路线
#

# @lc code=start
class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        g = [[] for _ in range(n)]
        re = [[] for _ in range(n)]
        for a, b in connections:
            g[a].append(b)
            re[b].append(a)
        visited = [False] * n
        res = 0

        def dfs(i):
            nonlocal res
            visited[i] = True
            for j in re[i]:
                if not visited[j]:
                    dfs(j)
            for j in g[i]:
                if not visited[j]:
                    res += 1
                    re[i] = j
                    dfs(j)


        dfs(0)
        return res
# @lc code=end

