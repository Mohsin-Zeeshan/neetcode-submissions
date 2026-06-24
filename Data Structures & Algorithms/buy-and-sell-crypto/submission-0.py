class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = []
        for i in range(len(prices)): 
            m = []
            for j in range(i,len(prices)):
                if prices[j] - prices[i] <= 0:
                    m.append(0)
                else: m.append(prices[j] - prices[i])
            dp.append(max(m))    
        return max(dp)