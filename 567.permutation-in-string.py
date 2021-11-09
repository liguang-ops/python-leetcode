'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-05 22:41:42
LastEditors: liguang-ops
LastEditTime: 2021-09-06 12:02:36
'''
#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #和#76一样的问题，有一种暴力解法，利用#76的方法算出最小substring，
        #然后判断当前最小字串长度是否和s1相等，相等就是True，否则就是False
        #当然，这样时间复杂度会更高一点，因为需要全部遍历s2
        #因此，更简单的方法是在更新字串时，直接判断其长度，如果相等，就直接返回
        #会更快
        left, right = 0, 0
        window = {i:0 for i in s1}
        need = window.copy()
        for i in s1:
            need[i] += 1
        valid = 0  #另外，这里不需要start和length去记录最小字串，找到一个直接返回
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in window.keys():
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            #当窗口长度大于等于s1的长度，因为是找全排列，所以不会比s1长
            while right - left >= len(s1):
                if valid == len(need):
                    return True
                c = s2[left]
                left += 1
                if c in window.keys():
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return False      
# @lc code=end

