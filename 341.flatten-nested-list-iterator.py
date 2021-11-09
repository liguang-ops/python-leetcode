# @before-stub-for-debug-begin
from python3problem341 import *
from typing import *
# @before-stub-for-debug-end

'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-12 15:50:58
LastEditors: liguang-ops
LastEditTime: 2021-10-12 20:47:57
'''
#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator1:
    def __init__(self, nestedList: [NestedInteger]):
        #其实就是n叉树遍历
        self.res = []
        def trevese(root):   #n叉树遍历
            if root.isInteger():
                self.res.append(root.getInteger())
            else:
                for child in root.getList():
                    trevese(child)

        for root in nestedList:  #n个n叉树
            trevese(root)
        self.iter = iter(self.res)
    def next(self) -> int:
        return self.res.pop(0)
    
    def hasNext(self) -> bool:
         return len(self.res) != 0
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
    #像上面这样做，有一个缺点，当nestedList比较大的时候，在初始化的时候会消耗大量时间
    #真正的迭代器应该是惰性的，即要一个才拿一个，而不是先一次性做好
        self.res = [root for root in nestedList]  #这里因为不能保证'[NestInteger]'有insert方法
    def next(self) -> int:
        return self.res.pop(0)
    
    def hasNext(self) -> bool:
        while self.res and (not self.res[0].isInteger()):
            root = self.res.pop(0).getList()
            for i in range(len(root)-1, -1, -1):  #倒序遍历
                self.res.insert(0, root[i])
        return len(self.res) != 0
# @lc code=end

