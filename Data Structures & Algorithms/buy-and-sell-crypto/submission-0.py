class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_l = 0
        profit = 0
        for i in range(len(prices)):
            if i != lowest_l:
                profit = prices[i] - prices[lowest_l]
            if profit > max_profit:
                max_profit = profit
            if prices[i] < prices[lowest_l]:
                lowest_l = i
        return max_profit
