'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-01 14:03:18
LastEditors: liguang-ops
LastEditTime: 2021-10-01 14:30:53
'''
#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """事实上，我是先做的#236。但是除了#236那种解法，我还是想不出任何其他解法，我的确想到利用BST
        性质来解决，但是仍旧被固陷在#236的思路中，无法出来。究其原因，我想还是对树不熟，对BST不熟，没有自己的
        思考。

        这道题可以利用BST的性质来做，对于root，如果root<p,root<q,说明p、q都在右子树上；如果root>p, 
        root>q, 说明p、q都在root的左子树上，如果一个比root大，另一个比root小，那root就是LCA
        """
        if root == None: return None
        if root.val > p.val and root.val > q.val:  #p、q在左子树上
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:   #p,q在右子树上
            return self.lowestCommonAncestor(root.right, p, q)
        else:   #其实这里才是base case， 即root节点的值在p，q之间
            return root 
# @lc code=end

