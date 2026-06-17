class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sort nums first so and l and r two pointer approach will work
        res = set()
        for i in range(len(nums)-2):
            target = nums[i]*-1 # Multiple by negative one becuase we want the other two nums to counteract this one
            l, r = i+1, len(nums)-1
            while l<r:
                if (nums[l]+nums[r]) == target:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
                elif (nums[l]+nums[r]) > target:
                    r-=1
                else:
                    l+=1
        return list(res)

# [-4,-1,-1,0,1,2]



"""
Brute Force Approach:
triple for loop
time, space
O(N^3), O(1)

Second Approach:
sort the list and use two pointers:
sort list -> O(nlogn)
[-1,0,1,2,-1,-4] -> [-4,-1,-1,0,1,2]

iterate through list
for each num have a left pointer and right pointer defined 
[-4,-1,-1,0,1,2]
  i l->     <-r

i is our target num for the other two numbers to counteract (trying to sum to 0). So in this case we are looking for positive 4
if the sum of l and r is too low, increment left pointer, if its too big, increment right pointer
if a match is found append a results list

after look return results

time, space
O(n^2), O(1)
"""


