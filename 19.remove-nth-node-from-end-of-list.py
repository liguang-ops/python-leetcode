'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-03 20:14:09
LastEditors: liguang-ops
LastEditTime: 2021-09-03 20:55:59
'''
#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        #将fast向前移动n步
        for _ in range(n):
            fast = fast.next
        #fast和slow同时、同步频移动
        while(fast is not None):
            fast = fast.next
            temp = slow   #记录需要删除节点的前一个节点
            slow = slow.next
        if slow is head:  #特殊情况，n=链表长度
            head = head.next
            return head
        temp.next = slow.next
        return head
# @lc code=end

