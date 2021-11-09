'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-26 14:01:42
LastEditors: liguang-ops
LastEditTime: 2021-09-26 16:24:25
'''
#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """nSum类型题，当然可以用之前#15的模板，在外面多加一层就可以。
        事实上，我们可以把它们抽象出来成为一个nSum题，不严格的来说，倒是有点像dfs
        求nSum，可以转化为求(n-1)(Sum - nums[i])，直到n=2，这样就回到了#1；或者n=3,
        这样就回到了#15
        """
        nums = sorted(nums, key=lambda x:x)
        return self.nSum(nums, 4, 0, target)
    
    def nSum(self, nums, n, start, target):
        res = []
        if n < 2 or len(nums) < n: return res
        elif n == 2:  #base case, 就是2Sum那一套
            left, right = start, len(nums) - 1
            while left < right:
                lo, hi = nums[left], nums[right]
                sum = lo + hi
                if sum < target:
                    while left < right and nums[left] == lo:
                        left += 1
                elif sum > target:
                    while left < right and nums[right] == hi:
                        right -= 1
                else:
                    res.append([nums[left], nums[right]])
                    while left < right and nums[left] == lo: left += 1
                    while left < right and nums[right] == hi: right -= 1
        else:   #其他情况，nSum转为(n-1)(Sum - nums[i])
            i = start
            while i < len(nums): 
                cur = nums[i]
                ress = self.nSum(nums, n-1, i+1, target - cur)   #计算出(n-1)(Sum - nums[i])
                for r in ress:  #遍历算出的结果，加上cur， r + cur = target
                    res.append([cur, *r])
                while i < len(nums) and cur == nums[i]: i +=1  
        return res
# @lc code=end

