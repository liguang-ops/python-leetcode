'''
Description:
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-05 20:50:00
LastEditors: liguang-ops
LastEditTime: 2021-10-05 22:37:23
'''
#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """解法，肯定是回溯，但是我想不出来。这里看书之后，是这样的：回溯有两样很重要的
        东西，分别是路径和选择列表，选择列表很简单，是1-9，而路径我一开始老是想双重循环
        遍历整个board，这样就无法递归了。应该是我N皇后问题忘记了，事实上每个递归体里考虑
        的只是当前行的情况，再通过行计数器和列计数器实现跳到下一行。
        这样整体思路就很清晰了
        """
        def isValid(row , col, char):
            # for i in range(9):
            #     if board[row][i] != '.' and board[row][i] == c: return False
            #     if board[i][col] != '.' and board[i][col] == c: return False
            if char in board[row]:
                return False
            if char in [board[i][col] for i in range(9)]:
                return False
            baseRow, baseCol = (row // 3) * 3, (col // 3) * 3
            for i in range(baseRow, baseRow + 3):
                for j in range(baseCol, baseCol + 3):
                    if board[i][j] != '.' and board[i][j] == c: 
                        return False
            return True
                
        def dfs(row, col):
            if row == len(board):  #注意，这里i，j都是索引范围是0-8，当等于9就代表整个棋盘已经遍历完了
                return True
            if col == len(board):  #最后一列已经遍历完了，那就换到下一行的第一列
                return dfs(row+1, 0)
            if board[row][col] != '.':  #说明题目已经给了值了, 直接看下一个就行
                return dfs(row, col+1)
            #其他情况
            for char in [str(num) for num in range(1,10)]:
                if not isValid(row, col, char):
                    continue
                board[row][col] = char
                if dfs(row,col + 1):
                    return True
                board[row][col] = '.'
            #如果当前格子穷举完依然没有合法答案，那么就需要上一个格子撤销选择
            return False
        dfs(0, 0)
# @lc code=end

