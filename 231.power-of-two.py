'''
Description:
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-13 16:10:31
LastEditors: liguang-ops
LastEditTime: 2021-10-13 16:27:54
'''
#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """暴力循环就完事了
        """
        a = 0
        while 2 ** a < n:
            a += 1
        return 2 ** a == n

# @lc code=end

