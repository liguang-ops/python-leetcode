'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-24 20:55:07
LastEditors: liguang-ops
LastEditTime: 2021-09-26 09:54:36
'''
#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """和#875类似，也是二分查找优化，载货能力最小max(weights),最大sum(weights)
        这一题和#875让我感觉最难的不是写二分查找(二分查找只要想到了就很简单)，我觉得难的
        是怎样实现canFinish这个函数。
        """
        left, right = max(weights), sum(weights) + 1

        def canFinish(boatload):
            #思路是这样的，将weight[i]一个一个向容量为boatload的瓶子里面放，如果当前weight[i]
            #放不下了，那就新拿一个瓶子，然后放进去
            realDays = 1  #为什么这里是1，已经开始减了，或者说第一个瓶子已经在上面了，开始放了
            temp = boatload
            for weight in weights:
                if temp - weight >= 0:  #瓶子还没满，更新瓶子的剩余容量
                    temp -= weight
                else:
                    realDays += 1      #前一个瓶子已经满了，新拿一个瓶子
                    temp = boatload    #更新瓶子容量
                    temp -= weight     #将这个weight[i]放入新瓶子，更新瓶子容量
            return realDays <= days
        
        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        return left 

# @lc code=end

