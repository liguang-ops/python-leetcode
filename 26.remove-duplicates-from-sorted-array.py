'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-14 21:55:07
LastEditors: liguang-ops
LastEditTime: 2021-10-14 22:36:47
'''
#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates1(self, nums: List[int]) -> int:
        """in-place, 要求在原地改。一开始我拿到的思路是双指针，快的那一个和慢的一样就删掉
        快的，然后快的前进1，如果不一样，两个同时前进1
        """
        slow, fast = 0, 1
        while slow < len(nums)-1:  # 注意nums长度是变化的
            if nums[slow] == nums[fast]:
                del nums[fast]  #nums变短了，就相当于fast + 1了
            else:
                slow += 1
                fast += 1
        return slow + 1

    def removeDuplicates(self, nums: List[int]) -> int:
        """上面做法有一个问题，python列表我忘了底层数据结构是什么了。但如果对于其他语言的数组来说，
        从中间删除是非常低效的。因此，更好的方法是交换，把相同的中fast交换和slow+1位置互换
        """
        slow, fast =0, 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1
# @lc code=end

