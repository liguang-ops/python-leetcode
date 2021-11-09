'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-06 16:29:24
LastEditors: liguang-ops
LastEditTime: 2021-09-06 21:26:33
'''
#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
class Solution:
    #时间复杂度O(n^2)时间复杂度太高
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 其实方法和#300类似，都是求最长递增子序列的问题
        # 我们只需要将这个二维数组，按第一列从小到大排序，
        # 然后再求第二列的最长递增子序列就能得到答案
        #先对二维列表排序
        envelopes = sorted(envelopes, key = lambda x : (x[0], -x[1]))
        #300方法
        dp = [1 for _ in range(len(envelopes))]  #初始化dpTable
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    #修改为二分搜索算法，时间复杂度O(nlogn) #300
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        #先对二维列表排序
        envelopes = sorted(envelopes, key = lambda x : (x[0], -x[1]))
        dp = [0 for _ in range(len(envelopes))]
        res = 0  #dp数组的有效长度
        for num in envelopes:
            left, right = 0, res  #左闭右开[left, right)
            #查找左侧边界的二分搜索算法，循坏结束后的left表示当前dp数组中小于num的有left个
            while(left < right):
                mid = left + (right - left) // 2
                if dp[mid] < num[1]:
                    left = mid + 1
                else:
                    right = mid
            dp[left] = num[1]  #把dp中第一个小于num的值用num覆盖，或者添加到尾部
            if right == res: #如果是添加到尾部，那么dp的有效长度+1
                res += 1
        return res
# @lc code=end

