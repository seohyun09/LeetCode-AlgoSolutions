class Solution:
    def trap(self, height: List[int]) -> int:
        left, right=0, len(height)-1
        leftMax, rightMax=height[left], height[right]
        totalWater=0

        while left<right:
            leftMax=max(leftMax, height[left])
            rightMax=max(rightMax, height[right])
            
            if height[left]<=height[right]:
                totalWater+=(leftMax-height[left])
                left+=1
            else:
                totalWater+=(rightMax-height[right])
                right-=1
        
        return totalWater
