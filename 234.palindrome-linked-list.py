'''
Description:
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-04 14:33:54
LastEditors: liguang-ops
LastEditTime: 2021-10-04 16:11:57
'''
#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """挺多方法的
        1. 先利用反转链表方法，反转这个链表，然后两个链表遍历。
        2. 后序遍历链表，利用系统堆栈，实现链表元素的倒序输出，
        在利用一个正序记录的指针，二者判断相不相同即可, 空间复杂度O(n)
        """
        #左指针
        left = head

        def traverse(right):
            nonlocal left
            if right == None: return True   
            res = traverse(right.next)   #当压栈到最后一个，res返回值True，right指向最后一个元素，left指向第一个元素
            res = res and (right.val == left.val)  #判断这两个是否相等
            left = left.next                       #left指向下一个，right由于上面的退站，会指向倒数第二个
            return res

        return traverse(head)

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """还有一种方法，先利用快慢指针找到链表中点，然后，反转后半部分链表，
        之后在判断是否是回文链表(利用链表的指针)
        """
        if head.next == None: return True
        def reverse(head):
            cur, pre  = head, head.next
            cur.next = None
            while pre:
                tmp = pre.next
                pre.next = cur
                cur = pre
                pre = tmp
            return cur

        slow = fast = head
        while fast != None and fast.next !=None:
            slow = slow.next
            fast = fast.next.next
        #此时slow在链表的中点。这里有一个小问题，当链表长度为奇数时，fast是链表最后一个，
        #slow在中点，当链表为偶数数的时候，slow在中间靠右位置，fast是NULL。
        #这里，当slow恰巧在中点时，需要将slow相后移一位，保证和链表长度为偶数时一样
        if fast != None:
            slow = slow.next
        right = reverse(slow)
        
        left = head
        res = True
        while right != None:
            res = res and left.val == right.val
            if not res:
                return False 
            left = left.next
            right = right.next
        return res
        
# @lc code=end

