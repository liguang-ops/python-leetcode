'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-28 21:30:06
LastEditors: liguang-ops
LastEditTime: 2021-09-28 21:47:13
'''
#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """唉，看了下之前刷的链表题，好像又快忘得差不多了。还是的多写，多思考，才能牢记，越来越觉得
        发明这些算法的人牛逼
        二叉搜索树的搜索还是很简单的。当然也有两种方法，一个树的遍历，另一个就是针对二叉搜索树的遍历
        """
        #先写第一种
        if root == None:
            return None
        if root.val == val:
            return root
        left = self.searchBST(root.left, val)
        right = self.searchBST(root.right, val)
        return left if left else right  #二叉搜索树的性纸决定了lef和right至少有一个为None
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #二叉搜索树的性质决定了，搜索某个值，只需要将这个值和root作比较，
        #如果这个值比root小，那么只可能存在于左子树，如果大于root，只可能存在于右子树
        if root == None:
            return None
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
# @lc code=end

