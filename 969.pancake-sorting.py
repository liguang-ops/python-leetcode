'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-10-09 13:53:32
LastEditors: liguang-ops
LastEditTime: 2021-10-09 18:49:36
'''
#
# @lc app=leetcode id=969 lang=python3
#
# [969] Pancake Sorting
#

# @lc code=start
class Solution:
    def pancakeSort1(self, arr: List[int]) -> List[int]:
        """一开始拿到这道题还以为是汉诺塔。思前想后还是不知道思路：看书上的意思，就是从前往后找，找到最大的，
        放最下面，然后继续从前往后找（最小面的那么就不再考虑了）， 找到最大的，放到最下面，直到找完，即子集
        长度为1就行。
        而放到最下面也很简单，两次反转就行
        """
        def revese(arr, tailIndex):
            #需处理数组和需要反转子集的尾索引
            arr[:tailIndex + 1] = list(reversed(arr[:tailIndex + 1])) 
        res = []   #记录反转的索引
        def sort(arr, n):
            #需处理数组和子集长度
            if n == 1: return
            #首先找到当前子集最大值的索引
            maxValue = max(arr[:n])
            maxValueIndex = arr[:n].index(maxValue)
            revese(arr, maxValueIndex)   #把最大值反转到最上面
            res.append(maxValueIndex + 1)
            revese(arr, n-1) #把最大值翻到最下面
            res.append(n)
            sort(arr, n-1) #继续调节前n-1个饼
        sort(arr, len(arr))
        return res
    def pancakeSort(self, arr: List[int]) -> List[int]:
        """这题有一个变种，上面这种求法只是给出了一个可行路径，他并非是最短路径。怎样求最短路径呢。
        比较好的方法就是用bfs。事实上就是n叉树的最小深度，树的每一叉就是在列表每一个索引进行反转，
        直到有一个节点达到要求
        """
        def revese(arr, tailIndex):
            #需处理数组和需要反转子集的尾索引
            arr[:tailIndex + 1] = list(reversed(arr[:tailIndex + 1]))
            return arr  #这里如果不处理成copy的话，arr永远指向一个地方
        
        standard = sorted(arr)
        queue = []  #队列里面存二元组，分别是反转后的列表和反转的索引
        visited = set()   #存放已经遍历过的，防止走回头路
        queue.append((arr, []))
        #记录已经穷举过的列表, 这边只需要考虑列表的唯一性就行，这样考虑：的确可能在不同res下可能会出现相同的
        #arr，由于bfs的特性，已记录在visited中的arr对应的res要么比刚检测到的相同arr对应res短，要么相等。
        #如果是短的话，由于对应子树一摸一样，总res长度肯定比后者要短，就不需要考虑；如果相等，那么总res
        #也相等，同样就也不需要考虑了
        visited.add(''.join([str(i) for i in arr]))

        while queue:
            arr, res = queue.pop(0)
            if arr == standard:
                return res
            for i in range(1, len(arr)):  #索引为0就不需要反转，直接从一开始就行
                newArr = revese(arr.copy(), i)
                newArrString = ''.join([str(i) for i in newArr])
                if newArrString not in visited:
                    newRes = res + [i + 1]
                    queue.append((newArr, newRes))
                    visited.add(newArrString)
        #一定会有解的，不需要返回[-1], 因为已经记录回头路了。
# @lc code=end

