class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curmax = 0
        l = 0
        for r in range(1,len(prices)):
            while prices[l]>prices[r]:
                l+=1

            res = max(res, prices[r]-prices[l])

        return res

