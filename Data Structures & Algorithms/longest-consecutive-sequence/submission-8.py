class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest=0
        for i in range (len(nums)):
            if nums[i]-1 not in numsSet:
                cur = 1
                while nums[i]+cur in numsSet:
                    cur+=1
                longest = max(longest,cur)
        return longest




"""
brute force
loop through for each num see what the biggest consecutive list we can build is

O(n^2)


we can sort the list 
then take one pass and keep track of the largest consecutive list

O(nlogn)

can we do this in one pass? O(n)


nums = [2,20,4,10,3,4,5]

(1,2,3,4,5,6,45,400,7)

"""
