#
# @lc app=leetcode.cn id=690 lang=python
#
# [690] 员工的重要性
#

# @lc code=start
"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        dic = {}
        for i in employees:
            dic[i.id] = i
        self.visited = set()
        return self.dfs(dic, id)

    def dfs(self,dic, id):
        if id in self.visited:
            return 0
        self.visited.add(id)
        res = dic[id].importance
        for i in dic[id].subordinates:
            res += self.dfs(dic, i)
        return res
        
# @lc code=end

