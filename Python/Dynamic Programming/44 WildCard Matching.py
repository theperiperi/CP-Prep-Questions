class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp=[[0 for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=1 #True
        if len(p)==0 and len(s)!=0:
            return 0
        for i in range(1,len(p)+1):
            if p[i-1]=="*":
                dp[0][i]=1
            else:
                break
        
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if s[i-1]==p[j-1] or p[j-1]=="?":
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=="*":
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]
        
