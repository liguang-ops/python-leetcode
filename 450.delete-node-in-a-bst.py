'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-29 13:55:59
LastEditors: liguang-ops
LastEditTime: 2021-09-29 19:48:43
'''
#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode1(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """首先先找到那个需要删除的节点，然后分三种情况：
            1. 需要的节点没有子节点：直接删除即可
            2. 需要删除的节点有一个子节点：删除当前节点，然后把子节点接到删除节点的父节点上
            3. 需要删除的节点有两个子节点：找到这个删除节点左子树的最大值，或者右子树的最小
            值然后二者替换一下，之后删掉这个替换的值(这里有个不怎么好的地方，书上给的方法是
            交换两个节点的val域，最好的方法是修改指针，但是这里没有给出。我尽量试一试能不能
            给出)
        """
        def getMaxNode(root):  #获取以root为根节点的BST的最大值
            while root.right:
                root = root.right
            return root
        
        if root == None: return None
        if root.val == key:
            #当前节点的没有子节点：
            if root.left == None:  #只有右节点
                return root.right
            if root.right == None:  #只有左节点
                return root.left
            #左右子节点都有，这里就找左子树最大，左子树的最大值在左子树的最右边
            maxNode = getMaxNode(root.left)   #找到左子树的最大节点
            root.val = maxNode.val            #替换(这里用交换值域来实现，不太完美)
            root.left = self.deleteNode(root.left, maxNode.val)  #递归删除左子树的最大值节点
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #上面那种写法不完美，修改的值域。这边通过修改树结构或者说指针来实现节点的删除
        #当然其他结构还是一样的，唯一思路不同的是，在处理被删除节点有两个自己点的时候：
        #需要把被删除节点的左子树全部迁移到被删除节点的右子树的最小值下，当左子树，有点绕口，
        #但是读几遍就懂了；当然还有一个对称的做法，把被删除节点的右子树全部迁移到被删除节点的
        #左子树的最大值下，当右子树。
        def getMinNode(root):  #获取以root为根节点的BST的最最小值
            while root.left:
                root = root.left
            return root

        if root == None: return None
        if root.val == key:
            #当前节点的没有子节点：
            if root.left == None:  #只有右节点
                return root.right
            if root.right == None:  #只有左节点
                return root.left
            #左右子节点都有，这里把左子树加到右边，先找到右子树最小值
            maxNode = getMinNode(root.right)   #被删除节点右子树最小节点
            maxNode.left = root.left            #替换, 被删除节点的左子树全部加到被删除节点右子树最小节点的左节点上
            return root.right  #跳过root，就代表root删除了
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root
        """这个方法比上面那个方法要更程序员一些，更优美一点。不过我不知道那个root节点需不需要手动删除，
        如果程序一直揭阳运行，那个被删除的节点内存好像一直没有被回收
        """
# @lc code=end

