'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-26 13:13:54
LastEditors: liguang-ops
LastEditTime: 2021-09-26 13:58:03
'''
#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """标准dfs，貌似没有更好的解法 
        """
        if len(digits) == 0: return []
        results = []
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', \
                '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def dfs(s, i):
            if len(s) == len(digits):
                results.append(s)
                return
            for c in dic[digits[i]]:  #遍历当前层的所有选择
                s += c                #添加这个选择
                dfs(s, i+1)           #进入下一层
                #s = s.strip(c)  #这样写不对，strip去掉的是字符串首尾所有等于c的值
                s = s[:-1]            #取消这个选择
        dfs('', 0)
        return results       
# @lc code=end

