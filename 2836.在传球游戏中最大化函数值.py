#
# @lc app=leetcode.cn id=2836 lang=python
#
# [2836] 在传球游戏中最大化函数值
#

# @lc code=start
class Solution(object):
    def getMaxFunctionValue(self, receiver, k):
        """
        :type receiver: List[int]
        :type k: int
        :rtype: int
        """
        target = [[0] * 36 for i in range(len(receiver))]
        path_sum = [[0] * 36 for i in range(len(receiver))]
        time = 0
        copy_k = k
        while copy_k > 0:
            time += 1
            copy_k = copy_k // 2
        max_val = 0
        for i in range(len(receiver)):
            target[i][0] = receiver[i]
            path_sum[i][0] = receiver[i]
            max_val = max(max_val, path_sum[i][0])

        for i in range(1,time):
            for j in range(len(receiver)):
                target[j][i] = target[target[j][i - 1]][i-1]
                path_sum[j][i] = path_sum[j][i - 1] + path_sum[target[j][i - 1]][i-1]
        #print(path_sum)
        for i in range(len(receiver)):
            copy_k = k
            now_target = i
            now_path = 0
            count = 0
            while copy_k> 0:
                if copy_k % 2 == 1:
                    now_path += path_sum[now_target][count]
                    now_target = target[now_target][count]
                count += 1
                copy_k = copy_k //2
            max_val = max(max_val, now_path + i)

        return max_val

# @lc code=end

