"""
(1) 用 Git 来讲讲二叉树最近公共祖先:https://mp.weixin.qq.com/s/9RKzBcr3I592spAsuMH45g
        题目1：236. 二叉树的最近公共祖先

(2) 二叉搜索树第一期：https://mp.weixin.qq.com/s/ioyqagZLYrvdlZyOMDjrPw
        题目1：230. BST第K小的元素（Medium）
        题目2：538. 二叉搜索树转化累加树（Medium）
        题目3：1038. BST 转累加树（Medium）
    
(3) 二叉搜索树第一期：https://mp.weixin.qq.com/s/SuGAvV9zOi4viaeyjWhzDw
        题目1：450. 删除二叉搜索树中的节点（Medium）
        题目2：701.二叉搜索树中的插入操作（Medium）
        题目3：700.二叉搜索树中的搜索（Easy）
        题目4：98. 验证二叉搜索树（Medium）
    
* 二叉搜索树，90%会考察中序遍历知识点


(4) 东哥手把手带你套框架刷通二叉树|第一期: https://mp.weixin.qq.com/s/izZ5uiWzTagagJec6Y7RvQ
        题目1：226. 翻转二叉树，难度 Easy
        题目2：114. 将二叉树展开为链表，难度 Medium
        题目3：116. 填充二叉树节点的右侧指针，难度 Medium

(5) 东哥手把手帮你刷通二叉树|第二期: https://mp.weixin.qq.com/s/OlpaDhPDTJlQ5MJ8tsARlA
        题目1：654.最大二叉树（难度 Medium）
        题目2：105.从前序与中序遍历序列构造二叉树（难度 Medium）
        题目3：106.从中序与后序遍历序列构造二叉树（难度 Medium）

(6) 东哥手把手带你刷二叉树|第三期: https://mp.weixin.qq.com/s/LJbpo49qppIeRs-FbgjsSQ
        题目1：652. 寻找重复的子树
        
   
(n)
        题目1：112. 路径总和
        题目2：113. 路径总和 II
        题目3：543. 二叉树的直径
        题目4：617. 合并二叉树
        题目5：110. 平衡二叉树
        
        ### 二叉树的层序遍历
        题目6：102.二叉树的层序遍历（面试）
        # 题目7：107.二叉树的层序遍历II （思路同102）
        题目8：199.二叉树的右视图
        # 题目9：637.二叉树的层平均值 （思路同102）
        题目10：429.N叉树的层序遍历
        题目11：515.在每个树行中找最大值
        题目12：116
        题目13：117
        ### 二叉树的层序遍历
        
        题目14：589. N 叉树的前序遍历
        题目15：590. N 叉树的后序遍历
        题目16：96. 不同的二叉搜索树
        题目17：108. 将有序数组转换为二叉搜索树
        

        
"""

------------------------（1）-------------------------------

"""
题目1：236. 二叉树的最近公共祖先
"""
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: # 如果p和q都在以root为根的树中，函数返回的即使p和q的最近公共祖先节点。
            return root
        if not left and not right: # 那如果p和q都不在以root为根的树中怎么办呢？函数理所当然地返回null呗。
            return None
        if left: # 那如果p和q只有一个存在于root为根的树中呢？函数就会返回那个节点。
            return left 
        else:
            return right


------------------------（2）-------------------------------
"""
题目1：230. BST第K小的元素（Medium）
"""
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)
        inOrder(root)
        return res[k-1]

"""
题目2：538. 二叉搜索树转化累加树（Medium）
题目3：1038. BST 转累加树（Medium）
"""
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total = 0 # 
        
        def inorder(root):
            if not root:
                return
            inorder(root.right)
            self.total += root.val #
            root.val = self.total #
            inorder(root.left)
            
        inorder(root)
        return root


------------------------（3）-------------------------------
"""
题目3：700. 二叉搜索树中的搜索
"""
# 法一：迭代法
def searchBST(root, val):
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

# 法二：递归法
def searchBST(root, val):
    if not root:
        return
    if root.val == val:
        return root
    elif root.val > val:
        return self.searchBST(root.left, val)
    elif root.val < val:
        return self.searchBST(root.right, val)
    
