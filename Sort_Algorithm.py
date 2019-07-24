#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
冒泡排序
快速排序
归并排序
堆排序
选择排序
'''
#冒泡排序
def Bubble_sort(array):
    length = len(array)
    for i in range(length): #外层排序控制排序趟数， 第 i 趟排序
        flag = False #是否进行排序的标志
        for j in range(0, length-i-1): #内层循环控制每趟排多少次
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True #如果第i趟进行了排序，则标志flag=True
        if flag == False: #本趟遍历没有发生交换，说明已经完成排序
            return array
                
#快速排序
def Quick_sort(array, start, end):
    #判断end是否小于start，若为false，直接返回
    if start < end:
        i, j = start, end
        #设置基准数
        base = array[i]
        
        while i<j:
            #如果列表后边的数，比基准数大或者相等，则前移一位，直到有比基准小的数出现
            #将大于base的数，划分到base的右边
            while (i<j) and (array[j]>=base):
                j = j-1
            array[i] = array[j] #只要跳出上面循环，说明array[j]<base，需要交换
            
            while(i<j) and (array[i]<=base):
                i = i+1
            array[j] = array[i] #只要跳出上面循环，说明array[i]>base，需要交换
            
        array[i] = base
        
        Quick_sort(array, start, i-1)
        Quick_sort(array, j+1, end)
    return array

#两个有序数组的归并排序
def Guibing_sort(array):
    A = [2,2,5]
    B = [1,2,3,4, 7, 10, 13]

    C = [] #初始化
    ai = 0 #初始化
    bi = 0 #初始化
    while ai < len(A) and bi < len(B):
        if A[ai] >= B[bi]: #
            C.append(B[bi])
            bi += 1
#        elif A[ai] < B[bi]:
        else:
            C.append(A[ai])
            ai += 1

    if ai !=len(A): #如果A有剩余，已经排好序,直接附加到C后面
        C = C + A[ai :]
    if bi != len(B):
        C= C + B[bi :]
    print('两个有序数组的归并排序:', C)

#堆排序
import heapq 

def heapq_sort(array):
    heapq.heapify(array) #将列表转化为最小堆结构
    #输出最大的k个值,k值可自定义，如k=3
    k = len(array)
    large_list = heapq.nlargest(k, array)
    #输出最小的k个值
    small_list = [heapq.heappop(array) for _ in range(k)]
    print("数组中最大的k个值为: ", large_list)
    print("数组中最小的k个值为: ", small_list)
              

if __name__ == "__main__":
#    array = [10, 18, 7, 26, 31, 65, 93, 36]
#    array = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]
#    print('冒泡排序：', Bubble_sort(array))
#    print('快速排序：', Quick_sort(array, 0, len(array)-1))
#    heapq_sort(array)
    A = [1,3,7,34,54]
    B = [2,5,9,10,18,24,76]
    C = []
    i = 0
    j = 0
    
    while i<len(A) and j<len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i = i+1
        else:
            C.append(B[j])
            j = j+1
    print(i, len(A))
    print(j, len(B))
    if i < len(A):
        C = C + A[1 :]
    if j < len(B):
        C = C + B[j :]
    print(C)
            







