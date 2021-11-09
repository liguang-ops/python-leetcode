'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-08 15:54:27
LastEditors: liguang-ops
LastEditTime: 2021-10-08 17:18:02
'''
#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        """这一题在本科时候就接触过，知道肯定要用栈，但是在考虑到括号之后就想不出来了。
        思路：总的思路是，把所有的减法变成负数的加法， 然后入栈，在到达字符串末尾后，将栈中所有数字出栈，加在一起
        1. 减号变负数
        2. 乘号、除号，是二元运算符，在遇到乘号除号时，把即将入栈的元素和栈顶元素pop出来，计算完之后，在入栈
        3. 括号，遇到括号优先计算，括号里面其实也是包含全部的运算，这里只要递归处理就好
        """
        #不理解为什么runtime消耗那么高，明明只有O(n)
        s = list(s)
        def calc(s):
            #先把数字计算出来
            stack = []
            sign = '+'   #题目中要求每个数字都是正数,记录的是当前数字前面最近的符号
            n = 0
            #我觉得这里最巧妙是用pop(),这样就巧妙的解决了递归时字符位置问题
            while s:
                char = s.pop(0)
                if char.isdigit():
                    n = n * 10 + int(char)   #这里不断迭代，计算数字，直到char不是数字
                if char == '(':    #遇到括号，就递归，用calc解决括号里面的字符串组合
                    n = calc(s)  #这么没有立马入栈，入栈的工作是在下面做了。
                if (not char.isdigit() and char != ' ') or len(s) == 0:
                    if sign == '+':
                        stack.append(n)
                    elif sign == '-':
                        stack.append(-n)
                    elif sign == '*':
                        stack[-1] = n * stack[-1]
                    elif sign == '/':
                        stack[-1] = int(stack[-1] / float(n))
                    n = 0
                    sign = char
                if char == ')': break
            return sum(stack)
        return calc(s)
# @lc code=end

