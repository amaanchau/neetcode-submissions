class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        leftWall, rightWall = 0,0
        area = 0

        while l<r:
            if height[l] < height[r]:
                if height[l] >= leftWall:
                    leftWall = height[l]
                else:
                    area += leftWall - height[l]
                l+=1
            else:
                if height[r] >= rightWall:
                    rightWall = height[r]
                else:
                    area += rightWall - height[r]
                r-=1
        return area
