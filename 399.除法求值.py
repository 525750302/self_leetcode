#
# @lc app=leetcode.cn id=399 lang=python
#
# [399] 除法求值
#

# @lc code=start
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dic = {}
        keys_set = set()
        for i, (x, y) in enumerate(equations):
            dic[(x, y)] = values[i]
            dic[(y, x)] = 1.0 / values[i]
            keys_set.add(x)
            keys_set.add(y)
        res = [-1.000] * len(queries)
        for i, (x, y) in enumerate(queries):
            if x not in keys_set or y not in keys_set:
                res[i] = -1.0
            else:
                res[i] = self.dfs(x, y, dic, set())
        return res
    def dfs(self, x, y, dic, visited):
        if (x, y) in visited:
            return -1.0
        visited.add((x, y))
        if x == y:
            return 1.0
        for i in dic.keys():
            if i[0] == x:
                flag = self.dfs(i[1], y, dic, visited)
                if flag != -1.0:
                    return dic[i] * flag
        return -1.0
                    
# @lc code=end

