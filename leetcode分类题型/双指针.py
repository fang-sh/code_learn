"""
（1）双指针技巧总结和常见题目类型：https://mp.weixin.qq.com/s/yLc7-CZdti8gEMGWhd0JTg
题目1：141. 环形链表，判断链表是否有环
题目2：142. 环形链表2，判断链表是否有环，并且返回环节点索引，起始位置
题目3：876. 链表的中间结点
题目4：剑指 Offer 22. 链表中倒数第k个节点（leetcode）
题目5：19. 删除链表的倒数第 N 个结点（在题目4的基础上改造）

（2）双指针技巧秒杀四道数组/链表题目：https://mp.weixin.qq.com/s/55UPwGL0-Vgdh8wUEPXpMQ
要求：在原地修改，不用额外空间，leetcode题目
    题目1：26.删除排序数组中的重复项
    题目2：83.删除排序链表中的重复元素
    题目3：27.移除元素
    题目4：283.移动零
    题目5：203. 移除链表元素
    
    
(n) 只有题目
题目1： 11. 盛最多水的容器
题目2：牛客网剑指offer：旋转数组的最小数字
"""

------------------------（1）-------------------------------
"""
题目1：141. 环形链表，判断链表是否有环
注意：不要改变链表
思路：快慢指针法。慢指针slow一次一步，快指针fast一次两步。当slow==fast时，表示有环。
    slow走k步， 则fast走2k步
"""
def hasCycle(head):
    slow = fast = head # 初始都赋值head
    while fast and fast.next: # 注意：fast fast.next
        slow = slow.next # 在slow上动
        fast = fast.next.next # 在slow上动
        if slow == fast: # 也可写成 if slow is fast:
            return True 
    return False

#######################################################

"""
题目2：142. 环形链表2，判断链表是否有环，并且返回环节点索引，起始位置
注意：不要修改原始链表
思路：快慢指针法。慢指针slow一次一步，快指针fast一次两步。当slow==fast时，表示有环。
    *** 判断有环时，此时slow到环起点的距离=head到环起点的距离，两者一起动，找到相交点 ***
"""
def detectCycle(head):
    slow = fast = head 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if slow is fast: # 表示有环
            res = head # 此时slow到环起点的距离=head到环起点的距离
            while slow != res:
                slow = slow.next 
                res = res.next 
            return res
    return None

#######################################################

"""
题目3：876. 链表的中间结点
注意：不要修改原始链表
思路：快慢指针法。慢指针slow一次一步，快指针fast一次两步。
    当遍历完一遍链表之后，slow刚好在中间位置。
    slow走k步， 则fast走2k步。
    奇数时，slow在中间，偶数时，slow在中间偏右的位置。
"""           
def middleNode(head):
    slow = fast = head
    while fast and fast.next: # 注意：fast and fast.next
        slow = slow.next 
        fast = fast.next.next
    return slow # 奇数时，slow在中间，偶数时，slow在中间偏右的位置

#######################################################

"""
题目4：剑指 Offer 22. 链表中倒数第k个节点（leetcode），目的是 找到 倒数第k个节点
思路：快慢指针法。
    让快指针先走 k 步，然后快慢指针开始同速前进。
    这样当快指针走到链表末尾 null 时，
    慢指针所在的位置就是倒数第 k 个链表节点（为了简化，假设 k 不会超过链表长度）
"""
def getKthFromEnd(head, k):
    slow = fast = head
    while k>0:
        fast = fast.next # fast先走k步
        k -= 1
    
    while fast: # 注意，此处只有fast
        slow = slow.next
        fast = fast.next
    return slow #fast 遍历完后，slow在中间位置

# 牛客网 剑指offer:输入一个链表，输出该链表中倒数第k个结点。
# 此题需要注意的特殊情况很多，需要关注一下
def FindKthToTail(head, k):
        # write code here
        if not head or k<=0:
            return None
        
        slow = fast = head
        
        while k>0:
            if fast: # k<=链表总长度
                fast = fast.next
                k -= 1
            else: # k>链表总长度
                return None
            
        while fast:
            slow = slow.next
            fast = fast.next
        return slow


