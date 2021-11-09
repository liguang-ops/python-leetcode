'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-13 11:48:24
LastEditors: liguang-ops
LastEditTime: 2021-09-24 15:10:34
'''
#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memory = {}
        def dp(i, j):
            if (i, j) in memory.keys():
                return memory[(i, j)]
        #base case:当正则表达式指针j指到末尾时，如果字符串指针i也指到了末尾，则说明正确匹配
            if j == len(p): return i == len(s)
            if i == len(s):
                #正则表达式剩余字符，必须是一个字符和*成对出现，如 P*a*之类，是2的整数倍，
                if (len(p) - j) % 2 == 1: 
                    return False
                if all([m == "*" for m in p[j+1::2]]):  #虽然是偶数个，但是还要保证剩余字符串是和*成对出现
                    return True
                else: 
                    return False
            if s[i] == p[j] or p[j] == ".":
                if j < len(p)-1 and p[j + 1] == "*":
                    #dp(i, j+2)表示匹配0个字符
                    #dp(i+1, j)先匹配一个字符，然后继续往下匹配
                    res = dp(i, j+2) or dp(i+1, j)
                else:
                    res = dp(i+1, j+1)  #只匹配一个字符
            else:
                if j < len(p)-1 and p[j + 1] == "*": #在不等于的情况下，只能匹配0个字符
                    res = dp(i, j+2)
                else:
                    res = False
            memory[(i, j)] = res
            return res
        return dp(0, 0)
# @lc code=end

