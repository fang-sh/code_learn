"""
(1) (强烈推荐)B站视频讲解动态规划：https://www.bilibili.com/video/BV12W411v7rd/?spm_id_from=333.788.recommend_more_video.-1
        题目1：动态规划——找不相邻位置元素和的最大值。198.打家劫舍(leetcode)
        题目2：198.打家劫舍(leetcode)

(2) 经典动态规划：打家劫舍系列问题: https://mp.weixin.qq.com/s/z44hk0MW14_mAQd7988mfw
        题目1：198. 打家劫舍
        题目2：213. 打家劫舍 II
        题目3：337. 打家劫舍 III
"""
------------------------（1）-------------------------------
"""
题目n：198.打家劫舍(leetcode)

动态规划——找不相邻位置元素和的最大值

#题目表述：给定数组arr，求数组中不相邻元素的和sum的最大值。
#例如：输入 arr = [1, 2, 4, 1, 7, 8, 3] 输出15
#      输入 arr = [4, 1, 1, 9, 1] 输出13
#   每个元素，存在选择与不选择两种情况。
#   选择arr[i], A = opt[i-2] + arr[i]
#   不选arr[i], B = opt[i-1] 
#   opt[i] = max(A, B)
#思路一（不推荐）：递归法。
#思路二（推荐）：（动态规划）记录前i个的，每个i的最优值
"""
#思路一：不推荐，递归法
def rec_opt(arr, i):
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    else:
        A = rec_opt(arr, i-2) + arr[i]
        B = rec_opt(arr, i)
        return max(A, B)

arr = [1, 2, 4, 1, 7, 8, 3]
print rec_opt(arr, len(arr))

#思路二：推荐，动态规划，保存前i次的最优结果

def dp_opt(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr[0], arr[1])
    
    opt = [0] * (len(arr))
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        A = opt[i-2] + arr[i]
        B = opt[i-1]
        opt[i] = max(A, B)
    return opt[-1]

arr = [1, 2, 4, 1, 7, 8, 3]
print dp_opt(arr)

------------------------（1）-------------------------------

"""
题目1：198.打家劫舍
"""
# (必须掌握)法一：动态规划 dp table
def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<=2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            A = dp[i-2] + nums[i] # 选择nums中，第i个元素
            B = dp[i-1] # 不选nums中，第i个元素
            dp[i] = max(A, B)
        return dp[-1]
    
 # 法二：只更新2个状态
 def rob(nums):
    n = len(nums)
    dp_i_1 = 0 # 第 i-1 的状态
    dp_i_2 = 0 # 第 i-2 的状态
    dp_i = 0 # 第 i 的状态
    for i in range(0, n):
        dp_i = max(dp_i_1, dp_i_2+nums[i])
        dp_i_2 = dp_i_1
        dp_i_1 = dp_i
    return dp_i

"""
题目2：213. 打家劫舍 II
思路：2种情况，nums[:-1], nums[1:]，结果取最大值
"""
def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.robRange(nums[:-1]), self.robRange(nums[1:]))
    
    def robRange(self, nums):
        n = len(nums)
        dp_i_1 = 0 # 第 i-1 的状态
        dp_i_2 = 0 # 第 i-2 的状态
        dp_i = 0 # 第 i 的状态

        for i in range(n):
            dp_i = max(dp_i_1, nums[i]+dp_i_2)
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i 
        return dp_i
    
"""
题目3：337. 打家劫舍 III
"""
class Solution:
    def rob(self, root: TreeNode) -> int:
        res = self.dp(root)
        return max(res[0], res[1]) # 取最大值


    def dp(self, root):
        if not root:
            return [0, 0] # 抢，不抢
            
        left = self.dp(root.left)
        right = self.dp(root.right)

        # 抢，下家就不能抢了
        rob = root.val + left[0] + right[0]
        # 不抢，下家可抢可不抢，取决与收益大小
        not_rob = max(left[0], left[1]) + max(right[0], right[1])
        # not_rob = max(left) + max(right)

        return [not_rob, rob]