class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        CountS, CountT = {}, {}

        for i in range(len(s)):
            CountS[s[i]] = 1 + CountS.get(s[i], 0)
            CountT[t[i]] = 1 + CountT.get(t[i], 0)

        return CountS==CountT           

"""
Problem:
    - if two string are anagrams return True, if not False
    - letters in two strings are the same, return True
    - strings must be the same size

Approach 1:
    - iterate through string s:
        - for each letter iterate through string t until that letter is found
            - if not found return False
        - if reach end ofs
        - not going to work
            - what if theres two of the same letter in string s
            - example letter and letger

Approach 2:
    - create a hashmap of both s and t and the counts of each letter and compare hashmaps
    - iterate through s, creating a hasmap with the letters and their respective counts 
    - iterate through t, creating a hasmap with the letters and their respective counts 
    - compare hasmaps
    - if same return true, else return false
    - O(s + t) time complexity since we need to iterate through both once
    - O(s + t) space complexity since we need to store each letter in each string
"""