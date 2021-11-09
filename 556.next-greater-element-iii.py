'''
Description:
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-01 21:47:48
LastEditors: liguang-ops
LastEditTime: 2021-10-02 13:43:03
'''
#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """如果在做这一题之前没有做那些‘nextGreatElement’题目，我大概会这么做：
        首先将n的所有digits算出来放到一个列表中，然后用DFS算出全排列组合，然后
        升序排序，最后用搜索左边界二分搜索的找到最小的大于n的数，然后在判断2^32 -1
        和这个数的关系，当然也可以再全排列的时候，直接去掉，这样时间复杂度和空间
        复杂度都巨高。
        利用单调栈的做法能快速找到最小的，大于n的数：
        先算出n的digits按顺序放入列表中，然后利用单调栈记录当前数字第后面第一个大于当前
        数的索引，最后，从后往前，找到第一个大于-1的(即key越大越好)，交换索引顺序，就找到了答案
        5873 -》 [5, 8, 2, 3] -> {0:1, 1:-1, 2:3, 3:-1}, 从后往前，最早value大于-1的
        是2：3， 这样就交换列表中对应索引的数字 -》 [5, 8, 3, 2]，就得到了最小的大于n的数字
        """
        #求n的digit
        nums = []
        while n:
            nums.insert(0, n % 10)  #insert 是为了保证各个数字的顺序
            n = n // 10

        #数字可能有重复，记索引
        hash, stack = {}, []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                hash[stack.pop()] = i
            stack.append(i)
        if len(hash) == 0:  #hash表没有值，说明当前数是所有nums组合中最大的了
            return -1
        #key, value对应的都是nums的索引,按key大小，找最大的键值对.最大键值对意味着越接近数字右边，改动越小
        key, value = max(hash.items(), key = lambda x : x[0])
        #value记录的是key之后第一个大于nums[key]的索引，但并不代表只有这个一个数nums[value]
        #大于nums[key],我们需要在value之后(包括value)的索引空间搜索，比nums[key]大的值，至少有一个
        #其值为nums[value]
        #这里写的比较拗口，简单来说就是找到在nums[value:]中大于nums[key]的最小值nums[minValueIndex]的
        #minValueIndex, 当然从上面我们可以知道，这个num[minValueIndex]一定是小于等于nums[value]
        tmpNums = [i if i > nums[key] else float('inf') for i in nums[value:]]
        minValueIndex = min(range(len(tmpNums)), key = tmpNums.__getitem__) + value

        #交换nums[key]和nums[minValueIndex]，把后面的数字升序排列
        nums[key], nums[minValueIndex] = nums[minValueIndex], nums[key]
        nums = nums[:key+1] + sorted(nums[key+1:])
        #将nums在组合成数
        res = 0
        length = len(nums)
        for i in range(length):
            res += nums[i] * (10 ** (length - i -1))
        return res if res <= 2 ** 31 -1 else -1
# @lc code=end

