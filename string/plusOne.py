# -*- coding: utf-8 -*-
# Time: 2022/10/19 8:57 PM
# Author : Ye

# From: leetcode.cn
# Subject：加一 [给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。]

class Solution:
    def plusOne(self, digits):
        #   1、先判断是否是全9
        #   2、各位先加1，看是否进位
        #   3、十位开始只加进位
        if digits.count(9) == len(digits):
            digits[0] = 1
            i = 1
            while i < len(digits):
                digits[i] = 0
                i = i + 1
            digits.append(0)
        else:
            carry = 0
            j = len(digits) - 2
            temp = digits[len(digits) - 1] + 1
            digits[len(digits) - 1] = temp % 10
            if temp < 10:
                return digits
            else:
                carry = 1
                while j >= 0:
                    temp = carry + digits[j]
                    digits[j] = temp % 10
                    carry = int(temp / 10)
                    j = j - 1
        return digits

    def plusOne2(self, digits):
        # 从各位开始比较，只要小于9，直接+1返回，等于9，则进位，直到小于9
        j = len(digits) - 1
        while j >= 0:
            if digits[j] < 9:
                digits[j] += 1
                return digits
            else:
                digits[j] = 0
                j -= 1
        digits[0] = 1
        digits.append(0)
        return digits


if __name__ == '__main__':
    so = Solution()
    digits = [9, 9, 9, 9]
    # print(so.plusOne(digits))
    print(so.plusOne2(digits))

# 9999