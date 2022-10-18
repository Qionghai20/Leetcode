# -*- coding: utf-8 -*-
# Time: 2022/10/18 5:27 PM
# Author : Ye

# From: leetcode.cn
# Subject：只出现一次的数字 【给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。】

class Solution:
    def singleNumber(self, nums):
        # 排序后，两个两个比较
        if len(nums) < 2:
            return nums[0]
        nums.sort()
        i = 0
        while i + 1 < len(nums):
            if nums[i] != nums[i + 1]:
                return nums[i]
            i = i + 2
        return nums[i]

    def singleNumber2(self, nums):
        # 定义一个集合，往其中插入不重复的数
        nset = set()
        for i in range(len(nums)):
            if nums[i] in nset:
                nset.remove(nums[i])
            else:
                nset.add(nums[i])
        return list(nset)[0]

    def singleNumber3(self, nums):
        # 使用异或运算
        s = nums[0]
        for i in range(1, len(nums)):
            s = s ^ nums[i]
        return s

if __name__ == '__main__':
    so = Solution()
    nums = [4,1,2,1,2]
    print(so.singleNumber3(nums))
