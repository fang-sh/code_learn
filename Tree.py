# 参考链接：https://zhuanlan.zhihu.com/p/308150123
# 二叉树前序，中序，后序排列 固定程序
# 二叉树的深度

# 题目1：给定一个二叉树的根节点，返回它的前序遍历
# 题目2：给定一个二叉树的根节点，返回它的中序遍历
# 题目3：给定一个二叉树的根节点，返回它的后序遍历
# 题目4：二叉树搜索树（左叶子节点值均大于root值，右 leaf都小于root）, leetcode 700
# 题目5：二叉树的深度





# 题目1：给定一个二叉树的根节点，返回它的前序遍历
# 题目2：给定一个二叉树的根节点，返回它的中序遍历
# 题目3：给定一个二叉树的根节点，返回它的后序遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 前序遍历 根左右
    # 从下往上，原因是stack 栈 先入后出
    def preorderTraversal(self, root: TreeNode) -> List[int]: 
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color==WHITE: 
                stack.append((WHITE, node.right)) # 右
                stack.append((WHITE, node.left)) # 左
                stack.append((GRAY, node)) # 根
            else:
                res.append(node.val)
        return res
    
    
    #中序遍历 左根右
    def inorderTraversal(self, root: TreeNode) -> List[int]: 
        White, Gray = 0, 1
        res = []
        stack = [(White, root)]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == White:
                stack.append((White, node.right)) # 右
                stack.append((Gray, node)) # 根
                stack.append((White, node.left)) # 左
            else:
                res.append(node.val)
        return res
    
    
    # 后序遍历 左右根
    def postorderTraversal(self, root: TreeNode) -> List[int]: 
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color==WHITE:
                stack.append((GRAY, node)) # 根
                stack.append((WHITE, node.right)) # 右
                stack.append((WHITE, node.left)) # 左
            else:
                res.append(node.val)
        return res


# 题目4：二叉树搜索树（左叶子节点值均大于root值，右 leaf都小于root）, leetcode 700
# 题目描述：给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
# 法一：递归  法二：迭代
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 法一：递归
        if not root:
            return
        if root.val == val:
            return root 
        elif root.val > val:
            return self.searchBST(root.left, val) # 从根节点左边找
        elif root.val < val:
            return self.searchBST(root.right, val) # 从根节点右边找
        return None
    
    
        #法二: 迭代
        if not root:
            return
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
        return None
    
    
 # 题目5：二叉树的深度 剑指offer 55
 # 题目描述：输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。      
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left) + 1
        right_depth = self.maxDepth(root.right) + 1 
        return max(left_depth, right_depth)


