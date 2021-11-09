#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes1(self, root: Optional[TreeNode]) -> int:
        """完全二叉树的节点个数，完全二叉树的定义先要搞清楚，(这定义我还收不清楚
        ，大概就是这颗二叉树除最下面一层外，其他层都放满了的二叉树，所谓放满是指
        可以右节点的位置都有节点)，它的一种特殊形式是满二叉树，即树的最大深度和
        最小深度相同，并且除叶子节点外所有节点的度都为2的树。
        对于普通完全二叉树：就直接用树的遍历方法
        对于满二叉树：树的节点个数 = 2 ^ 树的深度 - 1
        然后，有一个定义，或者说事实，一个完全二叉树一定存在一个子树是满二叉树，因此
        二者杰哥能够减少时间复杂度
        """

        def countNodes(root):
            #这是对于一颗满二叉树的算法，时间复杂度O(logn)
            i = 0
            while root:
                root = root.left  #左右都一样
                i += 1
            return 2 ** i -1

        #这样写直接AC了我是没想到的，
        if root == None: return 0
        return 1 + self.countNodes(root.right) + self.countNodes(root.left)  #时间复杂度O(n)
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        #这个是结合, 
        l, r = root, root
        i, j = 0, 0
        while l:
            l = l.left
            i += 1
        while r:
            r = r.right
            j += 1
        if i == j: #是满二叉树
            return 2 ** i - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
# @lc code=end

