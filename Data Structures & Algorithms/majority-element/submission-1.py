class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            # 1. If stamina drops to 0, a new candidate takes the stage
            if count == 0:
                candidate = num
                count = 1
            
            # 2. If the current number matches the candidate, boost stamina
            elif num == candidate:
                count += 1
                
            # 3. If it's an opposing faction, they cancel each other out
            else:
                count -= 1
                
        return candidate
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