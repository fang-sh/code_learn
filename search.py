# 基础二分查找
def binarySearch(A, target):
    low,high = 0,len(A)-1
    while low <= high:
        # mid = low + (high - low) // 2
        mid = (low + high)//2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1