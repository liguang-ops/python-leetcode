'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-27 11:30:33
LastEditors: liguang-ops
LastEditTime: 2021-09-27 13:24:55
'''
#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import LifoQueue
class Solution:
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """这里倒是有多种解法。
        1. 用栈，先进后出
        2. 循环遍历
        3. 递归，递归方法是书上看的，不明觉厉。因为后续的几道题都需要都需要用到
        这个方法，这里为了熟悉就把它写上
        """
        dummy = ListNode()   #虚拟头节点
        r = dummy
        q = LifoQueue()      #栈
        while head != None:  #所有元素入栈
            q.put(head)
            head = head.next
        while not q.empty(): #所有元素出栈
            r.next = q.get()
            r = r.next
        r.next = None        #链表末尾指向None
        return dummy.next
    
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #用遍历实现
        #思路是这样的：有三个临时节点，p、q、r,开始的时候p->q->r,p是尾节点
        #q是中间节点，r是最后的节点。先将尾节点的next置空，然后循环将p节点的
        #指向倒置，当然在这之前要用r先记录p节点原来的指向。这样循环，直至到重点
        #里面的细节最好还是画一下图，就很清晰了。
        if head == None or head.next == None: return head  #异常判断
        p, q = head, head.next  
        p.next = None  
        while q != None:
            r = q.next
            q.next = p
            p = q
            q= r
        return p

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #递归实现，我觉得是最不容易理解的
        #这边书上给出的理解方法是不去深究递归实现，而是严格按照递归函数的定义去看
        #由于递归要堆栈，因此空间复杂度很比较高
        if head == None or head.next == None : return head   #当只有一个节点时，直接返回
        head.next.next = head
        #假设reverseList已经成功反转了head.next链表，lasts是新链表的头，新链表的尾是head.next
        last = self.reverseList(head.next)  
        head.next.next = head  #此时将新链表尾部加上head，形成完整的链表
        head.next = None  #将链表结尾指向空
        return last
# @lc code=end

