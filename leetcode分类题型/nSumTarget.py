'''
参考：labuladong
https://mp.weixin.qq.com/s/fSyJVvggxHq28a0SdmZm6Q
'''
"""nSumTarget通用形式"""
# 题目1：2数之和：https://leetcode-cn.com/problems/two-sum/ 此题是通用2数之和的变形，曾经出过面试题
# 题目1：2数之和：通用解法
# 题目2：3数之和：https://leetcode-cn.com/problems/3sum/
# 题目3：4数之和：https://leetcode-cn.com/problems/4sum/
# 题目4：n数之和：eg 100数之和


"""
题目1：2数之和-leetcode变形题（单独解法，面试时出过）
https://leetcode-cn.com/problems/two-sum/
思路：遍历一遍nums,定义哈希字典d = {}，记录出现过值的下标，判断target-nums[i]是否在d中，注意不是nums中
"""
def twoSum(nums, target):
    d = {} #记录遍历nums时出现过的值的下标
    for i in nums:
        if target - nums[i] in d: # 判断是否在d中，不是判断是否在nums中
            return [i, d[target-nums[i]]]
        d[nums[i]] = i

#########################################################################

"""
题目2：2数之和-通用
2数之和：nums = [1,3,1,2,2,3], target = 4，返回和为target的两数的值（非下标）。
        结果要求不能重复：[[1,3],[2,2]]
        比如[1,3], [3,1]就是重复
思路：① nums从小到大排序 ② 双指针 ③ 排序后，判断重复值，去重
"""
# 这样写，输出值有重复，不建议
def twoSumTarget(nums, target):
    i = 0
    j = len(nums) - 1 
    r = []
    
    # 先对数组排序
    nums.sort()
    while i < j:
        sum_v = nums[i] + nums[j]
        left = nums[i]
        right = nums[j]
        # 根据 sum 和 target 的比较，移动左右指针
        if sum_v < target:
            i+= 1
        elif sum_v > target:
            j -= 1
        else:
            r.append([nums[i], nums[j]])
            i += 1 # 进行下一步迭代
#             j -= 1
    return r

# 推荐写法
def twoSumTarget(nums, target):
    i = 0
    j = len(nums) - 1 
    r = []
    
    # 先对数组排序
    nums.sort()
    while i < j:
        sum_v = nums[i] + nums[j]
        left = nums[i]
        right = nums[j]
        # 根据 sum 和 target 的比较，移动左右指针
        if sum_v < target:
            i += 1
            # while i<j and nums[i]==left: # 跳过所有重复的元素
            #     i += 1 
        elif sum_v > target:
            j -= 1
            # while i<j and nums[j]==right: # 跳过所有重复的元素
            #     j -= 1 
        else:
            r.append([nums[i], nums[j]])
            while i<j and nums[i]==left: i += 1  # 跳过所有重复的元素
            while i<j and nums[j]==right: j -= 1 # 跳过所有重复的元素
    return r
                 
#########################################################################

"""
题目3：3数之和-通用
3数之和：nums = [-1,0,1,2,-1,-4], target = 0，返回和为target的两数的值（非下标）。
        结果要求不能重复：[[-1, 2, -1], [0, 1, -1]]
思路：① nums从小到大排序 ② 调用2sum通用函数 ③ 排序后，判断重复值，去重
"""
# 从start开始
def twoSumTarget(nums, start, target):
    #nums.sort()
    i = start # 注意i=start
    j = len(nums)-1
    r = []
    while i<j:
        sum_v = nums[i] + nums[j]
        left = nums[i]
        right = nums[j]
        
        if sum_v < target:
            i += 1
            # while i<j and nums[i]==left:
            #     i += 1
        elif sum_v > target:
            j -= 1
            # while i<j and nums[j]==right:
            #     j -= 1
        else:
            r.append([nums[i], nums[j]])
            while (i<j and nums[i]==left): i += 1
            while (i<j and nums[j]==right):j -= 1
    return r

