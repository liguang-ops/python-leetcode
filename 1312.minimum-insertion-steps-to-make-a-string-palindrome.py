'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-13 10:30:24
LastEditors: liguang-ops
LastEditTime: 2021-09-13 11:00:24
'''
#
# @lc app=leetcode id=1312 lang=python3
#
# [1312] Minimum Insertion Steps to Make a String Palindrome
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        """动态规划：
            定义:dp[i][j]是字符串s[i...j]构造最小回文串的插入次数
            状态转移方程：
                1. s[i] = s[j], dp[i][j] = dp[i+1][j-1]
                2. s[i] != s[j], dp[i][j] = min(dp[i][j-1], dp[i+1][j]) + 1
                当s[i] != s[j]时，有几种情况。第一种s[i...j-1]或者s[i+1...j]都是同
                一种字符的时候(回文串)，只需要插入一个字符就能构成回文串。当s[i...j-1]
                或者s[i+1...j]都不是回文串的时候，dp[i][j-1],dp[i+1][j]就是构造s[i...j-1]
                或者s[i+1...j]回文串的最小插入次数，因此，在新添进来一个s[j]或者s[i]，只要在对
                侧插入一个相等的字符就能构成回文串，因此，只需要+1就行
            base case：
                1. i = j 时，只有一个字符，因此dp[i][j] = 0
                2. 1 > j 时，没有字符，也为0
        """
        dp = [[0] * len(s) for _ in range(len(s))]
        #从下往上，从左往右遍历
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        return dp[0][len(s)-1]
# @lc code=end

