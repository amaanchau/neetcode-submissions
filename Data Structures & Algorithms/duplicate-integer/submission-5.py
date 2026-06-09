class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for num in nums:
            if num in numsSet:
                return True
            else:
                numsSet.add(num)
        return False


"""
Have a storage container of nums (set)
go through each num in nums:
    check if that number is in our storage container (set)
    if it is then we know theres a dupe, so return true
    else then just add it to the storage container

Time complexity: iterating one time over the nums list so O(N)
storage complexity: worst case will store all nums in nums so O(N) also
"""


    