"""
题目1：287. 寻找重复数
题目2：3. 无重复字符的最长子串
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
        left = 1
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for n in nums:
                if n <= mid:
                    cnt += 1
            if cnt > mid:
                right = mid
            else:
                left = mid + 1
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



