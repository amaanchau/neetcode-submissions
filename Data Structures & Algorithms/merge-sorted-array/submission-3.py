class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = n+1
        for i in range(m,len(nums1)):
            nums1[i] = nums2[n-j]
            j-=1
        nums1.sort()


        

"""
Input: nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2
               [1,2,10,20,20,40]

brute force:
go through nums 2:



"""