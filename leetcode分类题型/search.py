"""
(1) 我作了首诗，保你闭着眼睛也能写对二分查找:https://mp.weixin.qq.com/s/M1KfTfNlu4OCK8i9PSAmug
(2) 二分搜索只能用来查找元素吗？:https://mp.weixin.qq.com/s/QC24hyg0ZgjR7-LgnEzMYg
(3) 二分查找算法如何运用？: https://mp.weixin.qq.com/s/0OaNLfQznaJAkjx870xRLQ

题目1：二分查找基本框架
题目2：二分查找难点题：剑指 Offer 11. 旋转数组的最小数字
题目3：50. Pow(x, n)（注意：面试考察 快速幂法）
题目4：287. 寻找重复数(面试)

（重点补充，（1）中有答案）
寻找左侧边界的二分搜索，左开右闭
寻找右侧边界的二分搜索，左闭右开
"""

""" 
题目1：二分查找基本框架：
二分查找前提：A一定是排好序的
""" 
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
# 推荐写法
def binarySearch(A, target):
    left = 0 
    right = len(A) - 1 
    while low <= high:
        mid = left + (right - left) //2 # 注意，常用这种写法
        # mid = (low + high) // 2
        if A[mid] == target:
            return mid 
        elif A[mid] < target:
            left = mid + 1
        elif A[mid] > target:
            right = mid - 1
    return -1
        
""" 
题目2：剑指 Offer 11. 旋转数组的最小数字
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/mian-shi-ti-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-3/
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/labuladong-er-fen-fa-mo-ban-shi-xiao-liao-ma-by-41/
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/python3-bao-li-he-er-fen-fa-duo-jie-fa-by-ting-tin/
""" 
class Solution:
    def minNumberInRotateArray(self, nums):
        # write code here
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid]>nums[right]: # 注意：和右侧right值相比
                left = mid + 1
            elif nums[mid]<nums[right]: 
                right = mid
            else:
                right -= 1
        return nums[left]

"""
题目3：50. Pow(x, n)
（注意：面试考察 快速幂法，字节跳动出过）
https://leetcode-cn.com/problems/powx-n/solution/50-powx-n-kuai-su-mi-qing-xi-tu-jie-by-jyd/
https://leetcode-cn.com/problems/powx-n/solution/er-fen-fa-pu-tong-xie-fa-yi-ji-wei-yun-s-cw8x/
"""
# (推荐)法一：二分查找普通写法
def myPow(self, x: float, n: int) -> float:
    res  = 1
    if n < 0:
        x = 1/x
        n = -n # n转为正数>0
        
    while n: # 通过折半计算，每次把 n 减半，降低时间复杂度
        if n%2 == 0: # n为偶数
            x *= x
            n /= 2
        else:
            res *= x
            n -= 1
    return res

# (尽量掌握，不强求)法二：位运算+二分查找
def myPow(self, x: float, n: int) -> float:
    res = 1
    if n < 0:
        x = 1/x
        n = -n # 转为正数
    while n:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res

"""
题目4：287. 寻找重复数
面试过，考察二分查找

作者：Nicosauto
链接：https://leetcode-cn.com/problems/find-the-duplicate-number/solution/python-xun-zhao-zhong-fu-shu-by-nicosaut-o8zu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
# 法一：普通方法
def findDuplicate(self, nums: List[int]) -> int:
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            return i

# (面试考察)法二：二分查找
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right-left)//2
            cnt = 0
            for n in nums:
                if n <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid
        return left