def threeSumTarget(nums, start, target):
    nums.sort()
    length = len(nums)
    res = []
    i = start
    while i < length:
        sub = twoSumTarget(nums, i+1, target-nums[i])
        for v in sub:
            v.append(nums[i])
            res.append(v)
        while i<length-1 and nums[i]==nums[i+1]: i+= 1
        i += 1 # 进行下一步迭代
    return res

#########################################################################

"""
题目4：4数之和-通用
4数之和：nums = [1,0,-1,0,-2,2], target = 0，返回和为target的两数的值（非下标）。
        结果要求不能重复：[
                            [1, 2, -1, -2], 
                            [0, 2, 0, -2], 
                            [0, 1, 0, -1]
                        ]
思路：① nums从小到大排序 ② 调用3sum通用函数 ③ 排序后，判断重复值，去重
"""
def fourSumTarget(nums, start, target):
    nums.sort()
    length = len(nums)
    res = []
    i = start
    while i < length:
        sub = threeSumTarget(nums, i+1, target-nums[i]) # 调用3sum
        for v in sub:
            v.append(nums[i])
            res.append(v)
        while i<length-1 and nums[i]==nums[i+1]: i+= 1
        i += 1 # 进行下一步迭代
    return res

# 四数之和
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def NSum(nums, k, start, target):
            nums.sort()
            i = start
            j = len(nums)
            res = []
            if len(nums)<k or k < 2:
                return res
            elif k == 2:
                res = self.twoSum(nums, i, target)
            else:
                while i < len(nums):
                    sub = NSum(nums, k-1, i+1, target-nums[i])
                    for v in sub:
                        v.append(nums[i])
                        res.append(v)
                    while i+1<len(nums) and nums[i] == nums[i+1]:
                        i += 1
                    i += 1
            return res
        
        return NSum(nums, 4, 0, target)
            
    def twoSum(self, nums, start, target):
        i = start
        j = len(nums) - 1
        r = []
        while i < j:
            left = nums[i]
            right = nums[j]
            if left + right < target:
                i += 1
            elif left + right > target:
                j -= 1
            else:
                r.append([nums[i], nums[j]])
                while i < j and nums[i] == left: i += 1
                while i < j and nums[j] == right: j -= 1
        return r

#########################################################################

"""
题目5：n数之和-通用,100数之和，4数之和可以直接用该通用型
4数之和：nums = [1,0,-1,0,-2,2], target = 0，返回和为target的两数的值（非下标）。
        结果要求不能重复：[
                            [1, 2, -1, -2], 
                            [0, 2, 0, -2], 
                            [0, 1, 0, -1]
                        ]
思路：① nums从小到大排序 ② 递归，调用(n-1)sum通用函数 ③ 排序后，判断重复值，去重
"""
def nSumTarget(nums, n, start, target):
    # 2sum函数
    def twoSumTarget(nums, start, target):
        #nums.sort()
        i = start # 注意i=start
        j = len(nums)-1
        r = []
        while i<j:
            left = nums[i]
            right = nums[j]
            if left + right < target:
                i += 1
            elif left + right > target:
                j -= 1
            else:
                r.append([nums[i], nums[j]])
                while (i<j and nums[i]==left): i += 1 # 重复值去重 
                while (i<j and nums[j]==right): j -= 1 # 重复值去重
        return r
    
    nums.sort() #排序
    length = len(nums)
    res  = []
    i = start # &&&&&注意&&&&&：从start开始
    if n < 2 or length < n:
        return res
    if n == 2:
        sub = twoSumTarget(nums, start, target) # &&&&&注意&&&&&:此处为start， 不是i+1
        # sub = twoSumTarget(nums, i, target) # 也可以用i，因为上面定义了i=start
        # for v in sub:
        #     res.append(v)
        res = sub # 此时res = sub
    else:
        while i < length:
            sub = nSumTarget(nums, n-1, i+1, target-nums[i]) #递归调用自身
            for v in sub:
                v.append(nums[i])
                res.append(v)
            while i<length-1 and nums[i]==nums[i+1]: i += 1
            i += 1 # 进行下一步迭代
    return res

