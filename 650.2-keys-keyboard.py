'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-13 15:26:51
LastEditors: liguang-ops
LastEditTime: 2021-09-13 21:17:08
'''
#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#

# @lc code=start
from queue import Queue
class Solution:
    def minSteps1(self, n: int) -> int:
        """BFS,事实上是求操作树的最小深度，每一个节点(num,copy),num是当前屏幕上
        A的个数，copy是剪贴板上A的个数。每个节点有两条边，分别是ctrl-c和ctrl-v,
        变化过程：
        (num, copy) xrightarrow{ctrl-c} (num, num)
        (num, copy) xrightarrow{ctrl-v} (num+copy, copy)
        当num == n 时，返回当前节点的深度"""
        q = Queue()
        q.put((1,0))
        depth = 0
        visited = set()
        while not q.empty():  #队列不为空
            size = q.qsize()  #当前层的节点数
            for _ in range(size):
                cur = q.get()
                if cur[0] == n:
                    return depth
                for op in ['cc', 'cv']:
                    if op == 'cc':
                        next = (cur[0], cur[0])
                    else:
                        next = (cur[0]+cur[1], cur[1])
                    if next not in visited:
                        q.put(next)
                        visited.add(next)
            depth +=1
        return -1
    
    def minSteps(self, n: int) -> int:
        """动态规划：
            定义dp[i]是生成i个A的最小操作次数，默认值应该是dp[i] = i,表示一个一个的黏贴
            状态转移方程：dp[i] = min(dp[i], dp[j] + dp[i/j]), 其中i能够被j整除，且j>=2
            base case : i = 1, dp[i] = 0
                        i = 2, dp[i] = 2
                        i = 3, dp[i] = 3
        """
        dp = [float('inf')] * (n+1)
        dp[1] = 0
        for i in range(2, n+1):
            for j in range(1, i):
                if i % j == 0:  #说明dp[i]可经过dp[j]复数次paste而来，因此，当前dp[i] 
                    #就等于dp[j]即制造j个A的最小操作数，加上复数次paste而来即i//j
                    dp[i] = min(dp[i], dp[j] + i//j)  
        return dp[-1]
# @lc code=end

