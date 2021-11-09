'''
Description:
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-19 17:16:10
LastEditors: liguang-ops
LastEditTime: 2021-10-19 19:09:43
'''
#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """和#26有点像, 双指针交换
        """
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            elif nums[left] != val and nums[right] == val:
                right -= 1
            elif nums[left] == val and nums[right] == val:
                right -= 1
            elif nums[left] != val and nums[right] != val:
                left += 1
        return left 
# @lc code=end

