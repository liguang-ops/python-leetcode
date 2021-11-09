'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-10 21:17:31
LastEditors: liguang-ops
LastEditTime: 2021-09-10 21:41:55
'''
#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            elif nums1[i] == nums2[j]:
                nums.extend([nums1[i]] * 2)
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                nums.append(nums2[j])
                j += 1
        nums.extend(nums1[i:] if i < len(nums1) else nums2[j:])
        mid = len(nums) // 2 
        return nums[mid] if len(nums) % 2 == 1 else (nums[mid] + nums[mid - 1])/2
# @lc code=end

