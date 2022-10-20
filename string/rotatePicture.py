# -*- coding: utf-8 -*-
# Time: 2022/10/20 11:18 PM
# Author : Ye

# From: leetcode.cn
# Subject： 旋转图像 【给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。】

class Solution:
    def rotate(self, array):
        # 旋转数组
        for i in range(int(len(array)/2)):
            temp = array[i]
            array[i] = array[len(array) - 1 - i]
            array[len(array) - 1 - i] = temp
        return array

    def symmetrical_rotate(self, matrix):
        for i in range(len(matrix)):
            j = i + 1
            while j < len(matrix):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                j += 1
        return matrix

    def rotate_picture(self, matrix):
        self.symmetrical_rotate(matrix)
        for i in range(len(matrix)):
            matrix[i] = self.rotate(matrix[i])
        return matrix

if __name__ == '__main__':
    so = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(so.rotate_picture(matrix))

    # 1 2 3
    # 4 5 6
    # 7 8 9
    #
    # 3 2 1
    # 6 5 4
    # 9 8 7
    #
    # 7 4 1
    # 8 5 2
    # 9 6 3

