"""
题目1：3. 无重复字符的最长子串
题目2：56. 合并区间
题目3：50. Pow(x, n)
题目4：402. 移掉K位数字
题目5：22. 括号生成
题目6：238. 除自身以外数组的乘积
"""

            
##########################################################################

"""
题目1：3. 无重复字符的最长子串
思路：滑动窗口
"""
# 法一：
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_r = 0
        r = ''
        for i in s: # 一次遍历
            if i not in r:
                r += i
            else:
                r = r[r.index(i)+1:] + i #滑动窗口
            max_r = max(max_r, len(r))
        return max_r
# 法二：
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口
        window = []
        left = 0
        right = 0
        max_len = 0
        while right < len(s):
            if s[right] not in window:
                window.append(s[right])
                right += 1
            else:
                window.remove(s[left]) # 注意此处为left
                left += 1
                # right += 1
            max_len = max(max_len, right - left)
        return max_len

"""
题目2：56. 合并区间
思路：先对输入排序，排序方法需要记住，再合并（分析）
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0]) # 记住写法
        print(intervals)
        
        res = []
        for item in intervals:
            if not res or res[-1][1] < item[0]:
                res.append(item)
            else:
                # 这种写法能通过，但是排序的intervals，下面的写法更好
                # a = res.pop()
                # res.append([a[0], max(a[1], item[1])])
                res[-1][1] = max(res[-1][1], item[1])
        return res

"""
题目3：50. Pow(x, n)
思路：需要优化，不然超时，n为奇数，n为偶数时分别判断
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
            
        res = 1
        
        while n > 0:
            if n % 2 == 0: # 当n为偶数时
                x *= x
                n /= 2
            else:
                res = res * x # 当n为奇数时
                n -= 1
        return res
    
"""
题目4：402. 移掉K位数字
思路：栈 stack
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        stack = []
        remain = len(num) - k
        for i in num:
            while stack and k>0 and i<stack[-1]:
                stack.pop()
                k -= 1
            stack.append(i)
        return str(int(''.join(stack)[:remain]))

"""
题目5：22. 括号生成
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n <= 0:
            return res
        self.dfs(n, '', res, 0, 0)
        return res
    
    def dfs(self, n, path, res, left, right):
        if left > n or right > left:
            return 
        if len(path) == 2 * n:
            res.append(path)
            return
        self.dfs(n, path+'(', res, left+1, right)
        self.dfs(n, path+')', res, left, right+1)

"""
题目6：238. 除自身以外数组的乘积
"""
# 法一：
# https://leetcode-cn.com/problems/product-of-array-except-self/solution/product-of-array-except-self-shang-san-jiao-xia-sa/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(2)
        res = [1]
        p = 1
        q = 1
        for i in range(len(nums)-1):
            p *= nums[i]
            res.append(p)
        for i in range(len(nums)-1, 0, -1):
            q *= nums[i]
            res[i-1] *= q
        return res

# 法二：
# https://leetcode-cn.com/problems/product-of-array-except-self/solution/gan-jue-da-bu-fen-ti-jie-du-shi-tie-dai-ma-jia-fu-/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [1] * n
        r = [1] * n 
        for i in range(1, n):
            l[i] = l[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            r[i] = r[i+1] * nums[i+1]
        res = []
        for i in range(n):
            res.append(l[i] * r[i])
        return res
