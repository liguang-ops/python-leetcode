'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-14 15:01:35
LastEditors: liguang-ops
LastEditTime: 2021-09-15 09:52:49
'''
#
# @lc app=leetcode id=887 lang=python3
#
# [887] Super Egg Drop
#

# @lc code=start
class Solution:
    def superEggDrop1(self, k: int, n: int) -> int:
        """动态规划
        定义dp函数：dp(k, n)是鸡蛋个数为k, 楼层个数为n时的最坏情况下的最小查找次数
        状态转移：
            假设我们在第i层扔下一颗鸡蛋，如果鸡蛋碎了，那么鸡蛋个数-1，搜索楼层就变为1~i-层,层数为i-1；
            如果鸡蛋没有碎，那么鸡蛋个数不变，搜索楼层就变为i+1 ~N层，层数为N-i层。但是其实我们把并不知道
            在第i层鸡蛋到底碎不碎，因此，我们需要取这个的最大值，才能保证是在最坏情况下.然后遍历所有楼层
            取得最小值
            这样，状态转移方程就出来了：
                dp(k, n) = min(dp(k,n), max(dp(k-1,i-1), dp(k, N-i))) ,i \in [0, N]
        base case:
            当k = 1时，只能线性扫描，dp(1, N) = N
            当N = 0时，不需要判断，dp(k, N) = 0  
        """
        #TLE,但是代码没错
        visited = {}
        def dp(k, n):
            if (k, n) in visited:
                return visited[(k, n)]
            if k == 1: return n
            if n == 0: return 0
            res = float('INF')
            for i in range(1, n+1):
                res =min(res, max(dp(k-1, i-1), dp(k, n-i)) + 1) 
            visited[(k, n)] = res
            return res
        return dp(k,n)

    def superEggDrop(self, k: int, n: int) -> int:
        """动态规划，上面时间复杂度为O(kn^2),TLE
        对于dp(k, n),我们可发现，当n增大时，dp(k,n)肯定是增大的，也就是说对于n来说，dp(k,n)单增。
        观察dp(k-1, i-1)，i \in [1,n+1]，是单增函数，dp(k, n-i), i \in [1,n+1]是单减函数。
        那么求min(max(dp(k-1, i-1), dp(k, n-i))),就是求这两个函数的交点(离散点)。
        因此，可以用二分法。时间复杂度降至O(knlogn)
        """
        #懂了二分法为什么可以找到二者最大值的最小值。求min(max(dp(k-1, i-1), dp(k, n-i))),
        #事实上就是求一条V型线的谷点(Valley)
        visited = {}
        def dp(k, n):
            if (k, n) in visited:
                return visited[(k, n)]
            if k == 1: return n
            if n == 0: return 0
            res = float('INF')
            #用二分搜索代替线性搜索
            left, right = 1, n
            while left <= right:
                mid = (left + right) // 2
                broken = dp(k-1, mid-1)
                notBroken = dp(k, n-mid)
                if broken > notBroken:
                    right = mid - 1
                    res = min(res, broken + 1)
                else:
                    left = mid + 1
                    res = min(res, notBroken + 1)
            visited[(k, n)] = res
            return res
        return dp(k, n) 
# @lc code=end

