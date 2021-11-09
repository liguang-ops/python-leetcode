'''
Description: 
Author: liguang-ops
Github: https://github.com/liguang-ops
Date: 2021-09-29 21:59:45
LastEditors: liguang-ops
LastEditTime: 2021-09-30 17:30:08
'''
#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    """序列化与反序列化大概有三种方法，分别是前序，后序，和层次
    这边分别写一下，写成三个子函数，共享一个全局字符串、队列。
    前序、后序层次也分别有两种情况：一种是采用全局变量的形式，另
    一种是采用return 拼接的方式，我觉得后者更优美. 中序遍历不可
    以是因为找不到根节点
    """
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #前序遍历,这个没什么好讲的,递归方式也有两种，
        """如下：
        stringTree = ''
        def preOrder(root):
            nonlocal stringTree
            if root == None:
                stringTree = 'NULL' +','
            stringTree = str(toot.val) + ','
            preOrder(root.left)
            preOrder(root.right)
        调用的时候，先调用preOrder，然后返回stringTree, 我觉得这样写不太优美，没下面写的好看
        """
        def preOrder(root):
            if root == None:
                return 'NULL' + ','
            stringTree = str(root.val) + ','
            stringTree += preOrder(root.left)
            stringTree += preOrder(root.right)
            return stringTree

        #后序遍历：return + 拼接。 同样的道理，也可以写成上面注释的那样的全局变量的方式
        def postOrder(root):
            if root == None:
                return 'NULL' + ','
            stringTree = ''
            stringTree += postOrder(root.left)
            stringTree += postOrder(root.right)
            stringTree += str(root.val) + ','
            return stringTree

        #层次遍历,层次遍历，需要使用队列，在遍历(从队列中取节点)的过程中把下一层放入队列
        def levelOrder(root):
            stringTree = ''
            queue = []   #新建一个队列
            queue.append(root)
            while len(queue) != 0:
                cur = queue.pop(0)
                if cur == None:
                    stringTree += 'NULL' + ','
                    continue
                stringTree += str(cur.val) + ','
                queue.append(cur.left)
                queue.append(cur.right)
            return stringTree

        return levelOrder(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        """反序列化的重点在于找到根节点，对于前序遍历来说根节点在最前面，
        后序遍历根节点在最后面，事实上将后序遍历的结果翻转一下就是前序遍历
        的结果
        """
        print(data)
        listTree: List[str] = data.split(',')[:-1]
        #前序遍历反序列化
        def dePreOrder():
            nonlocal listTree
            if len(listTree) == 0 : return None
            first = listTree.pop(0)   #当前listTree
            if first == 'NULL':
                return None
            root = TreeNode(int(first))
            root.left = dePreOrder()
            root.right = dePreOrder()
            return root

        #后序遍历反序列化
        def dePostOrder():
            nonlocal listTree
            if len(listTree) == 0: return None
            last = listTree.pop()
            if last == 'NULL':
                return None
            root = TreeNode(int(last))
            root.right = dePostOrder()
            root.left = dePostOrder()
            return root 

        #层次遍历反序列化，也是需要队列和一个非常取巧的方式
        #这里的i就写的非常巧妙，解决了父节点和子节点的对应问题
        def DelevelOrder():
            if len(listTree) == 0 or listTree[0] == 'NULL': 
                return None
            queue = []
            root = TreeNode(int(listTree[0]))
            queue.append(root)  #将根节点入队列
            i= 1
            while i < len(listTree):
                parent = queue.pop(0)    #把队列中的节点出队列
                left = listTree[i]        #取出当前节点的左节点
                i += 1                 #指针偏移一个位置
                if left != 'NULL':
                    parent.left = TreeNode(int(left))
                    queue.append(parent.left)
                else:
                    parent.left = None
                right = listTree[i]
                i += 1
                if right != 'NULL':
                    parent.right = TreeNode(int(right))
                    queue.append(parent.right)
                else:
                    parent.right = None
            return root
        return DelevelOrder()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

