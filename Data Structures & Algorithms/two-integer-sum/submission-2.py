class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookingFor = {}
        for i, num in enumerate(nums):
            if target-num in lookingFor:
                return [lookingFor[target-num],i]
            lookingFor[num] = i
        
"""
1) Brute Force
iterate through each int in the nums:
    - for each int, iterate through the rest of the list's ints
        - if the sum of the two equal the target, we can return a list of the index's

Time, Space
O(n^2), O(1)

2) Single Pass Hashmap
iterate through each int in the nums:
    - for each num lets save the target - int -> index in a hashmap
        now if we find any num in the keys of the hashmap, return the [the index from the hasmap, current index]

Time, Space
O(n), O(n)

3) Sorting Method
before we sort the nums lets save the value, index of each part of nums in a list
sort the nums
define a left and right pointer initialized at beginning and end of list
create a loop while l<r or until we find a match:
    - for each pair, see if the same is equal to the target
        - if bigger we move the right pointer left
        - if smaller we move the left pointer right
    - once we find a match we need to go through the index array we saved in the beginning
        - return the first two index's

Time, Space
O(nlogn), O(n)
"""