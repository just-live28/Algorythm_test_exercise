n = int(input())

d = [0] * (n+1)
prep = [0] * (n+1)
d[1] = 0
prep[1] = 0

for i in range(2, n+1):
    divide_3 = int(1e7)
    if i % 3 == 0:
        divide_3 = d[i // 3] + 1
    divide_2 = int(1e7)
    if i % 2 == 0:
        divide_2 = d[i // 2] + 1
    d[i] = min(divide_3, divide_2, d[i-1] + 1)
    
    if d[i] == divide_3:
        prep[i] = i // 3
    elif d[i] == divide_2:
        prep[i] = i // 2
    else:
        prep[i] = i - 1

print(d[n])
print(n, end=' ')
while prep[n] != 0:
    print(prep[n], end=' ')
    n = prep[n]