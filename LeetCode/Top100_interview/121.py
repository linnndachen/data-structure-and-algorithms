class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        profit, min_buy = 0, prices[0] 
        for price in prices:
            min_buy = min(min_buy, price) #is price less than min_buy
            profit = max(profit, price - min_buy)
        return profit

        """
        buy, ans = float('inf'), 0
        for p in prices:
            buy, ans = min(buy, p), max(ans, p-buy)
        return ans
        """

    def brute_force(self, prices):
        max_v = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                v = prices[j] - prices[i]
                if v > max_v:
                    max_v = v
        return max_v
