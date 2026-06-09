class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] =  countS.get(s[i],0)+1
            countT[t[i]] =  countT.get(t[i],0)+1

        return countS == countT

"""
1) Brute Force
len of the strings must be equal
iterate through each letter in s
    for each letter loop through t and if that letter is found remove it
    if not return False
after the loop if there are any letters left in t return False, else return True

Time + Space:
O(n^2), O(n)

2) Hash map/ Freq Counter (Winner)
len of the strings must be equal
create a map of s and t to hold character counts
iterate through one of them (since they are the same length we are technically iterating through both)
    - for each char, if its not in the map, add it with a value of 1
    - if its in the map, add 1 to its value
after loop is complete, compare the maps together
if equal then true else false

Time + Space:
O(n), 2*O(n) -> O(n)

3) Sorting
len of the strings must be equal
sort each one. If they are equal then its True, else False

Time + Space:
O(nlogn), O(1)

4) Ord
len of the strings must be equal
define a list of 26 representing the 26 letters in the alphabet all initialized at count 0
iterate through one of them (since they are the same length we are technically iterating through both)
    - for s, for each char increment the respective alphabet position in the list
    - for t, for each char decrement the respective alphabet position in the list
at the end of the loop, if the list has all 0's, that means they have the same amount of each letter, thus an anagram
if not then its not

Time + Space:
O(n), O(1)

"""