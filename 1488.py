class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        result = []
        tank_dic = {}

        rain_dic = []
        for i in range(len(rains)):
            if rains[i]>0:
                if tank_dic.get(rains[i])!= None:
                    rain_dic.append(rains[i])
                else:
                    tank_dic[rains[i]] = 1

        tank_dic.clear()
        for i in range(len(rains)):
            if tank_dic.get(rains[i])!= None:
                if tank_dic[rains[i]]> 0:
                    return []
            if rains[i]>0:
                tank_dic[rains[i]] = 1
                result.append(-1)
                continue
            if len(tank_dic) == 0:
                result.append(1)
                continue
            if len(rain_dic) == 0:
                result.append(1)
                continue
            target = 0
            while tank_dic.get(rain_dic[target]) == None or tank_dic[rain_dic[target]] == 0:
                target = target + 1
                if target == len(rain_dic):
                    result.append(1)
                    break
            if target == len(rain_dic):
                continue
            tank_dic[rain_dic[target]] = 0
            result.append(rain_dic[target])
            del rain_dic[target]
        return result

