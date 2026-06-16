class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums)/2
        freqCount = {}
        for i in range(len(nums)):
            freqCount[nums[i]] = freqCount.get(nums[i], 0) + 1
            if freqCount[nums[i]] > threshold:
                return nums[i]


"""
1. Freq Count
figure out the majority threshhold: len(nums)/2
declare a frequency count hashmap where the key=num and value=count
iterate through nums:
adding frequency counts per num
if count ever exceeds n/2 return key

time, space
O(n), O(n)

How to solve in O(1) space?

2. Sorting Approach
sort nums
keep count of each num. if the current nums count exceeds n/2 return it

time, space
O(nlogn), O(1)

How can we get linear time????

3.
iterate through nums


time, space
O(n), O(1)


"""