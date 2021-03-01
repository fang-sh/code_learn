# -*- coding: utf-8 -*-

#动态规划相关
#题目1：动态规划——找最大值
#题目2：动态规划——最长公共子序列
#题目3：动态规划—最小找零硬币数
#题目4：动态规划—最长回文子串
#题目5：动态规划—01背包问题


#题目1：动态规划——找最大值
#题目表述：给定数组arr，求数组中不相邻元素的和sum的最大值。
#例如：输入 arr = [1, 2, 4, 1, 7, 8, 3] 输出15
#      输入 arr = [4, 1, 1, 9, 1] 输出13
#   每个元素，存在选择与不选择两种情况。
#   选择arr[i], A = opt[i-2] + arr[i]
#   不选arr[i], B = opt[i-1] 
#   opt[i] = max(A, B)
#思路一（不推荐）：递归法。
#思路二（推荐）：（动态规划）记录前i个的，每个i的最优值

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

#########################################################################
    
#题目2：动态规划——最长公共子序列
#题目表述：A='ABCBDAB',B='BDCABA'，求最长公共子序列长度
#思路：
#    当i=0 or j = 0时， C[i][j] = 0
#    当i,j>0 and A[i]=B[j]时， C[i][j] = C[i-1][j-1] + 1
#    当i,j>0 and A[i]!=B[j]时， C[i][j] =max(C[i][j-1], C[i-1][j])

#A = ["a", "b", "c","d", "a", "f"]
#B = ["a", "c", "b", "c", "f"]
A = "ABCBDAB" #行
B = "BDCABA" #列
lena = len(A) #行
lenb = len(B) #列

C = [[0] * (lenb+1) for i in range(lena+1)]

for i in range(0,lena):
    for j in range(0,lenb):
        if A[i] == B[j]:
            C[i+1][j+1] = C[i][j] + 1
        else:
            C[i+1][j+1] = max(C[i+1][j] , C[i][j+1])
print C[-1][-1] #C[m][n]
       
#########################################################################

#题目3：动态规划—最小找零硬币数
#题目表述：Z国的货币系统包含面值1元、4元、16元、64元共4中硬币，以及面值1024元的纸币，
#        现在小Y使用1024元的纸币购买了意见价值为N(0<N<=1024)的商品，请问最少他会收到
#        多少硬币？
#例如：输入 200  输出17
#思路一：利用简单的思路，每次求余
#思路二：（动态规划）记录下从i~1024-N所有需要找零的最小硬币数
#       状态方程：
#   当i=c时：1
#   当i>max(Vc)时，dp[i] = min{dp[i-Vc]+1, i} Vc为硬币币值，前提i>Vc

#思路一：求余              
#coins = [1, 4, 16, 64]
#a = int(raw_input())
a = 200
n1 = 1024 - a

a1 = n1 / 64
a2 = (n1 % 64) /16
a3 = (n1 % 64) % 16 / 4
a4 = (n1 % 64) % 16 % 4 

mincoins_sum = a1 + a2 + a3 + a4
print mincoins_sum

# 贪心算法
rmb = [200, 100, 20, 10, 5, 1]
num = 6
x = 628
c = 0
for i in range(num):
    use = x // rmb[i]
    c += use
    x = x - rmb[i]*use
print(c)

#思路二：动态规划程序
def mincoins(coins,n):
    if n < 0:
        return None
#    coins = [1, 4, 16, 64]
    dp = [0] * (n+1)

    for i in range(1,n+1):
        min_n = i
        for c in coins:
            if i >= c:
                if min_n > dp[i-c] + 1:
                    min_n = dp[i-c] + 1
        dp[i] = min_n
    return dp[-1]

if __name__ == "__main__":
    a = int(raw_input())
    coins = [1, 4, 16, 64]
    n = 1024 - a
    print mincoins(coins, n)   

#########################################################################

#题目4：动态规划—最长回文子串
    
#--------------------- 
#作者：华软小白 
#来源：CSDN 
#原文：https://blog.csdn.net/chenhua1125/article/details/80395873 
#版权声明：本文为博主原创文章，转载请附上博文链接！    

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 使用动态规划，用空间换时间，把问题拆分
        # 获取字符串s的长度
        str_length = len(s)
        # 记录最大字符串长度
        max_length = 0
        # 记录位置
        start = 0
        # 循环遍历字符串的每一个字符
        for i in range(str_length):
            # 如果当前循环次数-当前最大长度大于等于1  并  字符串[当前循环次数-当前最大长度-1:当前循环次数+1]  == 取反后字符串
            if i - max_length >= 1 and s[i-max_length-1: i+1] == s[i-max_length-1: i+1][::-1]:
                # 记录当前开始位置
                start = i - max_length - 1
                # 取字符串最小长度为2，所以+=2，s[i-max_length-1: i+1]
                max_length += 2
                continue
            # 如果当前循环次数-当前最大长度大于等于0  并  字符串[当前循环次数-当前最大长度:当前循环次数+1]  == 取反后字符串
            if i - max_length >= 0 and s[i-max_length: i+1] == s[i-max_length: i+1][::-1]:
                start = i - max_length
                # 取字符串最小长度为1，所以+=1，s[i-max_length: i+1]
                max_length += 1
        # 返回最长回文子串
        return s[start: start + max_length]


if __name__ == '__main__':
    s = "babad"
    # s = "cbbd"
    sl = Solution()
    print(sl.longestPalindrome(s))


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
#########################################################################

#题目5：动态规划—01背包问题
#题目描述：
#    重量w    价值v
#      2       3 
#      3       4 
#      4       5 
#      5       8   
#      9       10
    
N = 5#一共有5件物品
Cap = 20#背包能承受最大重量

dp = [[0]*(Cap+1) for i in range(N+1)]
w = [0,2,3,4,5,9]#物品重量，注意从0开始
v = [0,3,4,5,8,10]#物品价值，与重量一一对应，注意从0开始

for k in range(1, N+1):
    for c in range(1, Cap+1):
        if w[k] > c:
            dp[k][c] = dp[k-1][c]
        else:
            A = dp[k-1][c-w[k]] + v[k]#不选第k件物品
            B = dp[k-1][c]#选第k件物品
            dp[k][c] = max(A,B)
print dp[-1][-1]
print dp[N][W]    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    