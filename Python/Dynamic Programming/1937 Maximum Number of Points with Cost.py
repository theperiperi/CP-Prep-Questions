class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m=len(points)
        n=len(points[0])
        dp=[0]*n

        for j in range(n):
            dp[j]=points[0][j]

        for i in range(1,m):
            leftMax=[0]*n
            rightMax=[0]*n
            dpNew=[0]*n

            #calculate left max
            leftMax[0]=dp[0]
            for j in range(1,n):
                leftMax[j]=max(leftMax[j-1],dp[j]+j)
            
            rightMax[n-1]=dp[n-1]-(n-1)
            for j in range(n-2,-1,-1):
                rightMax[j]=max(rightMax[j+1],dp[j]-j)
            
            for j in range(n):
                dpNew[j]=max(leftMax[j]-j,rightMax[j]+j)+points[i][j]

            dp=dpNew
        
        return max(dp)
