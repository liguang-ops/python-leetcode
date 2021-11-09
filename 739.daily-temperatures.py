'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-01 20:55:54
LastEditors: liguang-ops
LastEditTime: 2021-10-01 21:14:26
'''
#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """和#496很像，单调栈，但是之前是记值，这边记索引。
        说实话，虽然会这些题，理解了单调栈，但是我还是不知道什么时候用单调栈
        """
        hash, stack = {}, []
        for i in range(len(temperatures)):   #以索引遍历
            while stack and temperatures[stack[-1]] < temperatures[i]: #warmer, 等于应该不行
                cur = stack.pop()  #找到第一个大于栈顶元素的值，栈顶元素出栈
                hash[cur] = i - cur #记录栈顶元素和当前元素索引的差值
            stack.append(i)
        return [hash.get(x, 0) for x in range(len(temperatures))] 
# @lc code=end

