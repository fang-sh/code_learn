'''
提目1：给定入栈顺序，判断出栈顺序是否合理
题目2：20. 有效的括号（leetcode 利用栈实现）




(2) 力扣加加，一招吃遍力扣四道题: https://leetcode-cn.com/problems/remove-k-digits/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-5/
    题目1：402. 移掉 K 位数字 (中等)
    题目2：316. 去除重复字母 (困难)
    题目3：321. 拼接最大数 (困难)
    题目4：1081. 不同字符的最小子序列 （中等）

'''

"""
题目1：给定入栈顺序，判断出栈顺序是否合理
题目描述：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
   假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
   但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""
def is_right_order(pushV, popV):
    if len(pushV) == 0:
        return False
    stack = []
    for i in pushV:
        stack.append(i) #把元素压入栈中
        while stack and popV[0] == stack[-1]: # 判断条件
            stack.pop()
            popV.pop(0)
   
    if not stack: # 如果栈空，就返回True
        return True
    return False

###################################################

"""
题目2：20. 有效的括号（leetcode 利用栈实现）
输入：s = "()[]{}" 输出：True
输入：s = "([)]" 输出：False
"""
def isValid(s):
    d = { # 注意，左边括号作为key，不是右边
        '(': ')',
        '{': '}',
        '[': ']',
        '?': '?' # 添加一个字符
    }
    
    stack = ['?'] # 防止stack为空时，执行pop()出错
    for i in s:
        if i in d: # i 在d中时，append
            stack.append(i)
        elif i != d[stack.pop()]:
            return False
    return len(stack)==1 # 返回长度是否为1

------------------------（2）-------------------------------
"""
题目1：402. 移掉K位数字
"""
# 法一：超时
# ① 逐个移除第1个元素，比较，选择最小值
# ② 在①的结果上，逐个移除第2个元素，比较，选择最小值
# ③ 在②的结果上，逐个移除第3个元素，比较，选择最小值
def removeKdigits(self, num: str, k: int) -> str:
    if len(num)==k:
        return '0'
    min_v = num
    while k > 0:
        for i in range(len(num)):
            min_v = min(min_v, num[:i]+num[i+1:])
        num = min_v
        k -= 1
    # return min_v if min_v[0]!='0' else min_v[1:]
    return str(int(min_v))
    
# (推荐)法二：贪心 + 栈
def removeKdigits(self, num: str, k: int) -> str:
    if len(num) == k:
        return '0'
        
    stack = []
    remain = len(num) - k # 删除k个元素后，数字长度
    
    for i in num:
        while stack and k>0 and stack[-1]>i:
            stack.pop()
            k -= 1
        stack.append(i)
    return str(int(''.join(stack)[:remain])) # 如果遍历完，没有符合要求的值，则保留前remain个值

