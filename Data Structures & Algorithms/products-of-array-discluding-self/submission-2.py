class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #calculate prefix
        res = [1] * len(nums)
        for i in range (1,len(nums)):
            res[i] = res[i-1]*nums[i-1]

        postfix = 1 
        # 3. Walk backward through the array
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix      # Multiply prefix (stored in res) by the cumulative postfix
            postfix *= nums[i]     # Update postfix for the next element to the left    

        #compute post*prefix
        return res


"""
1) Brute force solution:
res = nums ([1] * len(nums))
for each number in nums, loop trhough nums and multiply nums[i] by every number except the current index

time, space
O(n^2), O(n)

2) Prefix/Postfix?

nums = [1,2,4,6]

go through nums and collect prefix
prefix = [1,1,2,8]

go through nums and collect postfix
postfix = [48,24,6,1]

go through arrays and fill in output array by taking product of prefix[i] and postfix[i]
res = [48, 24, 12, 8]

return res

time, space
O(n), O(n)

3) We can do better by doing O(1) space compelxity
"""
