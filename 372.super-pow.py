'''
Description:
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-13 15:13:29
LastEditors: liguang-ops
LastEditTime: 2021-10-13 16:28:46
'''
#
# @lc app=leetcode id=372 lang=python3
#
# [372] Super Pow
#

# @lc code=start
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        """这一题有溢出的可能，所以不能直接把b变成整数直接算。而是需要一些转化：
        把大值的大幂运算改成小值的小幂运算的组合。当然，我不会，看书的。
        例: b = [2, 1, 3]
        a^b = a^[2, 1, 3] = a^3 * (a^[2, 1])^10
                          = a^3 * (a^1 * ( a^[2] )^10 )^10
                          = a^3 * (a^1 * (a^2 * (a^[])^10 )^10 )^10
        这就是基本递归的过程
        第二个求模：如果我们直接算a^b的值再求模，很可能啊a^b会直接溢出，需要转成小数取模在组合起来。
        (B * D) % k = ((B % k) * (D % k)) % k 很容易证明，这也是一个递归的过程，且正好对应了
        上面小幂运算的过程：对拆出来的小幂直接求模，然后乘在一起，最后求一次模
        接上例：
        a^b %k= ((a^3 % k) * ((s^[2, 1])^10 %k)) %k
        其中：a^3 %k = ((a % k) * (a % k) * (a % k)) % k  = (a % k)^3 % k
        """
        base = 1337
        if not b or a == 1:
            return 1
        else:
            tail = b.pop()
            part1 = self.pow(a, tail)
            part2 = self.pow(self.superPow(a, b), 10)
            #这里加上模k操作
            return (part1 * part2) % base

    def pow(self, a, b):
        #用#50的写法，能够更快一点
        base = 1337
        if b == 0 or a == 1:
            return 1
        a %= base  #这个就是 a%k 的值
        if b % 2 == 0:
            #加上取递归操作
            return (self.pow(a, b // 2) ** 2) % base
        else:
            #加上取模操作
            return (self.pow(a, b-1) * a) % base
    #鲜有的写完就AC
# @lc code=end

