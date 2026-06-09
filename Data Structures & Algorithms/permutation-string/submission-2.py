class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False
            
        map1, window = {}, {}
        for letter in s1:
            map1[letter] = map1.get(letter, 0) + 1
        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1

        l = 0
        for r in range(len(s1), len(s2)):
            if map1==window:
                return True
            window[s2[r]] = window.get(s2[r],0) + 1
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l+=1

        if map1==window:
            return True

        return False





"""
Fixed window size of len(s1)
slide window across s2
compare if window contains same letters as s1 (hashmap?)
if it does return true
else keep iterating until reach end of s2
"""