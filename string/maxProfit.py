# -*- coding: utf-8 -*-
# Time: 2022/10/13 8:37 PM
# Author : Ye

# From: leetcode.cn
# Subject：买卖股票的最佳时机

class Solution(object):
    def maxProfit(self, prices):
        high_value = 0
        for i in range(len(prices) - 1):
            difference = prices[i + 1] - prices[i]
            if difference > 0:
                high_value = high_value + difference
        return high_value

if __name__ == '__main__':
    prices = [7, 6, 4, 3, 1]
    so = Solution()
    print(so.maxProfit(prices))
