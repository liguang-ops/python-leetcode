'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-29 13:08:13
LastEditors: liguang-ops
LastEditTime: 2021-09-29 13:17:13
'''
#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """这一题没那么难，BST的遍历差不多。主要是一个关键：插入的节点是原来树上
        度小于等于1的节点的子节点。当然，有一些另一种方法插入也可以。
        """
        if root == None: return TreeNode(val= val)   #当前节点为空，说明一定到度小于等于1的节点上了
        if root.val < val:    #新插入的节点应该在右子树上
            root.right = self.insertIntoBST(root.right, val)
        else:  #新插的节点应该在左子树上
            root.left = self.insertIntoBST(root.left, val)
        return root
# @lc code=end

