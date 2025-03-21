n, k = map(int, input().split())
number = input()
stack = []
for i in range(n):
    if not stack or number[i] <= stack[-1] or k == 0:
        stack.append(number[i])
    else:
        while k > 0 and stack and number[i] > stack[-1]:
            stack.pop()
            k -= 1
        stack.append(number[i])
while k > 0:
    stack.pop()
    k -= 1

print(''.join(stack))