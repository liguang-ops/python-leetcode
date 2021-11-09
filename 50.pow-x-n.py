#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """直接遍历n次肯定也是一个解决办法，但是时间复杂度为n
        利用幂的性质
        a^b = a * (a^(b-1))
        a^b = (a^(b/2))^2， 这个能把时间规模降一半
        """
        if n == 0:
            return 1
        if n < 0:   #负指数幂转为分数的正指数幂
            x = 1/x
            n = -n
        if n == 1:
            return x
        if n % 2 == 0: #偶数
            return self.myPow(x, n // 2) ** 2
        else:
            return x * self.myPow(x, n-1)
# @lc code=end

