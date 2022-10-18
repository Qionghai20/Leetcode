# -*- coding: utf-8 -*-
# Time: 2022/10/18 4:14 PM
# Author : Ye

# From: leetcode.cn
# Subject： 存在重复元素 【给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。】

import time

class Solution:
    def containsDuplicate(self, nums):
        # 先排序，然后一次循环遍历前后元素是否相等 【费时】
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

    def containsDuplicate1(self, nums):
        # 使用集合，集合中不存在重复元素 【费时少，但占内存】
        new_nums = set(nums)
        if len(new_nums) == len(nums):
            return False
        return True

    def containsDuplicate2(self, nums):
        # 使用集合，定义一个空集合，向其中插入nums中的元素，已存在则表示有重复
        new_nums = set()
        for i in range(len(nums)):
            if nums[i] in new_nums:
                return True
            new_nums.add(nums[i])
        return False

if __name__ == '__main__':
    nums = [1,2,3]
    so = Solution()
    t1 = time.time()
    so.containsDuplicate(nums)
    print(f'solution1 coast {time.time() - t1:.8f}s ')

    t2 = time.time()
    so.containsDuplicate1(nums)
    print(f'solution1 coast {time.time() - t2:.8f}s ')

    t3 = time.time()
    so.containsDuplicate2(nums)
    print(f'solution1 coast {time.time() - t3:.8f}s ')
