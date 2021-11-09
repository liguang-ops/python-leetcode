'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-26 21:57:31
LastEditors: liguang-ops
LastEditTime: 2021-09-26 22:34:31
'''
#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from queue import Queue
class Solution:
    def generateParenthesis(self, n):
        """首先，不要把左括号和右括号单独拆开理解，而是把左右括号当成一个整体
        把一对括号分别插入当前已经形成的括号组合中的每一个位置，当然其中会出现
        的重复的，只需记录一下去掉就ok。这个过程有点像bfs，但是还是有点不同的,
        都需要用到队列，只是while 结束条件不同
        """
        #事实上备忘录有个优化，其实visited里面的内容和q.put后里面的内容是一样的，其实可以
        #直接在q里面查，但是队列底层数据结构是列表，查询的时间复杂度为O(n), 而set底层是hash,
        #查询的时间复杂度是O(1).这里算是空间换时间吧。
        if n == 1: return ["()"]
        q = Queue(maxsize=0)
        q.put("()")
        i = 1   #至少两对括号
        while i < n:
            visited = set()      #记录已经出现了的括号组合，为什么这里每次循环的时候初始化呢，因为只需要记当前的就行
            size = q.qsize()     #当前队列中节点个数
            for _ in range(size):
                cur = q.get()  #取出该字符串
                for j in range(len(cur) + 1):   #像该字符串每一个位置插入一对括号
                    inserted = cur[:j] + "()" + cur[j:]
                    if inserted not in visited: #未出现的组合记入下一轮和备忘录
                        visited.add(inserted)
                        q.put(inserted)
            i +=1 #一轮结束，计数器加一
        return q.queue
# @lc code=end

