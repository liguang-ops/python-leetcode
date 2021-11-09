'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-03 11:20:28
LastEditors: liguang-ops
LastEditTime: 2021-09-03 18:45:36
'''
#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
from queue import Queue
import copy
class Solution:
    def wave(self, cur):
        cur = [int(i) for i in cur]
        changedDown =  [[*cur[0:i], cur[i] - 1, *cur[i+1:]] if cur[i] !=0 \
                                else [*cur[0:i], 9, *cur[i+1:]]for i in range(len(cur))]
        changedUp =  [[*cur[0:i], cur[i] + 1, *cur[i+1:]] if cur[i] !=9 \
                                else [*cur[0:i], 0, *cur[i+1:]]for i in range(len(cur))]
        return [''.join([str(i) for i in one]) for one in changedDown + changedUp]
    
    #单向BFS
    def openLock1(self, deadends, target):
        q = Queue(maxsize=0)
        visited = set()  #存储已经列举出的密码，防止走回头路
        init = '0000'
        q.put(init)
        visited.add(init)
        depth = 0
        deadends = set(deadends)
        while(not q.empty()):
            size = q.qsize()
            #判断当前队列的点
            for _ in range(size):
                cur = q.get()
                #有dead，这一条路线就跳过
                if cur in deadends:
                    continue
                if cur == target:
                    return depth
                #向周围扩散
                next = self.wave(cur)
                for i in range(len(next)):
                    if next[i] not in visited:
                        q.put(next[i])
                        visited.add(next[i])
            #这一轮结束
            depth += 1
        #当队列为空，表示所有可能路径都会碰到dead
        return -1
    
    #双向BFS:前提是知道终点在哪
    def openLock(self, deadends, target):
        init = '0000'
        q1 = set([init])  #这边用列表也可以，用集合能更快查询
        q2 = set([target])
        """
        这里是和上面不同的点，后面也有不一样的，这里只是将visited置空，
        并且节点加入visited时间从之前的向下扩散时加入改为判断时加入。
        想明白了一点，但是又没有完全想明白 
        
        """
        visited = set()
        depth = 0
        while(len(q1) !=0 and len(q2) !=0):
            temp = set() #储存当前遍历的节点的子节点
            for cur in q1:
                if cur in deadends:
                    continue
                if cur in q2:
                    return depth
                visited.add(cur)
                #向四周扩散
                next = self.wave(cur)
                for i in range(len(next)):
                    if next[i] not in visited:
                        temp.add(next[i])
            depth +=1
            q1 = q2
            q2 = temp
        return -1
    
    #双向BFS + 小trick:前提是知道终点在哪
    def openLock2(self, deadends, target):
        init = '0000'
        q1 = set([init])  #这边用列表也可以，用集合能更快查询
        q2 = set([target])
        """
        这里是和上面不同的点，后面也有不一样的，这里只是将visited置空，
        并且节点加入visited时间从之前的向下扩散时加入改为判断时加入。
        想明白了一点，但是又没有完全想明白 
        
        """
        visited = set()
        depth = 0
        while(len(q1) !=0 and len(q2) !=0):
            if len(q1) > len(q2):   #优先遍历size小的
                t = q1
                q1 = q2
                q2 = t
            temp = set() #储存当前遍历的节点的子节点
            for cur in q1:
                if cur in deadends:
                    continue
                if cur in q2:
                    return depth
                visited.add(cur)
                #向四周扩散
                next = self.wave(cur)
                for i in range(len(next)):
                    if next[i] not in visited:
                        temp.add(next[i])
            depth +=1
            q1 = q2
            q2 = temp
        return -1

# @lc code=end

