"""
(1)动态规划详解（修订版）: https://mp.weixin.qq.com/s/Cw39C9MY9Wr2JlcvBQZMcA
    题目1：322. 零钱兑换（3种解法），求最少零钱数
(2)经动态规划：编辑距离 https://mp.weixin.qq.com/s/uWzSvWWI-bWAV3UANBtyOw
    题目1：72. 编辑距离

"""

------------------------（1）-------------------------------
"""
题目1：322. 零钱兑换（3种解法），求最少零钱数
"""
# 法一：暴力递归，leetcode 超时
def coinChange(coins, amount):
    def dp(n):
        if n == 0:
            return 0
        if n < 0:
            return -1

        res = float('inf') # INF大小写均可
        for c in coins:
            subproblem = dp(n - c)
            if subproblem == -1:
                continue
            res = min(res, subproblem+1)
        
        if res != float('inf'):
            return res
        else:
            return -1
    return dp(amount)

# 法二：递归，添加备忘录
def coinChange(coins, amount):
    memo = {}
    def dp(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('inf')
        for c in coins:
            subproblem = dp(n-c)
            if subproblem == -1:
                continue
            res = min(res, 1 + subproblem)
        memo[n] = res if res != float('inf') else -1
        return memo[n]
    return dp(amount)

# （推荐）法三：动态规划 dp table
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1) # 下标从0 ~ amount
    dp[0] = 0
    for amt in range(1, len(dp)): # 从amount=1开始
        for c in coins:
            if amt >= c: # 金额amt >= 硬币面值c，才能计算
                dp[amt] = min(dp[amt], dp[amt-c] + 1)
    if dp[amount] != float('inf'):
        return dp[amount]
    else:
        return -1
                
------------------------（2）-------------------------------          
 """
 题目1：72. 编辑距离
 """           
















------------------------（2）-------------------------------
"""
题目4：5. 最长回文子串 leetcode
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            s1 = self.find(s, i, i) # 找到以s[i]为中心的最长回文子串（假设长度为奇数）
            s2 = self.find(s, i, i+1) # 找到以s[i]和s[i+1]为中心的回文串（假设长度为偶数）
            # res = max([len(res), len(s1), len(s2)]) # res = longest(res, s1, s2)
            res = s1 if len(res)<len(s1) else res
            res = s2 if len(res)<len(s2) else res
        return res

    def find(self, s, left, right):
        """找到串s中，以left、right为中心的最长回文串"""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1: right]