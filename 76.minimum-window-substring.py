'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-05 20:59:34
LastEditors: liguang-ops
LastEditTime: 2021-09-06 12:03:34
'''
#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #滑动窗口题，双指针
        left, right = 0, 0
        valid = 0  #记录当前窗口中数量已满足的字符的数量
        #window存 在当前窗口[left, right)中，t中每一个字符的数量，初始化为0
        window = {i:0 for i in t}
        #need存在当前窗口的情况下，t中每一个字符还需要的数量,初始为t中每个字符的数量
        need = window.copy()  #没有子对象，因此只需要浅复制
        for i in t:
            need[i] += 1
        start, length = 0, len(s) + 1 #记录当前最小字串的起始位置和长度
        while right < len(s):  #当right超过字符长度时结束
            c = s[right]
            right += 1  #窗口右指针向右+1
            if c in window.keys():  #如果当前字符是需要的，数量+1
                window[c] += 1  
                if window[c] == need[c]: #如果当字符在window中的数量够了，计数器+1
                    valid += 1
            #当窗口内的所有字符满足t时，开始缩小左边
            while valid == len(need):  #
                if right - left < length:  #如果当前符合要求的字串比之前记录的字串小，更新
                    start = left
                    length = right - left
                c = s[left]
                left += 1  #窗口左指针向右+1
                if c in window.keys():
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return "" if length == len(s) + 1 else s[start:start+length]

# @lc code=end

