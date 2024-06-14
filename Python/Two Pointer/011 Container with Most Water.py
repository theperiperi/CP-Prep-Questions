class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        left=0
        right=len(height)-1
        while left<right:
            a=(right-left)*min(height[right],height[left])
            if a>=area:
                area=a
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return area

        