"""
题目4：98. 验证二叉搜索树（Medium）
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []

        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        if res == sorted(res) and len(res) == len(set(res)):
            return True
        return False
------------------------（4）-------------------------------
"""
题目1：226. 翻转二叉树，难度 Easy
"""
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

"""
题目2：114. 将二叉树展开为链表，难度 Medium
"""
# 法一：后序遍历
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left) # 左
        self.flatten(root.right) # 右
        # 根
        # **** 后序遍历位置 ****   
        # 1、左右子树已经被拉平成一条链表
        left = root.left
        right = root.right
        # 2、将左子树作为右子树
        root.left = None
        root.right = left
        # 3、将原先的右子树接到当前右子树的末端
        p = root
        while p.right:
            p = p.right
        p.right = right
# 法二：前序遍历
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        # 根
        # **** 后序遍历位置 ****   
        # 1、左右子树已经被拉平成一条链表
        left = root.left
        right = root.right
        
        root.left = None # 2、将左子树作为右子树
        root.right = left
        
        p = root # 3、将原先的右子树接到当前右子树的末端
        while p.right:
            p = p.right
        p.right = right
        
        self.flatten(root.left) # 左
        self.flatten(root.right) # 右
"""
题目3：116. 填充二叉树节点的右侧指针，难度 Medium
"""
def connect(self, root: 'Node') -> 'Node':
        # 定义
        def connectTwoNode(node1, node2):
            if not node1 or not node2:
                return
            node1.next = node2
            connectTwoNode(node1.left, node1.right)
            connectTwoNode(node2.left, node2.right)
            connectTwoNode(node1.right, node2.left)
        # 执行
        if not root: 
            return None
        connectTwoNode(root.left, root.right)
        return root


------------------------（5）-------------------------------
"""
题目1：654.最大二叉树（难度 Medium）
"""
def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
    if not nums:
        return
    root = TreeNode(max(nums))
    idx = nums.index(max(nums))
    root.left = self.constructMaximumBinaryTree(nums[: idx])
    root.right = self.constructMaximumBinaryTree(nums[idx+1 :])
    return root

"""
题目2：105.从前序与中序遍历序列构造二叉树（难度 Medium）
"""
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    index = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1: index+1], inorder[: index])
    root.right = self.buildTree(preorder[index+1 :], inorder[index+1 :])
    return root

"""
题目3：106.从中序与后序遍历序列构造二叉树（难度 Medium）
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder: # 终止条件
            return
        
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[: idx], postorder[: idx])
        root.right = self.buildTree(inorder[idx+1 :], postorder[idx: -1])
        return root


------------------------（n）-------------------------------
"""
题目1：112. 路径总和
"""
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if root.val == targetSum and not root.left and not root.right:
            return True 
        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)
        return left or right

"""
题目1：113. 路径总和 II
"""
# 法一：非递归方法
def pathSum(root, targetSum):
    if not root:
        return []
    res = []
    stack = [([root.val], root)]

    while stack:
        tmp, node = stack.pop()
        if not node.left and not node.right and sum(tmp)==targetSum:
            res.append(tmp)
        if node.left:
            stack.append((tmp+[node.left.val], node.left))
        if node.right:
            stack.append((tmp+[node.right.val], node.right))
        # print(stack)
        # print('---------------')
    return res

# (推荐)法二：递归方法
def pathSum(root, targetSum):
    
    def helper(root, tmp, targetSum):
        if not root:
            return []
        if targetSum == root.val and not root.left and not root.right:
            tmp += [root.val]
            res.append(tmp) # targetSum是节点的和，只有到最后一步才会满足，所以可以再这一步用res直接append
        helper(root.left, tmp+[root.val], targetSum-root.val)
        helper(root.right, tmp+[root.val], targetSum-root.val)
    
    res = []
    helper(root,[], targetSum)
    return res    

