class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        print(nums)
        res = 1
        longest = 1
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i] - 1:
                longest += 1
                res = max(res,longest) 
            elif nums[i-1] == nums[i]:
                continue
            else:
                longest = 1
        return res





"""
brute force
loop through for each num see what the biggest consecutive list we can build is

O(n^2)


we can sort the list 
then take one pass and keep track of the largest consecutive list

O(nlogn)

can we do this in one pass? O(n)


nums = [2,20,4,10,3,4,5]

"""