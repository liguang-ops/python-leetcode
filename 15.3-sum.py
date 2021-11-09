'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-25 22:24:43
LastEditors: liguang-ops
LastEditTime: 2021-09-26 10:38:51
'''
#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """3sum问题可以转化为2sum问题：对于列表中每一个值，放入结果列表中，
        之后就是计算target - nums[i] 的2sum问题
        """
        if len(nums) < 3: return []
        results = []
        def twoSum(start, target):
            res = []
            left, right = start, len(nums) - 1
            while left < right:     #只允许用两个数组中的数，不允许重复
                lo, hi = nums[left], nums[right]
                sum = lo + hi
                if sum < target:
                    while left < right and nums[left] == lo:  #这边是和#1不一样的地方，
                        left += 1  #因为3sum有重复值，算的时候要去掉重复值
                elif sum > target:
                    while left < right and nums[right] == hi:  #一样的道理
                        right -= 1
                else:
                    res.append([lo, hi])
                    while left < right and nums[left] == lo: left += 1  #一样的道理
                    while left < right and nums[right] == hi: right -= 1 #一样的道理
            return res
        
        nums = sorted(nums, key = lambda x : x) 
        i = 0
        while i < len(nums):
        #for i in range(len(nums)):   #这里不可以用迭代式，否则后面的i+=1无法正确触发，因为迭代式
            cur = nums[i]             #中的i是只读的
            res= twoSum(i + 1, 0 - cur)
            for r in res:
                results.append([cur, *r])
            while i < len(nums) and cur == nums[i]: i += 1  #一样的道理，去掉重复值
        return results


# @lc code=end

