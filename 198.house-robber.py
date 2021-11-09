'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-20 09:51:57
LastEditors: liguang-ops
LastEditTime: 2021-09-20 11:28:32
'''
#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        """还是动态规划
        定义：dp[i]是从子数组nums[i...]中能取到的最大值
        状态转移： 
            dp[i] = dp[i-1], 此时nums[i]不拿，
            dp[i] = nums[i] + dp[i-2], 此时拿了nums[i]
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        base case:
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
        """
        if len(nums) == 1: return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]
# @lc code=end

