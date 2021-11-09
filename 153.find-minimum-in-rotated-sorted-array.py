'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-04 20:55:52
LastEditors: liguang-ops
LastEditTime: 2021-09-07 09:48:28
'''
#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #二分法，和#33一样的思路
        left = 0
        right = len(nums) - 1
        while(left < right): #当区间大小为1的时候，该数即为最小的数
            mid = (right + left) // 2
            #首先判断那一部分是有序的，其次，由于该序列是递增的，
            #因此，最小数一定在无序的那一边
            if nums[mid] > nums[right]:  #左边有序
                left = mid + 1  #最小值在右边
            elif nums[mid] <= nums[right]: #右边有序
                right = mid #这里不能加1应为nums[mid]可能是最小值
        #这里right= mid,为什么不用加1，我们还是从搜索区间去考虑：
        #原始搜索区间是[left, right],当计算完nums[mid]后，区间就分为两部分，
        #第一部分是[left, mid], 第二部分为[mid+1,right],因此，right = left
        #求最大最小值问题，不是查找问题，因此无法直接排除nums[mid]
        return nums[right]
# @lc code=end

