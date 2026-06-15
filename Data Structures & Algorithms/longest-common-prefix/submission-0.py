class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sortedStrs = sorted(strs)
        res = ""
        first = sortedStrs[0]
        last = sortedStrs[len(sortedStrs)-1]
        fp, lp = 0, 0
        while fp<len(first) and lp<len(last):
            if first[fp] != last[lp]:
                return res
            res+=first[lp]
            fp += 1
            lp += 1
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