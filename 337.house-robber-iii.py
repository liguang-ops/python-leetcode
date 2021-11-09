'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-22 16:28:30
LastEditors: liguang-ops
LastEditTime: 2021-09-22 16:50:12
'''
#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.memo = {}
    def rob(self, root: Optional[TreeNode]) -> int:
        """动态规划，套路是一样的，选择就是是否选择当前，然后求这两个的最大值
        不加备忘录就会TLE
        """
        if root in self.memo:
            return self.memo[root]
        if root == None: return 0
        res_get = self.rob(root.left) + self.rob(root.right)  #不选当前
        #选了当前， 还有一个语法点，python的三元运算符优先级很低，至少比加号低
        res_not_get = root.val + \
            (self.rob(root.left.left) + self.rob(root.left.right) if root.left != None else 0) + \
            (self.rob(root.right.left) + self.rob(root.right.right) if root.right != None else 0)  
        res = max(res_get, res_not_get)
        self.memo[root] = res
        return res
# @lc code=end

