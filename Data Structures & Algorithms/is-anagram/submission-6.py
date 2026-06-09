class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap, tMap = {}, {}

        for i in range(len(s)):
            sMap[s[i]] =  sMap.get(s[i],0)+1
            tMap[t[i]] =  tMap.get(t[i],0)+1

        if sMap == tMap:
            return True
        return False

"""
1) Brute Force
len of the strings must be equal
iterate through each letter in s
    for each letter loop through t and if that letter is found remove it
    if not return False
after the loop if there are any letters left in t return False, else return True

Time + Space:
O(n^2), O(n)

2) Hash map/ Freq Counter
len of the strings must be equal
create a map of s and t to hold character counts
iterate through one of them (since they are the same length we are technically iterating through both)
    - for each char, if its not in the map, add it with a value of 1
    - if its in the map, add 1 to its value
after loop is complete, compare the maps together
if equal then true else false

Time + Space:
O(n), 2*O(n) -> O(n)

"""