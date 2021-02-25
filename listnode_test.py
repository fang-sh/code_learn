# -*- coding: utf-8 -*-
#数据结构类型题：链表
#题目1-leecode-合并k个有序链表
#题目2：堆栈-判断括号是否匹配
#题目3：剑指offer-反转链表
#题目4：剑指offer-两个有序链表，拼接成有序链表输出


#########################################################################

#题目1-leecode-合并k个有序链表
#题目描述：merge k个有序链表，结果按照顺序，以链表形式输出
#输入描述：
#    Input:{
#        1->4->5,
#        1->3->4,
#        2->6
#            }
#输出描述：1->1->2->3->4->5->6
#思路：用最小堆的方式，每次pop出最小的值，即堆顶元素，构造成链表形式，输出
import heapq
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        
class Solution:
    def mergekList(self, lists[ListNode])->ListNode:
        h = [] #最小堆minheap
        
        #将链表中所有元素，放到list h中
        for head in lists:#链表形式，每个链表只提供头结点，剩下的元素需通过next输出
                          #因此，链表的list中的元素，都是头结点一个元素
            node = head
            while node: #只要node不为空
                h.append(node.val)
                #h.append(node) 有时不能直接用node，大部分情况需要用node.val
                node = node.next
        
        if not h: #忽略了[ [] ]的形式
            return None
        
        heapq.heapify(h)#将列表h构造成最小堆minheapq
        
        #构造链表，题目中要求以链表形式输出,注意为ListNode形式
        root = ListNode(heapq.heappop(h)) #将堆顶根元素输出
        curnode = root #指向头结点
        
        while h:
            nextnode = ListNode(heapq.heappop(h))
            curnode.next = nextnode
            curnode = nextnode
        return root #返回头结点即可
                
            

#########################################################################
    
#题目2：堆栈-判断括号是否匹配
#题目表述：给定字符串，只包含()[]{}
#例如：输入："([{[]}])" 输出：True
#     输如："{()})" 输出False
#思路:用堆栈stack
        
def isValid(s):
    stack = []
    par_dict = {")":"(", "]":"[", "}":"{"}
    
    for char in s:
        if char not in par_dict:
            stack.append(char)
        elif not stack or par_dict[char] != stack.pop():
            return False
    return True

s="({{})})"
print isValid(s)
                
#########################################################################
    
#题目3：剑指offer-反转链表
#题目表述：给定链表，反转输出
#例如：输入：1->2->3->4->5
#     输出：1<-2<-3<-4<-5
#思路:

def ReverseList(pHead):
    # write code here
    if not pHead:
        return None
    last = None #定义一个空值
    while pHead:
        tmp = pHead.next
        pHead.next = last
        last = pHead
        pHead = tmp
    return last

#########################################################################
    
#题目4：剑指offer-两个有序链表，拼接成有序链表输出
#题目表述：
#例如：输入：1->3->5     2->4->6
#     输出：1->2->3->4->5->6

#法一：不推荐
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq #使用python自带堆模块heapq
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        h = []
        while pHead1:#当pHead中的值不为空时
            h.append(pHead1.val) #取出链表中当前值
            pHead1 = pHead1.next #指向下一个元素
            
        while pHead2:
            h.append(pHead2.val)
            pHead2 = pHead2.next
            
        if not h: #如果列表为空，返回None
            return None
        heapq.heapify(h) #将列表h转为最小堆
        
        #以下为构建链表过程，并返回链表头结点
        root = ListNode(heapq.heappop(h)) #根节点，弹出最小堆的根节点，即弹出最小值
        curnode = root #当前指针指向根节点
        
        while h:#当最小堆不为空时
            nextnode = ListNode(heapq.heappop(h)) #取出下一个最小值
            curnode.next = nextnode #指针指向下一节点
            curnode = nextnode #指针指向下一节点
        return root #返回链表的根结点

#法二：推荐
# -*- coding:utf-8 -*-

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here

        head = ListNode(None)
        p = head
        while pHead1 and pHead2:
            if pHead1.val >= pHead2.val:
                head.next = pHead2
                pHead2 = pHead2.next
            else:
                head.next = pHead1
                pHead1 = pHead1.next
            
            head = head.next #记住此处
        
        if pHead1 and not pHead2:
            head.next = pHead1
        if pHead2 and not pHead1:
            head.next = pHead2
        return p.next

#法三：没有法二好

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq #使用python自带堆模块heapq
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        h = []
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                h.append(pHead1.val)
                pHead1 = pHead1.next
            else:
                h.append(pHead2.val)
                pHead2 = pHead2.next
        
        while pHead1:
            h.append(pHead1.val)
            pHead1 = pHead1.next
        
        while pHead2:
            h.append(pHead2.val)
            pHead2 = pHead2.next
        
        if not h:
            return None
        #把list转成链表形式
        root = ListNode(h[0])
        curnode = root
        for i in range(1, len(h)):
            nextnode = ListNode(h[i])
            curnode.next = nextnode
            curnode = nextnode
        return root 
