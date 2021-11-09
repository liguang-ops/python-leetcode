'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-10 21:48:34
LastEditors: liguang-ops
LastEditTime: 2021-09-10 22:19:03
'''
#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        left, right = 0, len(s) -1
        while left < right: #到达相等的时候，就说明是回文串
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
    
    def isPalindrome1(self, x: int) -> bool:
        #上面的做法需要额外空间
        #转成字符串是为了取得最左边和最右边的数，因此，不转换成字符串也有得做
        #error:1000021,循环1取余得时候，0没有了,
        if x < 0: return False
        ranger  = 1
        while x / ranger >= 10 :  
            ranger *= 10
        while x >= 10:
            left = x // ranger
            right = x % 10
            if left != right: return False
            x = (x % 10) // 10
            ranger /= 100
        return True
        
# @lc code=end

