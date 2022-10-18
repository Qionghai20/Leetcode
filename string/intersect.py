# -*- coding: utf-8 -*-
# Time: 2022/10/18 7:32 PM
# Author : Ye

# From: leetcode.cn
# Subject： 两个数组的交集2 [给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。]


class Solution:
    def intersect(self, nums1, nums2):
        # 两个数组先排序，再同时遍历
        nums1.sort()
        nums2.sort()
        nums = []
        i,j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                nums.append(nums1[i])
                i = i + 1
                j = j + 1
            elif nums1[i] < nums2[j]:
                i = i + 1
            else:
                j = j + 1
        return nums

    def intersect2(self, nums1, nums2):
        # 使用集合，先取两个集合交集，在获取交集中每个元素的最小数量
        n_set1 = set(nums1)
        n_set2 = set(nums2)
        n_set = set.intersection(n_set1, n_set2)
        n_nums = []
        for i in n_set:
            n_nums += [i] * min(nums1.count(i), nums2.count(i))
        return n_nums

if __name__ == '__main__':
    so = Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(so.intersect2(nums1, nums2))

