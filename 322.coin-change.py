'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-01 14:08:44
LastEditors: liguang-ops
LastEditTime: 2021-09-01 14:26:29
'''
#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount +1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i -coin])
        return dp[amount] if dp[amount] != amount +1 else -1
# @lc code=end

