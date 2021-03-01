'''
提目1：给定入栈顺序，判断出栈顺序是否合理
题目2：20. 有效的括号（leetcode 利用栈实现）

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

