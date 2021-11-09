'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-18 12:51:40
LastEditors: liguang-ops
LastEditTime: 2021-09-18 13:45:17
'''
#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        comPre = ""
        sptr = 0     #字符串中每一个字符的索引
        strsPtr = 1  #从索引为1的字符串开始
        cond = True
        if len(strs) == 1: return strs[0] 
        while sptr < len(strs[strsPtr]) and sptr < len(strs[strsPtr -1]):  #当前字符索引没超过当前字符串长度
            cond = cond and strs[strsPtr][sptr] == strs[strsPtr - 1][sptr] 
            if not cond:  #某两个字符不相等
                break
            elif strsPtr == len(strs) -1 and cond:  #字符都相等,将该字符加入comPre
                comPre += strs[strsPtr][sptr]
                strsPtr = 1  #重新回到第二个字符串
                sptr += 1    #搜索的字符向后移一个
            else:  #当前两个字符相等，但是还没到最后一个时，判断下一个字符串
                strsPtr +=1  
        return comPre

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """好像有种更好的方法，但我感觉时间复杂度差不多，上一个方法我也减枝了
        这里，先将字符串数组根据字符串长度升序排序，然后再计算,AC和上面的runtime没区别
        """
        strs = sorted(strs, key= lambda x :len(x)) #先升序排序
        N = len(strs[0])  #最多需要遍历字符的次数
        cond = True
        comPre = ""
        if len(strs) == 1: return strs[0] 
        for i in range(N):
            for j in range(1, len(strs)):
                cond = cond and strs[j-1][i] == strs[j][i]
                if not cond:
                    return comPre
                elif j == len(strs) -1 and cond:
                    comPre += strs[j][i]
        return comPre
# @lc code=end

