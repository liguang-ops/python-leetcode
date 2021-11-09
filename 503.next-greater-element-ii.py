'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-01 21:15:25
LastEditors: liguang-ops
LastEditTime: 2021-10-01 21:47:24
'''
#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """和#496，#739类似，单调栈。有一个环，最简单的方法就是把数组长度扩大一倍就能
        解决，当然还有一种方法就是通过取模的方式实现环形的索引遍历
        index = (index + 1) % len(nums), 这样空间复杂度就会降低,
        由于nums里面有重复数据，这里用index当作hash的key，虽然这里index重复了，但是其值
        没有变，所以也可以
        """
        hash, stack = {}, []
        i = 0
        while i < 2 * len(nums):  #最多只需要再遍历多一轮
            index = i if i < len(nums) else i - len(nums)  #这里没有用取模，如果取模的写法，不好确定while的break条件
            while stack and nums[stack[-1]] < nums[index]:
                hash[stack.pop()] = nums[index]
            stack.append(index)
            i += 1
        return [hash.get(x, -1) for x in range(len(nums))]
# @lc code=end

