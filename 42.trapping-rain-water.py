#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap1(self, height: List[int]) -> int:
        """刚开始看感觉和#11有点像，但是完全没思路,第一种，暴力遍历：
        即对于每一个点，找到其左边最大点和右边最大点，然后雨水量的最大高度就是
        这两个值的较小点，直接算当前差就行。(简单来说，虽然我们求的是所有雨水和，
        但是我们把雨水根据索引切开，一个索引一个索引的考虑，当前索引下能盛的水只和
        左边和右边的最大值有关)，TLE,时间复杂度O(n^2)
        """
        res = 0
        for i in range(1, len(height)-1):  #第一个点和最后一个点不用算
            l_max, r_max = 0, 0
            for l in range(i, -1, -1):
                l_max = max(l_max, height[l])
            for r in range(i, len(height)):
                r_max = max(r_max, height[r])
            res += min(l_max, r_max) - height[i]
        return res

    def trap2(self, height: List[int]) -> int:
        """另一个方法：先把对应index的左最大值和右最大值求出来。利用dp法，实现时间复杂度O(n)
        最后遍历时间复杂度O(n),空间复杂度O(n)
        """
        res = 0
        l_max, r_max = [height[0]] * len(height), [height[-1]] * len(height)
        #先找左最大值：
        for i in range(1, len(height)):
            l_max[i] = max(height[i], l_max[i-1])
        #右最大值
        for j in range(len(height)-2, -1, -1):
            r_max[j] = max(height[j], r_max[j+1])
        #遍历
        for k in range(1, len(height)-1):
            res += min(l_max[k], r_max[k]) - height[k]
        return res
    
    def trap(self, height: List[int]) -> int:
        """上面的做法空间复杂度O(n), 其实看代码可以发现，那个l_max[i]只和前一个状态有关，因此时间复杂度
        可以变为O(1),虽然这么说，自己还是不会写
        """
        res = 0
        left, right = 0, len(height) - 1
        l_max, r_max = height[0], height[-1]
        
        while left <= right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res
# @lc code=end

