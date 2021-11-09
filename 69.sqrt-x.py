'''
Description:
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-04 11:05:50
LastEditors: liguang-ops
LastEditTime: 2021-09-04 11:52:30
'''
#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    #有很多种解法，这里先用二分法(保证函数单调)
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x   #闭区间，因为1^2=1
        while(left <= right):   #闭区间，所以用<=,跳出条件为right<left
            mid = left + (right - left) // 2
            val = mid ** 2
            if val == x:
                return mid
            elif val < x:
                left = mid + 1
            elif val > x :
                right = mid - 1
        return right

        
# @lc code=end

