'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-08 18:27:52
LastEditors: liguang-ops
LastEditTime: 2021-09-08 19:39:43
'''
#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0: return 0
        i = 0
        num = ""
        sign = ""
        while(i< len(s) and s[i] == " " ):
            i += 1
        if i == len(s): return 0
        for j in range(i, len(s)):
            if s[j] in ["+", "-"] and len(sign) == 0 and len(num) == 0:
                sign += s[j]
            elif s[j] in [str(q) for q in range(10)] and len(sign) <2:
                num += s[j]
            else:
                break
        if len(num) == 0 or len(sign) >1:
            return 0
        num = int(sign + num)
        if num < -2**31:
            return -2**31
        elif num > 2**31 -1:
            return 2**31 -1
        else:
            return num
        
# @lc code=end

