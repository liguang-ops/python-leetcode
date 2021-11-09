'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-07 11:56:02
LastEditors: liguang-ops
LastEditTime: 2021-09-08 16:34:56
'''
#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 二维dp数组，大小len(st1) x len(st2)，dp[i][j]表示text2[0:i]和text1[0:j]两个字符串
        # 的最大公共序列
        # 状态转移方程： dp[i][j] = (dp[i-1][j-1] + 1) * int(str[i] == str[j]) +\
        #  max(dp[i-1][j], dp[i][j-1]) * int(str[i] == str[j])
        #行 = len(text2) + 1, 列 = len(text1) + 1,空间换时间，不用做判断了,把第0列和第0行全部当成0
        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
        for i in range(len(text2)):
            for j in range(len(text1)):
                isEqual = int(text2[i] == text1[j])
                if isEqual == 1:
                    dp[i+1][j+1] = dp[i][j]+ isEqual
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[len(text2)][len(text1)]

    #dp数组的定义是一样的，这里主要解释，为什么那样进行状态转移
    #考虑某一个dp点，dp[i][j]已经计算出来，这时候新来了一个字符a，
    #那么， 如果a在text1和text2中都存在，那么dp[i+1][j+1] = dp[i][j] + 1,
    #如果只存在与一个字符串中，那么dp[i+1][j+1]应该s是max(dp[i][j+1], dp[i+1][j]),
    #这里是暴力遍历，时间复杂度O(m^N)过高，没法AC,但是代码是对的
    #加上备忘录就能AC
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        #这里参照了上面的写法，把第0列和第一行全部设为0,相当于比较:
        # ''+ text1 和''+ text2两个字符串的最长公共序列
        #备忘录
        book = {}
        def dp(i,j):
            if (i,j) in book.keys():
                return book[(i,j)]
            if i == 0 or j == 0:
                return 0
            if text1[i-1] == text2[j-1]:
                book[(i,j)]  = dp(i-1, j-1) + 1
            else:
                book[(i,j)] = max(dp(i, j-1), dp(i-1, j))
            return book[(i,j)]
        return dp(len(text1),len(text2))

# @lc code=end

