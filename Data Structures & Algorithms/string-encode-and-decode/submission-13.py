class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '_' + s
        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        k=0
        while k<len(s)-1:
            length = ''
            while s[k]!='_':
                length+=s[k]
                k+=1
                continue
            intLength = int(length)
            strs.append(s[k+1:k+1+intLength])
            k = k + 1 + intLength
        return strs







