# -*- coding: utf-8 -*-
# Time: 2022/10/19 10:45 PM
# Author : Ye

# From: leetcode.cn
# Subject：移动零 【给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。】

class Solution:
    def moveZeroes(self, nums):
        #   从前往后遍历，只有不为0，则往前赋值，后面用零补齐
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                j += 1
                i += 1
            else:
                j += 1
        while i < len(nums):
            nums[i] = 0
            i += 1
        return nums

    def moveZeroes2(self, nums):
        #   先找到第一个零
        #   遇到非零则与零进行交换，交换次数少
        # 1 0 0 3 12
        # 1 3 0 0 12
        # 1 3 12 0 0
        i = 0
        while i < len(nums) and nums[i] != 0:
            i += 1
        j = i + 1
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                nums[i] = nums[j]
                nums[j] = 0
                i += 1
                j += 1
        return nums

    def moveZeroes3(self, nums):
        #   双指针，right只要不为零，就和left进行交换
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
        return nums




if __name__ == '__main__':
    so = Solution()
    nums = [0, 1, 0, 3, 12]
    print(so.moveZeroes3(nums))
    # [0, 1, 0, 3, 12]
