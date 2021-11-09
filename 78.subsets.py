'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-05 15:23:58
LastEditors: liguang-ops
LastEditTime: 2021-10-05 16:02:11
'''
#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        """没有仔细思考。(两个思路都是从书上来的)
        1. 数学归纳法， nums的子集个数是在nums[:-1]的基础上，再在nums[:-1]的子集的基础上加上nums[-1]
        得到的
        2. 回溯算法，但是我拘泥于回溯算法的形式框架，一直在找满足条件，但是一直没找到。我的确想到没有显式
        的回溯满足条件，或者说这里只要加进去就能够算一个答案，不用谢满足条件。所以我就一直在思考函数怎么停止，
        怎么控制重复。没想倒答案通过一个start参数就能很好的控制，很厉害
        """
        def getSubsets(nums):
            res = []
            if len(nums) == 1:
                return [[], nums]
            results = getSubsets(nums[:-1])   #计算nums[:-1]的子集个数
            res.extend(results)               #放入结果中
            for subset in results:            #遍历nums[:-1]的子集，在每个的基础上添上nums[-1]
                res.append(subset + [nums[-1]])
            return res
        return getSubsets(nums)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        #看代码还是很好懂的，让我自己写，还是不怎么会
        res = []   #存所有的子集
        def dfs(nums, start, subset):  #nums + start是选择列表，subset是已经做了的选择
            res.append(subset.copy())   #这里需要注意一下，如果不用copy(), 后面subset.append(nums[i])
            for i in range(start, len(nums)):  #会影响res中的结果，为什么这里用浅复制也可以呢，因为subset
                subset.append(nums[i])         #里面是值类型，不是引用类型，浅复制就够了
                dfs(nums, i + 1, subset)
                subset.pop()
        dfs(nums, 0, [])
        return res
# @lc code=end

