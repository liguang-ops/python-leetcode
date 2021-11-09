'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-07 10:11:13
LastEditors: liguang-ops
LastEditTime: 2021-09-07 10:59:24
'''
#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        #仍是dp题
        #定义，dp[i]表示已nums[i]结尾的最长子数组的和
        #转移方程：dp[i] = max(nums[i], dp[i-1] + nums[i]),子数组，因此下标一定
        #是连续的，只需要判断i和i-1就行
        dp = nums.copy() #初始化为本身
        for i in range(1, len(dp)):
            dp[i] = max(dp[i], dp[i-1] + dp[i])
        return max(dp)
    def maxSubArray(self, nums: List[int]) -> int:
    #可以发现，dp[i]只与dp[i-1]有关
        if len(nums) == 1: return nums[0]
        dp_0, dp_1 = nums[0], nums[1]
        res = dp_0
        for i in range(1, len(nums)):
            dp_1 = max(nums[i], dp_0 + nums[i])
            dp_0 = dp_1
            res = max(res, dp_1)
        return res
    #AC,但是所用的时间和空间确没上面的好
# @lc code=end

