#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #滑动窗口
        left, right = 0, 0
        window = {i:0 for i in p}
        need = window.copy()
        for i in p:
            need[i] += 1
        valid = 0
        result = []
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while right - left >= len(p):
                if valid == len(need):
                    #这里不需要重置left和right，因为window中还保存着有效信息，left是一位一位移的
                    result.append(left)   #满足，将结果放进去
                c = s[left]
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return result
# @lc code=end

