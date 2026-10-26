class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = prices[0]
        for i in range(len(prices)):
            profit = prices[i] - l
            max_profit = max(profit, max_profit)
            l = min(prices[i], l)
        return max_profit
        