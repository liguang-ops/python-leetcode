'''
Description:
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-12 20:53:31
LastEditors: liguang-ops
LastEditTime: 2021-10-13 12:47:34
'''
#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes1(self, n: int) -> int:
        """这一题是easy题，大概率直接不考虑时间复杂度也能ok
        先写最简单的, TLE了
        """
        def isPrimes(n):
            i = 2
            while i * i <=n:
                if n % i == 0:
                    return False
                i += 1
            return True  
        counts = 0
        for i in range(2, n):
            if isPrimes(i):
                counts += 1
        return counts
    
    def countPrimes(self, n: int) -> int:
        """另一种解法，更快速，但是我没想到。
        用传染法：如果cur是素数，那么 i x cur 肯定不是素数，i x cur \in n 
        """
        if n in [0, 1]:
            return 0
        #新建一个标记数组
        isPrimeList = [True] * n
        for i in range(2, n):
            if isPrimeList[i]:
                #for j in range(2 * i, n, i): 这样写还是有一部分数据重算了
                #比如i=4，4x2=8, 4x3=12，已经在i=2，2x4=8, 3x4=12算过了
                for j in range(i * i, n, i):
                    isPrimeList[j] = False
        counts = isPrimeList.count(True) - 2 #索引0-1不需要
        return counts
# @lc code=end

