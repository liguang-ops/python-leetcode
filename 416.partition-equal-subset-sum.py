'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-15 20:48:52
LastEditors: liguang-ops
LastEditTime: 2021-09-15 21:46:12
'''
#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """动态规划：可转换成0-1背包问题
        转换一下：求一个容量为sum/2的背包能否恰好装满，其中sum是nums的和
        定义dp函数：
            dp[i][j]表示对于前i物品，背包容量为j，True表示恰好能够装满，False
            表示没法装满
        状态转移：
            dp[i][j] = dp[i-1][j- nums[i-1]], nums[i-1]装入背包
            dp[i][j] = dp[i-1][j], nums[i-1]不装入背包
        base case:
            当j=0的时候，相当于背包已经是满的，因此，dp[...][0] = True
            当i=0的时候，相当于没有物品，那么背包肯定装不满，因此，dp[0][...] = False
        """
        if sum(nums) % 2 !=0 :  return False
        N = sum(nums) // 2 + 1#背包重量
        M = len(nums) + 1   #单个物品重量
        dp = [[False] * N for _ in range(M)] #M行，N列
        for i in range(M):
            dp[i][0] = True

        for i in range(1, M):
            for j in range(1, N):
                if j - nums[i -1] < 0:    #背包装不下，因此第nums[i-1]不放进去，其值就和dp[i-1][j]一样
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j] #nums[i-1]装入背包和不装入背包
        return dp[-1][-1]
# @lc code=end

