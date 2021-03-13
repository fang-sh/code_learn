"""
(1) 动态规划详解（修订版）: https://mp.weixin.qq.com/s/Cw39C9MY9Wr2JlcvBQZMcA
        题目1：322. 零钱兑换（3种解法），求最少零钱数
(2) 经动态规划：编辑距离 https://mp.weixin.qq.com/s/uWzSvWWI-bWAV3UANBtyOw
        题目1：72. 编辑距离
(3) 动态规划套路：最大子数组和: https://mp.weixin.qq.com/s/nrULqCsRsrPKi3Y-nUfnqg
        题目1：53. 最大子序和
(4) 从最长递增子序列学会如何推状态转移方程: https://mp.weixin.qq.com/s/7QFapCuvi-2nkh6gREcR9g
        题目1：300. 最长递增子序列
        题目2：674. 最长连续递增序列
(5) 最长递增子序列之信封嵌套问题: https://mp.weixin.qq.com/s/PSDCjKlTh8MtANdgi-QIug

(6) 详解最长公共子序列问题，秒杀三道动态规划题目: https://mp.weixin.qq.com/s/ZhPEchewfc03xWv9VP3msg
        题目1：1143.最长公共子序列（Medium）
        题目2：583. 两个字符串的删除操作（Medium）
        题目3：712.两个字符串的最小ASCII删除和（Medium）
        
        （比较难理解，以后有时间做）
(7) 子序列解题模板：最长回文子序列：https://mp.weixin.qq.com/s/zNai1pzXHeB2tQE6AdOXTA
        题目1：5. 最长回文子串(动态规划法不会)
        题目2：647. 回文子串(结合5理解，中心扩展法和动态规划法都要理解)

(8) 经典动态规划：0-1背包问题的变体: https://mp.weixin.qq.com/s/OzdkF30p5BHelCi6inAnNg
        题目1：416. 分割等和子集
(9) 经典动态规划：完全背包问题: https://mp.weixin.qq.com/s/zGJZpsGVMlk-Vc2PEY4RPw
        题目1：518. 零钱兑换 II
        题目2：377. 组合总和 Ⅳ

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
    for amt in range(1, amount+1): # 从amount=1开始
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

参考链接： 
    作者：powcai
    链接：https://leetcode-cn.com/problems/edit-distance/solution/zi-di-xiang-shang-he-zi-ding-xiang-xia-by-powcai-3/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    B站 熊猫刷题：https://www.bilibili.com/video/BV12k4y197mR

"""
 # 法一：暴力递归，自顶向下,超时        
def minDistance(word1, word2):
    def dp(i, j):
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1
        if word1[i] == word2[j]:
            return dp(i-1, j-1)
        else:
            # inserted = dp(i, j + 1) # 插入一个字符
            # deleted = dp(i + 1, j) # 删除一个字符
            # replaced = dp(i + 1, j + 1) # 替换一个字符
            # return 1 + min(inserted, deleted, replaced)
            return min(
                dp(i, j-1) + 1, # 插入一个字符
                dp(i-1, j) + 1, # 删除一个字符
                dp(i-1, j-1) + 1 # 替换一个字符
            )
    return dp(len(word1)-1, len(word2)-1)

# (推荐)法二：带备忘录的递归，自顶向下
def minDistance(word1, word2):
    memo = {}
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1
        if word1[i] == word2[j]:
            memo[(i, j)] = dp(i-1, j-1)
        else:
            memo[(i, j)] = min(
                dp(i, j-1) + 1,
                dp(i-1, j) + 1,
                dp(i-1, j-1) + 1
            )
        return memo[(i, j)]
    return dp(len(word1)-1, len(word2)-1)

# （推荐）法三：dp table 动态规划，自底向上
def minDistance(word1, word2):
    m, n = len(word1), len(word2) 
    dp = [[0]*(n+1) for _ in range(m+1)] # m行, n列
    # 第一行
    for i in range(n+1):
        dp[0][i] = i 
    # 第1列
    for j in range(m+1):
        dp[j][0] = j
    # 自底向上求解
    for i in range(1, m+1): # m 行
        for j in range(1, n+1): # n 列
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j]+1,
                    dp[i][j-1]+1,
                    dp[i-1][j-1] + 1
                )
    return dp[m][n]

------------------------（3）-------------------------------
"""
题目1：53. 最大子序和
"""
# (推荐)法一：动态规划，时间复杂度O(n)，空间复杂度O(n)
def maxSubArray(nums):
    if not nums:
        return 0
    dp = [float('-inf')] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        A = nums[i] # 连续子数组，要么从i开始，重新计算
        B = dp[i-1] + nums[i] # 连续子数组，要么前i-1的最大值dp[i-1]+nums[i]
        dp[i] = max(A, B)
    print(dp)
    # 找到最大子数组
    return max(dp)
