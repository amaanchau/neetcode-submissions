class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        prefix[0] = 1
        postfix[len(nums)-1] = 1
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(len(nums)-2, -1 , -1):
            postfix[i] = nums[i+1] * postfix[i+1]

        print(prefix)
        print(postfix)

        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]

        return res
# Input: nums = [1,2,4,6]
# Lets calculate the prefix before each number and the postfix after each num
# Then we can mutlply those to get the total product of everything but the number

