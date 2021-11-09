#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """这一题和#78的第二种解法类似，是回溯题，也需要一个start去控制选取的头
        #当然，头的选取范围为[1...n-k+1]
        """
        nums = list(range(1, n+1))
        res = [] #这里有个很奇怪的地方，为什么在跑这个dfs时候不需要在dfs内部申明nonlocal res?, 因为res是引用类型？
    
        def dfs(nums, k, start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            for i in range(start, len(nums)):
                comb.append(nums[i])
                dfs(nums, k, i + 1, comb)
                comb.pop()
        dfs(nums, k, 0, [])
        return res
# @lc code=end

