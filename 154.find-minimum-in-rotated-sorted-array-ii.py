'''
Description:
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-05 11:47:12
LastEditors: liguang-ops
LastEditTime: 2021-09-07 09:49:13
'''
#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while(left < right): #区间长度为1的时候，该值就是所求
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:  #右边有序，最小值在左边
                #这里right= mid,为什么不用加1，我们还是从搜索区间去考虑：
                #原始搜索区间是[left, right],当计算完nums[mid]后，区间就分为两部分，
                #第一部分是[left, mid], 第二部分为[mid+1,right],因此，right = left
                #求最大最小值问题，不是查找问题，因此无法直接排除nums[mid]
                right = mid   
            elif nums[mid] > nums[right]: 
                left = mid + 1
            else:   #中间点和右端点相等时，缩小右端点
                right -= 1
        return nums[right]
# @lc code=end

