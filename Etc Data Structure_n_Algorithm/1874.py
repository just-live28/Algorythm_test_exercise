import sys
input = sys.stdin.readline

n = int(input())
count = 1
stack = []
opers = []
enable = True
for _ in range(n):
    target = int(input())
    
    while target >= count:
        stack.append(count)
        opers.append("+")
        count += 1

    if stack[-1] != target:
        enable = False
        break
    else:
        stack.pop()
        opers.append("-")

if enable:
    for i in opers:
        print(i)
else:
    print("NO")