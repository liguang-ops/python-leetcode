'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-03 14:58:30
LastEditors: liguang-ops
LastEditTime: 2021-10-03 15:33:26
'''
#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """暴力遍历O(nk), 没法AC
        """
        res = []
        for i in range(0, len(nums) - k + 1):
            res.append(max(nums[i:i+k]))
        return res
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """另一个方法，单调队列，和单调栈类似(单调栈是如果需要进栈元素大于栈顶
        ，那就把栈顶元素出栈，直至小于，或者栈空)，单调队列是，从队尾开始，队尾
        元素小于需要进队元素，则将队尾元素出队列，直至队尾元素大于，或者队空。由于这边
        需要队尾元素出去，所以使用双链表，即对头队尾都可出队列。
        这样，最大值一定在对头，取的时间为O(1),总的时间复杂度为O(n)
        """
        #内部类，单调队列实现
        class monotonicQueue:
            def __init__(self) -> None:
                self.queue = []
            
            def push(self, n: int) -> None:
                while self.queue and self.queue[-1] < n:  #如果队尾元素小于需要进来的元素，
                    self.queue.pop()                      #就把该元素丢弃，直至队空，或者队尾
                self.queue.append(n)                      #有更大的元素，然后入队
            
            def getMax(self) -> int:                      #根据push方法，最大值一定在队头
                return self.queue[0]
            
            def pop(self, n) -> None:
                if n == self.queue[0]: #如果需要pop的值是不是对头的值，俺么说明已经丢弃了，不用管
                    self.queue.pop(0)

        mQ = monotonicQueue()
        res = []
        for i in range(len(nums)):
            if i < k -1:   #先将队列中塞入k-1个
                 mQ.push(nums[i])
            else:
                mQ.push(nums[i])   #在塞入第k个
                res.append(mQ.getMax())  #取k个中最大值
                mQ.pop(nums[i -k + 1])   #删除窗口中最左边的值
        return res
# @lc code=end

