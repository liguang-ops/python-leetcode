'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-15 11:18:43
LastEditors: liguang-ops
LastEditTime: 2021-09-15 15:27:52
'''
#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins1(self, nums:List[int]) -> int:
        """DFS,肯定会TLE。但是当作DFS练习
        """
        res = 0
        def dfs(score, nums):
            nonlocal res  #闭包，非局部作用域
            if len(nums) == 0:
                res = max(res, score)
                return
            for i in range(len(nums)):
                temp = nums[i]
                if len(nums) == 1:
                    curPoint = 1 * nums[i] * 1
                elif i == 0:  #这个值是起点
                    curPoint = 1 * nums[i] * nums[i+1]
                elif i == len(nums) - 1:
                    curPoint = nums[i-1] * nums[i] * 1
                else:
                    curPoint = nums[i-1] * nums[i] * nums[i+1]
                #这里把nums[i]是删掉
                del nums[i]
                dfs(score+ curPoint, nums)
                #这里把nums[i]添加回来
                nums.insert(i, temp)
        dfs(0, nums)
        return res

    def maxCoins(self, nums:List[int]) -> int:
        """动态规划
        首先，题目告诉我们，如果选择的数字在数组两边，或者数组只有一个数字，那么在两边
        不够的地方添1。那么我们可以在一开始就在数组左右两边添1，这样数组长度+2
        然后，定义dp[i,j]是子数组nums[i+1...j-1]最大计算值，注意dp[i,j]对于对于子数组而言是
        开区间，不包括气球i和气球j
        状态转移：
            定义区间(i,j)之间最后一个被戳的气球为k，那么状态转移方程：
                dp[i][j] = max(dp[i][k] + dp[k,j] + nums[i] * nums[k] *nums[j]), k \in (i,j)
        base case:
            当i <= j 的时候，区间长度为0，dp[i][j] = 0
        最后，我们要求的是dp[0,n+1],因此，可以判断出来遍历顺序是从下到上，从左到右
        """
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for i in range(len(dp)-2, -1, -1):
            for j in range(i+1, len(dp[i])):
                for k in range(i+1,j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + \
                        nums[i] * nums[k] * nums[j])
        return dp[0][-1]
# @lc code=end

