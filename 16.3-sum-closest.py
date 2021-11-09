'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-26 10:49:34
LastEditors: liguang-ops
LastEditTime: 2021-09-26 12:38:11
'''
#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums, target):
        """这一题和#15类似。求解的思路是一样的，都是二分搜索。主要在给解的时候需要修改一下
        """
        def twoSum(start, target):
            res = float('inf')
            closest = float('inf')
            left, right = start, len(nums) -1
            while left < right:
                lo, hi = nums[left], nums[right]
                sum = lo + hi
                if sum < target:
                    if target -sum < closest:
                        res = sum
                        closest = target - sum
                    while left < right and nums[left] == lo: 
                        left += 1
                else:
                    if sum - target < closest:
                        res = sum
                        closest = sum - target
                    while left < right and nums[right] == hi:
                        right -= 1
            return res, closest
        nums = sorted(nums, key=lambda x:x)
        i = 0
        result = float('inf')
        closest = float('inf')
        while i < len(nums):
            cur = nums[i]
            res, distance = twoSum(i+1, target - cur)
            #这边稍微有点绕：先找到最小距离，然后记录最小距离下的sum
            if distance < closest:
                result = res + cur
                closest = distance
            while i < len(nums) and cur == nums[i]: i+=1
        return result
# @lc code=end

