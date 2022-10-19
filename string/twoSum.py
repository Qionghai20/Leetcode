# -*- coding: utf-8 -*-
# Time: 2022/10/19 11:15 PM
# Author : Ye

# From: leetcode.cn
# Subject：两数之和【给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。】

class Solution:
    def twoSum(self, nums, target):
        index = []
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[j] == target - nums[i]:
                    index.append(i)
                    index.append(j)
                    return index
                j += 1

    def twoSum2(self, nums, target):
        i = 0
        j = 1
        while nums[i] + nums[j] != target:
            if j + 1 == len(nums):
                i += 1
                j = i + 1
            else:
                j += 1
        return [i, j]

    def twoSum3(self, nums, target):
        #   使用字典，依次存入值对于的index
        num_dict = dict()
        for v, k in enumerate(nums):
            temp = target - k
            if num_dict.get(temp) is not None:
                return [v, num_dict[temp]]
            else:
                num_dict[k] = v
        return 0, 0

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    so = Solution()
    print(so.twoSum3(nums, target))
