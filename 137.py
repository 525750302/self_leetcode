class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check_dic = {}
        for i in range(len(nums)):
            if check_dic.get(nums[i])!= None and check_dic.get(nums[i])>1:
                continue
            if check_dic.get(nums[i])== None:
                check_dic[nums[i]] = 1
            elif check_dic.get(nums[i]) == 1:
                check_dic[nums[i]] = 2

        for i in check_dic.keys():
            if check_dic[i] == 1:
                return i
