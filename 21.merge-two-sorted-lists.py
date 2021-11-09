'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-26 17:16:35
LastEditors: liguang-ops
LastEditTime: 2021-09-26 17:39:03
'''
#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """这里的思路和有一道题很像，找不到这道题在哪了。也是一道是双指针题。比较两个链表上
        当前指针的值，把较小的放入结果中，并且指针后移，然后继续计算，直至某个链表终点
        ，最后把没有到终点的链表补到最后。
        """
        ptr = ListNode() 
        p = ptr
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 if l1 != None else l2
        return ptr.next               
# @lc code=end

