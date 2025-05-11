n = int(input())

stk = []
count = 1
result = []
enable = True
for _ in range(n):
    target = int(input())
    
    if not enable:
        continue
    
    while target >= count:
        stk.append(count)
        count += 1
        result.append('+')
    
    if target != stk[-1]:
        enable = False
        continue
    else:
        stk.pop()
        result.append('-')

if enable:
    for i in result:
        print(i)
else:
    print('NO')