'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-06 14:43:26
LastEditors: liguang-ops
LastEditTime: 2021-09-06 15:28:25
'''
#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        #最长无重复字串，也就是要求window中所有字符个数为1，返回最长的那个窗的长度
        left, right = 0, 0
        window = {i:0 for i in s}
        length = 0
        while(right < len(s)):
            c = s[right]
            right += 1
            if window[c] == 0:  #如果当前字符在计数器中个数为0
                length = max(length, right - left)
            window[c] += 1  #计数器+1
            while(window[c] > 1):
                d = s[left]
                left += 1
                window[d] -= 1
        return length

    def lengthOfLongestSubstring(self, s: str) -> int:
        #最长无重复字串，也就是要求window中所有字符个数为1，返回最长的那个窗的长度
        left, right = 0, 0
        window = {i:0 for i in s}
        length = 0
        while(right < len(s)):
            c = s[right]
            right += 1
            window[c] += 1
            while(window[c] > 1):  #如果当前字符在计数器中个数大于一
                d = s[left]
                left += 1
                window[d] -= 1
            #缩小完左边界后，更新长度，这是能够保证是无重复的 
            length = max(length, right - left)
        return length

    
# @lc code=end