"""
题目5：19. 删除链表的倒数第 N 个结点（在题目4的基础上改造），目的是 删除 倒数第k个节点
思路：快慢指针法。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # p = head
        # length = 0
        # while p:
        #     length += 1
        #     p = p.next
        # k = length - n + 1
        # p = ListNode(0, head)
        # cur = p
        # for i in range(1, k):
        #     cur = cur.next
        # cur.next = cur.next.next 
        # return p.next
        if not head or n<=0:
            return head
        
        slow = fast = head

        pre_slow = ListNode(0,head) #在head前，添加新的节点
        q = pre_slow

        while n>0:
            if fast: # n<=链表最大长度
                fast = fast.next
                n -= 1
            else: # n>链表最大长度
                return head

        while fast:
            pre_slow = pre_slow.next
            slow = slow.next
            fast = fast.next
        # 跳出while后, slow指向要删除的节点，pre_slow为slow的前一个节点
        pre_slow.next = slow.next # 删除slow节点
        return q.next
------------------------（2）-------------------------------
"""
题目1：26.删除排序数组中的重复项
注意：是排序数组
输入：[1,1,2] 输出：[1,2]
输入：[0,0,1,1,1,2,2,3,3,4] 输出：[0, 1, 2, 3, 4]
"""
# 法一：推荐（4道题相同模式）
def removeDuplicates(nums):
    i = 0
    while i+1 < len(nums): # 注意 i+1，因为快指针 i+1 需要先到达 或 while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.pop(i)
        else:
            i += 1 
    return nums # leetcode不需要return

# 法二：链接（2）中作者思路（4道题相同模式）
def removeDuplicates(nums):
    if len(nums)==0:
        return 0
    slow = 0
    fast = 0 
    while fast < len(nums):
        if nums[slow] != nums[fast]: # 注意： !=
            slow += 1 # 注意：先slow += 1, 再赋值
            nums[slow] = nums[fast]
        fast += 1 # if之外执行
    # return slow + 1 # leetcode需要返回该值才能通过编译
    return nums[: slow+1]

#######################################################

"""
题目2：83.删除排序链表中的重复元素
注意：排序链表
输入：1->1->2 输出：1->2 
输入：1->1->2->3->3 输出：1->2->3
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next
    
# 法一：推荐（4道题相同模式）
def deleteDuplicates(head):
    p = head 
    while head and head.next: # 注意，此处需要head，因为 有 head 为空的情况
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next 
    return p

# 法二：链接（2）中作者思路（4道题相同模式）
def deleteDuplicates(head):
    if not head:
        return
    slow = head 
    fast = head
    while fast: # head为空的情况，前面已经判断
        if slow.val != fast.val: # 注意： != 
            slow.next = fast # 先赋值，后++ 
            slow = slow.next
        fast = fast.next 
        
    slow.next = None # 跳出循环后，断开与后面元素的连接
    return head

#######################################################
    
"""
题目3：27.移除元素
注意：原数组上操作，不增加额外空间
输入：[3,2,2,3], val=3 输出：2, [2,2]
输入：[0,1,2,2,3,0,4,2] val=2 输出：5, [0, 1, 3, 0, 4]
"""
# 法一：推荐（4道题相同模式）
def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1 
    return nums

# 法二：链接（2）中作者思路（4道题相同模式）
def removeElement(nums, val):
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != val: # 注意： !=
            nums[slow] = nums[fast] # 先赋值，后++
            slow += 1 
        fast += 1 
    return slow, nums[: slow]

#######################################################
"""
题目4：283.移动零
注意：
输入：[1,1,2] 输出：[1,2]
输入：[0,0,1,1,1,2,2,3,3,4] 输出：[0, 1, 2, 3, 4]
"""
# 法一：推荐（4道题相同模式）
def moveZeroes(nums):
    i = 0 
    n = 0 
    while i < len(nums):
        if nums[i] == 0:
            nums.pop(i)
            n += 1 
        else:
            i += 1 
    # for i in range(n):
    #     nums.append(0)
    nums[:] = nums + [0]*n # 注意：leetcode中是原数组修改，直接nums = nums + [0]*n会报错
    return nums # leetcode不需要return

"""
题目5：203. 移除链表元素
"""
def removeElements(head, val):
    pre_head = ListNode(None, head)
    p = pre_head
    while head:
        if head.val == val:
            pre_head.next = head.next
            head = head.next
        else:
            head = head.next
            pre_head = pre_head.next
    return p.next



------------------------（n）-------------------------------
"""
题目1：盛水最多的容器
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_vol = 0
        while left < right:
            cur = (right-left) * min(height[left], height[right])
            max_vol = max(max_vol, cur)
            if height[left] <= height[right]: # 右边更高，固定右边，移动左边，寻找左边高点
                left += 1
            else: # 左边更高，固定左边，移动右边，寻找右边高点
                right -= 1
        return max_vol



"""
题目2：牛客网剑指offer：旋转数组的最小数字
"""
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        left = 0
        right = len(rotateArray)-1
        while left < right:
            mid = left + (right-left)//2
            if rotateArray[mid]>rotateArray[right]: # 可以把[1,2,3,4,5,6,7]所有旋转数组写出来，判断应该left = mid + 1
                left = mid + 1
            elif rotateArray[mid]<rotateArray[right]:
                right = mid
            else:
                right -= 1
        return rotateArray[left]