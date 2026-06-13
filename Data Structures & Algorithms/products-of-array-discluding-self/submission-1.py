class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #calculate prefix
        prefix = [1] * len(nums)
        for i in range (1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        #calculate postfix
        postfix = [1] * len(nums)
        for i in range (len(nums)-2,-1,-1):
            postfix[i] = postfix[i+1]*nums[i+1]

        #compute post*prefix
        res = []
        for i in range(len(nums)):
            res.append(postfix[i]*prefix[i])
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
"""