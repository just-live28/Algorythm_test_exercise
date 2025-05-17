eq = input()

stk = []
result = ''
for i in eq:
    if i == '(':
        stk.append('(')
    elif i == ')':
        while stk and stk[-1] != '(':
            result += stk.pop()
        stk.pop()
    elif i == '*' or i == '/':
        while stk and (stk[-1] == '*' or stk[-1] == '/'):
            result += stk.pop()
        stk.append(i)
    elif i == '+' or i == '-':
        while stk and stk[-1] != '(':
            result += stk.pop()
        stk.append(i)
    else:
        result += i
            
while stk:
    result += stk.pop()

print(result)