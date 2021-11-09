'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-03 19:41:53
LastEditors: liguang-ops
LastEditTime: 2021-09-03 20:05:57
'''
#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        #到相遇点
        while(fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        if fast is None or fast.next is None:  #无环
            return 
        fast = head
        #将其中一个回到期待点，下一次相遇点一定是环起点
        while(fast is not slow):
            fast = fast.next
            slow = slow.next
        return slow
# @lc code=end

