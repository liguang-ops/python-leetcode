'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-27 13:44:24
LastEditors: liguang-ops
LastEditTime: 2021-09-27 15:59:31
'''
#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween1(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """这里也是有两种方法，一种是线性扫描+循环反转，第二种是递归
        线性扫描——循环反转思路还是有的：先找到第m个节点，然后和#206一样，进行反转，最后再把不需要反转的尾部
        节点放进去
        """
        if head.next == None or left == right: return head
        dummy = ListNode()
        dummy.next = head
        r = dummy #这个节点记录left - 1这一个位置 
        p, q = head, head.next   #反转的开始点和结束点都在于p，当p在left位置时开始反转，当p到达right位置停止反转
        i = 1
        while i < right:
            if i < left:
                r = r.next     #当进入反转操作时，r节点记录的就是left - 1这一个节点
                q = q.next     #p、q、r不断前进
                p = p.next
            else:  #开始反转
                #开始反转时第一个p节点需要指向谁，我先们现在还不确定，r.next记录了这个p节点，等循环结束在处理。先把q节点指向的方向改变
                temp = q.next  #临时记录q节点之前的指向
                q.next = p     #改变q节点的指向
                p = q          #p、q向前移动
                q = temp
            i += 1  #计数器加1
        #while 结束时，p的位置在right q的位置在right + 1， 此时r在left -1， 并且r.next 就是left位置
        r.next.next = q  #把反转后的节点插入原始节点里面
        r.next = p
        return dummy.next

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #递归方法有点难懂
        #先考虑这样一个问题：反转一个链表的前n和节点，事实上和#206的递归法有点相似，当然这里要求用递归实现。
        #只要把该链表分为两部分，前n个作为一个链表，后面的等反转完接上去就行，这里就需要一个临时变量去记住
        #n+1这个节点，方便后面接上。
        tmp = None  #这里我觉得用None比用ListNode好
        def reverseN(head, n):  #反转前n个节点
            nonlocal tmp
            if n == 1:
                tmp = head.next
                return head
            else:
                last = reverseN(head.next, n-1)  #已经反转完从head.next开始的n-1个节点，last是现在的头。
                head.next.next = head  #head.next是反转链表的尾巴，他的指向是NULL，这里修改为head
                head.next = tmp  #把后面的节点加在尾部
            return last

        #继续考虑，现在要反转第m到第n个节点，事实上就是在反转前n个节点题目的基础上，在头部加上一部分节点
        #思路就来了，可以先线性扫描到第left -1节点，然后对于left这个链表，反转前m-n个节点，最后拼一起就行。
        #这是思路一，很好完成，这里就不写了。
        """pass
        """
        #思路二，这是书上给的标准方法，有点难懂
        #第一，加入m = 1，那就是反转前n个节点；第二，如果n>1,那么我们可以看成反转
        #head.next链表的m-1到第n-1个节点，然后再把head加上，这样理解应该没错
        if left == 1:
            return reverseN(head, right)
        else:
            head.next =  self.reverseBetween(head.next, left-1, right-1)
            return head
    #递归果然浪费空间，时间上也没快多少
# @lc code=end

