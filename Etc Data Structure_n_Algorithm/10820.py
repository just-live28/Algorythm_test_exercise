stack = []
n = int(input())
for _ in range(n):
    line = input().split()
    if len(line) == 2:
        stack.append(int(line[1]))
    elif line[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif line[0] == 'size':
        print(len(stack))
    elif line[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)