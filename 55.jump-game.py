'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-14 22:41:25
LastEditors: liguang-ops
LastEditTime: 2021-10-15 22:59:29
'''
#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """贪心算法, 首先，要直到，如果能达到这个点，那一定能达到这个点之前的所有点
        furthest记录了全局远点，遍历更新最远点
        """
        furthest = 0
        for i in range(0, len(nums)-1):
            furthest = max(furthest, i + nums[i])
            if furthest <= i:
                return False
        return furthest >= len(nums)-1
# @lc code=end

