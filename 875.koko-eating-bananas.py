'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-24 20:07:08
LastEditors: liguang-ops
LastEditTime: 2021-09-24 20:47:41
'''
#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles, h):
        """思路其实就是暴力遍历。speed的最小值是1，最大值是max(piles)。因此最多只能吃一堆。
        要取得满足要求的最小值。我们可以发现在大于这个最小值之后，后面的都可以满足要求，而在这】
        之前都不可以。这就可以用搜索左边界的二分搜索，来查找最小值
        """
        left, right = 1, max(piles) + 1

        def canFinish(speed):
            time = 0
            for pile in piles:
                time += pile // speed + (1 if pile % speed !=0 else 0)
            return time <= h

        while left < right:  #搜索区间为[left, right)
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        return left
# @lc code=end

