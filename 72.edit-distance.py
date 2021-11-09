'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-07 17:27:07
LastEditors: liguang-ops
LastEditTime: 2021-09-08 15:34:51
'''
#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    #动态规划
    def minDistance1(self, word1: str, word2: str) -> int:
        """
        定义dp函数，dp(i,j)表示word1[0:i]和word[0:j]的编辑距离
        状态转移方程 dp(i,j) = (word1[i] == word2[j]) * dp(i-1, j-1) + 
        (word1[i] == word2[j]) * min(dp(i-1,j) + 1, dp(i,j-1) + 1, dp(i-1,j-1) + 1)
        base case: 
            当 i=0时， dp(0,j) = j+1
            当 j=0时， dp(i,0) = i+1
        解释：
            1. 首先base case：当i或者j等于0时，就代表求一个非空字符串和空字符串的编辑距离。
        此时，只需要将非空串全部插入到空串中，就能得到相同的字符串，操作次数等于非空串长度
            2. 当word1[i] = word2[j]，什么都不用做，直接跳过
            3. 当word1[i] != word2[j]，就需要找到进行插，删和替换操作的最小编辑距离：
                3.1 第一种， dp(i-1,j) + 1,相当于把word1[i]删除，这样去比较word1[i-1]和word2[j]
                3.2 第二种， dp(i,j-1) + 1,相当于在word1[i+1]处插入word2[j],这样，word1[i+1] = word2[j],j指针前移
                3.3 第三种， dp(i-1,j-1) + 1,相当于将word1[i]的字符替换成word2[j]的字符，word1[i]=word2[j]，两个指针都前移
        """
        #注意，和#1143LCS一样,需要在原字符串前面加一个空字符，成为一个新字符串
        #这边要注意i,j的定义，我们定义成新字符串的索引，因此，相比较原字符串，索引大了1
        #在索引原字符串时需要-1
        #在没有备忘录的情况下，会TLE，加了备忘录就会AC
        books = {}
        def dp(i, j):
            if (i,j) in books.keys():
                return books[(i,j)]
            if i == 0: return j
            if j == 0: return i
            if word1[i-1] == word2[j-1]:  #加了空字符的字符串比源字符串索引小1
                books[(i,j)] = dp(i-1, j-1)
            else:
                books[(i,j)] = min(
                    dp(i-1, j) + 1,
                    dp(i, j-1) + 1,
                    dp(i-1, j-1) + 1
                )
            return books[(i,j)]
        return dp(len(word1), len(word2))

    def minDistance(self, word1: str, word2: str) -> int:
        #这边再用dpTable实现一边，dp数组的定义和dp函数的定义是一样的
        #定义dp数组，一样的道理，在字符串头部加一个空字符
        #注意：
        #   dp[0,:] = [0, 1, ..., len(word2)]
        #   dp[:,0] = [o,1, ..., len(word1)]
        #这就是边界条件，base case.可以这么理解，一个空字符和一个开头为空的字符串计算编辑距离。
        dp = [list(range(len(word2)+1)) if i == 0 else [i] * (len(word2)+1) for i in range(len(word1) + 1)]  #行是len(word1)+1,列是len(word2)+1
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    ) + 1
        return dp[len(word1)][len(word2)]
# @lc code=end

