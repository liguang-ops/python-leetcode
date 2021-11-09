'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-11 21:09:57
LastEditors: liguang-ops
LastEditTime: 2021-10-11 21:54:00
'''
#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum1(self, nums: List[int], k: int) -> int:
        """第一个方法是枚举全部的子数组，时间复杂度O(n!).
        有一种很简单的方法：前缀和，定义Presum[i]是nums[0...i]子数组的和，
        这样sum(nums[i...j]) = Presum[j] - Presum[i], 最后就剩下遍历O(n^2)
        时间复杂度还是太高，TLE
        """
        res = 0
        preSum = [sum(nums[:i]) for i in range(len(nums) + 1)]
        for i in range(len(preSum)):
            for j in range(i + 1, len(preSum)):
                if preSum[j] - preSum[i] == k:
                    res += 1
        return res
    def subarraySum(self, nums: List[int], k: int) -> int:
        """空间换时间。但是我不知道怎么做，只能看书。
        就是把preSum[j] == preSum[i]  + k存到字典里面，找的时候就能保证O(1)的查找时间复杂度，
        由于仍旧要遍历整个nums，时间复杂度O(n)
        """
        ans = 0 
        res = {}
        res[0] = 1
        nums_j, nums_i = 0, 0
        for num in nums:
            nums_j += num
            nums_i = nums_j - k
            if nums_i in res.keys():
                ans += res[nums_i]
            if nums_j in res.keys():
                res[nums_j] += 1
            else:
                res[nums_j] = 1
        return ans
# @lc code=end

