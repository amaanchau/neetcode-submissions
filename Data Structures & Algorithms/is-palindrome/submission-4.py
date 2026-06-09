class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l <= r:
            while l < r and not s[l].isalnum():
                l+=1
            while r > l and not s[r].isalnum():
                r-=1
            if s[l].upper() != s[r].upper():
                return False
            l+=1
            r-=1
        return True



"""
Two pointers
l starts at beginning, r starts at end
increment both passed all non alphanum chars
compare to see they are the same
if not the same return false
if same move l and r 1 closer

"""