# 法二：状态压缩
def maxSubArray(nums):
    if not nums:
        return 0
    dp_0 = nums[0]
    dp_1 = 0
    res = dp_0
    for i in range(1, len(nums)):
        dp_1 = max(nums[i], nums[i]+dp_0)
        dp_0 = dp_1
        res = max(res, dp_1)
    return res

------------------------（4）-------------------------------
"""
题目1：300. 最长递增子序列
题目要求：严格递增
法一，法二都要会
"""
# 法一：动态规划，时间复杂度O(n^2),4000ms
def lengthOfLIS(nums):
    if not nums:
        return 0
    dp = [1] * len(nums) # 至少为1
    # dp[0] = 1
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                A = dp[j] + 1 # 选择nums[i]
                B = dp[i] # 不选nums[i]
                dp[i] = max(A, B)
        # print(dp)
    return max(dp) # 选择dp中最大的值
# (面试应该会问该法)法二：动态规划 + 二分查找，时间大幅加快，O(NlogN), 60ms
def lengthOfLIS(nums):
    top = [0] * len(nums) #要处理的扑克牌
    res = 0 # 初始化牌堆为0
    for i in nums:
        left = 0
        right = res

        # 搜索左边界的二分查找(右边界闭，左开右闭)
        while left < right:
            mid = left + (right - left)//2
            if top[mid] < i:
                left = mid + 1
            else:
                right = mid
            
        # 如果没有找到合适的，新建一堆，res加一
        if right == res:
            res += 1

        top[left] = i # 把这张牌放到牌堆顶
    return res # 牌堆数就是 LIS 长度


"""
674. 最长连续递增序列
"""
# （推荐）法一：
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        dp = [1] * length
        for i in range(1,length):
            if nums[i]>nums[i-1]: # 连续递增
                dp[i] = dp[i-1] + 1
            else: # 从当前位置重新开始计算
                dp[i] = 1
        return max(dp)
# （推荐）法二：   
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        dp = [0] * length
        dp[0] = 1
        for i in range(1,length):
            if nums[i]>nums[i-1]: # 连续递增
                dp[i] = dp[i-1] + 1
            else: # 从当前位置开始计算
                dp[i] = 1
        return max(dp)

------------------------（5）-------------------------------         




------------------------（6）-------------------------------
"""
题目1：1143.最长公共子序列（Medium）
"""



------------------------（7）-------------------------------
"""
题目1：5. 最长回文子串 leetcode
"""
# (推荐)法一: 遍历，中心扩展法
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
    
# (必须掌握)法二：动态规划
def longestPalindrome(s):
    目前还不会

"""   
题目2：647. 回文子串(结合5理解，中心扩展法和动态规划法都要理解)
"""
# (掌握)法一：中心扩展法
class Solution:
    def countSubstrings(self, s: str) -> int:
        c1 = 0
        c2 = 0
        for i in range(len(s)):
            c1 += self.find(s, i, i) 
            c2 += self.find(s, i, i+1)
        return c1+c2
 
    def find(self, s, left, right):
        count = 0
        while left>=0 and right<len(s) and s[left]==s[right]:
            left -= 1
            right += 1
            count += 1
        return count

# (掌握)法二：动态规划法
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n): # i 列
            for j in range(i+1): # j 行
                if s[i]==s[j] and (i-j<2 or dp[j+1][i-1]):
                    dp[j][i] = 1
                    res += 1
        return res

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        # 枚举所有可能 因为代表子串 所以 i <= j
        for j in range(n):
            for i in range(j+1):
                # 子串长度
                length = j - i + 1
                # 只有一个字符，直接就是一个回文串
                if length == 1:
                    dp[i][j] = True
                    count += 1
                # 两个字符，只有相等才是回文串
                if length == 2 and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
                # 超过两个字符 首位相同 且除去首尾的子串是回文串 才是回文串
                if length > 2 and s[i]==s[j] and dp[i+1][j-1] is True:
                    dp[i][j] = True
                    count += 1
        return count


------------------------（8）-------------------------------
"""
题目1：416. 分割等和子集
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numSum = sum(nums)
        if numSum % 2 != 0:
            return False
        
        capacity = numSum // 2
        if capacity < max(nums):
            return False
        
        bag = [False] * (capacity+1)
        bag[0] = True
        for i in nums:
            for j in range(len(bag)-1, -1, -1):
                if j >= i:
                    bag[j] |= bag[j-i] # bag[j] = bag[j] or bag[j-i]
        return bag[len(bag)-1]

------------------------（9）-------------------------------
"""
题目1：518. 零钱兑换 II
"""
def change(amount, coins):
    dp = [0] * (amount + 1) # 金额从0 ~ amount
    dp[0] = 1
    for c in coins: # 遍历物品
        for amt in range(1, amount+1): # 遍历背包
            if amt >= c:
                dp[amt] += dp[amt - c]
    print(dp)
    return dp[amount]













------------------------（n）-------------------------------
"""
题目n：5. 最长回文子串 leetcode
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
    
    
    
