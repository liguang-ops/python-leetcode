#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
from queue import LifoQueue
class Stack(LifoQueue):
    def __init__(self, maxsize : int =...) -> None:
        super().__init__(maxsize=maxsize)
    def peek(self):
        if self.qsize() == 0:
            return ''
        else:
            return self.queue[-1]

class Solution:
    def isValid(self, s: str) -> bool:
        """这题用栈好像会比较好做，思路就是将(、[、{等入栈,当下一个入栈的字符和
        栈顶元素是匹配的就将栈顶元素出栈，当遍历结束，看栈是否为空，这里就不自己
        实现栈了，没必要，标准库里有现成的(标准库的那个没有peek函数(获取栈顶元素
        但是不删除))，这边继承一下好了
        """
        dic = {'}':'{', ')':'(', ']':'['}
        stack = Stack(maxsize=0)
        for char in s:
            if char in ['(', '[', '{']:
                stack.put(char)
            elif stack.peek() == dic[char]:
                stack.get()
            else:
                stack.put(char)
        return stack.empty()
# @lc code=end

