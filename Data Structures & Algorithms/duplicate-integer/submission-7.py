class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appearsInNums = set()
        for num in nums:
            if num in appearsInNums:
                return True
            else:
                appearsInNums.add(num)
        return False


"""
1. Brute Force
- iterate through the nums
    - for each num iterate the rest of the list and if a dupe is found return true
- if loop completes, that means no dupes were found so we return false

Time + Space Complexity
O(n^2), O(1)

2. Hashmap
- initialize an empty hashmap
- iterate through the nums
    - for each num we throw it in the hashmap with a value of true
    - if the num is already in the hashmap then we just return True
- if loop completes, that means no dupes were found so we return false

Time + Space Complexity
O(n), O(n)

3. Set
- initialize an empty set
- iterate through the nums
    - for each num if its in the set return true, else add it to the set
- if loop completes, that means no dupes were found so we return false

Time + Space Complexity
O(n), O(n)

"""