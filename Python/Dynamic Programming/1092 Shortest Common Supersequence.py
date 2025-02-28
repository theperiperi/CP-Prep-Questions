class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        m,n = len(str1),len(str2)

        # finding longest common subsequence

        dp = [[0] * (n + 1) for _ in range(m + 1)]


        for i in range(1, m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
         

        # finding shortest common supersequence containing lcs (traceback)

        res = []

        while m > 0 and n > 0:
            
            if str1[m-1] == str2[n-1]:
                res.append(str1[m-1])
                m-=1
                n-=1

            elif dp[m-1][n] >= dp[m][n-1]:
                res.append(str1[m-1])
                m-=1
                
            else:
                res.append(str2[n-1])
                n-=1

        #add other character
        while m>0:
            res.append(str1[m-1])
            m-=1
        
        while n>0:
            res.append(str2[n-1])
            n-=1
        
        #reverse and return res
        return ''.join(res[::-1])

        







        
        
        

            
                        
