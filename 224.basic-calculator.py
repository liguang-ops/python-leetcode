'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-08 15:42:18
LastEditors: liguang-ops
LastEditTime: 2021-10-08 17:18:37
'''
#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        """我先做的#227，思路一摸一样，还简单一代点，直接把乘号和除号的注释掉就好
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
                    # elif sign == '*':
                    #     stack[-1] = n * stack[-1]
                    # elif sign == '/':
                    #     stack[-1] = int(stack[-1] / float(n))
                    n = 0
                    sign = char
                if char == ')': break
            return sum(stack)
        return calc(s)
        
# @lc code=end

