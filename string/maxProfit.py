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


