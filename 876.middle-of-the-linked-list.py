#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        #fast走的路程是slow的两倍，当fast到最后的时候slow就在中点
        while(fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
        return slow
# @lc code=end

