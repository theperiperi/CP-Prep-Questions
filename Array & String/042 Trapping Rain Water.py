class Solution:
    def trap(self, height: List[int]) -> int:
        rightwall=0
        leftwall=0
        res=0
        
        l=0
        r=len(height)-1

        if not height: return res

        while l<r:
            if height[l]<=height[r]:
                if height[l]>leftwall:
                    leftwall=height[l]
                else:
                    res+=(leftwall-height[l])
                l+=1
            else:
                if height[r]>rightwall:
                    rightwall=height[r]
                else:
                    res+=(rightwall-height[r])
                r-=1
        return res
            

        
