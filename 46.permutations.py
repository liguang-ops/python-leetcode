'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-05 16:43:57
LastEditors: liguang-ops
LastEditTime: 2021-10-05 16:47:29
'''
#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """这就是简单的排列问题，回溯
        """
        res = []
        def dfs(nums, per):
            if len(per) == len(nums):
                res.append(per.copy())
                return
            for i in range(len(nums)):
                if nums[i] in per:
                    continue
                per.append(nums[i])
                dfs(nums, per)
                per.pop()
        dfs(nums, [])
        return res
# @lc code=end

