"""
题目1：287. 寻找重复数
题目2：3. 无重复字符的最长子串
题目3：56. 合并区间
题目4：50. Pow(x, n)
题目5：402. 移掉K位数字
"""
##########################################################################
"""
题目1：287. 寻找重复数
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
# 法三：快慢指针
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = cir_start = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        while True:
            slow = nums[slow]
            cir_start = nums[cir_start]
            if cir_start == slow:
                return slow
            
##########################################################################

"""
题目2：3. 无重复字符的最长子串
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
                window.remove(s[left])
                left += 1
                # right += 1
            max_len = max(max_len, right - left)
        return max_len

"""
题目3：56. 合并区间
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
题目4：50. Pow(x, n)
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
题目5：402. 移掉K位数字
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