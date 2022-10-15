# -*- coding: utf-8 -*-
# Time: 2022/10/13 8:37 PM
# Author : Ye

# From: leetcode.cn
# Subject：买卖股票的最佳时机



class Solution(object):
    # 因为提前预知每天的股票价格，则只要后一天比前一天股票价格高，就可以买入
    def maxProfit(self, prices):
        high_value = 0
        for i in range(len(prices) - 1):
            difference = prices[i + 1] - prices[i]
            if difference > 0:
                high_value = high_value + difference
        return high_value

    # 动态规划解决
    def maxProfit2(self, prices):
        if len(prices) < 2:
            return 0
        nohold = 0    #第1天没有持股票的利润
        hold = -prices[0]   #第1天持有股票的利润
        for i in range(len(prices) - 1):
            nohold = max(nohold, hold + prices[i + 1])
            hold = max(nohold - prices[i + 1], hold)
        return nohold

    def maxProfit_result(self, prices, result):
        for i in range(len(prices) - 1):
            difference = int(prices[i + 1])- int(prices[i])
            if difference > 0:
                result = result - difference
        if result == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    # prices = [7, 6, 4, 3, 1]
    # so = Solution()
    # print(so.maxProfit(prices))

    # 从文件中读取测试数据
    filename = "../testdata/maxProfitdata.txt"
    file = open(filename, 'r')
    test_data = []
    result_data = []
    file_data = file.readlines()
    for row in file_data:
        tem_list = row.split(' ')
        result_data.append(int(tem_list[1]))
        array_list = tem_list[0].split(',')
        test_data.append(array_list)
    so = Solution()

    for i in range(len(test_data)):
        result = so.maxProfit_result(test_data[i], result_data[i])
        if result:
            print(f"第 %d 组测试数据 正确\n" % i)
        else:
            print(f"第 %d 组测试数据 错误\n" % i)


