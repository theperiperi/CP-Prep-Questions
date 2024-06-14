class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score=0
        #either subtract token value from power to gain 1 score
        #or subtract 1 score to gain token value power

        #maximize score, play in any order

        tokens.sort()
        left=0
        right=len(tokens)-1

        score=0
        res=0

        while left<=right:
            #smallest
            if power>=tokens[left]:
                power-=tokens[left]
                score+=1
                res=max(res,score)
                left+=1
            #largest
            elif power<=tokens[left] and score>=1:
                power+=tokens[right]
                right-=1
                score-=1
            else:
                break
        return res
