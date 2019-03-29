# -*- coding: utf-8 -*-


#题目1：今日头条笔试——最小找零硬币数
#题目2：每日优鲜面试——两个有序数组，求合并后，按顺序排序输出，要求时间复杂度低
#题目3：今日头条面试——贪心算法
#题目4：小年糕笔试1
#题目5：小年糕笔试2
#题目6：求全排列算法


#题目1：今日头条笔试——最小找零硬币数
#题目表述：Z国的货币系统包含面值1元、4元、16元、64元共4中硬币，以及面值1024元的纸币，
#        现在小Y使用1024元的纸币购买了意见价值为N(0<N<=1024)的商品，请问最少他会收到
#        多少硬币？
#例如：输入 200  输出17
#思路一：利用简单的思路，每次求余
#思路二：（动态规划）记录下从i~1024-N所有需要找零的最小硬币数

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

#########################################################################
    
#题目2：每日优鲜面试——两个有序数组，求合并后，按顺序排序输出，要求时间复杂度低
#题目表述：两个有序的数组A和B，分别有序，将两组数合并为C后，按照从小到大的顺序输出。
#例如：输入：A = [1,3,7,34,56]  B = [2,5,9,10,18,24,76]
#     输出：C = [1,2,3,5,7,9,10,18,24,34,56]
#思路一（不推荐）：将C = A + B，在对C用排序算法排序
#思路二（推荐）：因为前提是A和B已经排好序，故一个一个比较A和B中值的大小，依次将小的append到C中，i += 1

#思路一：可以用各种排序方法，比如冒泡排序
def bubble_sort(array):
    length = len(array)
    for i in range(length): #外层循环控制排序趟数
        flag = False #是否进行排序的标志
        for j in range(0, length-i-1):#内层循环控制每趟排多少次
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True
        
        if flag == False:#本趟遍历后没有发生交换，说明已完成排序
            return array

A = [1,3,7,34,56]
B = [2,5,9,10,18,24,76]
C = A + B
print bubble_sort(C)

#思路二（推荐）：
#A = [1,3,7,34,56]
#B = [2,5,9,10,18,24,76]
A = [2,2,5]
B = [1,2,3,4, 7, 10, 13]

C = [] #初始化
ai = 0 #初始化
bi = 0 #初始化
while ai < len(A) and bi < len(B):
    if A[ai] >= B[bi]: #
        C.append(B[bi])
        bi += 1
    elif A[ai] < B[bi]:
        C.append(A[ai])
        ai += 1

if ai !=len(A): #如果A有剩余，已经排好序
    C = C + A[ai :]
if bi != len(B):
    C= C + B[bi :]
print C

#########################################################################
    
#题目3：今日头条面试——贪心算法
#题目表述：给定数组A,一只青蛙每次只能跳[3,4,5]步，
#       要求用贪心算法，求出跳过的数中，最小数的和sum。
#例如：A = [1,3,5,3,7,0,1,2,3,0,3,5,6,8,3,2,1,4,2,1]    
#思路：贪心算法：只要求局部最优即可，则获取每步从跳3 4 5步时对应A中最小的那个值，求和即可
#    跳到最后，会出现能够跳至少3步时，数组长度不够的问题。
#    有3中情况，C为[],C中剩下1个数，C中剩下2个数，    

A = [1,3,5,3,7,0,1,2,3,0,3,5,6,8,3,2,1,4,2,1]
pos = 0 #记录位置变量position
min_sum = 0
while pos+5 < len(A):
    B = [A[pos+3], A[pos+4], A[pos+5]]
    min_value = min(B)
    min_sum += min_value
    i = B.index(min(B)) #获取最小值的索引
    pos = pos+3+i

C = A[pos+3 :]
if C:
    min_v = min(C)
    min_sum += min_value

print min_sum

#########################################################################
    
#题目4：小年糕笔试
#题目表述：图片：小年糕笔试1
#   
#思路：判断连续的值，相差1

def solution(n,array):   
    count = 0
    for i in range(n-1):
        if array[i+1] - array[i] == 1:
            count += 1
    if array[0] == 1 and array[1] == 2:
        count += 1
    if array[n-2] == 999 and array[n-1] == 1000:
        count += 1
    return count - 1

if __name__ == "__main__":
    n = int(raw_input())
    array = [int(i) for i in raw_input().split()]

    print solution(n, array)

#########################################################################
    
#题目5：小年糕笔试
#题目表述：图片：小年糕笔试1  
#   
#思路：

def solution(n,m,A,B):
    C = [0] #区间范围
    sum_n = 0
    for i in A:
        sum_n += i
        C.append(sum_n)
    for i in B:
        for j in range(1, len(C)):
            if i in range(C[j-1]+1,C[j]+1):         
                print j, i-C[j-1]
    
if __name__ == "__main__":
    #n,m = 3, 6
    #A = [10,15,12]
    #B = [1,9,12,23,26,37]
    n, m = [int(i) for i in raw_input().split()]
    A = [int(i) for i in raw_input().split()]
    A = A[: n]
    B = [int(i) for i in raw_input().split()]
    B = B[: m]
    
    solution(n,m,A,B)

#########################################################################
    
#题目6：面试-求全排列算法
#题目表述：递归法，见
#    https://blog.csdn.net/zhoufen12345/article/details/53560099
#    https://blog.csdn.net/ASJBFJSB/article/details/85711664   
#思路：

def perm(array, begin, end):
    if begin >= end:
        print "".join(array)
    else:
        for index in range(begin, end):
            array[index], array[begin] = array[begin], array[index]
            perm(array, begin+1, end)
            array[index], array[begin] = array[begin], array[index]

array="abc"
b=list(array)
perm(array, 0, len(array))
 #----------------   
def perm(array, begin, end):
    if begin == end:
        print "".join(array)
    else:
        for i in range(begin, end):
            array[i], array[begin] = array[begin],array[i]
            perm(array, begin+1, end)
            array[i], array[begin] = array[begin],array[i]

array = list(raw_input())
perm(array, 0, len(array)) 
















