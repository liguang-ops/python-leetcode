'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-22 16:20:28
LastEditors: liguang-ops
LastEditTime: 2021-09-22 16:27:03
'''
#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        """还是动态规划，如果是环形情况，这样考虑:如果取了头，就不能取尾；如果取了尾
        就不能取头，因此把这个nums数组分成两种情况讨论：nums[0:-1];nums[1:]
        取两者最大的就ok
        """
        if len(nums) == 1: return nums[0]
        def dp(start, end):
            dp_i_2, dp_i_1 = 0, 0
            for i in range(end, start-1, -1):
                dp_i = max(dp_i_1,  #不取第i个，因此就等于后面那一个
                            nums[i] + dp_i_2)  #取第i个
                dp_i_2 = dp_i_1
                dp_i_1 = dp_i
            return dp_i
        return max(dp(0, len(nums)-2), 
                    dp(1, len(nums)-1))
# @lc code=end

