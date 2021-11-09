'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-06 15:39:07
LastEditors: liguang-ops
LastEditTime: 2021-09-06 21:20:28
'''
#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))] #dp数组定义以dp[i]结尾的最长子序列的长度，初始化为1
        for i in range(1, len(nums)): #nums中第一个值不用看
            temp = 0
            for j in range(i):        #比较当前数nums[i]和nums[0:i-1]大小
                if nums[i] > nums[j]: #获取在nums[0:i-1]中比nums[i]小的数的dp最大值
                    temp = max(temp, dp[j])
                    dp[i] = temp + 1
        return max(dp)

        #有一种更优美一点的写法，
        #获取在nums[0:i-1]中比nums[i]小的数的dp最大值再加1，就是获取
        #+1后的最大值
    def lengthOfLIS2(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)): #nums中第一个值不用看
            for j in range(i):        #比较当前数nums[i]和nums[0:i-1]大小
                if nums[i] > nums[j]: #获取在nums[0:i-1]中比nums[i]小的数的dp最大值
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    #前两种时间复杂度太高O(n^2),修改为二分查找，时间复杂度O(nlogn)
    def lengthOfLIS(self, nums: List[int]) -> int:
        #维护一个新的dp数组，定义为:dp[i]表示长度为i的递增子序列的尾
        dp = [0 for _ in range(len(nums))] #长度为N
        res = 0
        for num in nums:
            left, right = 0, res
            while(left < right):   #搜索左边界的二分搜索算法，循坏结束后的left表示当前dp数组中小于num的有left个
                mid = left + (right - left) // 2
                if dp[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            dp[left] = num
            if right == res:
                res+=1
        return res
# @lc code=end

