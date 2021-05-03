"""
题目1：剑指 Offer 14- I. 剪绳子（LeetCode）
题目2：64. 最小路径和
题目3：152. 乘积最大子数组
"""

"""
题目1：剑指 Offer 14- I. 剪绳子（LeetCode）

作者：edelweisskoko
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/jian-zhi-offer-14-i-jian-sheng-zi-huan-s-xopj/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(2, i):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n]

"""
题目2：64. 最小路径和
思路：动态规划
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 动态规划
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*(n) for _ in range(m)] # m行 n列
        dp[0][0] = grid[0][0]
        # base case
        for i in range(1, m): # m行
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1,n): # n列
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # 状态转移
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(
                    dp[i-1][j],
                    dp[i][j-1]
                ) + grid[i][j]
        return dp[m-1][n-1]

"""
题目3：152. 乘积最大子数组
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val = float('-inf')
        imax, imin = 1, 1 # 记录当前最大值，最小值
        for i in range(len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])
            max_val = max(max_val, imax)
        return max_val