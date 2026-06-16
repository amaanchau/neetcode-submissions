class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            prefix = ""
            for i in range(len(strs[0])):
                first = strs[0][i]
                for j in range(1,len(strs)):
                    if i>=len(strs[j]) or strs[j][i]!=first:
                        return prefix
                prefix+=strs[0][i]
            return prefix

"""
1. Brute Force Solution)
loop through each word comparing the current letter to see if they are all equal.
keep a counter and if they arent equal at any point we return the current count

time, space
O(m*n) O(1) 

2. Sort the list
Input: strs = ["bat","bag","bank","band"]
-> ['bag', 'band', 'bank', 'bat']

we only need to compare the first and last word since they are sorted


time,space
O(m*nlogn)


"""