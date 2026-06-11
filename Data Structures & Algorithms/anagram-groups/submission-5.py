class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        # {a: [], b: []}
        for string in strs:
            freqMap = [0] * 26
            for letter in string:
                freqMap[ord(letter)-ord('a')] += 1
            anagrams[tuple(freqMap)].append(string)
        
        return (list(anagrams.values()))




"""
1. Sorting method
loop through strs:
    - sort each str and store the sorted string as a key in a dictionary
        - store the original str as the value
    
after the loop we now have a list of lists containing all the anagrams in the values of the dict

just return the values

Time, Space
O(m * nlogn), O(m * n)

2. 
for str in strs:
    create a frequency map of the characters in each string
    store the frequency map as a key in a dictionary
        - store the original str as the value

after the loop we now have a list of lists containing all the anagrams in the values of the dict

just return the values

Time, Space
O(n), O(n)

"""




