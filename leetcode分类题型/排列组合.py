"""
题目1：46. 全排列
题目2：78. 子集
题目3：77. 组合
题目4：17. 电话号码的字母组合
题目5：39. 组合总和
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

"""
题目3：77. 组合
思路：树图，k限制树的最大高度为k， n限制了最大宽度
思路：回溯法
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(n, k, start, track):
            if k == len(track):
                res.append(track)
                return
            for i in range(start, n+1):
                backtrack(n, k, i+1, track+[i])
        backtrack(n, k, 1, [])
        return res

"""
题目4：17. 电话号码的字母组合
思路：回溯法
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
    
        res = []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(track, digits):
            if not digits:
                res.append(track)
                return
            for letter in phone[digits[0]]:
                backtrack(track+letter, digits[1:])
        backtrack('', digits)
        return res
    
"""
题目5：39. 组合总和
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(candidates, track, target):
            if target == 0: # if target <= 0:
                track.sort()
                if track not in res:
                    res.append(track)
                # track = [] # 没有这一句也可以
                return 
            for i in candidates:
                if target - i >= 0:
                    backtrack(candidates, track+[i], target - i)
        backtrack(candidates, [], target)
        return res



