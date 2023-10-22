#
# @lc app=leetcode.cn id=135 lang=python
#
# [135] 分发糖果
#

# @lc code=start
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        data = []
        candy = 0
        flag = 0
        last = 0
        for i in range(len(ratings)):
            if len(data) ==0:
                data.append(ratings[i])
                candy += 1
                last = 999999
                continue
            if ratings[i] == data[-1]:
                data =[]
                candy += 1
                data.append(ratings[i])
                last = 999999
                flag = 0
            elif ratings[i]>data[-1]:
                if flag == -1:
                    a = data[-1]
                    data = []
                    data.append(a)
                    candy += len(data) + 1
                    data.append(ratings[i])
                    flag = 1
                else:
                    flag = 1
                    candy += len(data) + 1
                    data.append(ratings[i])
            elif ratings[i]< data[-1]:
                if flag == 1:
                    last = len(data)
                    data = []
                    candy += len(data) + 1 + int(last<=len(data) + 1)
                    data.append(ratings[i])
                    flag = -1
                else:
                    flag = -1
                    candy += len(data) + 1+ int(last<=len(data) + 1)
                    data.append(ratings[i])
        return candy


# @lc code=end

