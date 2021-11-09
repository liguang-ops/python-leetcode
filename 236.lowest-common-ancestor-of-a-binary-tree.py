'''
Description:
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-30 17:59:25
LastEditors: liguang-ops
LastEditTime: 2021-09-30 22:23:24
'''
#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
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
        """老递归怪了，虽然题目给的难度是中等，但是我感觉这道题好难，拿到时候一点思路都没有，看完书才有一点点
        最近公共祖先，说明要找到一个节点，其中p在左子树上，q在右子树上，这样就能给出框架，递归root的左子树和右子树
        ，去找q和p，由于p,q是唯一的，只要找到了(有返回值)，就说明root是LCA，如果都没有返回值，说明不在，返回None，
        如果只有一个返回值，就说明p或q，只有一个存在root的左右子树上，这个时候返回这个p或者q，这样就回到了上一层，
        再次判断上层左子树后者右子树有没有值，有值就说明左右子树都有值返回，上一个节点就是LCA，不是，就继续往上
        base  case很好理解，找到q或者p就返回，当root为None，表明低轨道最后一层也没找到，也返回None
        """
        #base case,很好理解
        if root == None or root == q or root == p:
            return root
        #如果root不为空，也不是p或者q，在root的左右子树上寻找
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 根据base case和题目条件， 如果left、right有返回值，那么一定是p或者q，
        # 并且，当left和right都有值时，那一定是p和q，不会重复，此时LCA就是root
        if left and right:
            return root
        #当left、right都没有值时，那肯定返回None
        if left == None and right == None:
            return None
        #最难懂得情况是，只有一个有值，根据base case，这个值一定是p或者q。这个时候
        #做一个假设(这样更好理解)：left有值(right有值是一样的)，说明在root这个节点上的左右子树只有p
        #或者q，这个返回这个left， 回到上一层(即当前root的父节点)的left和right，
        #其中一个返回值一定是这个left，这时，只要看上一层另外的left、right是否有值，就
        #能够判断出上一层的root是否是LCA(递归)
        return left if left else right
# @lc code=end

