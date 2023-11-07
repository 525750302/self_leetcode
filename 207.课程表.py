#
# @lc app=leetcode.cn id=207 lang=python
#
# [207] 课程表
#

# @lc code=start
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        group = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            group[i].append(j)
        visited = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            if not self.dfs(group, visited, i):
                return False
        return True

    def dfs(self, group, visited, i):  
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for j in group[i]:
            if not self.dfs(group, visited, j):
                return False
        visited[i] = 1
        return True
# @lc code=end

