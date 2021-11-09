'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-01 14:34:55
LastEditors: liguang-ops
LastEditTime: 2021-09-01 18:50:16
'''
#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
"""
这个问题里面涉及python的几个问题，代码本身没有错，但是
涉及到python的特性，逻辑上一直报错
第一个：
    python 字符串的值无法通过下表索引的方法更改
第二个：
    python 对象类型有深复制浅复制问题。
    比如，在self._solution.append(copy.deepcopy(board))
    中，如果没有copy模块，即便在此处加了进去，仍会在后面被
    赋值操作所更改
"""
import copy
class Solution:
    def __init__(self) -> None:
        self._solution = []
    def solveNQueens(self, n: int):
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.n = n
        self.traceback(board, 0)
        self._solution = [[''.join(a) for a in i] for i in self._solution]
        return self._solution
    def traceback(self, board, row):
        #终止条件：行数大于棋盘的行数
        if row == len(board):  
            self._solution.append(copy.deepcopy(board))
            return 
        #遍历该行的每一列
        for i in range(self.n):
            #去掉不合法位置
            if self.is_illegal(board, row, i):
                continue
            #选择
            board[row][i] = 'Q'
            #进入下一行
            self.traceback(board, row + 1)
            #撤销选择
            board[row][i]= '.'
    
    def is_illegal(self, board, row, col):
        #小技巧，当前位置的下面肯定没有皇后,并且当前行也肯定没有其他皇后
        for i in range(0,row+1):
            if board[i][col] == 'Q':         #当前列
                return True
        for r,c in zip(range(row,-1,-1), range(col, -1,-1)):  #左边
            if board[r][c] == 'Q':
                return True
            if r==0 or c==0:
                break
        for r,c in zip(range(row,-1,-1), range(col,self.n,1)):
            if board[r][c] == 'Q':
                return True
            if r ==0 or c==self.n-1:
                break
        return False
# @lc code=end

