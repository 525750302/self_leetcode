class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        new_station = []
        new_station.append(0)
        for i in range(len(stations)):
            new_station.append(new_station[i] + stations[i])
        
        min_power = 99999999999
        power = []
        for i in range(len(stations)):
            power.append(new_station[min(len(stations),i+r + 1)] - new_station[max(0,i-r)])
            min_power = min(min_power,power[-1])
        left = min_power
        right = k + min_power + 1
        while(left<right):
            mid = int((left+right)/2)
            if self.check(mid,power,k,r) == False:
                right = mid
            else:
                left = mid + 1
        
        return right-1
    
    def check(self,target,power,max_station,r):
        diff = []
        diff.append(power[0])
        for i in range(1,len(power)):
            diff.append(power[i]-power[i-1])
        diff.append(0)
        sum = 0
        used = 0
        for i in range(len(diff)-1):
            sum = sum + diff[i]
            if sum <target:
                add_staion = target - sum
                sum = sum + add_staion
                used = add_staion + used
                diff[min(i+2*r +1,len(diff)-1)] = diff[min(i+2*r + 1,len(diff)-1)] - add_staion
            if used > max_station:
                return False
        
        return True
