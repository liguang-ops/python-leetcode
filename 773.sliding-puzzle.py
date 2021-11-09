#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#

# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """bfs,和密码那一题有点像。就是遍历当前0和可以和0交换的数字，
        直至到达题目给的board。难点在于怎样确定状态和选择。状态肯定是board
        但是这是一个二维列表，选择是能和0互换位置的点，二维表不好确定，但是直接用
        二维表也肯定能弄出来。这里书上给了一个更好用的方法，将二维表专为一维表，
        并用一个字典记录二维表每一个点的相邻索引。
        [[0, 1, 2],
         [3, 4, 5]] -> [0, 1, 2, 3, 4, 5]
        """
        neighborIndex = {   #key是一维表索引，value是在key索引在二维表周围的索引
            0: [1, 3],      #这个就是选择
            1: [0, 4, 2],
            2: [1, 5],
            3: [0, 4],
            4: [3, 1, 5],
            5: [2, 4]
        }
        queue = []
        #这里有个麻烦的地方，set()里面不能直接存列表，因为list是unhashable, 有两种解决办法
        # 1 把visited用list, 搜索时间复杂度O(n), 
        # 2 每次加入visited时转成字符串，感觉比上面要省一点时间
        visited = set()   
        board = [*board[0], *board[1]] #将输入二维表转为1维表
        visited.add(''.join([str(b) for b in board]))
        answer = [1, 2, 3, 4, 5, 0]    #标准答案
        step = 0
        queue.append(board.copy())

        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                if cur == answer:
                    return step
                zeroIndex = cur.index(0)  #board中元素是unique的
                for index in neighborIndex[zeroIndex]:  #找到0在二维表中相邻的点在一维表中的索引， 交换值
                    curCopy = cur.copy()
                    curCopy[index], curCopy[zeroIndex] = curCopy[zeroIndex], curCopy[index]
                    curString = ''.join([str(c) for c in curCopy])
                    if curString not in visited:
                        visited.add(curString)
                        queue.append(curCopy)
            step += 1
        return -1
# @lc code=end

