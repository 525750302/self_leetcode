class Solution:
    def racecar(self, target: int) -> int:
        hop = 0
        speed = 1
        t = 1
        dp1 = [99999] * (target + 1)
        dp1[0] = 0
        while hop + speed <= target:
            hop = hop + speed
            speed = speed * 2
            dp1[hop] = t
            t = t + 1
        def cal(target):
            nonlocal dp1
            step = 1
            t = 1
            while (step <= 2*target):
                if step == target:
                    dp1[target] = t
                elif step > target:
                    dp1[target] = min(dp1[target],t+1+dp1[step - target])
                else:
                    for backward in range(t):
                        backward_distance = 1<<backward
                        backward_distance = backward_distance - 1
                        dp1[target] = min(dp1[target],t+1+backward+1+dp1[target - step + backward_distance])
                                
                step = step<<1
                step = step + 1
                t = t + 1
        for i in range(1,target+1):
            cal(i)
        print(dp1)

        return dp1[target]