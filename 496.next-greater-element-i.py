'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-01 15:09:04
LastEditors: liguang-ops
LastEditTime: 2021-10-01 20:49:16
'''
#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """自己想出来的方法只有暴力遍历，事实上就是找一个大于cur的数，没有就赋值-1。
        当然，这题还和书上有点点不同，书上是求nums2元素的的nextGreaterElement，我们可以这样想，
        先算出nums2的nextGreaterElement，然后遍历nums1，去找对应的nums2的nextGreaterElement，
        可是这个查找过程就需要O(MN)了，之前暴力遍历是O(N^2),，因此这样计算的时间复杂度为O(n^2).
        当然，如果利用字典，查找过程会降到O(1),但是总的时间复杂度不会变
        """
        hash = {}
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):  
                if nums2[j] > nums2[i]:   #如果后面有数大于当前值，计入hash，计算后面值
                    hash[nums2[i]] = nums2[j]  
                    break
                if j == len(nums2) - 1:   #已经迭代到最后没有发现，赋值-1
                    hash[nums2[i]] = -1
        hash[nums2[-1]] = -1
        return [hash[x] for x in nums1] 

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """上面虽然有一个小优化，但是时间复杂度没有变化，因为查找的时间还是O(n^2)。书上给出一种
        做法时间复杂度为O(n), 具体做法需要用到一个单调栈，即栈中所有元素都是单调的。说实话，看不太懂
        """
        #这是第一种写法：
        # 思路是这样的：首先将nums2[i]入栈，然后然后比较栈顶元素和nums[i+1]大小，大于栈顶元素：那么栈顶元素
        # 出栈，栈顶元素对应的nextGreatElement就是nums[i+1];小于栈顶元素就将nums[i+1]入栈，在进入下一轮循环
        # 比较栈顶元素(这次是nums[n+1])和nums[n+2]大小
        hash, stack = {}, []
        
        for n in nums2:
            while stack and stack[-1] < n:
                hash[stack.pop()] = n
            stack.append(n)

        #思路二,这思路根符合我得思路，或者说是我最容易看懂的
        """
        for i in range(len(nums2-1), -1, -1):  #倒着遍历
            #倒着遍历，nums2[-1]对应的值肯定是-1，
            while stack and stack[-1] < n:
                stack.pop()
            hash[nums2[i]] = stack[-1] if len(stack) != 0 else -1
            stack.append(nums2[i])
        """
        return [hash.get(x, -1) for x in nums1]
# @lc code=end

