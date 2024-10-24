class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set =set(wordDict)
        #intialize dp array to store True/False values
        dp = [False] * (len(s) +1)
        #empty String : edge case
        dp[0]= True
        
        for index in range(1, len(s)+1):
            for character in range(index):
                if dp[character] and s[character:index] in word_set:
                    dp[index]=True
                    break
        return dp[len(s)]
