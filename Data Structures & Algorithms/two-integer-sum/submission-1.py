class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target-num in seen:
                return [seen[target-num], i]
            seen[num] = i



"""
Problem:
    return indexes of nums that add up to the target
        smaller index first
    assume the target exists always and there is exctly two numbers that add up to it

Approach 1: Brute Force
iterate through nums
    for each num, iterate through the the rest of the nums
        see if any of the combinations add up to the target
        if yes return the two indexes
        else move to the next num

Time Complexity: O(n^2)
Space Complexity: O(1)

Approach 2: 
iterate through nums
for each num keep a store of the target minus the num (and its index)
if that number appears in the rest of the list we have a match

Time Complexity: O(n)
Space Complexity: O(n)

Approach 3: 
iterate through nums
for each num keep a seen numbers (and its index)
for each new num if the target minus num is in the hashmap of seen nums return the indexes

Time Complexity: O(n)
Space Complexity: O(n)


"""
