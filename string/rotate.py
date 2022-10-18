# -*- coding: utf-8 -*-
# Time: 2022/10/15 11:07 AM
# Author : Ye

# From: leetcode.cn
# Subject：旋转数组:给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

class Solution:
    def rotate_array(self, nums, left, rigth):
        i = left
        while(i < (rigth - left) / 2):
            temp = nums[i]
            nums[i] = nums[rigth - i + left]
            nums[rigth - i + left] = temp
            i = i + 1
        return nums

    def rotate(self, nums, k):
        k = k % len(nums)
        if len(nums) < 2 or k == 0:
            return nums
        self.rotate_array(nums, 0, len(nums) -1 - k)
        self.rotate_array(nums, len(nums) - k, len(nums) - 1)
        self.rotate_array(nums, 0, len(nums) - 1)
        return nums

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    so = Solution()
    print(so.rotate(nums, k))

