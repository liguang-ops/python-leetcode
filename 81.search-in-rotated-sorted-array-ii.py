'''
Description:
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-05 12:55:14
LastEditors: liguang-ops
LastEditTime: 2021-09-06 22:42:03
'''
#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #二分搜索
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[right]: #右边界有序
                if nums[mid] < target and target <= nums[right]:  #target在右边
                    left = mid + 1
                else:  #taeget 在左边，或者没有
                    right = mid - 1
            elif nums[mid] > nums[right]: #左边有序
                if nums[left] <= target and target < nums[mid]:    #target在左边
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] == nums[right]:
                right -= 1  #中间点和右端点相等时，缩小右端点
        return False
# @lc code=end

