# -*- coding: utf-8 -*-
# Time: 2022/10/13 8:31 PM
# Author : Ye

# From: leetcode.cn
# Subject：删除排序数组中的重复项

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        while(j < len(nums)):
            if nums[i] == nums[j]:
                j = j + 1
            else:
                i = i + 1
                nums[i] = nums[j]
                j = j + 1
        return i + 1

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    so = Solution()
    print(so.removeDuplicates(nums))

