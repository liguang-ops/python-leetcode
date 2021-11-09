'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-27 09:47:42
LastEditors: liguang-ops
LastEditTime: 2021-09-27 10:39:11
'''
#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """这里我没有想到更好的方法，只想到利用两个爬行节点相互交换，然后继续向后爬
        知道到达链表终点,竟然AC了。说实话，我觉得我过几天再来看一遍我写的代码，我大
        概是看不懂了。
        """
        dummy = ListNode()  #虚拟节点，当作return的头节点
        r = dummy           #跟着p、q前进的爬行节点
        if head == None : return head  #异常值判断
        p, q = head, head.next
        dummy.next = p
        if q == None: return p
        #p、q是需要交换的节点，r是p和q的头
        while q != None:    #链表长度为奇数的时候，最后一个不用交换
            r.next = q      #这里三部就是交换步骤，画个图就理解了
            p.next = q.next
            q.next = p
            #节点后移
            if p.next  == None:   #链表长度为偶数
                break
            r = p                 #这里三部是恢复r、p、q的顺序，并同时向后移两位，
            q = p.next.next       #移两位是因为题目要求每两位交换一次
            p = p.next 
        return dummy.next
# @lc code=end

