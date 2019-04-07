# -*- coding: utf-8 -*-

#动态规划相关
#题目1：动态规划——找最大值
#题目2：动态规划——最长公共子序列
#题目3：动态规划—最小找零硬币数

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




