'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-16 16:20:57
LastEditors: liguang-ops
LastEditTime: 2021-09-16 22:10:36
'''
#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#

# @lc code=start
#一开始能想到的就是DFS，思路就是对于coins[i], 最多能够拿的硬币个数为amount // coins,
#对于每一个coins[i]的取值范围就是[0,amount//coins[i]],的整数，设为f(i),那么整个遍历的
#空间 复杂度就是 \prod_{i=0}^{n-1} f(i) = \prod_{i=0}^{n-1}{amount // coins[i] +1}
#然可以有减枝操作,对于coins[i] ,如果当前个数加在一起的和已经大于amount，那么后面的个数
#就不用考虑了
#但是时间复杂度巨高，考虑用动态规划
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """动态规划(完全背包问题),这里其实我还不会做，dp的定义是看书的
        定义：
            dp[i][j]是当有前i个coins，需要凑得钱为j时，可以凑成的方法的个数
        状态转移：
            首选选择就两个，当第i-1个(i-1是dp的索引，dp长度比coins长度大1)允许选择时：
                dp[i][j] = dp[i][j-coins[i-1]], ? 这里有个问题，这里为什么是dp[i][j-coins[i-1]]
                而不是dp[i-1][j-coins[i-1]](这是#416的写法)，应该是硬币可以重复使用的缘故
            当第i-1个coin不选时：
                dp[i][j] = dp[i-1][j]
            最终要求的是所有方法个数，因此应该是两者的和：
                dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
        base case:
            当i=0时，任何钱也凑不齐，dp[0][j] = 0
            当j=0时，不需要动，就直接凑齐了， dp[i][j] = 1
        """
        M = len(coins) + 1  #行
        N = amount + 1   #列
        dp = [[0] * N for _ in range(M)]
        for i in range(M):
            dp[i][0] = 1
        for i in range(1, M):
            for j in range(1, N):
                if j - coins[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        return dp[-1][-1] 
# @lc code=end

