class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqBuckets = [[] for i in range(len(nums) + 1)]
        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num,0)+1

        for num, count in freqMap.items():
            freqBuckets[count].append(num)
            
        res = []
        for i in range(len(freqBuckets)-1,0,-1):
            for num in freqBuckets[i]:
                res.append(num)
            if len(res)==k:
                return res


    """
    Input: nums = [1,2,2,3,3,3], k = 2

    freeuqnecy can be at most 6 (len(nums))

    frequency list (size is len(nums)+1)
    [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    ]

    each index represents frequency

    ok lets go through the list and keep track of freq counts using a hashmap
    {
        1:1
        2:2
        3:3
    }

    loop throug hashmap and store the actual num inside the list (append)

    [
        [],
        [1],
        [2],
        [3],
        [],
        [],
        [],
    ]

    iterate through this hashmap backwards appending to our output list until it is length k

time, space
O(n) , O(n)
"""