'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-10 19:20:24
LastEditors: liguang-ops
LastEditTime: 2021-09-10 20:58:04
'''
#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
import numpy as np
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """动态规划，和#516相似
        定义dp[i][j]是字符串s[i...j]是回文串是的长度，如果不是回文串值变为0，是回文串，则是他的长度
        状态转移方程：dp[i-1][j+1] = dp[i][j] + 2,当dp[i][j]是回文串，且s[i-1] == s[j+1]
                    dp[i-1][j+1] = 0,当s[i-1] !=s[j+1]
        base case:当 i=j时，默认是回文串，长度1
                当i>j时，默认是回文串，长度0，(为了偶数长度回文串好算)
        """
        dp = [[0] * len(s) for _ in range(len(s))]
        maxIndex = [0,0,0]  #row,col,index
        for i in range(len(s)):  #对角线元素为1
            dp[i][i] = 1
        for i in range(len(s)-2, -1,-1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if i+1 > j-1 or dp[i+1][j-1]>0:   #如果属于左下角，或者dp[i+1][j-1]是回文串
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = 0
                else:  #其他情况都不是回文串
                    dp[i][j] = 0
                if dp[i][j] > maxIndex[2]:
                    maxIndex[0] = i
                    maxIndex[1] = j
                    maxIndex[2] = dp[i][j]
        return s[maxIndex[0]:maxIndex[1]+1]
# @lc code=end

