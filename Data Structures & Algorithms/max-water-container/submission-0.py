class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmt = 0
        l, r = 0, len(heights) - 1
        while l<r:
            area = (r-l)*(min(heights[l],heights[r]))
            maxAmt = max(area,maxAmt)
            if heights[l] == heights[r]:
                l+=1
            elif heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxAmt


"""
brute force
iterate through heights
for each height iterate through rest of the array and calculate areas
store a max area and keep replacing with bigger areas
return max area

Time: O(N^2)
Space: O(1)
"""

"""
brute force
iterate through heights
for each height iterate through rest of the array and calculate areas
store a max area and keep replacing with bigger areas
return max area

Time: O(N^2)
Space: O(1)
"""