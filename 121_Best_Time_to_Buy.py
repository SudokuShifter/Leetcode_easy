from typing import Optional


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1 
        max_profit = 0
        while right < len(prices):
            current_profit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(current_profit, max_profit)
            else:
                left = right
            right += 1
        return max_profit
