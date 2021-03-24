"""
题目1：46. 全排列
题目2：78. 子集
"""


"""
题目：46. 全排列
思路：回溯法
"""
class Solution:
    def permute(self, nums):
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)): 
                backtrack(nums[: i]+nums[i+1:], tmp+[nums[i]])

        backtrack(nums,[])
        return res

"""
题目2：78. 子集
思路：回溯法
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        def backtrack(nums, start, track):
            res.append(track)
            for i in range(start, len(nums)):
                backtrack(nums, i+1, track+[nums[i]])
        
        backtrack(nums, 0, [])
        return res