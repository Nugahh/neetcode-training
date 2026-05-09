class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        seen = set()
        minBuy = prices[0]

        maxSell = 0
        for sell in prices:
            maxSell = max(maxSell, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxSell            