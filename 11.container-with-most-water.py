'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-17 16:02:05
LastEditors: liguang-ops
LastEditTime: 2021-09-17 16:47:36
'''
#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """暴力遍历,TLE
        """
        maxContain = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)): #不用和自己比
                minHeight = min(height[i], height[j])
                contain = minHeight * (j-i)
                if maxContain < contain:
                    maxContain = contain
        return maxContain

    def maxArea(self, height: List[int]) -> int:
        """双指针法。分别有一个头指针和一个尾指针，和一个记录当前最大值的maxContain
        看左右指针指的height谁更短，将更短指针向未移动过的位置移动一下。(不怎么懂为什么这样做就
        能够找到最大值)
        水的含量由两个东西决定，一个是两个指针的距离，另一个是指针指向值的较小值，距离应该尽量大
        ，较小值应该尽量大
        因此，每一次变化时，都是在最大距离的基础上，选取较大的指针，这样就能保证水含量的最大值
        """
        maxContain = 0
        left, right = 0, len(height) -1
        while left < right:  #等于的时候就已经是0，不用判断
            contain = min(height[left], height[right]) * (right - left)
            if maxContain < contain:
                maxContain = contain
            if height[left] > height[right]:
                right -=1
            else:
                left +=1
        return maxContain
# @lc code=end

