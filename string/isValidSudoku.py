# -*- coding: utf-8 -*-
# Time: 2022/10/20 2:49 PM
# Author : Ye

# From: leetcode.cn
# Subject：有效的数独

class Solution:
    def isValidSudoku(self, board):
        row = [[0 for i in range(len(board))] for j in range(len(board))]
        col = [[0 for i in range(len(board))] for j in range(len(board))]
        cel = [[0 for i in range(len(board))] for j in range(len(board))]
        for i in range(len(board) - 1):
            for j in range(len(board) - 1):
                if board[i][j] == '.':
                    continue
                temp = int(board[i][j]) - int('0') - 1
                k = int(i / 3 * 3 + j / 3)
                if row[i][temp] != 0 or col[j][temp] != 0 or cel[k][temp] != 0:
                    return False
                row[i][temp] = col[j][temp] = cel[k][temp] = 1

        return True

if __name__ == '__main__':
    so = Solution()
    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(so.isValidSudoku(board))


