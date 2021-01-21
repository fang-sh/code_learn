# 参考链接：https://zhuanlan.zhihu.com/p/308150123
# 二叉树前序，中序，后序排列 固定程序
# 二叉树的深度

# 题目1：给定一个二叉树的根节点，返回它的前序遍历
# 题目2：给定一个二叉树的根节点，返回它的中序遍历
# 题目3：给定一个二叉树的根节点，返回它的后序遍历
# 题目4：二叉树搜索树（左叶子节点值均大于root值，右 leaf都小于root. 二叉搜索树的中序遍历为 递增序列）, leetcode 700
# 题目5：二叉树的深度 剑指offer 55
# 题目6: 二叉搜索树的第k大节点（知识点：获取树的val，保存到list中）剑指offer 54
# 题目7：翻转二叉树
# 题目8：打印按照前序，中序，后序遍历顺序二叉树的值
# 题目9：创建BST 二叉搜索树
# 题目10: 找到树的最大值
# 题目11: 二叉堆属性：完全二叉树。最大(小)二叉堆，最大(小)值。时间复杂度nlog(n)




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


# 题目4：二叉树搜索树（左叶子节点值均大于root值，右 leaf都小于root.  二叉搜索树的中序遍历为 递增序列）, leetcode 700
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


# 题目6: 二叉搜索树的第k大节点（知识点：获取树的val，保存到list中）剑指offer 54
# 本文解法基于此性质：二叉搜索树的中序遍历为 递增序列 。

# 打印中序遍历
def dfs(root):
    if not root: return
    dfs(root.left)  # 左
    print(root.val) # 根
    dfs(root.right) # 右

作者：jyd
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/solution/mian-shi-ti-54-er-cha-sou-suo-shu-de-di-k-da-jie-d/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def kthLargest(self,root, k):
        res = [] #存放节点值
        def dfs(root, res):
            if not root:
                return
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)
        dfs(root, res)
        return res[-k]

# 题目7：翻转二叉树
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root   


# 题目8：打印按照前序，中序，后序遍历顺序二叉树的值
# 记住树的这种写法
def preOrder(root):
    if not root:
        return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)
  
# 对于BST二叉搜索树，中序遍历是按照从小到大顺序排好顺序的  
def inOrder(root):
    if not root: 
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)
    
def postOrder(root):
    if not root: 
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)
    

# 题目9：创建BST 二叉搜索树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None  
        self.right = None
        
def creatBST(nums):
    root = None
    for n in nums:
        root = insert(root, n)
    return root
    
def insert(root, val):
    if not root:
        return TreeNode(val)
    if root.val >= val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root
    
def inorder(root):
    if not root: 
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# 调用方法
root = creatBST([5,3,1,4,7,6])
inorder(root)
            
 
 # 题目10: 找到树的最大值
 # 法一：传统方式，不建议
 def maxVal(root):

     ans = traverse(root)
     return ans  
 
 def traverse(root):
     ans = None
     if not root: 
        return ans
     ans = max(ans, root.val)
    traverse(root.left)
    traverse(root.right)
    return ans
            
# 法二：递归方式，推荐
def maxVal(root):
    if not root: 
        return None
    max_left = maxVal(root.left) # 左子树最大值
    max_right = maxVal(root.right) # 右子树最大值
    return max(root.val, max_left, max_right) # 最大值一定来自这三个值

