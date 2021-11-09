'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-02 23:13:41
LastEditors: liguang-ops
LastEditTime: 2021-09-03 10:59:54
'''
#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = Queue(maxsize=0)
        if root ==  None:
            return 0
        q.put(root)
        depth = 1
        while(not q.empty()):
            size = q.qsize()
            #将当前队列中所有值一个个推出
            for _ in range(size):
                cur = q.get()
                if cur.left == None and cur.right == None:
                    return depth
                if cur.left != None:
                    q.put(cur.left)
                if cur.right !=  None:
                    q.put(cur.right)
            depth +=1
        return depth
# @lc code=end

