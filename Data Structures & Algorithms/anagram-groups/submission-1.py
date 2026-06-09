class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)
        for word in strs:
            chars = [0] * 26
            for char in word:
                chars[ord(char) - ord('a')] += 1
            tup = tuple(chars)
            anagrams[tup].append(word)
        return list(anagrams.values())
            

"""
Problem:
    group anagrams into a list of lists
    two strings are anagrams if they have the characters and amount of characters


Approach 1: 
    - sort each word and save index
    - find out which indexes have the same words
    - group them into a list of lists
    Time Complexity: O(nlogn)

Approach 2: 
    - iterate through strs
    - for each str iterate through and generate a list of all lower case letters and the frequency they appear in the string
    - save this list to a hashmap with the list as the index, and the word as the key
    - hashmap key should be a list so anagrams can group up 
    - return the values of the hashmao
    Time Complexity: O(n*m)
    Space Complexity: O(nlogn)

"""