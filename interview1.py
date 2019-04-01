# -*- coding: utf-8 -*-


#题目1：今日头条笔试——最小找零硬币数
#题目2：每日优鲜面试——两个有序数组，求合并后，按顺序排序输出，要求时间复杂度低
#题目3：今日头条面试——贪心算法
#题目4：小年糕笔试1
#题目5：小年糕笔试2
#题目6：求全排列算法
#题目7：快手笔试1-寻找奇数
#题目8：快手笔试2-非递减序列


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
    
#题目4：小年糕笔试1
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
    
#题目5：小年糕笔试2
#题目表述：图片：小年糕笔试2  
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

#########################################################################
    
#题目7：快手笔试1-寻找奇数
#题目表述：已知数组长度为n，且其中只有一个数字出现过奇数次，其他数字都出现偶数次，找出
#    出现奇数次的这个数。
#    输入：
#    5（个数）
#    2,1,2,3,1 
#    输出：3
#    输入[2,2,2,2, 1,1,1,4,4,4,1,1,1] 输出 4
#   
#思路一（不推荐）：建立一个字典，记录每个数字出现的次数，最后输出个数为奇数的数
#    这种思路虽然可以运行，但是笔试中，会超出最大内存和时间限制，通过率达不到100%
#    也限制了，无法使用array.count(i)函数，系统不能调用这个函数。
#思路二（推荐）:使用异或

#思路一：
def get_count(arr):
    if not arr:
        return None
#    for i in arr:
#        if arr.count(i) % 2 != 0:#笔试时无法调用该函数
#            return key
    res_dict = {}
    for i in arr:
        if int(i) in res_dict:
            res_dict[i] += 1
        else:
            res_dict[i] = 1
    for key in res_dict:
        if res_dict[key] % 2 != 0:
            return key

if __name__ == "__main__":
    n = int(raw_input()) # 5
    arr = [int(i) for i in raw_input().split()] # 2 1 2 3 1
    arr = arr[: n]
    print get_count(arr)
    
#思路二（推荐）：
def get_odd_times(arr):
    res = 0
    for ele in arr:
        res ^= ele
    return res

arr = [2,2,2,2, 1,1,1,4,4,4,1,1,1] 
print get_odd_times(arr)

#########################################################################
    
#题目8：快手笔试2-非递减序列
#题目表述：对于一个长度为n的整数序列，你需要检查这个序列是否可以是非递减序列，假如你最多可以改变
#         其中一个数。非递减序列的定义是：array[i] <= array[i+1], for 1 <= i <= n
#输入描述：输入是一个长度为n的整数序列
#输出描述：输出为：是为1，否为0
#示例一:输入：3 4 6 5 5 7 8  输出：1（说明：将6变成4，序列变为[3,4,4,5,5,7,8],符合递减序列，因此输出1）
#示例二：输入：3 4 6 5 4 7 8 输出：0
#备注：n的取值范围为[2, 1000]   

#思路一:
def solution(arr):
    if len(arr) < 2:
        return True
    count = 0
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            count += 1
            if count > 1:
                return 0
            if i == 1 or arr[i-2] <= arr[i]:
                arr[i-1] = arr[i]
            else:
                arr[i] = arr[i-1]
    return 1
        
n = [int(i) for i in raw_input().split()]#3 4 6 5 5 7 8
print solution(n)  

#########################################################################

#题目9：牛客网-剑指offer刷题-和为S的两个数子
#题目表述：输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
#   如果有多对数字的和等于S，输出两个数的乘积最小的。
#输入描述：
#输出描述：
#思路：题目中数组array递增，已经有序。若无序，最好先排序。定义两个指针，i=0，j=len(array)-1
#        一个指针，从头开始，一个指针从尾开始。tsum为指定的和

def GetSum(A, tsum):
    i = 0
    j = len(A)-1
    while i < j:
        if (i<j) and A[i] + A[j] > tsum:
            j -= 1
        elif (i<j) and A[i] + A[j] <tsum:
            i += 1
        else:
            return A[i],A[j]
    return []


A = [1,2,3,4,5,6,7,8]
tsum = 9
print GetSum(A, tsum)
            
#########################################################################

#题目10：牛客网-剑指offer刷题-和为S的两个数子
#题目表述：小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了
#    正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
#    没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快
#    的找出所有和为S的连续正数序列? Good Luck!。
#输入描述：
#输出描述：
#思路：与题目9相比较，不一定都是low += 1 , high -= 1，本题是low +=1 , high += 1
#    本题是连续的一组数，相邻两数差为1，求出和为tsum的所有数，数的个数不定

def Find_Lianxu_Xulie(tsum):
    res = []
    low = 1#正整数，从1开始
    high = 2#两个指针之间的数求和
    while low < high:
        getsum = (low+high)*(high-low+1)/2 #更新low和high之间序列的和
        if getsum < tsum:
            high += 1
        elif getsum > tsum:
            low += 1
        else:
            zz = [i for i in range(low, high+1)]
            low += 1 #为了使循环继续，需要使low += 1
            res.append(zz)
    return res

print Find_Lianxu_Xulie(50)
#结果：[[8, 9, 10, 11, 12], [11, 12, 13, 14]]