"""
题目3：543. 二叉树的直径

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/diameter-of-binary-tree/solution/er-cha-shu-de-zhi-jing-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        
        def depth(node):
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
    
"""
题目4：617. 合并二叉树
"""
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        
        m = TreeNode(root1.val + root2.val)
        m.left = self.mergeTrees(root1.left, root2.left)
        m.right = self.mergeTrees(root1.right, root2.right)
        return m
    
"""
题目5：110. 平衡二叉树
"""
# 法一：从顶至底（暴力法）
# 此方法容易想到，但会产生大量重复计算，时间复杂度较高。
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1
            
        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# (推荐)法二：从底至顶（提前阻断）
# 此方法为本题的最优解法，但“从底至顶”的思路不易第一时间想到。
# 思路是对二叉树做先序遍历，从底至顶返回子树最大高度，若判定某子树不是平衡树则 “剪枝” ，直接向上返回。
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 定义函数
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            if left == -1 or right == -1 or abs(left - right)>1:
                return -1
            else:
                return max(left, right) + 1
        # 执行
        return height(root) >= 0

"""
题目6：102.二叉树的层序遍历（面试）
思路：队列queue，BFS
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# （推荐）法一：面试考过
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        # 定义队列queue
        queue = [root]
        res = [] 

        while queue:
            size = len(queue) # 一层一层的遍历
            tmp = []
            for i in range(size): # 一层一层的遍历
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        
        return res
# （推荐）法二：类似于N叉树层序遍历
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            tmp = []
            res.append([node.val for node in queue])
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
        return res
""" 
题目8：199.二叉树的右视图
思路：同102题，获取每一层的val，放在tmp中，每次把tmp[-1]最后一个值，append到res中
BFS
"""
# 法一：BFS, 同102题，获取每一层的val，放在tmp中，每次把tmp[-1]最后一个值，append到res中
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue: # 一层一层的遍历
            size = len(queue) # 一层一层的遍历
            tmp = [] # 存放这一层的值
            for i in range(size): # 一层一层的遍历
                node = queue.pop(0) # 先把左边的值pop出
                tmp.append(node.val)
                if node.left: # 先把左子树放进去
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp[-1])
        return res

# (推荐)法二：bfs，思路：存放每一层所有的节点
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []

        def bfs(root):
            queue = [root]
            while queue:
                tmp = [] # 存放每一层所有的节点
                res.append(queue[-1].val)
                for node in queue:
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
                queue = tmp # 更新queue，每次表示其中一层
        bfs(root)
        return res
# 法三：DFS 
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        
        def dfs(root, depth):
            if not root:
                return
            if len(res) <= depth:
                res.append(0)
            res[depth] = root.val
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
            
        dfs(root, 0)
        return res
"""
题目10：429.N叉树的层序遍历
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            tmp = [] # 存放一层的所有节点
            res.append([node.val for node in queue])
            for node in queue:
                for child in node.children:
                    tmp.append(child)
            queue = tmp # 更新queue，每次表示其中一层
        return res

"""
题目14：589. N 叉树的前序遍历
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(root):
            if not root:
                return []

            res.append(root.val) # 前序
            for child in root.children:
                helper(child)
        helper(root)
        return res

"""
题目15：590. N 叉树的后序遍历
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def helper(root):
            if not root:
                return []
            for child in root.children:
                helper(child)
            res.append(root.val)
        
        helper(root)
        return res

"""
题目16：96. 不同的二叉搜索树

作者：xiao-yan-gou
链接：https://leetcode-cn.com/problems/unique-binary-search-trees/solution/er-cha-sou-suo-shu-fu-xi-li-zi-jie-shi-si-lu-by-xi/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。 


作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
# 法一：动态规划
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            count = 0
            for j in range(i):
                count += dp[j] * dp[i-j-1]
            dp[i] = count
        return dp[n]
# 法二：动态规划
class Solution:
    def numTrees(self, n: int) -> int:
        
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]
  
"""
题目17：108. 将有序数组转换为二叉搜索树
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 选择任意一个中间位置数字作为根节点
        # 中序遍历

        def helper(left, right):
            if left > right:
                return None
            mid = (left + right + randint(0,1))//2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid+1, right)
            return root
        return helper(0, len(nums)-1)
# 法二：中间节点
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        # 找到中点作为根节点
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        # 递归调用
        node.left = self.sortedArrayToBST(nums[: mid]) 
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node 