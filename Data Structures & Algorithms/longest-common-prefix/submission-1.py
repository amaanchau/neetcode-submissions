class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sortedStrs = sorted(strs)
        first, last = sortedStrs[0], sortedStrs[-1]
        res = ""
        
        # A single loop index handles both strings simultaneously
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return res
            res += first[i]
            
        return res        
"""
1. Brute Force Solution)
loop through each word comparing the current letter to see if they are all equal.
keep a counter and if they arent equal at any point we return the current count

time, space
O(n^2) O(1) 

2. Sort the list
Input: strs = ["bat","bag","bank","band"]
-> ['bag', 'band', 'bank', 'bat']

we only need to compare the first and last word since they are sorted


3. One pass?



"""