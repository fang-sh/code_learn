"""
题目1：287. 寻找重复数
"""

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
