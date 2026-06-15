class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l<r:
            while isNotAlphaNum(s[l]) and l<r:
                l+=1
            while isNotAlphaNum(s[r]) and l<r:
                r-=1
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True

def isNotAlphaNum(char):
        if ord(char) >= ord('A') and ord(char) <= ord('Z'):
            return False
        if ord(char) >= ord('0') and ord(char) <= ord('9'):
            return False
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            return False
        return True
