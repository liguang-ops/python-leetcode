'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-08 20:45:14
LastEditors: liguang-ops
LastEditTime: 2021-09-10 19:09:20
'''
#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        还是动态规划
        定义dp[i][j]等于子数组s[i:j+1]最长回文子序列的长度
        状态转移方程：
            1. 当s[i-1] = s[j+1]时，那么dp[i-1][j+1] = d[i][j] + 2
            2. 不等于时，s[i:j+1]的最长回文子序列的长度应该等于s[i-1:j+1]、s[i:j+2]这两个
                的最长回文子序列的长度的最大值，即max(dp[i-1,j], dp[i,j+1])
        base case:
            i和j肯定是往中间缩的，当i=j的时候，此时，子数组只有一个字符，最长回文子序列长度就为1
            当i < j 时, s[i....j]没有字符，因此，dp[i][j] = 0
        """ 
        dp = [[0] * len(s) for _ in range(len(s))]  #dp是一个二维的len(s) x len(s)数组
        for i in range(len(dp)):
            dp[i][i] = 1
        #由于我们求dp[i-1][j+1]变量需要用到dp[i][j],dp[i-1,j],dp[i,j+1]三个变量，,画一下
        #分布会发现，需要用第二、三、四象限去求第一象限，因此，遍历方向需要从下网上，从左往右
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):   #对角线元素全为1，对角线元素以及左下角不需要算
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2  #左下角
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j]) #左边和下边
        return dp[0][len(s)-1]

# @lc code=end

