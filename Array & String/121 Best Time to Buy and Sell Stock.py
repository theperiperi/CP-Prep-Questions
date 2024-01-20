class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=i
        max_profit=0

        while j<len(prices):
            if prices[j]>prices[i]:
                profit=prices[j]-prices[i]
                max_profit=max(max_profit,profit)
            else:
                i=j
            j+=1
        return max_profit
        
