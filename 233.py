class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """

        max_num = 0
        copy = n 
        while copy > 0:
            copy = int(copy / 10)
            max_num = max_num + 1
        
        return self.cal_1(n,max_num)

    
    def cal_1(self,n,num_location):
        if n < 10 and n > 0:
            return 1
        if n == 0:
            return 0
        
        dev = 1
        for i in range(num_location - 1):
            dev = dev * 10

        copy = n
        now_num = int(copy/dev) % 10
        result = 0
        if now_num == 1:
            result = result + int(copy % dev) + 1
            add_result = self.cal_1(copy % dev,num_location - 1)
            result = result + add_result
            add_result = self.cal_1(dev-1,num_location - 1)
            result = result + add_result
        else:
            add_result = self.cal_1(copy % dev,num_location - 1)
            result = result + add_result
            add_result = self.cal_1(dev-1,num_location - 1)
            for i in range(2,now_num):
                result = result + add_result
            if now_num > 0:
                result = result + dev
                result = result + add_result
                result = result + add_result
        
        return result



