class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxVal = max(count.values())
            while (r-l+1) - maxVal > k:
                count[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
        
        return res

"""
A:1
B:2
C:1
maxVal = 2
while 2>2
"""
