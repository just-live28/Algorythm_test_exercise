# 65 ~ 90 (A~Z)
# 후위 표기식: 숫자1 숫자2 연산자

n = int(input())
equation = input()
arr = [0] * 91
for i in range(65, 65 + n):
    arr[i] = int(input())
    
stk = []
for i in equation:
    if 65 <= ord(i) <= 90:
        stk.append(arr[ord(i)])
    else:
        n2 = stk.pop()
        n1 = stk.pop()
        
        if i == '+':
            stk.append(n1 + n2)
        elif i == '-':
            stk.append(n1 - n2)
        elif i == '*':
            stk.append(n1 * n2)
        elif i == '/':
            stk.append(n1 / n2)

print("{:.2f}".format(stk.pop()))