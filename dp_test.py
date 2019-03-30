# -*- coding: utf-8 -*-

#动态规划相关

#题目1：找最大值
#题目表述：给定数组arr，求数组中不相邻元素的和sum的最大值。
#例如：输入 arr = [1, 2, 4, 1, 7, 8, 3] 输出15
#      输入 arr = [4, 1, 1, 9, 1] 输出13
#   每个元素，存在选择与不选择两种情况。
#   选择arr[i], A = opt[i-2] + arr[i]
#   不选arr[i], B = opt[i-1] 
#   opt[i] = max(A, B)
#思路一（不推荐）：递归法。
#思路二（推荐）：（动态规划）记录下从i~1024-N所有需要找零的最小硬币数

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









