'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-27 16:07:13
LastEditors: liguang-ops
LastEditTime: 2021-09-27 17:02:24
'''
#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """这一题，做完了#206和#92，思路大概还是有的。比如利用#92的反转第[m,n]节点，遍历一下，
        反转[n, n+k-1]个节点，n \in [1, L // k],其中L是链表的长度。完全能做出来，但是不够简洁，
        应该有更好的方法。并没有，看了一下书上的答案，其实差不多，只是不需要线性扫描。当然，时间复杂度会低一点
        """
        #思路是将完整链表拆成L//K + 1个子链表，分别反转，最后拼一起就行，当然也是递归的：
        #reverseKGroup(head, k) = reverseKGroup(head.next..., K),其中head.next..., 共有k个next，
        #当剩余的链表长度小于K的时候，就是base case

        #先完成反转移a为头，b为尾的链表的函数
        def reverse(a, b):  #和#206方法一摸一样，区别在于一个反转整个链表，一个反转a，b之间的链表
            p ,q = a, a.next #其实是一样的，之前是反转head到null之间的链表，现在是反转a到b之间的链表
            p.next = None
            while q != b:
                r = q.next
                q.next = p
                p = q
                q = r
            return p

        if head == None: return head   
        a = b = head
        for i in range(k):  #base case, 取出长度为k的链表
            if b == None: return head
            b = b.next
        newHead = reverse(a, b)     #反转之后，newHead是头，a是尾巴，在reverse函数中a指向了None(第34行)
        a.next = self.reverseKGroup(b, k)  #因此，在这里把后面的答案链接回来
        #还是和#206递归做法一样思考，假设已经正确返回b开头链表的K组反转函数结果，newhead根据reverse函数发现是长度为k
        #的链表的头，a是尾巴，此时只需要把尾巴链到b开头链表的K组反转函数结果就能得到正确答案
        return newHead
        """链表题好难
        """
# @lc code=end

