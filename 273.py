class Solution(object):
    ten = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    Ten_to_Nineteen = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    Ten_times = ["Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        word = ""
        if num >= 1000000000:
            add_word = self.three_digit(int(num/1000000000))
            if add_word != "Zero":
                if len(word)>0:
                    word = word + " " + add_word + " Billion"
                else:
                    word = add_word + " Billion"
        if num >= 1000000:
            add_word = self.three_digit(int(num/1000000)%1000)
            if add_word != "Zero":
                if len(word)>0:
                    word = word + " " + add_word + " Million"
                else:
                    word = add_word + " Million"
        if num >= 1000:
            add_word = self.three_digit(int(num/1000)%1000)
            if add_word != "Zero":
                if len(word)>0:
                    word = word + " " + add_word + " Thousand"
                else:
                    word = add_word + " Thousand"
        
        add_word = self.three_digit(int(num/1)%1000)
        if add_word == "Zero" and num >= 1000:
            word = word
        else:
            if len(word)>0:
                word = word + " " + add_word
            else:
                word = add_word
        
        return word




    def three_digit(self,num):
        word = ""
        if num >= 100:
            word = word + self.ten[int(num/100)] + " Hundred"
        
        if num%100 >= 0:
            add_word = self.two_digit(num%100)
            if num >= 100 and add_word == "Zero":
                return word
            if len(word)>0:
                word = word + " " + add_word
            else:
                word = add_word
        return word

    
    def two_digit(self,num):
        if num < 10:
            return self.ten[num]
        if num < 20:
            return self.Ten_to_Nineteen[num - 10]
        
        word = self.Ten_times[int(num/10) - 2]
        if num > 20 and num % 10 != 0:
            word = word + " " + self.ten[num % 10]
        
        return word
