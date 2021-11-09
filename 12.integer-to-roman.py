'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-18 11:26:05
LastEditors: liguang-ops
LastEditTime: 2021-09-18 12:18:15
'''
#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        """唯一想到的就是将数字分解成各个位数，然后拼在一起
        """
        digit = 1  #当前数字的位数
        roman = ""
        while num // digit >=10:
            digit *= 10
        
        while num > 0:
            curNum = num // digit  #找到当前数字最左边的数
            if digit == 1000:  #最大一千
               roman += "".join(['M'] * curNum)  #小于4千
            elif digit == 100:
                if curNum in [4, 9]:
                    roman += 'CD' if curNum == 4 else 'CM'
                else:
                    roman += ('D' + ''.join(['C'] * (curNum - 5))) if curNum >= 5 \
                        else ''.join(['C'] * curNum)
            elif digit == 10:
                if curNum in [4, 9]:
                    roman += 'XL' if curNum == 4 else 'XC'
                else:
                    roman += ('L' + ''.join(['X'] * (curNum - 5))) if curNum >= 5 \
                        else ''.join(['X'] * curNum)
            elif digit == 1:
                if curNum in [4, 9]:
                    roman += 'IV' if curNum == 4 else 'IX'
                else:
                    roman += ('V' + ''.join(['I'] * (curNum - 5))) if curNum >= 5 \
                        else ''.join(['I'] * curNum)
            num = num % digit
            digit = digit // 10
        return roman

    def intToRoman(self, num: int) -> str:
        """应该有更好的方法，就和知乎上有一题“实现36进制内的数值转换”一样
        不行，有一丢丢思路，但是无法完全想出来
        """
        roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        digit = 1  #当前数字的位数
        roman = ""
        while num // digit >=10:
            digit *= 10
        while num > 0:
            curNum = num // digit  #找到当前数字最左边的数
        
# @lc code=end

