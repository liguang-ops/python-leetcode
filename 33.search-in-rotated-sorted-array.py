'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-04 19:54:16
LastEditors: liguang-ops
LastEditTime: 2021-09-04 20:48:00
'''
#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #题目要求时间复杂度O(logn)，肯定要用二分搜索
        #虽然排序数组被旋转了，但是可以确定的是将这个数组从中间切开时，
        #一定有一半的数组是有序的，只要确定了那部分是有序的，就得到结果了
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            #将中间的数和最右的数进行比较
            #   nums[mid] > nums[right],左边是有序的
            #   nums[mid] < nums[right],右边是有序的
            #之后只需判断在有序的数组中是否有target就行
            elif nums[mid] > nums[right]:  #左边有序
                if nums[left] <=target and target< nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:  #右边有序
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1
# @lc code=end

