class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxCount = 0
        for num in numsSet:
            if num - 1 not in numsSet:
                count = 0
                x = num
                while x in numsSet:
                    count += 1
                    x += 1
                maxCount = max(maxCount, count)

        return maxCount
"""

Sorting Approach - O(nlogn) time complexity and O(1) space complexity
Define consec to 0 
One approach is to sort first, 
then keep track of longest sequences, 
update consec variable as soon as a longer sequence appear, 
return consec variable

You must write an algorithm that runs in O(n) time.

Alternate Solution???

Intialize a set
convertt nums to set
iterate throuhg set

maxCount = 1
for num in set:
    count = 1
    x = num
    while x in set:
        count+=1
        x+=1
    maxCount = Max(maxCount, count)

return maxCOunt


Instead of starting from every number, 
only start counting when the number is the start of a sequence — 
meaning num - 1 is not in the set.


"""