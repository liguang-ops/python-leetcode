'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-17 15:23:29
LastEditors: liguang-ops
LastEditTime: 2021-09-17 15:36:53
'''
#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """动态规划，这题貌似比较好做
        定义dp[i]是以nums[i]结尾的最长递增字串的长度，那么选择就两个nums[i]是否加入这个
        字串中
        状态转移方程：
            dp[i] = dp[i-1] + 1， nums[i] > nums[i-1]
            dp[i] = 1, nums[i] <= nums[i-1]
        base case:
            dp[0] = 1
        最后遍历整个dp数组，找到最大值
        """
        dp = [1] * len(nums)
        for i in range(1, len(dp)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
        return max(dp)
# @lc code=end

