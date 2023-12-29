#
# @lc app=leetcode.cn id=2646 lang=python
#
# [2646] 最小化旅行的价格总和
#

# @lc code=start

class node():
    def __init__(self, val):
        self.val = val
        self.connect = []
        self.count = 0 
    def add_edge(self, child):
        self.connect.append(child)
        self.count += 1

class Solution(object):
    def minimumTotalPrice(self, n, edges, price, trips):
        """
        :type n: int
        :type edges: List[List[int]]
        :type price: List[int]
        :type trips: List[List[int]]
        :rtype: int
        """
        self.used_count = {}
        self.node_dic = {}
        self.point1 = set()
        self.point2 = set()
        for i in range(len(price)):
            self.node_dic[i] = node(price[i])
        for i in range(len(edges)):
            a = self.node_dic[edges[i][0]]
            b = self.node_dic[edges[i][1]]
            a.add_edge(edges[i][1])
            b.add_edge(edges[i][0])

        for begin, end in trips:
            self.dfs(begin, end, -1)
            print(self.used_count)
        
        sum1 = 0
        for i in range(n):
            if self.used_count.get(i, 0) >= 1:
                self.node_dic[i].val = self.used_count[i] * price[i]
            else:
                self.node_dic[i].val = 0
        return self.val_cal()
        
    
    def dfs(self, begin, end, father):
        if begin == end:
            self.used_count[begin] = 1 if self.used_count.get(begin, 0) == 0 else self.used_count[begin] + 1
            return True
        self.used_count[begin] = 1 if self.used_count.get(begin, 0) == 0 else self.used_count[begin] + 1
        for i in self.node_dic[begin].connect:
            if father != i and self.dfs(i, end, begin):
                return True
        self.used_count[begin] = self.used_count[begin] - 1
        return False

    def val_cal(self):
        self.val_dic = {}
        return min(self.val_dfs(0,0,-1) +  self.node_dic[0].val, self.val_dfs(0,1,-1) +self.node_dic[0].val //2)

    def val_dfs(self, now, state,father):
        sum = 0
        if state == 0:
            for i in self.node_dic[now].connect:
                if father != i:
                    if self.val_dic.get((i,0)) == None:
                        self.val_dic[(i,0)] = self.val_dfs(i,0,now)
                    if self.val_dic.get((i,1)) == None:
                        self.val_dic[(i,1)] = self.val_dfs(i,1,now)
                    sum += min(self.val_dic[(i,0)] + self.node_dic[i].val, self.val_dic[(i,1)] + self.node_dic[i].val // 2)
        if state == 1:
            for i in self.node_dic[now].connect:
                if father != i:
                    if self.val_dic.get((i,0)) == None:
                        self.val_dic[(i,0)] = self.val_dfs(i,0,now)
                    if self.val_dic.get((i,1)) == None:
                        self.val_dic[(i,1)] = self.val_dfs(i,1,now)
                    sum += self.val_dic[(i,0)] + self.node_dic[i].val
            
        
        return sum


# @lc code=end

