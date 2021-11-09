#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roamn = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        left = 0
        integer = 0
        while left < len(s):
            if (left + 1) <= (len(s) -1) and roamn[s[left]] < roamn[s[left + 1]]:  #4或9
                integer += roamn[s[left + 1]] - roamn[s[left]]
                left += 2
            else:
                integer += roamn[s[left]]
                left += 1
        return integer
# @lc code=end

