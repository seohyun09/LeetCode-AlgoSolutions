class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit=0, 0

        for i in range(len(prices)):
            if prices[i]<prices[buy]:
                buy=i
            elif profit<prices[i]-prices[buy]:
                profit=prices[i]-prices[buy]
        
        return profit