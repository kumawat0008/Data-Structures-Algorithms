class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        def max_profit_util(prices, i, buysell, k, hm):
            if i >= len(prices) or k == 0:
                return 0
            if str(i) + "day" + str(buysell) + str(k) in hm:
                return hm[str(i) + "day" + str(buysell) + str(k)]
            profit = 0
            if buysell == 0:
                buy = max_profit_util(prices, i + 1, 1, k, hm) - prices[i]
                nobuy = max_profit_util(prices, i + 1, 0, k, hm)
                profit = max(buy, nobuy)
            else:
                sell = max_profit_util(prices, i + 1, 0, k - 1, hm) + prices[i]
                nosell = max_profit_util(prices, i + 1, 1, k, hm)
                profit = max(sell, nosell)
            hm[str(i) + "day" + str(buysell) + str(k)] = profit
            return profit

        hm = {}
        return max_profit_util(prices, 0, 0, 1, hm)

