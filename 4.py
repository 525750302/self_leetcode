class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sum = len(nums1) + len(nums2)
        if sum%2 == 0:
            flag = 0
        else:
            flag = 1
        
        def getKthElement(k):
            nonlocal nums1,nums2
            start_point1 = 0
            start_point2 = 0
            print(k)
            while True:
                if start_point1 == len(nums1):
                    return nums2[start_point2 + k -1]
                if start_point2 == len(nums2):
                    return nums1[start_point1 + k -1]
                if k==1:
                    return min(nums1[start_point1],nums2[start_point2])
                new_point_location1 = min(start_point1 + int(k/2) - 1,len(nums1)-1)
                new_point_location2 = min(start_point2 + int(k/2) - 1,len(nums2)-1)
                point1 = nums1[new_point_location1]
                point2 = nums2[new_point_location2]
                if point1 <= point2:
                    k -= new_point_location1 - start_point1 + 1
                    start_point1 = new_point_location1 + 1
                else:
                    k -= new_point_location2 - start_point2 + 1
                    start_point2 = new_point_location2 + 1
        
        if flag == 1:
            return getKthElement(int((sum + 1) /2))
        else:
            return (getKthElement(int(sum /2)) + getKthElement(int(sum/2)+1))/2