class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded = encoded + str(len(word)) + "#" + word 
        return encoded

    def decode(self, s: str) -> List[str]:
        #       encode: 4#neet4#code
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

            
                
        return res



"""
Input: ["neet","code"]

encode: neet#code

decode: ["neet","code"]

Input: ["neet","co#de"]

encode: neet#co#de

decode: ["neet","co","de"]

What if we put a number before each string telling us how long each string is

Input: ["neet","code"]

encode: 4neet4code

decode: ["neet","code"]

Input: ["3neet","code"]

encode: 53neet4code

decode: ["neet4code"]

We need a way to know when the length number ends.

Input: ["3neet","code"]

encode: #4neet4#code

decode: ["3neet","code"]


"""


