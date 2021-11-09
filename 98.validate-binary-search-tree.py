'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-27 17:38:31
LastEditors: liguang-ops
LastEditTime: 2021-09-28 21:22:09
'''
#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        """二叉树的遍历,这道题还是满难的。看的还是不是很懂。
        二叉搜索树的定义是每一个根节点都大于它的左子树，小于它的右子树(这样看，貌似不能有相同值节点)
        """
        #说实话，这边还不是特别懂
        def isValidBST(root, min, max):  #根节点，左子树，右子树
            if root == None: return True
            if min != None and root.val <= min.val: return False #根节点小于左子树
            if max != None and root.val >= max.val: return False #根节点大于右子树
            #递归，对于root.left 他一定比root小，比min大，同样的道理root.right一定比root大，比max小
            #有一点思路，画图倒是能理解，但是脱离图就太难理解了。我觉得如果这道题我弄懂了，二叉树的题我大概都能理解了。  
            return isValidBST(root.left, min, root) and isValidBST(root.right, root, max)
        return isValidBST(root, None, None)

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        """这里其实就是树的遍历。上面那种写法我实在不好理解。换了一个思路。
        一颗二叉搜索树的中序遍历结果其实是一个升序序列，因此，我们只需要判断中序遍历
        的结果是否是升序序列就行，当然，更好的方法是每遍历一个结果就和上一个比较。
        二叉搜索树的中序遍历有两种，递归和用栈实现的非递归，这里都实现一下，作为不熟
        的锻炼
        """
        #先用非递归的吧
        prev = TreeNode(val = float('-inf'))   #记录前一个节点
        stack = list()
        while root or len(stack) != 0:
            while root:    #先将左节点入栈
                stack.append(root)
                root = root.left
            cur = stack.pop()  #取出中间节点(叶子节点也是中间节点，看成左右子节点都是NULL)
            if cur.val <= prev.val:  #比较当前节点和上一个出栈的节点
                return False
            else:
                prev = cur    #把当前节点当下下一轮的上一个出栈的节点
            root = cur.right  #把这个节点右节点入栈
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #递归的写法，其实和中序遍历很像，非递归感觉比较好懂一点(好懂个屁)
        #看不懂，很难受，其实和非递归方法非常像。但就是无法完全看懂
        prev = TreeNode(val = float('-inf'))
        def isValidBST(root):
            nonlocal prev
            if root == None:
                return True
            if not isValidBST(root.left):   #先解决左节点
                return False
            if root.val <= prev.val:        #看当前节点， 相当于出栈
                return False
            else:
                prev = root
            if not isValidBST(root.right):  #再看右节点
                return False
            return True                     #左中右都没有问题，就return True
        return isValidBST(root)         
# @lc code=end

