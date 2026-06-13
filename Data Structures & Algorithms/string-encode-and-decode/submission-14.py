class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '_' + s
        return res

    def decode(self, s: str) -> List[str]:
        strs = []               # output list to return
        k=0                     # k is out pointer to iterate through the string
        while k<len(s)-1:       # we continue as long as the pointer is in the bounds of the word
            length = ''         # variable to keep track of the length of the list item before the delimeter '_'
            while s[k]!='_':    # keep iterating until the length number is finished and we hit the delimeter
                length+=s[k]    # add the digit to the length variable since we havent hit the delimeter yet 
                k+=1            # move to the next character
            intLength = int(length)             # now we have the total length of the word as we have hit the delimeter, so lets convert it to an integer as currently we have it saved as a string
            strs.append(s[k+1:k+1+intLength])   # now we take the string from the index after the delimeter to the index after the delimeter plus the length of the word we just resolved and append it to our list
            k = k + 1 + intLength               # move the k pointer to next character after the word is complete
        return strs







