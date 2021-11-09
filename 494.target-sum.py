'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-23 21:07:52
LastEditors: liguang-ops
LastEditTime: 2021-09-24 19:55:44
'''
#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        """dfs, 先暴力走一遍,选择就是当前num是加号还是减号，test case 可以通过，
        但是submit就会TLE
        """
        res = 0
        def dfs(ptr):
            nonlocal res
            if ptr == len(nums):
                if sum(nums) == target:
                    res +=1
                return
            for sign in [-1, 1]:
                nums[ptr] = sign * nums[ptr]  #做选择
                dfs(ptr + 1)  #进入下一层
                nums[ptr] = sign * nums[ptr]  #撤回选择
        dfs(0)
        return res
    
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        """递归+备忘录
            dp(ptr, rest) 指数组在rest下，nums[0...ptr]计算能够的次数
        """
        memo = {}
        def dp(ptr, rest):
            if ptr == len(nums):
                if rest == 0:
                    return 1
                return 0
            if (ptr, rest) in memo:
                return memo[(ptr, rest)]
            results = dp(ptr+1, rest-nums[ptr]) + dp(ptr+1, rest + nums[ptr])
            memo[(ptr, rest)] = results
            return results
        return dp(0, target)

    def findTargetSumWays3(self, nums: List[int], target: int) -> int:
        """动态规划：
            定义dp[i][j]是nums[0...i]能够计算出j的次数
            状态转移方程：
                首先由两个选择，+ 或者-，应该是取这两种情况的和
                dp[i][j] = dp[i-1][j-nums[i]]  注意，这里其实是做+
                dp[i][j] = dp[i-1][j-(-nums[i])] ,这里是-
                取二者的和
                    dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j-(-nums[i])]
        我觉得这样定义是可以的，但是target可以为负数，就无法当作索引了，应该有更好的定义方法
        """
        pass
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """动态规划：转化为背包问题。思路如下：
        可以将题目转换一下思路(这样做的前提条件是nums中的数全是非负数)：将数组中的数分为两份，一份+背包A，一份减背包B，
        sum(A) -sum(B) = target
        sum(A) = target + sum(B), 两边再加上sum(A) 
        sum(A) + sum(A) = target + sum(A) +sum(B) = target + sum(nums)
        即sum(A) = (target + sum(nums)) /2,问题转换为nums中有多少个子集A满足左边的等式，即子集背包问题
        同样：定义dp[i][j]为当背包容量为j、nums[0...i]有dp[i][j]个子集A恰好能够装满背包
        选择很简单，就是nums[i]是否放入背包：
            dp[i][j] = dp[i-1][j -nums[i]]  这是放入背包
            dp[i][j] = dp[i-1][j], 不放入背包
        求和：
            dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j],这里注意nums索引和dp索引差1
        base case：
            当i=0时，没有东西，肯定无法放满背包， dp[0][j] = 0
            当j=0时， 不用放东西，直接就满了，dp[i][0] = 1
        """
        if target > sum(nums) or (target + sum(nums))  % 2 !=0 or target + sum(nums) < 0:
            return 0
        dp = [[0] * ((sum(nums) + target) // 2 + 1) for _ in range(len(nums) + 1)]

        for i in range(len(dp)):  #初始化状态
            dp[i][0] = 1 

        for i in range(1, len(dp)):
            for j in range(0, len(dp[i])):  #这里很奇怪，为什么j从0开始。以往的子集背包问题都是从1开始
                if j - nums[i-1] >=0:       #如果从1开始，测试用例[0,0,0,0,1]\n1不通过。这边不是很明白。
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]    
# @lc code=end

