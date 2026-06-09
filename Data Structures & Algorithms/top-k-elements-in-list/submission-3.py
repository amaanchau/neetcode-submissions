class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = [[] for i in range(len(nums) + 1)]
        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num,0)+1
        for num, freq in freqMap.items():
            freqList[freq].append(num)

        print(freqList)
        res = []
        for i in range(len(freqList)-1,0,-1):
            for num in freqList[i]:
                res.append(num)
                if len(res) == k:
                    return res


"""
Find the Kth most frequent element in the list
return those numbers in a list format

create a list that is the size of the max frequency (len(nums))
for this list the index is the frequeny and the value is the numbers
create a dictionary with mappings of the numbers and their frequency
iterate through the nums and map numbers to their frequency

map: {1:1, 2:2, 3:3}

now we have this
lets iterate through the items in this dictionary and place the numebers in
the frequency list

[ [],[1],[2],[3],[],[],[] ]

define a result list
iterate backwords through this list
for ecah number added to the result list reduce the k value by 1
until k = 0

time complexity O(n) iterating through nums once
space complexity O(n) 
"""