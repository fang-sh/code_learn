"""
(1) 用 Git 来讲讲二叉树最近公共祖先:https://mp.weixin.qq.com/s/9RKzBcr3I592spAsuMH45g
题目1：236. 二叉树的最近公共祖先

(2) 二叉搜索树第一期：https://mp.weixin.qq.com/s/ioyqagZLYrvdlZyOMDjrPw
    230. BST第K小的元素（Medium）
    538. 二叉搜索树转化累加树（Medium）
    1038. BST 转累加树（Medium）
    
    二叉搜索树第一期：https://mp.weixin.qq.com/s/SuGAvV9zOi4viaeyjWhzDw
    450. 删除二叉搜索树中的节点（Medium）
    701.二叉搜索树中的插入操作（Medium）
    700.二叉搜索树中的搜索（Easy）
    98.验证二叉搜索树（Medium）
    
二叉搜索树，99%会考察中序遍历知识点


"""
题目1：236. 二叉树的最近公共祖先
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

