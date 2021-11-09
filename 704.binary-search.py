'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-03 21:00:34
LastEditors: liguang-ops
LastEditTime: 2021-09-03 21:29:35
'''
#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    #自己写的版本,逻辑上不通顺，虽然也AC了
    def search1(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = int(0.5*(start + end))
        while(nums[mid] != target):
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
            mid = int(0.5*(start + end))
            if start > end:
                return -1
        return mid
    
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while(start <= end):
            mid = int(0.5*(start + end))  #向下取整
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
# @lc code=end

