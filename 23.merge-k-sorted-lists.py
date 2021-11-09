'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-26 19:58:57
LastEditors: liguang-ops
LastEditTime: 2021-09-26 21:44:00
'''
#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class ListNode1:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __lt__(self, other):  #重载小于
        return self.val < other.val
    
    def __gt__(self, other):  #重载大于
        return self.val > other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """和#21类似，甚至说一摸一样。在这一题中，思路是一样的，每一个链表都给一个指针
        然后计算这些指针指向的节点的最小值加入dummy，对应指针后移，直到所有指针都为NUll
        这里考察的点在于怎样求当前的最小值。排序最低klogk，如果用最小堆实现，时间复杂度
        会降为logn python标准库中有最小堆实现(headq)、优先级队列PriorityQueue.
        !!!这里还有一点，比较两个对象，需要重载比较运算符，还需要把ListNode对象转为ListNode1
        1对象。(这边我不知道父对象怎样调用子对象的方法，只好硬转)
        """
        dummy = ListNode1()  #虚拟节点
        p = dummy  #爬行节点
        pq = PriorityQueue()  #最小堆
        for i in lists:  #将所有的头节点加入最小堆
            if i == None:   #避免某些头节点本身就是None
                continue
            pq.put(ListNode1(i.val, i.next))
        while not pq.empty():
            cur = pq.get()  #取出最小值
            p.next = cur    #链接到虚拟节点上
            p = p.next      #爬行节点向前走一步
            if cur.next != None:  #取出的节点并非是当前链表的最后一个节点
                pq.put(ListNode1(cur.next.val, cur.next.next))
            else:  #已经是最后一个节点了
                pass #在n-1个节点中继续比较
        return dummy.next
# @lc code=end

