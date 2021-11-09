'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-03 19:02:13
LastEditors: liguang-ops
LastEditTime: 2021-09-03 19:49:49
'''
#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        #如果有环，fast一定会追上slow
        while(fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        return False
# @lc code=end

